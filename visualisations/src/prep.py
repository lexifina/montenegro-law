"""Compute every number of the 20 charts and the data profile into .build/data.json.

    python prep.py <.build dir>          (REPO and HEAD_SHA in the environment; make.py sets them)

Reads the tables make.py extracted (.build/repo/data/), the tree listing (.build/tree.tsv), the Constitution's history
(.build/ustav.json), the commit summary (.build/log.json) and the act texts themselves through `git cat-file`
(the opening file of every act; every file of the laws, decrees and rulebooks; every file of the acts up to 2008).
Every classification rule is in this file.
"""
import collections, csv, json, os, re, statistics, subprocess, sys

B = sys.argv[1]
REPO, SHA = os.environ['REPO'], os.environ.get('HEAD_SHA', '')
ENV = dict(os.environ, GIT_NO_LAZY_FETCH='1')
D = os.path.join(B, 'repo', 'data')
C = collections.Counter
DD = collections.defaultdict


class Blobs:
    def __init__(self):
        self.p = subprocess.Popen(['git', '-C', REPO, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=ENV)

    def get(self, oid):
        self.p.stdin.write((oid + '\n').encode()); self.p.stdin.flush()
        hdr = self.p.stdout.readline().decode().split()
        if len(hdr) < 3 or hdr[1] != 'blob': sys.exit('missing blob ' + oid + ' (run make.py, which fetches it)')
        n = int(hdr[2]); data = self.p.stdout.read(n); self.p.stdout.read(1)
        return data.decode('utf-8', 'replace')


BL = Blobs()

# ------------------------------------------------------------------ text helpers
CYR2LAT = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'ђ': 'đ', 'е': 'e', 'ж': 'ž', 'з': 'z', 'и': 'i', 'ј': 'j', 'к': 'k', 'л': 'l',
           'љ': 'lj', 'м': 'm', 'н': 'n', 'њ': 'nj', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'ћ': 'ć', 'у': 'u', 'ф': 'f',
           'х': 'h', 'ц': 'c', 'ч': 'č', 'џ': 'dž', 'ш': 'š', 'й': 'j', 'ы': 'i', 'э': 'e', 'ю': 'ju', 'я': 'ja'}
for _k, _v in list(CYR2LAT.items()): CYR2LAT[_k.upper()] = _v.capitalize()
CYR = re.compile('[Ѐ-ӿ]')
LAT = re.compile('[A-Za-zČčĆćŠšŽžĐđŚśŹź]')


def script_of(s):
    """'cyr' or 'lat': the script most letters of the text are in (None under 20 letters)"""
    c, l = len(CYR.findall(s)), len(LAT.findall(s))
    if c + l < 20: return None
    return 'cyr' if c > l else 'lat'


def norm(s):
    """transliterated to Latin, one line, words broken across lines joined"""
    s = ''.join(CYR2LAT.get(ch, ch) for ch in s).replace('|', ' ')
    s = re.sub(r'[­​]', '', s).replace('ś', 's').replace('Ś', 'S').replace('ź', 'z').replace('Ź', 'Z')
    s = re.sub(r'(\w)- (\w)', r'\1\2', s)
    return re.sub(r'\s+', ' ', s).strip()


FOLD = str.maketrans({'č': 'c', 'ć': 'c', 'š': 's', 'ž': 'z', 'Č': 'C', 'Ć': 'C', 'Š': 'S', 'Ž': 'Z'})


def fold(s):
    """diacritics folded the way titles typed without them spell (č, ć -> c; š -> s; ž -> z; đ -> dj): every rule matches folded text"""
    return s.translate(FOLD).replace('đ', 'dj').replace('Đ', 'Dj')


def RX(p, flags=re.I):
    """a rule written with diacritics, compiled to match folded text"""
    return re.compile(fold(p), flags)


def diacritics(s):
    return sum(1 for ch in s if ch in 'čćšžđČĆŠŽĐ')


MON = [('januar', 1), ('februar', 2), ('mart', 3), ('april', 4), ('maj', 5), ('jun', 6), ('jul', 7), ('avgust', 8), ('august', 8),
       ('septemb', 9), ('oktob', 10), ('novemb', 11), ('decemb', 12)]
DATE = re.compile(r'\b(\d{1,2})\.\s*(januara|februara|marta|aprila|maja|juna|jula|avgusta|augusta|septembra|oktobra|novembra|decembra)\s*(\d{4})', re.I)


def mnum(w):
    w = w.lower()
    return next((v for k, v in MON if w.startswith(k)), None)


# ------------------------------------------------------------------ municipalities (25) and issuers
MUNI = [('andrijevica', r'Andrijevic'), ('bar', r'\bBar\b|\bBaru\b|\bBara\b'), ('berane', r'Beran'), ('bijelo-polje', r'Bijel\w* Polj'), ('budva', r'Budv'),
        ('cetinje', r'Cetinj|Prijestonic|Prijjestonic|Prestonic'), ('danilovgrad', r'Danilovgrad'), ('gusinje', r'Gusinj'), ('herceg-novi', r'Herceg[\s-]*Nov'),
        ('kolasin', r'Kola[sš]in'), ('kotor', r'Kotor'), ('mojkovac', r'Mojkov'), ('niksic', r'Nik[sš]i[cć]'), ('petnjica', r'Petnjic'),
        ('plav', r'\bPlav\b|\bPlavu\b|\bPlava\b'), ('pljevlja', r'Pljevlj|Pljevalj'), ('pluzine', r'Plu[zž]in'), ('podgorica', r'Glavn\w* grad|Podgoric'),
        ('rozaje', r'Ro[zž]aj'), ('savnik', r'[SŠ]avnik'), ('tivat', r'Tivat|Tivt'), ('tuzi', r'\bTuz[ia]\b|\bTuzima\b'), ('ulcinj', r'Ulcinj'),
        ('zabljak', r'[ZŽ]abljak'), ('zeta', r'\bZet[aeiu]\b|Golubov')]
MUNI_RX = [(k, RX(r)) for k, r in MUNI]


def muni_of(s):
    return next((k for k, rx in MUNI_RX if rx.search(s)), None)


VERB = RX(r'\b(donij?el[aoi]|donijelo|donosi|donio|donijeo|donese|utvrdi(?:o|la|lo)?|utvrđuje|propisuje|izdaje|raspisuje|objavljuje|'
                  r'proglašava|daje|imenuje|razrješava|bira|usvaja|usvojil[aoi]|d\s?o\s?n\s?i\s?j\s?e\s?l\s?a|d\s?o\s?n\s?o\s?s\s?i)\b', re.I)
SESS = RX(r'\bna\s+(?:[\w.]+\s+){0,4}(?:sjednici|sednici)\b')
NAOSN = re.compile(r'\b[Nn]a osnovu\b')
ISS = [
    ('parliament', RX(r'Skup[sš]tin\w*\s+(Republike\s+)?Crne\s+Gore|Ustavotvorn\w*\s+skup[sš]tin')),
    ('government', RX(r'\bVlad[aei]\b|\bVlada\s+RCG', 0)),
    ('president', RX(r'Predsjedni\w*\s+(Republike\s+)?Crne\s+Gore|Generaln\w* sekretarijat\w* predsjednika')),
    ('municipal', RX(r'Skup[sš]tin\w*\s+(gradske\s+)?(op[sš]tin|Glavnog|Prijestonic|Prijjestonic|Prestonic)|Predsjedni\w*\s+(gradske\s+)?op[sš]tin|Gradonačelni|'
                             r'Glavni administrator|Odbor\w* povjerenika|Op[sš]tinsk\w* izborn\w* komisij|Gradsk\w* izborn\w* komisij|Glavn\w* grad|Prijestonic|'
                             r'\bGradsk\w* op[sš]tin|\bop[sš]tin[aeiu]\b|Komunaln\w* polic|Sekretarijat\w* za|Služb\w* zaštite', re.I)),
    ('ministry', RX(r'Ministarstv|\b[Mm]inist(ar|arka|rica)\b|Ministrarstv|Direkcij\w* javnih prihoda|Poresk\w* uprav|Uprav\w* carina|Uprav\w* za')),
    ('cbank', RX(r'Centraln\w*\s+bank|Narodn\w* bank')),
    ('other', RX(r'Agencij|Komisij|Regulatorn|Savjet|\bFond|Zavod|\bUprav[ae]\b|Upravni odbor|Institut|Komor|Univerzitet|\bSud\b|Sudsk|Ustavn\w* sud|Tužil|Zaštitnik|'
                         r'Izborn|Direktor|direktor|Odbor|Senat|Revizorsk|Zajednic|Savez|Društv|Udruženj|Akademij|Biro|Služb|Centar|Kancelarij|Inspekcij|Generalni sekretar|'
                         r'Kolegij|Sindikat|Konferencij|Vijeć|Berz|Crven\w* krst|Matic')),
]
STATUTE = RX(r'Statut\w*\s+(gradske\s+)?(op[sš]tin\w*|Glavnog grada|Prijestonic\w*)\s+[^\s(,"]+(\s+[A-Z][^\s(,"]+)?')
STATUTE2 = RX(r'Statutarn\w* odluk\w* (gradske\s+)?op[sš]tin\w*\s+\S+')


