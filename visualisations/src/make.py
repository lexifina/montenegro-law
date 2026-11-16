"""Rebuild visualisations/crnogorsko-pravo-u-20-grafikona.html from this repository.

    python visualisations/src/make.py [--repo PATH] [--ref REF]

Steps (read-only on the repository; scratch output goes to visualisations/src/.build/):
  1. the blobs the charts read are fetched in batches if the clone lacks them (a blobless clone);
     nothing else is downloaded: the data tables, the Constitution, the ambassadors' decrees (ukaz/),
     the opening file of every act (its preamble), every file of the laws, Government decrees and rulebooks,
     every file of the other acts published up to 2008, and the pension adjustment decisions
  2. data/acts.json, laws.csv, held.json, versions.json, pending.json, status.json -> .build/repo/data/
  3. the tree of REF (path and blob id of each file in the act folders)    -> .build/tree.tsv
  4. git log: the Constitution's amendment commits, and every commit's Kind -> .build/ustav.json, .build/log.json
  5. prep.py reads the tables and the act texts (git cat-file) into .build/data.json; build.py fills page.tpl.html.
Works in a blobless or --no-checkout clone, because everything is read from git objects.
"""
import argparse, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument('--repo', default=os.path.abspath(os.path.join(HERE, '..', '..')))
ap.add_argument('--ref', default=None, help='default: origin/main if present, else HEAD')
ap.add_argument('--out', default=os.path.join(HERE, '..', 'crnogorsko-pravo-u-20-grafikona.html'))
ap.add_argument('--no-fetch', action='store_true', help='never download missing blobs (fail instead)')
a = ap.parse_args()
B = os.path.join(HERE, '.build')
os.makedirs(os.path.join(B, 'repo', 'data'), exist_ok=True)
ENV = dict(os.environ, GIT_NO_LAZY_FETCH='1')   # nothing is fetched behind our back


def git(*args, inp=None):
    return subprocess.run(['git', '-C', a.repo, *args], input=inp, check=True, capture_output=True, env=ENV).stdout


ref = a.ref
if not ref:
    ref = 'origin/main' if subprocess.run(['git', '-C', a.repo, 'rev-parse', '--verify', '-q', 'origin/main'], capture_output=True).returncode == 0 else 'HEAD'
sha = git('rev-parse', ref + '^{commit}').decode().strip()
print('ref', ref, sha, flush=True)


def prefetch(oids, what):
    """fetch the blobs among oids that the clone does not have (batches of 4000; never an empty request)"""
    oids = sorted(set(oids))
    if not oids: return
    have = git('cat-file', '--batch-check', inp=('\n'.join(oids) + '\n').encode()).decode().splitlines()
    missing = [l.split()[0] for l in have if l.endswith(' missing')]
    print(f'{what}: {len(oids)} blobs, {len(missing)} to fetch', flush=True)
    if missing and a.no_fetch: sys.exit('missing blobs and --no-fetch')
    for i in range(0, len(missing), 4000):
        chunk = missing[i:i + 4000]
        if not chunk: break
        subprocess.run(['git', '-C', a.repo, '-c', 'fetch.negotiationAlgorithm=noop', 'fetch', 'origin', '--no-tags', '--no-write-fetch-head',
                        '--recurse-submodules=no', '--filter=blob:none', '--stdin'], input=('\n'.join(chunk) + '\n').encode(), check=True, capture_output=True)


# 1a. the data tables
TABLES = ['acts.json', 'laws.csv', 'held.json', 'versions.json', 'pending.json', 'status.json']
oid_of = {}
for line in git('ls-tree', sha, '--', *['data/' + t for t in TABLES]).decode('utf-8').splitlines():
    meta, path = line.split('\t', 1)
    oid_of[path] = meta.split()[2]
prefetch(oid_of.values(), 'data tables')
for t in TABLES:
    with open(os.path.join(B, 'repo', 'data', t), 'wb') as f:
        f.write(git('cat-file', 'blob', oid_of['data/' + t]))

