"""Counts the "do <day>. <month> <year>" and "do kraja <year>. godine" phrases in this repository that the lapsed-time-limit
scan (ingest/textscan.py, limits()) does not read.

    python -X utf8 do_gap_check.py <scripts dir> [<commit>]

<scripts dir> is global-law's vulnerabilities/scripts, with sources/corpus/montenegro-law.git. Phrases are counted on one line
of a .md file at the commit (default: the one in pins.json); "past" means a date before the commit's day.
"""
import collections, json, os, re, subprocess, sys

S = os.path.abspath(sys.argv[1])
sys.path.insert(0, os.path.join(S, "ingest"))
import textscan  # noqa: E402

G = os.path.join(S, "sources", "corpus", "montenegro-law.git")
PIN = sys.argv[2] if len(sys.argv) > 2 else json.load(open(os.path.join(S, "pins.json"), encoding="utf-8"))["corpora"][0]["sha"]
CUT = subprocess.run(["git", "show", "-s", "--format=%cs", PIN], cwd=G, capture_output=True, text=True).stdout.strip()

GEN = dict(zip("januara februara marta aprila maja juna jula avgusta septembra oktobra novembra decembra".split(), range(1, 13)))
GEN["augusta"] = 8
CYR = dict(zip("јануара фебруара марта априла маја јуна јула августа септембра октобра новембра децембра".split(), range(1, 13)))
NOM = dict(zip("januar februar mart april maj jun jul avgust septembar oktobar novembar decembar".split(), range(1, 13)))
ALL = {**NOM, **GEN, **CYR}
MON = "|".join(sorted(map(re.escape, ALL), key=len, reverse=True))
RX = re.compile(rf"(?i)(?<![\w])(?:do|до)\s+(\d{{1,2}})\s*\.\s*({MON})\s*(\d{{4}})")
RXK = re.compile(r"(?i)(?<![\w])(?:do|до)\s+(?:kraja|краја)\s+(\d{4})\.?\s*(?:godine|године)")

lines = subprocess.run(["git", "grep", "-I", "-h", "-i", "-E", r"(do|до) +[0-9]|(do|до) +(kraja|краја)", PIN, "--", "*.md"],
                       cwd=G, capture_output=True).stdout.decode("utf-8", "replace").splitlines()
tot, miss, ex = collections.Counter(), collections.Counter(), collections.defaultdict(list)
for line in lines:
    read = {d for d, _ in textscan.limits(line)}
    for m in RX.finditer(line):
        w = m.group(2).lower()
        kind = "cyrillic" if w in CYR else ("genitive" if w in GEN else "nominative")
        iso = f"{int(m.group(3)):04d}-{ALL[w]:02d}-{int(m.group(1)):02d}"
        tot[kind, iso < CUT] += 1
        if iso not in read:
            miss[kind, iso < CUT] += 1
            ex[kind].append(line[max(0, m.start() - 40):m.end() + 20])
    for m in RXK.finditer(line):
        kind = "do kraja" + (" (cyrillic)" if "краја" in m.group(0).lower() else "")
        iso = f"{int(m.group(1)):04d}-12-31"
        tot[kind, iso < CUT] += 1
        if iso not in read:
            miss[kind, iso < CUT] += 1
            ex[kind].append(line[max(0, m.start() - 40):m.end() + 20])
for k in sorted(tot):
    print(f"{k[0]:<22} {'past' if k[1] else 'later':<6} phrases {tot[k]:>5}  not read {miss[k]:>4}")
for k, v in ex.items():
    print("==", k)
    for s in v[:10]:
        print("   ", s)