def issuer(t):
    """(class, municipality, clause, text before the verb) from the normalised opening text: the words between the last
    citation of the legal basis and 'na ... sjednici' / the verb, or the words before 'Na osnovu' when the issuer is named first"""
    head = t[:2500]
    cut = len(head)
    for rx in (SESS, VERB):
        m = rx.search(head)
        if m: cut = min(cut, m.start())
    pre = head[:cut]
    k = max(pre.rfind(')'), pre.rfind('»'), pre.rfind('”'), pre.rfind('"'), pre.rfind('“'))
    clause = (pre[k + 1:] if k >= 0 else pre[-200:]).strip(' ,.;:-–')
    cands = [clause]
    m = NAOSN.search(head)
    if m and m.start() > 3: cands.append(head[:m.start()])
    if len(clause) < 4: cands.append(pre[-160:])
    cls = None
    for c in cands:
        cls = next((name for name, rx in ISS if rx.search(c)), None)
        if cls: clause = c; break
    mk = muni_of(clause) if cls == 'municipal' else None
    if not mk and cls in ('municipal', None):
        mm = STATUTE.search(pre) or STATUTE2.search(pre)
        if mm:
            mk = muni_of(mm.group(0))
            if mk and cls is None: cls = 'municipal'
    return cls, mk, clause[-160:], pre


# the gazettes cited in the legal basis: Službeni list of the SFRY (to 1992), of the Socialist Republic of Montenegro (to 1992),
# of the FRY (1992-2003), of Serbia and Montenegro (2003-2006), of the Republic of Montenegro (1992-2006), of Montenegro (since 2007)
GAZ = RX(r'(?:Sl\.?|Služben\w*|Sluzben\w*)\s*\.?\s*(?:list\w*|glasnik\w*)\s*["„“”«»\'’]*\s*'
                 r'(SFRJ|SRJ|SCG|SRCG|SR\s?CG|RCG|R\s?CG|CG|C\.\s?G\.?|Crne Gore|Republike Crne Gore|Srbije i Crne Gore|Savezne Republike Jugoslavije|'
                 r'Socijalističke Republike Crne Gore|SFR Jugoslavije|SR Crne Gore|SR Jugoslavije|Socijalističke Federativne)')


def era_key(g):
    g = re.sub(r'\s+', ' ', g).strip().upper().replace('.', '')
    if g.startswith('SFR') or g.startswith('SOCIJALISTICKE FEDERATIVNE'): return 'SFRJ'
    if g in ('SRCG', 'SR CG') or g.startswith('SOCIJALISTICKE REPUBLIKE') or g == 'SR CRNE GORE': return 'SRCG'
    if g in ('SRJ',) or g.startswith('SAVEZNE') or g == 'SR JUGOSLAVIJE': return 'SRJ'
    if g in ('SCG',) or g.startswith('SRBIJE'): return 'SCG'
    if g in ('RCG', 'R CG') or g.startswith('REPUBLIKE'): return 'RCG'
    return 'CG'


ERA_ORDER = ['SFRJ', 'SRCG', 'SRJ', 'SCG', 'RCG', 'CG']

FOLD1 = str.maketrans({'č': 'c', 'ć': 'c', 'š': 's', 'ž': 'z', 'đ': 'd', 'Č': 'C', 'Ć': 'C', 'Š': 'S', 'Ž': 'Z', 'Đ': 'D'})


def fold1(s):
    """diacritics folded one letter for one (đ -> d), so a span found in fold1(s) cuts the same words out of s"""
    return s.translate(FOLD1)


BASIS = re.compile(fold1(r'\b[Nn]a osnovu\s+(?:(?:člana|čl\.|članova|čl|tačke|stava|odredbe|odredaba|alineje|t\.)\s*[^Z]{0,120}?)?'
                         r'(Opšteg\s+zakona|Zakona|Zakonika|Zakon|Carinskog\s+zakona|Krivičnog\s+zakonika|Porodičnog\s+zakona|Ustava|Statuta|Statutarne|Uredbe|Odluke|Pravilnika|Poslovnika|Amandmana)\b\s*([^("“”«»]{0,160})'))
BASIS_CUT = re.compile(fold1(r'\s+(?:i|a u vezi|kao i)\s+(?:člana|čl\.|sa članom|u vezi|tačke)|,\s'))


def basis_law(t):
    """the first law named after 'Na osnovu', in the nominative ('Zakon o ...') and spelt as in the text, or None"""
    head = t[:2500]
    hf = fold1(head)
    m = BASIS.search(hf)
    if not m: return None
    kind = m.group(1).split()[-1].lower()
    if not kind.startswith('zakon'): return None
    seg, segf = head[m.start(2):m.end(2)], hf[m.start(2):m.end(2)]
    c = BASIS_CUT.search(segf)
    name = re.sub(r'\s+', ' ', seg[:c.start()] if c else seg).strip(' ,.;:-')
    if not re.match(r'o\s+\S', name, re.I): return None
    g1 = m.group(1).lower()
    if g1.startswith('carinsk'): return 'Carinski zakon'
    pre = 'Opšti zakon' if g1.startswith('opsteg') else 'Zakonik' if 'zakonik' in g1 else 'Zakon'
    name = re.sub(r'\s+(Crne Gore|Republike Crne Gore|RCG|CG)$', '', name)
    return (pre + ' ' + name)[:110]


SAZIV = RX(r'Skup[sš]tin\w*\s+(Republike\s+)?Crne\s+Gore,?\s+(\d{1,2})\.?\s+saziva')
ZASJ = RX(r'(prv\w*|drug\w*)?\s*(vanredn\w*|redovn\w*)\s+(\((proljećnj|prolećnj|proljetnj|jesenj)\w*\)\s+)?zasijedanj')
POSEBNA = RX(r'posebn\w* (sjednic|sednic)')
REVOTE = RX(r'ponovn?o\s+izglasa|ponovn\w* odlučivanj|ponovo odlučuj')


def law_session(t):
    """for a law (folded text): the Skupština's convocation, the kind of session, the day of the vote and of a second vote"""
    head = t[:2500]
    out = {}
    m = SAZIV.search(head)
    if m: out['saziv'] = int(m.group(2))
    s = ZASJ.search(head)
    if s:
        if s.group(2).lower().startswith('van'): out['sess'] = 'x'
        elif s.group(4): out['sess'] = 's' if s.group(4).lower().startswith('pro') else 'a'
        elif s.group(1): out['sess'] = 's' if s.group(1).lower().startswith('prv') else 'a'
        else: out['sess'] = 'r'
    elif POSEBNA.search(head): out['sess'] = 'p'
    ds = [(int(d.group(3)), mnum(d.group(2)), int(d.group(1)), d.start()) for d in DATE.finditer(head)]
    ds = [d for d in ds if d[1] and 1990 <= d[0] <= 2030]
    if ds: out['adopted'] = '%04d-%02d-%02d' % ds[0][:3]
    rv = REVOTE.search(head)
    if rv:
        before = [d for d in ds if d[3] < rv.start()]
        if len(before) >= 2:
            out['revote'] = '%04d-%02d-%02d' % before[-1][:3]
    return out