# 1b. the tree: one line per file of the act folders, the Constitution and the decrees
KINDS = {'akt', 'naredba', 'odluka', 'plan', 'poslovnik', 'pravila', 'pravilnik', 'program', 'rjesenje', 'statut', 'ugovor', 'uputstvo', 'uredba', 'zakon'}
FULL_ALL = {'zakon', 'uredba', 'pravilnik'}          # every file read (EU citations)
FULL_UPTO = 2008                                      # other kinds: every file read up to this year (currency of amounts)
acts = json.load(open(os.path.join(B, 'repo', 'data', 'acts.json'), encoding='utf-8'))['acts']
pension = {x['path'] for x in acts if re.search(r'usklađivanj\w* penzij|uskladjivanj\w* penzij', x['title'], re.I)}
del acts
need, folders = [], {}
p = subprocess.Popen(['git', '-C', a.repo, 'ls-tree', '-r', sha], stdout=subprocess.PIPE, env=ENV)
with open(os.path.join(B, 'tree.tsv'), 'w', encoding='utf-8', newline='\n') as out:
    for raw in p.stdout:
        meta, path = raw.decode('utf-8').rstrip('\n').split('\t', 1)
        parts = path.split('/')
        top = parts[0]
        if top not in KINDS and top not in ('ustav', 'ukaz'): continue
        oid = meta.split()[2]
        out.write(path + '\t' + oid + '\n')
        if top == 'ustav' or top == 'ukaz':
            need.append(oid); continue
        d = '/'.join(parts[:4]) if top == 'odluka' else '/'.join(parts[:3])
        f = path[len(d) + 1:]
        if f in ('README.md', 'record.json'): continue
        try: y = int(parts[1])
        except ValueError: y = 9999
        if top in FULL_ALL or y <= FULL_UPTO or d in pension:
            need.append(oid)
        else:
            folders.setdefault(d, {})[f] = oid
p.wait()
# the opening file of every other act: its preamble (0-uvod.md), else its whole text (tekst.md, text.md), else its first article
for d, fs in folders.items():
    pick = next((c for c in ('0-uvod.md', 'tekst.md', 'text.md') if c in fs), None)
    if not pick:
        cl = sorted(f for f in fs if re.match(r'clan-\d+\.md$', f))
        pick = cl[0] if cl else None
    if pick: need.append(fs[pick])
del folders
prefetch(need, 'act texts')
del need

# 2. the Constitution's history: every commit on ustav/ (author, day, files)
ust, cur = [], None
for line in git('log', sha, '--reverse', '--format=@@C %H|%ad|%an', '--date=short', '--name-only', '--', 'ustav', ':!ustav/README.md').decode('utf-8').split('\n'):
    if line.startswith('@@C '):
        h, ad, an = line[4:].split('|', 2)
        cur = {'h': h, 'd': ad, 'a': an, 'files': []}; ust.append(cur); continue
    if line.strip() and cur: cur['files'].append(line.strip())
json.dump(ust, open(os.path.join(B, 'ustav.json'), 'w', encoding='utf-8'), ensure_ascii=False)
print('ustav commits', len(ust), flush=True)

# 3. every commit's Kind trailer and author day (streamed)
kinds, n, first, last = {}, 0, None, None
p = subprocess.Popen(['git', '-C', a.repo, 'log', sha, '--format=%ad|%(trailers:key=Kind,valueonly,separator=;)', '--date=short'], stdout=subprocess.PIPE, env=ENV)
for raw in p.stdout:
    d, _, k = raw.decode('utf-8', 'replace').rstrip('\r\n').partition('|')
    k = k.strip() or '(none)'
    kinds[k] = kinds.get(k, 0) + 1; n += 1
    first = d if first is None or d < first else first
    last = d if last is None or d > last else last
p.wait()
json.dump({'commits': n, 'kinds': kinds, 'first': first, 'last': last}, open(os.path.join(B, 'log.json'), 'w', encoding='utf-8'))
print('commits', n, flush=True)

# 4. prep + build
env = dict(ENV, HEAD_SHA=sha, REPO=a.repo)
subprocess.run([sys.executable, '-X', 'utf8', os.path.join(HERE, 'prep.py'), B], check=True, env=env)
subprocess.run([sys.executable, '-X', 'utf8', os.path.join(HERE, 'build.py'), os.path.join(B, 'data.json'), os.path.abspath(a.out)], check=True)
