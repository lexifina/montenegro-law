# Montenegro: law history in git

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Montenegro's national law, which global-law reads at `montenegro/national/acts/`.

**Scope**
- The acts the Službeni list Crne Gore (the Official Gazette) publishes and its legal information system (PIS) marks in force: the Constitution with its amendments, laws, Government decrees, regulations, decisions, rules, orders, instructions, plans, programmes, statutes and treaties, national and local, each from its official PDF.
- Tens of thousands of acts, growing as the fetch of the PIS completes; [ACTS.md](ACTS.md) lists every act held, and [data/held.json](data/held.json) every act in force that is not yet held, with the reason.

**Use**
- The PIS shows an act as it was published, and lists the acts that later amended it. Here each act is a folder of article files, so what a provision said, and which act wrote it, is one `git log` or `git blame`.
- Everything can be searched, compared and reused: the texts are official, and our work is public domain (CC0).

## Layout

| Where | What |
| --- | --- |
| `ustav/` | the Constitution (2007), with Amendments I-XVI (2013) and XVII-XXI (2026) applied to the provisions they replace |
| `zakon/`, `uredba/` | laws and Government decrees, by year of publication and PIS id; laws in force from the first publish sit at the top level under their title (`zakon-o-...`, listed in data/paths.json) |
| `odluka/`, `rjesenje/`, `pravilnik/`, `naredba/`, `uputstvo/`, `pravila/`, `poslovnik/`, `statut/`, `program/`, `plan/`, `akt/` | decisions, rulings, regulations, orders, instructions, rules, rules of procedure, statutes, programmes, plans and other acts, national and local |
| `ugovor/` | treaties and other international acts published in the Gazette |
| `<act>/clan-NNN.md` · `<act>/README.md` | one article per file (one paragraph per line) · the act's versions and notes |
| [ACTS.md](ACTS.md) · `data/` · `tools/` | the act list · tables and indexes · the tools below |

## Use it

| Question | Command |
| --- | --- |
| What did Article 91 of the Constitution say on 1 January 2020? | `python tools/on.py 2020-01-01 ustav clan-091` |
| Which amendment wrote each paragraph of Article 91? | `git blame ustav/clan-091.md` |
| Every change to an article, word by word | `git log -p --word-diff ustav/clan-127.md` |
| Everything one amendment changed | `git log --author="Amandman XX " --stat` |
| Is an act here current? | `python tools/freshness.py <act id>` |

Read dates with the tools, not `git rev-list --before`: they pick each version by its `In-force:` trailer.

## Sources

- The Službeni list's legal information system (PIS, [sluzbenilist.me/propisi](https://www.sluzbenilist.me/propisi)): each act's page gives its issue, publication, in-force and application days, its status (Važeći / Nevažeći) and the acts that amend it; `/propisi/<id>/download` gives its PDF, whose text layer is read. No OCR is run.
- Every version names the official page and PDF it was read from (the `Source:` and `Consolidated:` trailers of its commit, and `portal` in [data/acts.json](data/acts.json)).

## How current is it

Every version names the official page it was read from, so every act can be checked against its source.

<!-- freshness-summary -->
Checked against the official sources: 2026-11-10; 78% of acts verified in the last 7 days, 78% in the last 30 ([data/freshness.json](data/freshness.json)).
<!-- /freshness-summary -->

`python tools/freshness.py <act>` gives an act's status, its last check and the official link. A refresh runner re-reads each act's PIS page within its threshold (7 days for the Constitution, laws and Government decrees, 30 for the rest) and adds new acts as the Gazette publishes them; [data/status.json](data/status.json), rewritten by every run, says whether updates are running and which official sources answered. Statuses and fields are explained in [data/freshness.json](data/freshness.json). Acts in force but not held are in [data/held.json](data/held.json), with the reason; acts published but not yet in force are in [data/pending.json](data/pending.json), and are added on their day.

## Dates, authors and limits

- Each commit is dated at noon, Europe/Podgorica, on the day the change took effect (the PIS "Datum stupanja na snagu", checked against the act's own final article); the author is the act that made it, the committer Lexifina. A separate application day ("Datum početka primjene") is noted on the version.
- The PIS publishes no consolidated texts. An act is held as it was published; where the PIS lists later amending acts, the act's status in data/acts.json is `amended, not consolidated` and `amended_by` names those acts, with their official links. Only the Constitution's amendments are applied to its text.
- Only the Službeni list Crne Gore is authoritative. The President's promulgation decree printed above a law, and the signatures, are left out; an annex printed after the signature is one unit.
- The 2007 Constitution was published in Cyrillic and its amendments in Latin; each line keeps the script of the text that gave it its words. Nothing is transliterated.
- Every version is read back from git on its in-force day and must match the source; results are in `REPRODUCE.md`.

## Licence

The texts are official texts of Montenegro, which the Law on Copyright and Related Rights (Zakon o autorskom i srodnim pravima) excludes from copyright protection, taken from the Službeni list Crne Gore (www.sluzbenilist.me). Lexifina's arrangement, tables, commit messages and tools are in the public domain (CC0 1.0), as set out in `LICENSE`. This repository is not legal advice and not an official publication.

## Crnogorski

Istorija crnogorskog prava u git-u: jedna datoteka za svaki član i jedan commit za svaku promjenu, na dan kada je stupila na snagu, sa aktom koji ju je donio kao autorom. Akti su onakvi kakvi su objavljeni u Službenom listu Crne Gore; akt koji je kasnije mijenjan označen je kao `amended, not consolidated`, sa aktima koji ga mijenjaju. Spisak akata je u [ACTS.md](ACTS.md); tekst na snazi na određeni dan: `python tools/on.py 2020-01-01 ustav clan-091`. Ovo nije službeni prečišćeni tekst, niti pravni savjet.