# EU legal acts cited in a text: a directive, regulation, decision or recommendation marked (EU), (EZ), (EEZ), (EC)...,
# a number such as 2001/83/EZ or (EU) 2016/679, or the Official Journal of the European Union
EU = RX(r'\b(?:Direktiv\w*|Regulativ\w*|Uredb\w*|Odluk\w*|Preporuk\w*|Smjernic\w*)\s+(?:[\w.]+\s+){0,4}?\(?(?:EU|EZ|EEZ|EC|EEC|EU/Euratom|Euratom)\)\s*(?:br\.|broj|No\.?)?\s*\d'
                r'|\b\d{2,4}/\d{1,4}/(?:EU|EZ|EEZ|EC|EEC|EK|ZVSP|CFSP)\b'
                r'|\((?:EU|EZ|EEZ|EC|EEC)\)\s*(?:br\.|broj|No\.?)?\s*\d{1,4}/\d{2,4}'
                r'|Služben\w* list\w* Evropsk\w* unij|Official Journal of the European'
                r'|\b(?:direktiv|regulativ)\w*\s+(?:Evropsk\w* unij|EU\b|Evropsk\w* zajednic|Savjeta\s+(?:EU|Evropsk\w* unij))')
NUM = r'\d[\d.,]*'
CUR = {'din': RX(r'(?:' + NUM + r')\s*(?:novih\s+|jugoslovensk\w*\s+)?(?:dinar\w*|din\b\.?|din/|YUM\b|NDIN\b)'),
       'dem': RX(r'(?:' + NUM + r')\s*(?:DEM\b|DM\b|njemačk\w*\s+mar\w*|nemačk\w*\s+mar\w*|maraka\b)', 0),
       'eur': RX(r'(?:' + NUM + r')\s*(?:eur(?:a|o|ima|u)?\b|EUR\b|€)|(?:€|\bEUR)\s*\d')}

# ------------------------------------------------------------------ load the tables
acts = []
for x in json.load(open(os.path.join(D, 'acts.json'), encoding='utf-8'))['acts']:
    acts.append({'slug': x['slug'], 'path': x['path'], 'kind': x['kind'], 'y': int(x['year']) if x['year'] else None, 'id': x['number'],
                 'title': re.sub(r'\s+', ' ', x['title']).strip(), 'status': x['status'], 'from': x['from'], 'pid': x['portal'].rstrip('/').rsplit('/', 1)[-1]})
A = {x['path']: x for x in acts}
laws = {}
with open(os.path.join(D, 'laws.csv'), encoding='utf-8', newline='') as f:
    for r in csv.DictReader(f):
        m = re.search(r'broj\s+(\d+)/(\d{4})\)', r['label'])
        if r['key'].startswith('amandman-'): continue          # the Constitution's amendments share their gazette page
        laws[r['url'].rstrip('/').rsplit('/', 1)[-1]] = {'pub': r['published'], 'inf': r['in_force_days'], 'issue': (m.group(1) + '/' + m.group(2)) if m else None}
for x in acts:
    l = laws.get(x['pid'], {})
    x['pub'] = l.get('pub') or None
    x['inf'] = l.get('inf') or x['from']
units = {}
for x in json.load(open(os.path.join(D, 'versions.json'), encoding='utf-8'))['acts']:
    units[x['path']] = x['versions'][-1].get('units')
held = json.load(open(os.path.join(D, 'held.json'), encoding='utf-8'))
held_reasons = held['by_reason']
held_ids = {str(h['id']) for h in held['acts']}
reg_ids = {x['id'] for x in acts}
held_only = [h for h in held['acts'] if str(h['id']) not in reg_ids]
held_amb_ids = {str(h['id']) for h in held_only if re.match(r'\s*ukaz', h['title'], re.I) and re.search(r'ambasador', h['title'], re.I)}
held_titles = [re.sub(r'\s+', ' ', h['title']).strip() for h in held_only]
HELD_N, HELD_OVERLAP = held['count'], len(held_ids & reg_ids)
del held
pending = json.load(open(os.path.join(D, 'pending.json'), encoding='utf-8'))
LOG = json.load(open(os.path.join(B, 'log.json'), encoding='utf-8'))
UST = json.load(open(os.path.join(B, 'ustav.json'), encoding='utf-8'))

# the tree: files of each act folder
folders, ustav_files, ukaz_files = DD(dict), {}, []
with open(os.path.join(B, 'tree.tsv'), encoding='utf-8') as f:
    for line in f:
        path, oid = line.rstrip('\n').split('\t')
        parts = path.split('/')
        if parts[0] == 'ustav': ustav_files[parts[1]] = oid; continue
        if parts[0] == 'ukaz': ukaz_files.append((path, oid)); continue
        d = '/'.join(parts[:4]) if parts[0] == 'odluka' else '/'.join(parts[:3])
        folders[d][path[len(d) + 1:]] = oid

FULL_ALL, FULL_UPTO = {'zakon', 'uredba', 'pravilnik'}, 2008
PENS = RX(r'usklađivanj\w* penzij|uskladjivanj\w* penzij')


def opener(fs):
    pick = next((c for c in ('0-uvod.md', 'tekst.md', 'text.md') if c in fs), None)
    if not pick:
        cl = sorted(f for f in fs if re.match(r'clan-\d+\.md$', f))
        pick = cl[0] if cl else None
    return pick


def order_key(f):
    m = re.match(r'clan-(\d+)', f)
    return (0, f) if f.startswith('0-') else (1, int(m.group(1)), f) if m else (2, f)


# ------------------------------------------------------------------ one pass over every act
F = {}
pens_text = {}
n_open = n_full = 0
for x in acts:
    fs = folders.get(x['path'])
    if not fs: continue
    op = opener(fs)
    if not op: continue
    raw = BL.get(fs[op]); n_open += 1
    t = norm(raw)
    tf = fold(t)
    r = {'sc': script_of(raw[:3000])}
    cls, mk, clause, pre = issuer(tf)
    if x['kind'] == 'zakon': cls, mk = 'parliament', None
    if x['kind'] == 'uredba' and cls is None: cls = 'government'
    r['iss'], r['mu'], r['cl'] = cls, mk, clause
    r['eras'] = sorted({era_key(m.group(1)) for m in GAZ.finditer(pre)}, key=ERA_ORDER.index)
    bl = basis_law(t)
    if bl: r['basis'] = bl
    if x['kind'] == 'zakon': r.update(law_session(tf))
    ft = fold(x['title'])
    full = x['kind'] in FULL_ALL or (x['y'] or 9999) <= FULL_UPTO or PENS.search(ft)
    if full:
        texts = [tf] + [fold(norm(BL.get(fs[f]))) for f in sorted(fs, key=order_key) if f != op and f not in ('README.md', 'record.json')]
        n_full += 1
        whole = ' '.join(texts)
        r['eu'] = len(EU.findall(whole))
        r['cur'] = {k: len(rx.findall(whole)) for k, rx in CUR.items()}
        if PENS.search(ft): pens_text[x['path']] = whole
    F[x['path']] = r
print('opening texts', n_open, 'full texts', n_full)

PF = {'built': '', 'head': SHA, 'acts': len(acts), 'commits': LOG['commits'], 'opening_texts': n_open, 'full_texts': n_full,
      'held': HELD_N, 'held_overlap': HELD_OVERLAP, 'held_reasons': held_reasons, 'pending': pending.get('count'), 'log_kinds': LOG['kinds']}
last_inf = max(x['inf'] for x in acts if x['inf'])
last_pub = max(x['pub'] for x in acts if x['pub'])
PF['built'] = last_inf if last_inf > last_pub else last_pub
PF['last_inf'], PF['last_pub'] = last_inf, last_pub
YEARS = list(range(1992, int(PF['built'][:4]) + 1))
OUT = {}

