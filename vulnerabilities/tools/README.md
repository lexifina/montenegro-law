# Tools

The scripts behind this Montenegro-only run of global-law's vulnerability detectors. They run inside a copy of
[global-law/vulnerabilities/scripts](https://github.com/lexifina/global-law/tree/main/vulnerabilities/scripts) (Python 3.11+,
`pip install duckdb pyarrow`), with a bare clone of this repository at `sources/corpus/montenegro-law.git`, a blobless bare
clone of global-law at `sources/global-law.git`, and a `pins.json` that names only montenegro-law and its commit.
`build_vulns.py`, `flags_chart.py`, `late_ext_select.py`, `late_ext_rebut.py`, `redo.py` and `config.json` sit two folders above it.

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
| `patch_detectors.py` | Fixes blind spots found in runs on several country repositories in the copy of global-law's scripts (`python -X utf8 patch_detectors.py <scripts dir>`; a fix already in place is skipped) |
| `redo.py` | Runs `patch_detectors.py`, then again only the scans and detectors the fixes change, the model review of lapsed time limits, references to deleted provisions and empty periods, and the build (`python -X utf8 redo.py <run folder> [--keep-reviews]`; `EMBED_FONTS` names the script that embeds the chart's fonts) |
| `do_gap_check.py` | Counts the "do <day>. <month> <year>" and "do kraja <year>. godine" phrases in this repository that the lapsed-time-limit scan does not read (`python -X utf8 do_gap_check.py <scripts dir>`) |

The model review needs `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL` and `LLM_AUTH` set for an OpenAI-compatible Responses API.

Two changes were made for this repository:

- `add_root.py` counted only commits with no `Kind:` trailer, or `as-promulgated`, `law`, `amendment` or `original`, as law
  changes. This repository marks an act's text with `Kind: decree` (by-laws, decisions and rulings, 35,150 commits),
  `as-enacted` (179) and `treaty` (142) as well, so those three were added: 36,629 commits count as law changes, and the
  292 metadata-only records, the case law and the documentation keep their own kind.
- `run.sh` reads `LE_WORKERS` and `LE_GREP_THREADS` from the environment; this run used `LE_WORKERS=3 LE_GREP_THREADS=3 bash run.sh 3`.
  `ingest/refscan.py --fileact` is not run, so `run.sh` writes an empty `index/refs_fileact` table for `detectors/ref_detectors.py`.

The run was then repeated with `redo.py`, and twice more with `--keep-reviews`, which keeps every review already made and
sends to the model only strong flags not yet reviewed (117 lapsed time limits reviewed in all; the 40 reviewed before the fixes
are not kept, and 4 of them were reviewed again). Of `patch_detectors.py`'s fixes, these change this repository's flags:

- Dates (`ingest/textscan.py`): the Montenegrin month names "januara", "februara", "marta", "juna" and "jula" and the month
  names in Cyrillic ("јануара" ... "децембра") are now read, as are numeric dates written with spaces ("31. 12. 2020."),
  months in Roman numerals ("31.XII.2001") and "do kraja 2020. godine" (31 December of that year); "najkasnije" marks a
  deadline. Lapsed time limits went from 1,999 to 2,911 flags; the 912 added include 584 dates with one of those five month
  names, 79 in Cyrillic and 76 "do kraja" phrases. `do_gap_check.py` finds 1,967 phrases "do <day>. <month> <year>" at this
  commit, 2 of them not read (the month in the nominative, "do 1. decembar 2026"), and 102 "do kraja <year>. godine", 8 of them
  not read (in Cyrillic, "до краја 2018. године"); 3 Cyrillic dates with a Roman-numeral month and no dot after it
  ("до 31. VIII 1994") are not read either.
- Currencies (`detectors/currency_scan.py`): "DM" only in capitals, and "inti", "lire" and the like only as whole words, which
  took out four "dm" (decimetres) and "Intimizacija"; the Belgian franc brought in three "francs" in the French text of the
  Metre Convention and the name "Franc Prešern". Dead currencies went from 314 to 313. (The fourth round's "lira" with Turkish
  endings matched "lira" inside words such as "recikliranja", 19 flags in the second run; the fifth round reads "lira" only at
  the start of a word, and they are gone.)
- Links (`build_vulns.py`): each retroactive-date flag now links to the commit that made that act's version on that day, read
  from the detectors' history table (`index/root.parquet`), not to the first commit credited to an act of the same name: 62
  flags link to another commit than before, 9 of them flags that had no link.
- References (`ingest/refscan.py`): "clan-N" file names now give the article, but no reference to a deleted provision is
  found before or after, as no act here has a history of changes.

The third run applied `patch_detectors.py`'s fifth round: "lira" only at the start of a word; the same row order in every
shard and a stable split of acts between `refscan.py` shards (the old split by Python's `hash()` could read some acts twice and
others not at all; here the flags of the other categories came out the same); Croatian "listopada" read as October; and a fixed
tie-break among flags with the same score when the model review picks the strongest. That pass sent 37 more lapsed time limits
with the top score to the model, none of which survived.
