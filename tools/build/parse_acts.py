"""Montenegro: acts published in the Službeni list Crne Gore that no later act has amended, each as published.

Reads only a local copy of the Official Gazette's legal information system (sluzbenilist.me, PIS):
  list/<type>/<page>.html.gz   listing pages (/propisi?type=0&act=<type>&page=<page>): title, status, issue
  act/<id//1000>/<id>.html.gz  act pages (/propisi/<id>): status, issue, publication and in-force days, amending acts
  pdf/<id//1000>/<id>.json.gz  the text layer of the act's PDF (/propisi/<id>/download), read line by line with its
                               position: {sha256, pages: [{lines: [[x0, y0, x1, y1, size, bold, text, block]]}]}
and writes corpus.d parts (SCHEMA.md in scripts/gitlaw_common). Deterministic: the same inputs give the same bytes.

    python -X utf8 parse_acts.py --src <folder> --retrieved YYYY-MM-DD [--exclude ids.txt] [--report holds.jsonl]

What becomes an act here: an act the PIS marks in force ("Važeći") whose page lists no amending act ("Izmjene i/ili
dopune"), with a text layer in its PDF. Its one version is the text as published, dated by the PIS "Datum stupanja na
snagu" (checked against the act's own final article when that names a day counted from publication).

An act is held back, not published, when (the reason goes to the report):
- the PIS lists acts amending it, or a later act's title names it as amended, corrected (Ispravka) or repealed;
- it has no in-force day, or its own final article gives a different one;
- its PDF has no text layer (a scan) or its articles don't number cleanly (a gap, a repeat, a heading out of order).
The President's promulgation decree printed above a law, and the signatures, are left out (as in the rest of this
repository); annexes printed after the signature are kept as one unit, their tables run on as lines.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import html
import json
import re
import unicodedata
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARTS = HERE / "corpus.d"
PAGE = "https://www.sluzbenilist.me/propisi/{id}"
PDF = "https://www.sluzbenilist.me/propisi/{id}/download"

KINDS = {"Zakon": ("zakon", "law"), "Uredba": ("uredba", "decree"), "Pravilnik": ("pravilnik", "decree"),
         "Odluka": ("odluka", "decree"), "Uputstvo": ("uputstvo", "decree"), "Naredba": ("naredba", "decree"),
         "Statut": ("statut", "decree"), "Pravila": ("pravila", "decree"), "Poslovnik": ("poslovnik", "decree"),
         "Program": ("program", "decree"), "Plan": ("plan", "decree"), "Rješenje": ("rjesenje", "decree"),
         "Druga akta": ("akt", "decree"), "Potvrđeni međunarodni ugovori i obavještenja": ("ugovor", "treaty"),
         "Drugi međunarodni ugovori i međunarodni akti": ("ugovor", "treaty")}
# A later act's title naming another act as amended, corrected or repealed: "Zakon o izmjenama i dopunama Zakona o X",
# "Ispravka Pravilnika o Y", "Zakon o prestanku važenja Zakona o Z".
AMENDING = re.compile(r"\b(?:o\s+(?:izmjen\w*|dopun\w*|izmjeni|dopuni)(?:\s+i\s+(?:dopun\w*|izmjen\w*))?|ispravk\w*|"
                      r"o\s+prestanku\s+va[zž]enja|o\s+stavljanju\s+van\s+snage)\s+(\w+)\s+(o|za|kojim|u)\b(.*)$", re.I)
STEMS = ["zakonik", "zakon", "uredb", "pravilnik", "odluk", "uputstv", "naredb", "statut", "pravil", "poslovnik",
         "program", "plan", "rjesenj"]
ART = re.compile(r"^(?:Č\s*l\s*a\s*n|Ч\s*л\s*а\s*н)\s+(\d+)\s*([a-zа-я]?)\s*\.?$")
CHAPTER = re.compile(r"^(?:[IVXLC]+\s*[.)]?\s+\S|(?:GLAVA|Glava|DIO|Dio|ODJELJAK|Odjeljak|POGLAVLJE|Poglavlje|"
                     r"ODSJEK|Odsjek)\b)")
SECTION = re.compile(r"^\d+(?:\.\d+)*\.\s+\S")
SIG = re.compile(r"^(?:Broj|Br\.|Број|SU-SK\s+Broj|Number)\s*[:.]?\s*\S|^(?:Podgorica|Cetinje|Подгорица),?\s+\d|"
                 r"^(?:Podgorica|Cetinje),\s*$")
SR = re.compile(r"s\.\s*r\.?\s*$|с\.\s*р\.?\s*$")
DECREE = re.compile(r"^(?:U\s*K\s*A\s*Z|У\s*К\s*А\s*З)\b")
OPEN_Q, CLOSE_Q = "„", "“”"
MONTHS = {"januar": 1, "februar": 2, "mart": 3, "april": 4, "maj": 5, "jun": 6, "jul": 7, "avgust": 8, "septembar": 9,
          "oktobar": 10, "novembar": 11, "decembar": 12}
IN_FORCE = re.compile(r"(?:stup(?:a|aju)\s+na\s+snagu|ступа(?:ју)?\s+на\s+снагу)\s+(.{0,160})", re.I)
SIGNER = re.compile(r"^(?:Skupština|Скупштина|Vlada|Влада|Predsjedni|Predśedni|Предсједни|Ministar|Ministarka|Министар|Direktor|Guverner|Upravni|Savjet|Glavni|Generaln|Potpredsjedni|Pot?predśedni|SKUPŠTINA|VLADA)")


class Hold(Exception):
    pass


def norm(s: str) -> str:
    s = html.unescape(s).replace(" ", " ").replace("­", "")
    s = s.replace("–", "-").replace("—", "-").replace("„", '"').replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def fold(s: str) -> str:
    s = s.replace("đ", "dj").replace("Đ", "Dj")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def stem(word: str) -> str | None:
    w = fold(word)
    return next((s for s in STEMS if w.startswith(s)), None)


def tail_key(kind_word: str, rest: str) -> tuple[str, str] | None:
    st = stem(kind_word)
    return (st, fold(rest)[:120]) if st else None


def dmy(s: str | None) -> str | None:
    m = re.search(r"(\d{1,2})\.(\d{1,2})\.(\d{4})", s or "")
    return f"{int(m.group(3)):04d}-{int(m.group(2)):02d}-{int(m.group(1)):02d}" if m else None


# ------------------------------------------------------------------------------------------------ sources

def meta(page: str) -> dict:
    t = re.sub(r"<script.*?</script>", "", page, flags=re.S)
    t = re.sub(r'<a [^>]*href="https://www\.sluzbenilist\.me/propisi/(\d+)"[^>]*>', r" [[\1]] ", t)
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))
    m = re.search(r"\(PIS\) Objavljeno: [\d.]+ (.*?) Status: (\S+) Izdanje: (.*?) Registarski broj", t)
    if not m:
        raise Hold("page_unreadable")
    out = {"title": m.group(1).strip(), "status": m.group(2), "issue": m.group(3).strip()}
    for key, lab in (("published", "Datum objavljivanja"), ("in_force", "Datum stupanja na snagu"),
                     ("applies", "Datum početka primjene")):
        mm = re.search(lab + r": (\d{1,2}\.\d{1,2}\.\d{4})", t)
        out[key] = dmy(mm.group(1)) if mm else None
    mm = re.search(r"Vrsta propisa: (.*?) (?:Datum|Oblast|Prethodna)", t)
    out["vrsta"] = mm.group(1).strip() if mm else ""
    mm = re.search(r"Donosilac propisa: (.*?) Vrsta propisa", t)
    out["donosilac"] = mm.group(1).strip() if mm else ""
    out["amended"] = "Izmjene i/ili dopune" in t
    return out


def page_meta(path: Path) -> dict:
    """meta() of an act page file, or {"hold": reason}."""
    try:
        return meta(gzip.decompress(path.read_bytes()).decode("utf-8", "replace"))
    except Hold as h:
        return {"hold": str(h)}


LIST_ITEM = re.compile(r'<a href="https://www\.sluzbenilist\.me/propisi/(\d+)" class="text-18[^"]*">\s*(.*?)\s*</a>'
                       r'(.*?)(?=<a href="https://www\.sluzbenilist\.me/propisi/\d+" class="text-18|$)', re.S)


def listing_page(f: Path):
    """Every act listed on one listing page: (id, title, status, issue, type)."""
    t = gzip.decompress(f.read_bytes()).decode("utf-8", "replace")
    for m in LIST_ITEM.finditer(t):
        rest = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(3))))
        st = re.search(r"Status:\s*(\S+)", rest)
        iz = re.search(r"Izdanje:\s*(.*?)\s*Registarski", rest)
        yield (int(m.group(1)), re.sub(r"\s+", " ", html.unescape(m.group(2))).strip(),
               st.group(1) if st else "", iz.group(1) if iz else "", f.parent.name)


def listing(src: Path):
    """Every listed act: (id, title, status, issue, type)."""
    for f in sorted((src / "list").glob("*/*.html.gz")):
        yield from listing_page(f)


def named_on(f: Path) -> list:
    """[stem, folded rest, id] for each act on a listing page whose title names another act as amended, corrected or
    repealed (see AMENDING and tail_key)."""
    out = []
    for i, title, status, issue, typ in listing_page(f):
        m = AMENDING.search(title)
        if m:
            k = tail_key(m.group(1), m.group(2) + " " + m.group(3))
            if k:
                out.append([k[0], k[1], i])
    return out


# ------------------------------------------------------------------------------------------------ text

def paragraphs(doc: dict) -> list[dict]:
    """The PDF's lines joined into paragraphs: {'t': raw text, 'bold', 'center', 'depth'} (quote depth at its start).
    A paragraph's first line is indented and its other lines start at the left margin; centred lines (titles,
    article numbers, captions) stand alone, and consecutive centred bold lines of one title are joined."""
    out: list[dict] = []
    prev = None
    # The text block's margins, over the whole document: the left edge of continuation lines and the right edge of
    # full lines (a page with only indented lines must not move them).
    body = sorted(l[0] for p in doc["pages"] for l in p["lines"] if len(l[6].strip()) > 40)
    ends = sorted(l[2] for p in doc["pages"] for l in p["lines"] if len(l[6].strip()) > 40)
    if not body:
        body = sorted(l[0] for p in doc["pages"] for l in p["lines"]) or [0]
        ends = sorted(l[2] for p in doc["pages"] for l in p["lines"]) or [0]
    left = body[len(body) // 20]
    right = ends[len(ends) * 19 // 20]
    mid = (left + right) / 2
    for p in doc["pages"]:
        h = p.get("height") or 842.0
        # page numbers: a line holding only a number, in the top or bottom tenth of the page
        lines = [l for l in p["lines"] if l[6].strip()
                 and not (re.fullmatch(r"\s*-?\s*\d{1,3}\s*-?\s*", l[6]) and (l[3] < 0.1 * h or l[1] > 0.9 * h))]
        if not lines:
            continue
        for l in lines:
            x0, y0, x1, y1, size, bold, text = l[:7]
            t = text.strip()
            center = x0 > left + 8 and x1 < right - 8 and abs((x0 + x1) / 2 - mid) < 15
            cont = False
            if prev is not None and out:
                same_page = prev["page"] is p
                gap = y0 - prev["y1"] if same_page else 0
                if center and prev["center"] and bold == prev["bold"] and same_page and gap < size * 0.9 \
                        and not ART.match(norm(t)) and not ART.match(norm(prev["text"])) \
                        and (norm(t).upper() == norm(t)) == (norm(prev["text"]).upper() == norm(prev["text"])) \
                        and not SR.search(prev["text"]) and not re.search(r"[.,:]$", prev["text"].rstrip()):
                    cont = True   # a title or caption over several centred lines
                elif not center and not prev["center"] and x0 <= left + 4 and gap < size * 0.9 \
                        and (prev["x1"] >= right - 30 or not re.search(r"[.:;!?]$", prev["text"].rstrip())):
                    cont = True
            if cont:
                out[-1]["t"] += " " + t
            else:
                out.append({"t": t, "bold": bool(bold), "center": center})
            prev = {"page": p, "y1": y1, "x1": x1, "center": center, "bold": bool(bold), "text": t}
    depth = 0
    for para in out:
        para["depth"] = depth
        for ch in para["t"]:
            # „ opens a quotation; “ ” close it, and so does a plain " inside one (gazettes mix „...")
            if ch == OPEN_Q:
                depth += 1
            elif depth and (ch in CLOSE_Q or ch == '"'):
                depth -= 1
        para["t"] = norm(para["t"])
    return [p for p in out if p["t"]]


def caps(t: str) -> bool:
    return t.upper() == t and bool(re.search(r"[A-ZČĆŠŽĐА-Я]", t))


def art_key(n: int, suf: str) -> str:
    return f"clan-{n:03d}" + (f"-{suf}" if suf else "")


def split(paras: list[dict], is_law: bool, amending: bool = False) -> tuple[dict, int]:
    """Units of an act: '0-uvod' (enacting formula and title), headings, 'clan-NNN' articles, 'tekst' for an act
    without articles, 'prilog' for what follows the signature. Returns (units, number of articles)."""
    ps = list(paras)
    if ps and re.fullmatch(r"\d+\.", ps[0]["t"]):
        ps = ps[1:]          # the gazette's running number of the item
    # The President's promulgation decree above a law: up to the line signed "s.r." after "UKAZ".
    if any(DECREE.match(p["t"]) for p in ps[:6]):
        # the decree ends at the last line signed "s.r." before the law's first article
        first_art = next((k for k, p in enumerate(ps) if ART.match(p["t"]) and p["depth"] == 0), len(ps))
        signed = [k for k, p in enumerate(ps[:min(30, first_art)]) if SR.search(p["t"]) and len(p["t"]) < 120]
        end = signed[-1] if signed else None
        if end is None:
            raise Hold("decree_end_not_found")
        ps = ps[end + 1:]
    elif is_law:
        raise Hold("no_promulgation_decree")
    if not ps:
        raise Hold("no_text")
    # Articles: "Član N" standing alone, outside quotes, in order 1, 2, 2a, 3 ...
    starts: list[tuple[int, int, str]] = []
    stray = []
    expect, last_n, last_suf = 1, 0, ""
    for k, p in enumerate(ps):
        m = ART.match(p["t"])
        if not m:
            continue
        n, suf = int(m.group(1)), m.group(2)
        if p["depth"] > 0:
            continue
        if (n == expect and not suf) or (n == last_n and suf and (ord(suf) == ord(last_suf or "`") + 1)):
            starts.append((k, n, suf))
            last_n, last_suf = n, suf
            expect = n + 1 if not suf else expect
        else:
            stray.append(p["t"])
    if stray:
        # An amending act quotes the articles it inserts; their headings stay in the text of the article that
        # quotes them, but only when none of the act's own headings follows a "... glasi:" line or opens a quote.
        if not amending:
            raise Hold("article_out_of_sequence:" + "; ".join(stray[:3]))
        for k, n, suf in starts:
            before = ps[k - 1]["t"] if k else ""
            after = ps[k + 1]["t"] if k + 1 < len(ps) else ""
            if before.endswith(":") or before.startswith('"') or after.startswith('"'):
                raise Hold(f"article_heading_ambiguous:{n}{suf}")
    # The signature block: after the last article (or anywhere, for an act without articles), the first "Broj:" /
    # "Podgorica, ..." line; it ends at the last line signed "s.r." shortly after; what follows is an annex.
    lo = starts[-1][0] + 1 if starts else 1
    sig = next((k for k in range(lo, len(ps)) if SIG.match(ps[k]["t"]) and len(ps[k]["t"]) < 120), None)
    annex: list[str] = []
    if sig is None:
        # no "Broj"/"Podgorica" line: the signer's lines at the end ("Skupština Crne Gore", "Predsjednik,", "..., s.r.")
        k = len(ps)
        while k > lo and len(ps[k - 1]["t"]) < 90 and (SR.search(ps[k - 1]["t"]) or SIGNER.match(ps[k - 1]["t"])):
            k -= 1
        if k < len(ps):
            sig = k
        elif starts and IN_FORCE.search(ps[-1]["t"]):
            sig = len(ps)     # printed without a signature: the act ends with its in-force article
        else:
            raise Hold("signature_not_found")
    sr = [k for k in range(sig, min(sig + 10, len(ps))) if SR.search(ps[k]["t"]) and len(ps[k]["t"]) < 120]
    tail_from = (sr[-1] + 1) if sr else sig
    if not sr:
        # no "s.r." line: the block is the short lines after "Broj"; anything long after it is not a signature
        k = sig
        while k < len(ps) and len(ps[k]["t"]) < 90 and k < sig + 8:
            k += 1
        tail_from = k
    annex = [p["t"] for p in ps[tail_from:]]
    body = ps[:sig]
    units: dict[str, dict] = {}
    if not starts:
        lines = [p["t"] for p in body]
        if not lines:
            raise Hold("no_text")
        if any(re.search(r"(?:Član|Члан)\s+1\b", t) for t in lines):
            raise Hold("articles_not_split")
        units["tekst"] ={"label": "Tekst", "kind": "text", "text": "\n".join(lines) + "\n"}
    else:
        first = starts[0][0]
        # headings and caption just above article 1 belong to it; the rest above is the preamble
        def lead(k0: int, lo_: int) -> tuple[list[str], str | None, int]:
            """Headings and the caption directly above the article at k0, down to lo_: (headings, caption, start)."""
            cap = None
            j = k0 - 1
            if j >= lo_ and (ps[j]["bold"] or ps[j]["center"]) and not caps(ps[j]["t"]) and len(ps[j]["t"]) < 200 \
                    and not CHAPTER.match(ps[j]["t"]) and not re.search(r"[.;:,]$", ps[j]["t"]):
                cap = ps[j]["t"]
                j -= 1
            heads = []
            while j >= lo_ and len(ps[j]["t"]) < 200 and (CHAPTER.match(ps[j]["t"]) or (caps(ps[j]["t"]) and lo_ > 0)
                                                          or (SECTION.match(ps[j]["t"]) and ps[j]["bold"])) \
                    and not re.search(r"[;:,]$", ps[j]["t"]) and ps[j]["depth"] == 0:
                heads.insert(0, ps[j]["t"])
                j -= 1
            return heads, cap, j + 1
        bounds = []
        lo_ = 0
        for idx, (k, n, suf) in enumerate(starts):
            heads, cap, s = lead(k, lo_ if idx == 0 else starts[idx - 1][0] + 1)
            bounds.append((k, n, suf, heads, cap, s))
        pre = [p["t"] for p in ps[:bounds[0][5]]]
        if pre:
            units["0-uvod"] = {"label": "Uvod", "kind": "preamble", "text": "\n".join(pre) + "\n"}
        prev_key = None
        for idx, (k, n, suf, heads, cap, s) in enumerate(bounds):
            end = bounds[idx + 1][5] if idx + 1 < len(bounds) else sig
            key = art_key(n, suf)
            for j, h in enumerate(heads, 1):
                hk = f"{prev_key}-zz-naslov-{j}" if prev_key else f"0-naslov-{j}"
                units[hk] = {"label": h[:80], "kind": "heading", "text": f"# {h}\n"}
            text = [p["t"] for p in ps[k + 1:end]]
            if not text:
                raise Hold(f"empty_article:{n}{suf}")
            word = "Члан" if ps[k]["t"].startswith("Ч") else "Član"   # the heading as printed, in its script
            lines = [f"# {word} {n}{suf}"] + ([f"## {cap}"] if cap else []) + text
            units[key] = {"label": f"{word} {n}{suf}", "kind": "art", "text": "\n".join(lines) + "\n"}
            prev_key = key
    if annex:
        units["prilog"] = {"label": "Prilog", "kind": "annex", "text": "\n".join(annex) + "\n"}
    return units, len(starts)


CYR = dict(zip("абвгдђежзијклљмнњопрстћуфхцчџшАБВГДЂЕЖЗИЈКЛЉМНЊОПРСТЋУФХЦЧЏШ",
               ["a", "b", "v", "g", "d", "đ", "e", "ž", "z", "i", "j", "k", "l", "lj", "m", "n", "nj", "o", "p", "r",
                "s", "t", "ć", "u", "f", "h", "c", "č", "dž", "š", "A", "B", "V", "G", "D", "Đ", "E", "Ž", "Z", "I",
                "J", "K", "L", "Lj", "M", "N", "Nj", "O", "P", "R", "S", "T", "Ć", "U", "F", "H", "C", "Č", "Dž",
                "Š"]))


def cyr2lat(s: str) -> str:
    """Only for reading an in-force clause: the text itself keeps its script."""
    return "".join(CYR.get(ch, ch) for ch in s)


def own_in_force(units: dict, published: str) -> str | None:
    """The day the act's own final words give, when counted from publication or named; None when not readable."""
    keys = [k for k in units if k.startswith(("clan-", "tekst"))]
    if not keys:
        return None
    # The act's last article first (its own in-force article), then the whole text without the long quoted
    # provisions an amending act inserts into another act. Cyrillic is read through a Latin transliteration.
    last = cyr2lat(units[keys[-1]]["text"].replace("\n", " "))
    hits = list(IN_FORCE.finditer(last))
    if not hits:
        text = cyr2lat(" ".join(units[k]["text"].replace("\n", " ") for k in keys))
        text = re.sub(r'"[^"]{80,}?"', " ", text)
        hits = list(IN_FORCE.finditer(text))
    if not hits:
        return None
    c = hits[-1].group(1)
    if not re.search(r"objavljivanja|objave|donošenja|dono[sš]enja", c[:80]):
        m = re.match(r"(?:dana\s+)?(\d{1,2})\.\s*(\w+)\s+(\d{4})", c)
        if m and fold(m.group(2))[:5] in {k[:5] for k in MONTHS}:
            mo = next(v for k, v in MONTHS.items() if k[:5] == fold(m.group(2))[:5])
            return date(int(m.group(3)), mo, int(m.group(1))).isoformat()
        return None
    pub = date.fromisoformat(published)
    if re.match(r"(?:danom|na\s+dan)\s+objavljivanja", c):
        return published
    words = {"narednog": 1, "sljedećeg": 1, "slijedećeg": 1, "prvog": 1, "drugog": 2, "trećeg": 3, "petog": 5,
             "osmog": 8, "desetog": 10, "petnaestog": 15, "tridesetog": 30}
    m = re.match(r"(\w+)\s+dana\s+od\s+dana\s+objavljivanja", c)
    if m and m.group(1).lower() in words:
        return (pub + timedelta(days=words[m.group(1).lower()])).isoformat()
    return None