# ------------------------------------------------------------------ c01: what is in force, by year of publication and kind
KG = {'zakon': 'law', 'uredba': 'decree', 'pravilnik': 'rule', 'odluka': 'dec', 'rjesenje': 'ruling'}
rows = {y: C() for y in YEARS}
for x in acts:
    if x['y'] in rows: rows[x['y']][KG.get(x['kind'], 'other')] += 1
OUT['c01'] = {'rows': [dict(y=y, **rows[y]) for y in YEARS], 'kinds': dict(C(x['kind'] for x in acts)),
              'independence': A.get('odluka/2006/06/302424', {}).get('inf'), 'no_year': sum(1 for x in acts if not x['y'])}

# ------------------------------------------------------------------ c02: who adopted the acts in force
PERIODS = [(1992, 1997), (1998, 2002), (2003, 2006), (2007, 2011), (2012, 2016), (2017, 2021), (2022, YEARS[-1])]
ISSK = ['municipal', 'government', 'ministry', 'other', 'parliament', 'cbank', 'president', None]
iss_tot, iss_kind, iss_per = C(), DD(C), {p: C() for p in PERIODS}
for x in acts:
    r = F.get(x['path'])
    c = r['iss'] if r else None
    iss_tot[c] += 1; iss_kind[c][KG.get(x['kind'], 'other')] += 1
    for p in PERIODS:
        if x['y'] and p[0] <= x['y'] <= p[1]: iss_per[p][c] += 1
OUT['c02'] = {'tot': {str(k): v for k, v in iss_tot.items()}, 'kinds': {str(k): dict(v) for k, v in iss_kind.items()},
              'periods': [{'p': f'{a}–{b}', 'a': a, 'b': b, **{str(k): v for k, v in iss_per[(a, b)].items()}} for a, b in PERIODS]}

# ------------------------------------------------------------------ c03: Cyrillic or Latin, by year (state bodies and municipalities)
sc = {y: {'state': C(), 'mun': C()} for y in YEARS}
for x in acts:
    r = F.get(x['path'])
    if not r or not r['sc'] or x['y'] not in sc: continue
    sc[x['y']]['mun' if r['iss'] == 'municipal' else 'state'][r['sc']] += 1
OUT['c03'] = {'rows': [{'y': y, 'sc': sc[y]['state']['cyr'], 'sl': sc[y]['state']['lat'], 'mc': sc[y]['mun']['cyr'], 'ml': sc[y]['mun']['lat']} for y in YEARS],
              'unknown': sum(1 for x in acts if x['path'] in F and not F[x['path']]['sc'])}

# ------------------------------------------------------------------ c04: days from publication to entry into force, by kind
import datetime as _dt
DT = _dt.date.fromisoformat
LAG = ['neg', 'd0', 'd1', 'd27', 'd8', 'late']
def lag_bucket(n):
    return 'neg' if n < 0 else 'd0' if n == 0 else 'd1' if n == 1 else 'd27' if n < 8 else 'd8' if n == 8 else 'late'
groups = [('zakon', lambda x, r: x['kind'] == 'zakon'), ('uredba', lambda x, r: x['kind'] == 'uredba'), ('pravilnik', lambda x, r: x['kind'] == 'pravilnik'),
          ('odl_state', lambda x, r: x['kind'] == 'odluka' and r and r['iss'] != 'municipal'), ('odl_mun', lambda x, r: x['kind'] == 'odluka' and r and r['iss'] == 'municipal'),
          ('rjesenje', lambda x, r: x['kind'] == 'rjesenje'), ('ostalo', lambda x, r: x['kind'] in ('naredba', 'uputstvo', 'pravila', 'program', 'plan', 'statut', 'poslovnik', 'akt'))]
c04, lawyear = {}, DD(C)
for g, fn in groups:
    cc, lags = C(), []
    for x in acts:
        if not x['pub'] or not x['inf']: continue
        r = F.get(x['path'])
        if not fn(x, r): continue
        n = (DT(x['inf']) - DT(x['pub'])).days
        cc[lag_bucket(n)] += 1
        if n >= 0: lags.append(n)
        if g == 'zakon': lawyear[x['y']][lag_bucket(n)] += 1
    c04[g] = {**cc, 'n': sum(cc.values()), 'med': statistics.median(lags) if lags else None}
OUT['c04'] = {'groups': c04, 'lawyear': {str(y): dict(v) for y, v in sorted(lawyear.items())}}

# ------------------------------------------------------------------ c05/c06: laws, convocations, sessions, second votes
L5, RV = [], []
for x in acts:
    if x['kind'] != 'zakon': continue
    r = F.get(x['path']) or {}
    if r.get('saziv') and r.get('adopted'):
        L5.append([r['adopted'], r.get('sess') or 'u', r['saziv'], x['title'][:140], x['path'], x['pub']])
    if r.get('revote'):
        RV.append([r['adopted'], r['revote'], x['title'], x['path'], x['pub'], r.get('saziv')])
L5.sort(); RV.sort(key=lambda z: (z[1], z[0]))
nlaw = sum(1 for x in acts if x['kind'] == 'zakon')
OUT['c05'] = {'laws': L5, 'n_laws': nlaw, 'no_preamble': nlaw - len(L5)}
OUT['c06'] = {'laws': RV}

# ------------------------------------------------------------------ c07/c08: laws by area; amending laws and the law they amend
AMEND = re.compile(fold1(r'^\s*Zakon\w*\s+o\s+(?:izmjen\w*|dopun\w*|izmjeni|dopuni)(?:\s*(?:,|i)\s*(?:izmjen\w*|dopun\w*|izmjeni|dopuni))*\s+'
                         r'(Opšteg\s+zakona|Zakona|Zakonika|Carinskog\s+zakona|Krivičnog\s+zakonika|Porodičnog\s+zakona|Zakonika)\s+(.*)$'), re.I)
REPEAL = RX(r'^\s*Zakon\w*\s+o\s+prestanku\s+va[žz]enja')
RATIF = RX(r'\bpotvr(?:đ|dj)ivanj')


def law_base(title):
    """'Zakon o izmjenama i dopunama Zakona o X' -> 'Zakon o X', spelt as in the title (None if the title amends nothing)"""
    t = re.sub(r'\s+', ' ', title).strip().rstrip('.*').strip()
    m = AMEND.match(fold1(t))
    if not m: return None
    head = m.group(1).lower()
    pre = 'Opšti zakon' if head.startswith('opsteg') else 'Carinski zakon' if head.startswith('carinsk') else 'Krivični zakonik' if head.startswith('krivicn') \
        else 'Porodični zakon' if head.startswith('porodicn') else 'Zakonik' if 'zakonik' in head else 'Zakon'
    rest = re.sub(r'\s*\(.*$', '', t[m.start(2):m.end(2)]).strip().rstrip('.*,').strip()
    return (pre + ' ' + rest).strip()


