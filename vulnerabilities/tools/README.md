# Tools

The scripts behind this Montenegro-only run of global-law's vulnerability detectors. They run inside a copy of
[global-law/vulnerabilities/scripts](https://github.com/lexifina/global-law/tree/main/vulnerabilities/scripts) (Python 3.11+,
`pip install duckdb pyarrow`), with a bare clone of this repository at `sources/corpus/montenegro-law.git`, a blobless bare
clone of global-law at `sources/global-law.git`, and a `pins.json` that names only montenegro-law and its commit.
`build_vulns.py`, `flags_chart.py`, `late_ext_select.py`, `late_ext_rebut.py` and `config.json` sit two folders above it.

| Script | What it does |
| --- | --- |
| `run.sh` | Indexes the history and texts, adds Montenegro's history rows, and runs the detectors |
| `add_root.py` | Builds Montenegro's history rows from this repository's own commits, so the history detectors read every change |
| `run_triage.sh` | The model review: the 40 strongest flags per category, the 40 strongest lapsed time limits in law texts, and the empty periods |
| `late_ext_select.py` | Chooses the 40 empty periods for global-law's review of that category (none were found here) |
| `late_ext_rebut.py` | Adds the second, arguing-against pass to the empty-period review, as `triage.py` does for the other categories |
| `build_vulns.py` | Builds `data/flags.csv`, `data/reviewed.csv` and `data/by_category.csv` from the findings and the model review |
| `flags_chart.py` | Draws the chart at the top of the READMEs, in Montenegrin and English, light and dark |
| `config.json` | The repository, the Montenegrin category names, the folders that are not law, and the chart's labels |

The model review needs `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL` and `LLM_AUTH` set for an OpenAI-compatible Responses API.

Two changes were made for this repository:

- `add_root.py` counted only commits with no `Kind:` trailer, or `as-promulgated`, `law`, `amendment` or `original`, as law
  changes. This repository marks an act's text with `Kind: decree` (by-laws, decisions and rulings, 35,150 commits),
  `as-enacted` (179) and `treaty` (142) as well, so those three were added: 36,629 commits count as law changes, and the
  292 metadata-only records, the case law and the documentation keep their own kind.
- `run.sh` reads `LE_WORKERS` and `LE_GREP_THREADS` from the environment; this run used `LE_WORKERS=3 LE_GREP_THREADS=3 bash run.sh 3`.
  `ingest/refscan.py --fileact` is not run, so `run.sh` writes an empty `index/refs_fileact` table for `detectors/ref_detectors.py`.

The lapsed-limit scan (`ingest/textscan.py`) is unchanged. It reads "do" ("until") before a date, but its month list lacks
the Montenegrin genitive names of five months (januara, februara, marta, juna, jula) and every Cyrillic month name other than
the Russian ones, so dates written that way are not read; dates written in figures are.