SELF = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:16]
_STATS: dict[Path, object] = {}


def stat(path: Path):
    """The file's stat, taken once per run."""
    if path not in _STATS:
        _STATS[path] = path.stat()
    return _STATS[path]


def read_text(path: Path, is_law: bool, amending: bool, cache: dict | None) -> tuple[dict, int, str]:
    """(units, number of articles, sha256 of the PDF) for one act's PDF text, or Hold. Results are kept in `cache`
    keyed by the input file's size and time and this parser's own hash, so a cached run gives the same bytes."""
    st = stat(path)
    key = f"{path.name}|{st.st_size}|{st.st_mtime_ns}|{int(is_law)}|{int(amending)}|{SELF}"
    if cache is not None and key in cache:
        r = cache[key]
        if "hold" in r:
            raise Hold(r["hold"])
        return r["units"], r["n_art"], r["sha"]
    try:
        doc = json.loads(gzip.decompress(path.read_bytes()).decode("utf-8"))
        if doc.get("no_text") or not doc.get("pages"):
            raise Hold("pdf_unreadable")
        if any(p.get("scanned") for p in doc["pages"]):
            raise Hold("scanned_pages")
        letters = sum(len(re.findall(r"[^\W\d_]", l[6])) for p in doc["pages"] for l in p["lines"])
        if letters < 200:
            raise Hold("no_text_layer")
        if re.search(r"[ĈĉĆ]lan\b|[ĈĉţŢðÐ]", "".join(l[6] for p in doc["pages"] for l in p["lines"])):
            raise Hold("text_layer_wrong_glyphs")   # an old font maps Č to Ĉ: the text layer is not the text
        units, n_art = split(paragraphs(doc), is_law, amending)
    except Hold as h:
        if cache is not None:
            cache[key] = {"hold": str(h)}
        raise
    if cache is not None:
        cache[key] = {"units": units, "n_art": n_art, "sha": doc["sha256"]}
    return units, n_art, doc["sha256"]