# a law's area, from its title (an amending law: the name of the law it amends), folded and in lower case; rules in this order
AREAS = [
    ('other', r'\bpotvrdjivanj'),                                                     # ratifications
    ('env', r'bezbjednost\w* hran|zastit\w* bilja|zdravstven\w* zastit\w* bilja'), ('econ', r'bezbjednost\w* (saobracaj|plovidb)|sigurnost\w* (pomorsk|snabdijevanj)'),
    ('econ', r'ogranicavanj\w* cijen'), ('state', r'drustveno-politick'), ('fin', r'penzion\w* fond'), ('soc', r'zarazn\w* bolest'),
    ('fin', r'\b(porez|poresk|akciz|carin|taks|doprinos|budzet|zavrsn\w* racun|fiskal|racunovodstv|revizij|bank|kreditn|hartij|kapital|investicion\w* fond|platn|devizn|'
            r'igr\w* na srec|lutrij|stecaj|faktoring|lizing|sanacij|trezor|drzavn\w* pomoc|zaduz|dug|prihod|finansij|finansiranj|novc|novcan|zarad\w* zaposlenih u javnom|'
            r'banc|kredit|depozit|kamat|knjigovodstv|rezerv|obveznic)'),
    ('soc', r'na radu\b|\b(rad|radu|rada)\b|\b(radn\w* odnos|zaposljavanj|nezaposlen|penzij|socijaln|djecj|invalid|zarad|strajk|borack|borc|porodic|roditelj|materinstv|'
            r'volonter|kolektivn|zdravstv|zdravlj|ljekov|lijek|medicin|bolest|apotek|ljekar|transfuzi|transplant|psihoaktiv|drog|duvan|pusenj|stomatolo|trudnoc|biolosk|starij|'
            r'oboljel|mentaln|krv[iu]?\b|slijep|sindikat|sidikat|tkiv|presadjivanj|partnerstv|djec|izdrzavanj)'),
    ('fin', r'\bosiguranj'),
    ('edu', r'\b(obrazovanj|vaspitanj|skol|gimnazij|univerzitet|nauk|naucn|udzbenik|kultur|sport|medij|informisanj|kinematograf|bibliotek|arhiv|muzej|bastin|izdavack|'
            r'audiovizuel|radio|televizij|javn\w* servis|omladin|mlad|studen|ucenik|akademij|inovacij|skijalist|matic\w* crnogorsk)'),
    ('just', r'\b(sud|sudij|tuzila|tuzioc|krivicn|prekrsaj|parnic|vanparnic|izvrsenj|advokat|notar|medijacij|posredovanj|vjestac|amnesti|pomilovanj|kazn|zatvor|maloljet|'
             r'pravosudj|pravn\w* pomoc|oduzimanj|naknad\w* stet|obligacion|nasljedj|svojinsk|arbitraz|zalog|zaloz|odbran|vojsk|vojn|polic|unutrasnj|bezbjednost|oruzj|'
             r'eksploziv|granic|strana?c|azil|tajn|obezbjedjenj|detektiv|terorizm|vanredn\w* stanj|spasavanj|civiln\w* zastit|sajber|obavjestajn|pranj\w* novca|zvizdac|nepravilnost|'
             r'vojsc|javn\w* red|okupljanj|dnk|tumac|ovjer|privatn\w* prav)'),
    ('env', r'\b(prostor|planiranj|izgradnj|gradjevin|gradnj|stanovanj|stambe|komunaln|zivotn\w* sredin|otpad|vod[aeiou]?\b|vodama|vodosnabd|prirod|park|klim|zagadj|buk[aeiu]?\b|'
            r'hemikalij|zracenj|jonizuj|geolosk|katast|nepokretnost|svojin|eksproprijacij|denacionalizacij|restitucij|povracaj|legalizacij|bespravn|geodet|premjer|spomen|groblj|'
            r'sahranjivanj|zemljist|obal|morsk\w* dobr|poljoprivred|hran|prehramben|veterin|bilj|sjemen|sadn|ribarstv|ribolov|akvakultur|stocar|stocn|vin[aeiou]?\b|vinsk|vinograd|'
            r'vinarstv|sum[aeiu]|sumarstv|lov[aeiu]?\b|lovstv|divljac|pcel|ruraln|zadrug|zivotinj|genetick|navodnjavanj|melioracij|organsk|geografsk\w* porijekl|reproduktivn|'
            r'maslin|planinsk|vodosna|rafting|nepogod|zemljotres)'),
    ('econ', r'\b(energet|energij|elektricn|elektroenerget|gas|naft|rud|privred|drustv|trgovin|turizm|turistick|ugostitelj|zanat|konkurencij|nabavk|koncesij|javno-privatn|'
             r'standardizacij|akreditacij|metrolog|zig|patent|dizajn|autorsk|intelektualn|potrosac|cijen|investicij|ulaganj|zon[aeiu]?\b|registracij|djelatnost|trzist|robn\w* rezerv|'
             r'spoljn|saobracaj|put(evi|evima|eva|u|a)?\b|drum|zeljezn|vazdusn|vazduhoplov|pomorsk|plovidb|luk[aeiu]\b|luck|brod|jaht|prevoz|tahograf|vozac|vozil|aerodrom|autoput|'
             r'zicar|post[ae]\b|postansk|elektronsk\w* komunikacij|telekomunikacij|tehnick\w* zahtjev|proizvod|preduze|privatizacij|kompanij|komapnij|airlines|plantaz|kombinat|'
             r'aluminij|topografij|poluprovodnik|klasifikacij\w* djelatnost|ino dug|drustav|akcionar|kooperativ|oglasavanj|brend|uslug|optick|poslovanj)'),
    ('state', r'\b(drzavn|uprav|sluzbenik|namjestenik|samouprav|teritorijal|opstin|glavn\w* grad|prijestonic|vlad|predsjedni|skupstin|poslanik|odbornik|izbor|referendum|birac|'
              r'politick|maticn|licn|isprav|drzavljanstv|prebivalist|boravist|pecat|simbol|grb|zastav|himn|praznik|inspekcij|informacij|podatak|podataka|korupcij|zastitnik|'
              r'ombudsman|interes|statistik|popis|nevladin|udruzenj|fondacij|vjer|crkv|manjin|dijaspor|iseljen|ljudsk|ravnopravnost|diskriminacij|dinastij|potomak|potomaka|'
              r'digital|elektronsk|identifikacij|ustav|propis|naziv|sukcesij|imovin|odlikovanj|funkcioner|crven\w* krst|objavljivanj|medjunarodn\w* ugovor|revizorsk|imenu\b|'
              r'kontragarancij|savezn|jugoslavij|republik|ministarstv|spoljn\w* poslov|lustracij|nacionaln\w* savjet|vanjsk|imen[aeu]?\b|savjet)'),
    # fallbacks for the titles none of the rules above recognised
    ('env', r'emisij|morsk\w* sredin|vazduh|alkohol|sluzben\w* kontrol'), ('just', r'izvrsitelj|rjesavanj\w* sporov|kriticn\w* infrastruktur'),
    ('soc', r'radn\w* spor|krv[iu]?\b'), ('edu', r'kvalifikacij|akademsk'), ('econ', r'\b(luk(a|e|i|u|ama)|zon(a|e|i|u|ama))\b|izvoz|uvoz|regionaln\w* razvoj'),
    ('fin', r'referentn\w* vrijednost'),
    ('state', r'sluzbenic|namjestenic|registr\w* stanovnistv|popis\w* stanovnistv|restriktivn|racunanj\w* vremena|lobiranj|medjunarodn\w* razvojn'),
]
AREA_RX = [(k, re.compile(r, re.I)) for k, r in AREAS]


def law_area(title):
    b = law_base(title)
    t = fold(b or title).lower()
    t = re.sub(r'^\s*(opsti\s+)?zakon\w*\s+o\s+', '', t)
    return next((k for k, rx in AREA_RX if rx.search(t)), 'other')


LPER = [(1992, 2008), (2009, 2012), (2013, 2016), (2017, 2020), (2021, 2023), (2024, YEARS[-1])]
c07 = DD(lambda: {f'{a}–{b}': [0, 0] for a, b in LPER})
law_rows = []
for x in acts:
    if x['kind'] != 'zakon' or not x['y']: continue
    ar = law_area(x['title'])
    am = law_base(x['title']) is not None
    for a, b in LPER:
        if a <= x['y'] <= b:
            c07[ar][f'{a}–{b}'][0] += 1
            c07[ar][f'{a}–{b}'][1] += am
    law_rows.append([x['y'], ar, int(am), int(bool(REPEAL.match(x['title']))), x['title'][:150]])
OUT['c07'] = {'areas': {k: v for k, v in c07.items()}, 'periods': [f'{a}–{b}' for a, b in LPER], 'laws': law_rows}

base_years, base_titles = DD(list), {}
for x in acts:
    if x['kind'] != 'zakon': continue
    b = law_base(x['title'])
    if b:
        k = fold(b).lower()
        base_years[k].append(int(x['pub'][:4]) if x['pub'] else x['y'])
        if k not in base_titles or diacritics(b) > diacritics(base_titles[k]): base_titles[k] = b
held_base = C()
for t in held_titles:
    if re.match(r'\s*zakon', t, re.I):
        b = law_base(t)
        if b: held_base[fold(b).lower()] += 1
