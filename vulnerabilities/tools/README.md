# Tools

The scripts behind this Montenegro-only run of global-law's vulnerability detectors. They run inside a copy of
[global-law/vulnerabilities/scripts](https://github.com/lexifina/global-law/tree/main/vulnerabilities/scripts) (Python 3.11+,
`pip install duckdb pyarrow`), with a bare clone of this repository at `sources/corpus/montenegro-law.git`, a blobless bare
clone of global-law at `sources/global-law.git`, and a `pins.json` that names only montenegro-law and its commit.
`build_vulns.py`, `flags_chart.py`, `late_ext_select.py`, `late_ext_rebut.py`, `redo.py` and `config.json` sit two folders above it.

| Script | What it does |
| --- | --- |
| `run.sh` | Indexes the history and texts, maps paths to the folders since a move of act folders (`map_moved.py`), adds Montenegro's history rows, and runs the detectors |
| `add_root.py` | Builds Montenegro's history rows from this repository's own commits, so the history detectors read every change |
| `run_triage.sh` | The model review: the 40 strongest flags per category, the 40 strongest lapsed time limits in law texts, and the empty periods |
| `late_ext_select.py` | Chooses the 40 empty periods for global-law's review of that category (none were found here) |
| `late_ext_rebut.py` | Adds the second, arguing-against pass to the empty-period review, as `triage.py` does for the other categories |
| `build_vulns.py` | Builds `data/flags.csv`, `data/reviewed.csv` and `data/by_category.csv` from the findings and the model review |
| `flags_chart.py` | Draws the chart at the top of the READMEs, in Montenegrin and English, light and dark |
| `config.json` | The repository, the Montenegrin category names, the folders that are not law, and the chart's labels |
| `patch_detectors.py` | Fixes blind spots found in runs on several country repositories in the copy of global-law's scripts (`python -X utf8 patch_detectors.py <scripts dir>`; a fix already in place is skipped) |
| `patch_detectors_vi.py` | The same for Vietnamese dates, references and amounts (found by the Vietnam run); it changes nothing here, but `redo.py` runs it on every repository |
| `patch_es.py` | The same for Spanish dates and for "marco" and "escudo" read as currencies; it changes nothing here either |
| `patch_ca.py` | The same for Catalan dates and time limits, the Catalan peseta, and "sucre" (sugar) read as the Ecuadorian sucre; it changes nothing here either |
| `map_moved.py` | Rewrites the paths in the history table to each act's folder since a repository moved its act folders (`data/paths.json`), so that an act's history is not split in two at the move; `run.sh` runs it after the history is indexed. This repository has not moved its folders, and it rewrote no path |
| `patch_build_r7.py` | Brings a country's `build_vulns.py` up to date: lapsed-limit reviews matched on 400 characters of context, not 80, and a file deleted before a move of folders linked under its old folder (already applied to the `build_vulns.py` here) |
| `redo.py` | Runs the patches, then again only the scans and detectors the fixes change, the model review of lapsed time limits, references to deleted provisions and empty periods, and the build (`python -X utf8 redo.py <run folder> [--keep-reviews] [--full]`; `--full` runs every step again through `run.sh`, `map_moved.py` among them, sends every category to the model and keeps every review already made; `EMBED_FONTS` names the script that embeds the chart's fonts) |
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

A last run, `redo.py --full`, repeated every step with the current `patch_detectors.py`, keeping every review already made
(`map_moved.py` rewrote no path here). What changed for this repository:

- References to repealed placeholders and dead fines (`detectors/placeholder_ref.py`, `detectors/dead_fine.py`): the
  earlier `redo.py` passes did not run these two detectors again, so their last run predated the first round's "clan-N"
  fix, when no Montenegrin file name gave an article and they found nothing. Run again, they found 20 references and 1 dead
  fine, all misread: the repeal words include "brisan" with no word end, so "brisanje", "brisanja" and "brisanjem"
  (deletion from a register, of personal data, of a ship) mark an article in force as repealed (see EDGE-CASES).
- Currencies (`detectors/currency_scan.py`, sixth round): "lira" is no longer read inside "liraglutid" (4 flags) and the
  Latvian "lati" and "latu" only as words, not inside "uplati", "isplatu", "naplatu", "plati", "alati" or "Latić" (27
  flags): dead currencies went from 313 to 282. The other new currency fixes ("BEF" only in capitals, no Swiss "frank",
  francs CFP, French "lire" and "sucre", the dinar left out for French, Arabic and Serbian texts) change nothing here; the
  repository's language is not set to Serbian, so the dinars of 1998 to 2000 still count.
- `placeholder_ref.py` no longer reads the French noun "abrogations" as a repeal marker; it changes nothing here.
- `placeholder_ref.py` (twelfth round, found here): "brisan" counts only as a whole word ("brisan", "brisana", "brisano"),
  not followed by "iz": the 20 references and the dead fine above are gone (9,977 flags to 9,956).
- Lapsed time limits went from 2,911 to 2,913: the run, on 16 November 2026, counts two deadlines of 15 November 2026.
  The model reviewed 32 more with the top score, none surviving.
- `build_vulns.py` (`patch_build_r7.py`): lapsed-limit reviews are matched on 400 characters of context, not 80, so two
  flags that shared their first 80 characters with a reviewed flag no longer count as reviewed (147 reviewed in all), and
  each retroactive-date row names the first file of its act in `path`.