def cached(cache: dict | None, used: set, kind: str, path: Path, derive):
    """derive(path) through `cache`, keyed like read_text's results by the file's size and time and this parser's own
    hash (and `kind`, which names what is derived and from what else)."""
    if cache is None:
        return derive(path)
    st = stat(path)
    key = f"{kind}|{path.parent.name}/{path.name}|{st.st_size}|{st.st_mtime_ns}|{SELF}"
    if key not in cache:
        cache[key] = derive(path)
    used.add(key)
    return cache[key]


def replace(tmp: Path, f: Path) -> None:
    """Atomic rename; a reader holding the old file open (Windows) gets a few seconds to let go."""
    import time
    for k in range(20):
        try:
            tmp.replace(f)
            return
        except PermissionError:
            if k == 19:
                raise
            time.sleep(0.5)


# ------------------------------------------------------------------------------------------------ main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--retrieved", required=True, help="the day the inputs were retrieved (YYYY-MM-DD)")
    ap.add_argument("--exclude", help="file of PIS ids already published under other slugs (one per line)")
    ap.add_argument("--report")
    ap.add_argument("--rejects", help="JSON {id: reason}: acts held back by hand or by a failed read-back check")
    ap.add_argument("--out", help="folder for the parts (default: corpus.d next to this file)")
    ap.add_argument("--kinds", help="comma-separated kinds to publish (default: all)")
    ap.add_argument("--cache", help="optional .json.gz file keeping what is read from each input file (PDF text, act "
                                    "page, listing page) between runs")
    a = ap.parse_args()
    src = Path(a.src)
    exclude = set(Path(a.exclude).read_text().split()) if a.exclude and Path(a.exclude).exists() else set()
    rejects = json.loads(Path(a.rejects).read_text(encoding="utf-8")) if a.rejects and Path(a.rejects).exists() else {}
    cache = None
    if a.cache:
        try:
            cache = json.loads(gzip.decompress(Path(a.cache).read_bytes()).decode("utf-8"))
        except (OSError, ValueError, EOFError):
            cache = {}

    used: set[str] = set()  # cache keys of listing pages, act pages and in-force readings used in this run
    named: dict[tuple[str, str], set[int]] = defaultdict(set)
    for f in sorted((src / "list").glob("*/*.html.gz")):
        for st, rest, i in cached(cache, used, "list", f, named_on):
            named[(st, rest)].add(i)

    parts: dict[str, dict] = defaultdict(lambda: {"laws": {}, "acts": []})
    holds = []
    pdfs = sorted(int(f.name.split(".")[0]) for f in (src / "pdf").glob("*/*.json.gz"))
    for i in pdfs:
        if str(i) in exclude:
            continue
        title = ""
        try:
            pf = src / "act" / str(i // 1000) / f"{i}.html.gz"
            m = cached(cache, used, "page", pf, page_meta)
            if "hold" in m:
                raise Hold(m["hold"])
            title = norm(m["title"])
            if str(i) in rejects:
                raise Hold("rejected:" + str(rejects[str(i)])[:200])
            if not m["status"].startswith("Važe"):
                raise Hold("not_in_force:" + m["status"])
            if m["amended"]:
                raise Hold("amended_on_pis")
            if m["vrsta"] not in KINDS:
                raise Hold("kind_not_built:" + m["vrsta"])
            kind, law_kind = KINDS[m["vrsta"]]
            if a.kinds and kind not in a.kinds.split(","):
                raise Hold("kind_not_selected:" + kind)
            tm = re.match(r"^(\S+)\s+(.*)$", title)
            if tm:
                k = tail_key(tm.group(1), tm.group(2))
                others = (named.get(k) or set()) - {i}
                if others:
                    raise Hold("named_as_amended:" + ",".join(map(str, sorted(others)[:5])))
            if not m["published"]:
                raise Hold("no_publication_day")
            iss = re.search(r"broj\s+(\d+)\s*/\s*(\d{4})", m["issue"])
            if not iss:
                raise Hold("issue_unreadable:" + m["issue"])
            if kind == "zakon" and re.search(r"potvr[dđ]ivanju|ratifikacij", fold(title)):
                raise Hold("ratification_not_built")
            amending = bool(re.search(r"\b(?:izmjen|dopun|izmjeni|dopuni)", fold(title)))
            pdf = src / "pdf" / str(i // 1000) / f"{i}.json.gz"
            units, n_art, sha = read_text(pdf, kind == "zakon", amending, cache)
            doc = {"sha256": sha}
            last_art = units[max(k for k in units if k.startswith("clan-"))]["text"] if n_art else ""
            if n_art and not IN_FORCE.search(last_art) and not m["in_force"]:
                raise Hold("last_article_not_in_force_clause")
            own = cached(cache, used, f"own:{m['published']}:{int(kind == 'zakon')}:{int(amending)}", pdf,
                         lambda p: own_in_force(units, m["published"]))
            day = m["in_force"] or own
            if not day:
                raise Hold("in_force_unknown")
            if m["in_force"] and own and own != m["in_force"]:
                raise Hold(f"in_force_mismatch:pis {m['in_force']} vs text {own}")
            if day < m["published"] and not own:
                raise Hold(f"in_force_before_publication:{day}")
        except Hold as h:
            holds.append({"id": i, "title": title[:160], "reason": str(h)})
            continue
        year = int(m["published"][:4])
        slug = f"{kind}-{year}-{i}"
        label = f"{title} (Službeni list Crne Gore, broj {iss.group(1)}/{iss.group(2)})"
        note = None
        if m["applies"] and m["applies"] != day:
            note = f"Applies from {m['applies']} (PIS: Datum početka primjene); in force from {day}."
        part = f"50-{kind}-{year}"
        parts[part]["laws"][slug] = {"label": label, "title": title, "kind": law_kind, "enacted": m["published"],
                                     "published": m["published"], "url": PAGE.format(id=i), "temporary_until": None,
                                     "restores": None, "note": None}
        parts[part]["acts"].append({
            "slug": slug, "short": title, "title": title, "url": PAGE.format(id=i), "first_law": slug,
            "earlier_laws": [],
            "versions": [{"from": day, "source_url": PDF.format(id=i), "sha256": doc["sha256"], "units": units,
                          "credits": {}, **({"note": note} if note else {})}]})
    if cache is not None:
        tmp = Path(a.cache + ".tmp")
        cache = {k: v for k, v in cache.items() if k.endswith("|" + SELF) and (k in used or not k.startswith(
            ("list|", "page|", "own:")))}
        tmp.write_bytes(gzip.compress(json.dumps(cache, ensure_ascii=False).encode("utf-8"), 3))
        tmp.replace(a.cache)
    PARTS = Path(a.out) if a.out else HERE / "corpus.d"
    PARTS.mkdir(exist_ok=True)
    written = []
    for name in sorted(parts):
        p = parts[name]
        p["acts"].sort(key=lambda x: x["slug"])
        p["sources"] = [{"name": "Službeni list Crne Gore (PIS): acts in force, as published",
                         "url": "https://www.sluzbenilist.me/propisi", "retrieved": a.retrieved,
                         "licence": "Official texts, not protected by copyright (Zakon o autorskom i srodnim pravima)",
                         "notes": "Each act's PIS page (status, issue, dates, amending acts) and the text layer of its "
                                  "PDF."}]
        p["decisions"] = [
            "Acts the PIS marks in force (Važeći) whose page lists no amending act, and that no later act's title "
            "names as amended, corrected (Ispravka) or repealed, as published in the Službeni list Crne Gore; the "
            "others are held back until their later versions are built.",
            "Each act's one version takes effect on the PIS 'Datum stupanja na snagu'; where the act's own final "
            "article counts its day from publication or names a date, the two must agree or the act is held back. "
            "A different application day (PIS 'Datum početka primjene') is noted on the version.",
            "The President's promulgation decree printed above a law and the signatures are left out. Article "
            "captions are the second line of the article file ('## ...'); chapter and section headings are units of "
            "their own; an annex printed after the signature is one unit, its tables run on as lines.",
            "The enacted date given is the publication day (the PIS gives no adoption day)."]
        p["ai_use"] = ["none"]
        f = PARTS / f"{name}.json"
        body = json.dumps(p, ensure_ascii=False, indent=1) + "\n"
        if not f.exists() or f.read_text(encoding="utf-8") != body:
            tmp = f.with_suffix(".tmp")
            tmp.write_text(body, encoding="utf-8", newline="\n")
            replace(tmp, f)
        pub = PARTS / f"{name}.PUBLISH"
        line = (f"{len(p['acts'])} acts checked against the PIS record and the PDF text layer: status Važeći, no "
                f"amending act, in-force day from the PIS (agreeing with the act's own clause where it has one), "
                f"articles numbered in sequence.\n")
        if not pub.exists() or pub.read_text(encoding="utf-8") != line:
            pub.write_text(line, encoding="utf-8", newline="\n")
        written.append((name, len(p["acts"])))
    if a.report:
        Path(a.report).write_text("".join(json.dumps(h, ensure_ascii=False) + "\n" for h in holds), encoding="utf-8")
    reasons = defaultdict(int)
    for h in holds:
        reasons[h["reason"].split(":")[0]] += 1
    print(json.dumps({"pdfs": len(pdfs), "published": sum(n for _, n in written), "held": len(holds),
                      "held_by_reason": dict(reasons), "parts": len(written)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