# the amended law itself: in the register (with its year) or among the acts held back
reg_titles = {}
for x in acts:
    if x['kind'] == 'zakon' and not law_base(x['title']):
        reg_titles.setdefault(fold(x['title'].rstrip('.*').strip()).lower(), x)
top = sorted(base_years, key=lambda k: (-len(base_years[k]), k))[:22]
OUT['c08'] = {'rows': [{'k': k, 'name': base_titles[k], 'years': sorted(base_years[k]), 'held': held_base.get(k, 0),
                        'base_y': reg_titles[k]['y'] if k in reg_titles else None, 'base_path': reg_titles[k]['path'] if k in reg_titles else None} for k in top],
              'amending': sum(len(v) for v in base_years.values()), 'bases': len(base_years), 'laws': nlaw}

# ------------------------------------------------------------------ c09: acts citing EU legal acts, by kind and year
c09 = {k: {} for k in ('zakon', 'uredba', 'pravilnik')}
for x in acts:
    if x['kind'] in c09 and x['y']:
        r = F.get(x['path'])
        if not r or 'eu' not in r: continue
        e = c09[x['kind']].setdefault(x['y'], [0, 0])
        e[0] += 1; e[1] += r['eu'] > 0
starred = C((x['kind'], x['y']) for x in acts if x['title'].rstrip().endswith('*'))
OUT['c09'] = {'rows': {k: [[y, *v] for y, v in sorted(d.items())] for k, d in c09.items()},
              'starred': [[k, y, n] for (k, y), n in sorted(starred.items(), key=lambda z: (z[0][0], z[0][1] or 0))]}

# ------------------------------------------------------------------ c10: the laws that are the legal basis of the most bylaws
BYK = ('pravilnik', 'uredba', 'naredba', 'uputstvo', 'pravila')
pl, plk, ply, pln = C(), DD(C), DD(C), {}
nby = 0
for x in acts:
    if x['kind'] not in BYK: continue
    nby += 1
    r = F.get(x['path'])
    if r and r.get('basis'):
        k = fold(r['basis']).lower()
        pl[k] += 1; plk[k][x['kind']] += 1; ply[k][x['y']] += 1
        if k not in pln or diacritics(r['basis']) > diacritics(pln[k]): pln[k] = r['basis']
OUT['c10'] = {'rows': [{'k': k, 'name': pln[k], 'n': n, 'kinds': dict(plk[k]), 'first': min(ply[k]), 'last': max(ply[k]),
                        'area': law_area(pln[k])} for k, n in pl.most_common(20)],
              'bylaws': nby, 'with_basis': sum(pl.values()), 'distinct': len(pl)}

# ------------------------------------------------------------------ c11: rulebooks by the area of the ministry (or other body) that made them, by year
MIN_AREAS = [  # on the issuer clause of a rulebook (folded): the same areas as the laws of chart 7
    ('env', r'poljoprivred|sumarstv|vodoprivred|ruraln|ribarstv|veterin|bezbjednost\w* hrane|odrzivog razvoja|uredjenja prostora|prostorn|urbaniz|ekologij|zivotne sredine|zastite zivotne|drzavne imovine'),
    ('fin', r'finansij|poresk|carin|javnih prihoda'),
    ('just', r'unutrasnj|polic|odbran|pravd|pravosudj'),
    ('soc', r'zdravlj|\brada\b|socijaln|zaposljavanj|porodic|manjinsk|ljudskih'),
    ('edu', r'prosvjet|nauk|obrazovanj|kultur|sport|medij|mladih'),
    ('econ', r'ekonom|energetik|rudarstv|turizm|privred|trgovin|saobracaj|pomorstv|vazduhoplov|kapitalnih investicij|investicij'),
    ('state', r'javne uprave|uprave|informacion|digital|vanjskih|spoljnih|evropskih poslova'),
]
MIN_RX = [(k, re.compile(r, re.I)) for k, r in MIN_AREAS]
c11 = DD(C)
for x in acts:
    if x['kind'] != 'pravilnik' or not x['y']: continue
    r = F.get(x['path']) or {}
    cl = r.get('cl') or ''
    if r.get('iss') in ('other', 'cbank'): k = 'reg'
    elif r.get('iss') == 'ministry' or re.search(r'ministar|ministr', cl, re.I):
        k = next((kk for kk, rx in MIN_RX if rx.search(cl)), 'other')
    else: k = 'other'
    c11[k][x['y']] += 1
OUT['c11'] = {'rows': {k: dict(v) for k, v in c11.items()}}

# ------------------------------------------------------------------ c12: the pandemic orders and decisions
COV = RX(r'koronavirus|corona|covid|sars-cov')
cov = []
for x in acts:
    if COV.search(fold(x['title'])):
        r = F.get(x['path']) or {}
        cov.append([x['pub'], x['kind'], r.get('iss'), x['title'][:200], x['path'], x['inf'], fold(r.get('basis') or '').lower()])
cov.sort()
OUT['c12'] = {'acts': cov}

# ------------------------------------------------------------------ c13: the Constitution, provision by provision
readme = BL.get(ustav_files['README.md'])
prov = []
for line in readme.split('\n'):
    m = re.match(r'^\|\s*(.+?)\s*\|\s*\[([\w.-]+)\]\(', line)
    if m and m.group(2) != 'README.md': prov.append((m.group(1), m.group(2)))
changed = DD(list)
amend = []
for cmt in UST:
    if cmt['a'].startswith('Amandman'):
        amend.append({'a': cmt['a'], 'd': cmt['d'], 'files': cmt['files']})
        for f in cmt['files']: changed[f.split('/')[-1]].append([cmt['a'].replace('Amandman ', ''), cmt['d']])
cprov = []
for label, f in prov:
    txt = BL.get(ustav_files[f]) if f in ustav_files else ''
    sub = next((l[3:].strip() for l in txt.split('\n') if l.startswith('## ')), '')
    cprov.append({'f': f, 'l': label, 'sc': script_of(txt), 'am': changed.get(f, []), 'sub': norm(sub),
                  'cyr': len(CYR.findall(txt)), 'lat': len(LAT.findall(txt)), 'n': int(f[5:8]) if f.startswith('clan-') else None})
OUT['c13'] = {'prov': cprov, 'amend': amend}

# ------------------------------------------------------------------ c14: ambassadors appointed and recalled by decree
HOST = [  # (code, rule) on the words after "u"/"pri"/"za" in the decree's title
    ('UN', r'Ujedinjen\w* nacij|\bUN\b|OUN'), ('EU', r'Evropsk\w* unij|\bEU\b|Brisel'), ('NATO', r'NATO|Sjevernoatlantsk'), ('OSCE', r'OEBS|OSCE|Organizacij\w* za evropsk\w* bezbjednost'),
    ('COE', r'Savjet\w* Evrope|Vijeć\w* Evrope|Strazbur'), ('UNESCO', r'UNESCO|Pariz.*UNESCO'), ('UNGE', r'Ženev'), ('VA', r'Svet\w* Stolic|Vatikan'), ('SMOM', r'Malteš|Suveren\w* vojn\w* red'),
    ('RS', r'Srbij'), ('BA', r'Bosn\w* i Hercegovin|BiH|Bosni'), ('HR', r'Hrvatsk'), ('MK', r'Makedonij|Sjevern\w* Makedonij'), ('SI', r'Slovenij'), ('AL', r'Albanij'), ('XK', r'Kosov'),
    ('IT', r'Itali'), ('DE', r'Njemačk|Nemačk|Savezn\w* Republi\w* Njema'), ('FR', r'Francusk'), ('GB', r'Ujedinjen\w* Kraljev|Velik\w* Britanij'), ('US', r'Sjedinjen\w* Američk|\bSAD\b'),
    ('RU', r'Rusk\w* Federacij|Rusij'), ('CN', r'Kin[aeiu]\b|Kinesk|Narodn\w* Republi\w* Kin'), ('TR', r'Turs|Turk'), ('AT', r'Austrij'), ('HU', r'Mađarsk|Madjarsk'), ('GR', r'Grčk|Grck'),
    ('BE', r'Belgij'), ('NL', r'Holandij|Nizozemsk|Kraljevin\w* Holand'), ('ES', r'Španij|Spanij'), ('PT', r'Portugal'), ('PL', r'Poljsk'), ('CZ', r'Češk|Česk|Ceska'), ('SK', r'Slovačk|Slovack'),
    ('RO', r'Rumunij'), ('BG', r'Bugarsk'), ('UA', r'Ukrajin'), ('SE', r'Švedsk|Svedsk'), ('NO', r'Norvešk|Norvesk'), ('DK', r'Dansk'), ('FI', r'Finsk'), ('CH', r'Švajcarsk|Svajcarsk|Konfederacij'),
    ('IE', r'Irsk'), ('IL', r'Izrael'), ('EG', r'Egip'), ('AE', r'Ujedinjen\w* Arapsk\w* Emirat|\bUAE\b'), ('SA', r'Saudijsk'), ('QA', r'\bKatar'), ('KW', r'Kuvajt'), ('AZ', r'Azerbejdžan|Azerbejdzan'),
    ('JP', r'Japan'), ('IN', r'\bIndij'), ('KR', r'Korej'), ('KZ', r'Kaza[hk]stan'), ('BR', r'Brazil'), ('AR', r'Argentin'), ('CA', r'Kanad'), ('MT', r'\bMalt'), ('SM', r'San Marin'), ('AM', r'Jermenij'),
    ('LU', r'Luksemburg'), ('CY', r'Kipar|Kipr'), ('LT', r'Litvanij'), ('LV', r'Letonij'), ('EE', r'Estonij'), ('MD', r'Moldavij|Moldov'), ('GE', r'Gruzij'), ('BY', r'Bjelorusij'), ('AU', r'Australij'),
    ('MX', r'Meksi[kč]'), ('CL', r'Čile|Cile'), ('ID', r'Indonezij'), ('MA', r'Marok'), ('DZ', r'Alžir|Alzir'), ('TN', r'\bTunis'), ('LY', r'\bLibij'), ('IR', r'\bIran'), ('PK', r'Pakistan'), ('MY', r'Malezij'),
    ('SG', r'Singapur'), ('TH', r'Tajland'), ('VN', r'Vijetnam'), ('ZA', r'Južnoafričk|Juzno'), ('NG', r'Nigerij'), ('CU', r'Kub[aeiu]\b'), ('JO', r'\bJordan'), ('LB', r'\bLiban'), ('IS', r'\bIsland'),
    ('MC', r'\bMonak'), ('AD', r'\bAndor'), ('LI', r'Lihtenštajn'), ('UZ', r'Uzbekistan'), ('TM', r'Turkmenistan'), ('MN', r'Mongolij'), ('NZ', r'Nov\w* Zeland'), ('OM', r'\bOman'), ('BH', r'Bahrein'), ('CR', r'Kostarik'), ('UY', r'Urugvaj'), ('ET', r'Etiopij'), ('PS', r'Palestin'), ('KG', r'Kirgi[sz]'),
    ('ASEAN', r'ASEAN'), ('AFU', r'Afričk\w* [Uu]nij'), ('WTO', r'Svjetsk\w* trgovinsk'),
]
HOST_RX = [(k, RX(r)) for k, r in HOST]
amb = []
for path, oid in ukaz_files:
    txt = BL.get(oid)
    title = re.sub(r'^#\s*', '', txt.split('\n', 1)[0]).strip()
    m = re.search(r'·\s*(Službeni list[^·]*?),\s*broj\s+(\d+)/(\d{4})\s*·\s*in force\s+(\d{4}-\d\d-\d\d)', txt)
    day = m.group(4) if m else None
    tl = fold(norm(title))
    kind = 'rec' if re.search(r'opoziv', tl, re.I) else 'app' if re.search(r'postavlj|imenovanj', tl, re.I) else 'oth'
    tail = re.split(r'\s+(?:u|pri|za|kod)\s+|\s+-\s+', tl, maxsplit=0)
    tail = ' '.join(tail[1:]) if len(tail) > 1 else tl
    hits = sorted((m.start(), k) for k, rx in HOST_RX for m in [rx.search(tail)] if m)   # the state named first
    host = hits[0][1] if hits else next((k for k, rx in HOST_RX if rx.search(tl)), None)
    amb.append([day, kind, host, title[:200], path.rsplit('/', 1)[0]])
amb.sort(key=lambda z: z[0] or '')
ukaz_ids = {path.split('/')[2] for path, _ in ukaz_files}
OUT['c14'] = {'decrees': amb, 'held_only': len(held_amb_ids - ukaz_ids), 'held_all': len(held_amb_ids)}

# ------------------------------------------------------------------ c15: the oldest gazette cited in the legal basis, by year
c15 = {y: C() for y in YEARS}
for x in acts:
    if x['kind'] in ('zakon',) or x['y'] not in c15: continue
    r = F.get(x['path'])
    if not r: continue
    e = r['eras']
    c15[x['y']][e[0] if e else 'none'] += 1
OUT['c15'] = {'rows': [{'y': y, **c15[y]} for y in YEARS]}

# ------------------------------------------------------------------ c16: the currency of amounts, acts published up to 2008
c16 = {y: C() for y in range(1992, FULL_UPTO + 1)}
for x in acts:
    if not x['y'] or x['y'] > FULL_UPTO: continue
    r = F.get(x['path'])
    if not r or 'cur' not in r: continue
    c = r['cur']; d, m_, e = c['din'] > 0, c['dem'] > 0, c['eur'] > 0
    k = 'none' if not (d or m_ or e) else 'eur' if e and not d else 'dem' if m_ and not e else 'din' if d and not m_ and not e else 'mix'
    c16[x['y']][k] += 1
OUT['c16'] = {'rows': [{'y': y, **c16[y]} for y in sorted(c16)]}

# ------------------------------------------------------------------ c17/c18/c19: municipalities
MKIND = C()
mun = DD(lambda: {'n': 0, 'cyr': 0, 'lat': 0, 'first': 9999, 'kinds': C(), 'years': C()})
for x in acts:
    r = F.get(x['path'])
    if not r or r['iss'] != 'municipal': continue
    mk = r['mu'] or '?'
    e = mun[mk]
    e['n'] += 1
    if r['sc']: e[r['sc']] += 1
    if x['y']: e['first'] = min(e['first'], x['y']); e['years'][x['y']] += 1
    e['kinds'][KG.get(x['kind'], 'other')] += 1
OUT['c17'] = {'mun': {k: {**v, 'kinds': dict(v['kinds']), 'years': dict(v['years'])} for k, v in mun.items()}}

TOPICS = [  # on the title of a municipal act, folded and in lower case, in this order (an amending or repealing act: by the words of the act it changes)
    ('appoint', r'\b(?:imenovanj|razrjesenj|razrjesavanj|razresenj|izbor\w*\b|prestank\w* mandat|potvrdjivanj\w* mandat|utvrdjivanj\w* prestank|postavljenj|'
                r'potvrdjivanj\w* (?:izbor|imenovanj))'),
    ('consent', r'\bsaglasnost'),
    ('budget', r'\b(?:budzet|zavrsn\w* racun|privremen\w* finansiranj|zaduzenj|zaduzivanj|kredit|rebalans|dobit|raspodjel\w* sredstav|subvencij|finansiranj\w* rada|'
               r'trezor|garancij)'),
    ('plan', r'\b(?:urbanistick|dup\b|lokaln\w* studij|studij\w* lokacij|prostorn\w* plan|prostorno-urbanistick|plan\w* generaln|generaln\w* regulacij|lokacij|parcelacij|'
             r'planskog|planskih|pup\b|gup\b|izrad\w* (?:izmjen|plan|detaljn|lokaln|urbanist|studij|program uredj)|nacrt\w* plan|program\w* uredjenja|uredjenj\w* prostor|'
             r'detaljn\w* urbanist|privremen\w* objek)'),
    ('fees', r'\b(?:naknad|tak[sz]|porez|prirez|oslobadjanj\w* placanj|cijen|cjenovnik|tarif|boravisn|koeficijent)'),
    ('services', r'\b(?:komunaln|cistoc|otpad|prevoz|saobracaj|parking|parkiralist|vodosnabdijevanj|vodovod|kanalizacij|groblj|pogrebn|rasvjet|zelenil|pijac|'
                 r'zoohigijen|kucn\w* ljubim|pasa\b|psa\b|vodn\w* objek|putev|ulic\w* i|javn\w* povrsin|zimsk\w* sluzb|plaz)'),
    ('property', r'\b(?:prenos\w* prava|otkup|prodaj|razmjen|zakup|davanj\w* na koriscenj|davanj\w* u|nepokretnost|zemljist|eksproprijacij|sluznost|kupovin|pribavljanj|'
                 r'imovin|poklon|darovanj|katastarsk|parcel|objekt|stan\b|stanov[ae]\b|poslovn\w* prostor|koncesij|lovist)'),
    ('progr', r'\b(?:program|strategij|akcion\w* plan|plan\w* razvoj|stratesk|izvjestaj|izvjestaj|plan\w* rada|lokaln\w* plan|plan\b|plana\b|planom\b|bilans|investicion)'),
    ('social', r'\b(?:socijaln|djecj|pomoc|stipendij|stambe|ucenik|student|skol|obrazovanj\w* (?:i|odrasl)|kultur|sport|omladin|mlad|zdravstv|penzioner|invalid|'
               r'borack|romsk|nevladin|vjersk|kulturn)'),
    ('org', r'\b(?:statut|poslovnik|organizacij|sistematizacij|osnivanj|obrazovanj\w* (?:komisij|odbor|savjet|radn|koordinacion|tim)|savjet|komisij|odbor|drustv|'
            r'ustanov|preduzec|mjesn\w* zajednic|pravilnik|kodeks|etick|zarad|funkcioner|sluzbenik|namjestenik|lokaln\w* uprav|sekretarijat|sluzb\w* zastit|'
            r'izborn\w* komisij|birack|referendum|ovlascenj|povjeravanj|vrsioc)'),
    ('names', r'\b(?:naziv|nagrad|priznanj|ziri|spomen|obiljezj|pocasn|grb|zastav|praznik|dan opstine|jubile|bratimljenj|saradnj|prijateljstv|inicijativ|naselj)'),
]
TOP_RX = [(k, re.compile(r, re.I)) for k, r in TOPICS]
REPEALT = RX(r'stavljanj\w* van snage|prestank\w* važenj\w*')
c19, c19y = C(), DD(C)
for x in acts:
    r = F.get(x['path'])
    if not r or r['iss'] != 'municipal': continue
    t = fold(x['title']).lower()
    k = next((kk for kk, rx in TOP_RX if rx.search(t)), 'other')
    c19[k] += 1
    if x['y']: c19y[k][x['y']] += 1
OUT['c19'] = {'n': {k: v for k, v in c19.items()}, 'years': {k: dict(v) for k, v in c19y.items()}}

# ------------------------------------------------------------------ c20: pension adjustments
# the percentage each decision of the pension fund sets, read from its point 1 (texts folded); a cut is negative
PNUM = r'(\d{1,3}(?:\.\d{3})+(?:,\s?\d+)?|\d+(?:[.,]\s?\d+)?)'      # 5.185.520,9 | 1.345 | 2,13 | 2, 08 | 1.98
PCT_DOWN = RX(r'smanjuju(?:\s+se)?\s+(?:za\s+){1,2}' + PNUM + r'\s*%')
PCT_VIS = RX(r'u visini(?:\s+od)?\s+' + PNUM + r'\s*%')
PCT_UP = RX(r'\b(?:za|u procentu(?: od)?)\s+' + PNUM + r'\s*%')


def pnum(s):
    """a number as the decisions write it: dots group thousands when a comma or three digits follow, the comma is the decimal mark"""
    s = s.replace(' ', '')
    if ',' in s: return float(s.replace('.', '').replace(',', '.'))
    if re.fullmatch(r'\d{1,3}(?:\.\d{3})+', s): return float(s.replace('.', ''))
    return float(s)
NONE_RX = RX(r'nijesu ispunjeni uslovi')
FORMULA = [('m', r'u mjesecu|za mjesec|u odnosu na cijel\w* \d{4}|neto[- ]zarad|u \d{4}\. godini u odnosu na (?:prosječnu|prosjecnu)|u periodu'),
           ('h', r'polovine procenta rasta'), ('q', r'prethodn\w* kvartal\w*|prethodna četiri mjeseca|četiri mjeseca'),
           ('y', r'75% procenta|25% procenta|u \d{4}\. godini u odnosu na \d{4}'), ('x', r'.')]
FORMULA_RX = [(k, RX(r)) for k, r in FORMULA]
MNOM = {'januar': 1, 'februar': 2, 'mart': 3, 'april': 4, 'maj': 5, 'jun': 6, 'jul': 7, 'avgust': 8, 'septembar': 9, 'oktobar': 10, 'novembar': 11, 'decembar': 12}
MLOC = {'januaru': 1, 'februaru': 2, 'martu': 3, 'aprilu': 4, 'maju': 5, 'junu': 6, 'julu': 7, 'avgustu': 8, 'septembru': 9, 'oktobru': 10, 'novembru': 11, 'decembru': 12}


def pens_month(title):
    """the month the decision's title names: 'od 1. maja 2023', 'za mjesec januar 1994', 'u junu 1995. godine', 'u periodu jul 2002 - decembar 2003'"""
    t = fold(norm(title)).lower().replace('2ooo', '2000')
    m = re.search(r'\bod\s+(\d{1,2})\.\s*(januara|februara|marta|aprila|maja|juna|jula|avgusta|septembra|oktobra|novembra|decembra)\s*(\d{4})', t)
    if m: return '%04d-%02d' % (int(m.group(3)), mnum(m.group(2)))
    m = re.search(r'za\s+mjesec\s+(' + '|'.join(MNOM) + r')\s+(\d{4})', t)
    if m: return '%04d-%02d' % (int(m.group(2)), MNOM[m.group(1)])
    m = re.search(r'\bu\s+(' + '|'.join(MLOC) + r')\s+(\d{4})', t)
    if m: return '%04d-%02d' % (int(m.group(2)), MLOC[m.group(1)])
    m = re.search(r'decembar\s+(\d{4})', t)
    if m: return '%04d-12' % int(m.group(1))
    return None


pens = []
for x in acts:
    if x['path'] not in pens_text: continue
    t = pens_text[x['path']]
    body = t[t.find(' 1.') if ' 1.' in t else 0:]
    v, how = None, None
    m = PCT_DOWN.search(body)
    if m: v, how = -pnum(m.group(1)), 'down'
    else:
        m = PCT_VIS.search(body) or PCT_UP.search(body)
        if m: v, how = pnum(m.group(1)), 'up'
    if v is None and NONE_RX.search(body): v, how = 0.0, 'none'
    fm = next(k for k, rx in FORMULA_RX if rx.search(body))
    ft = fold(x['title']).lower()
    sp = 'new' if re.search(r'osiguranike koji pravo|preindeksacij|u odnosu na cijel', ft) else 'extra' if 'vanredn' in ft else 'reg'
    pens.append([pens_month(x['title']) or (x['pub'] or '')[:7], v, how, fm, x['title'][:220], x['path'], x['pub'], sp,
                 x['kind']])
pens.sort()
OUT['c20'] = {'dec': pens}

# ------------------------------------------------------------------ profile
PF['kinds'] = dict(C(x['kind'] for x in acts))
PF['status'] = dict(C(x['status'] for x in acts))
PF['laws'] = nlaw
PF['municipal'] = iss_tot['municipal']
PF['amendments'] = len(amend)
PF['ukaz'] = len(ukaz_files)
PF['first_pub'] = min(x['pub'] for x in acts if x['pub'])
OUT['profile'] = PF
json.dump({'charts': OUT, 'profile': PF}, open(os.path.join(B, 'data.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('data.json written; built', PF['built'])
