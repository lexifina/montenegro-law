# Montenegro: law history in git

The law of Montenegro as a git history: one file per provision, one commit per amendment or law on the day it took effect, and the amendment or law that made each change as the commit's author. `git blame` names the amendment behind every paragraph; `git log` lists every change to an article; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `me/`. The texts are in Montenegrin (crnogorski jezik), the official language, exactly as the Official Gazette (Službeni list Crne Gore) published them.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `ustav/` | Ustav Crne Gore (the Constitution, 2007) | 3 | As proclaimed on 22 October 2007, through Amendments I-XVI (31 July 2013) and XVII-XXI (24 August 2026) |
| `zakon-o-zastiti-podataka-o-licnosti/` | Zakon o zaštiti podataka o ličnosti (the Law on Personal Data Protection, 2026) | 1 | As enacted (Službeni list CG 133/2026), in force 19 September 2026, applying from 19 March 2027 |

**The Constitution is never officially consolidated.** Officially it is the 2007 text plus the amendments, each of which "čini sastavni dio Ustava" (is a constituent part of the Constitution) and names the provision it replaces, supplements or deletes ("Ovim amandmanom zamjenjuje se član 33 Ustava Crne Gore"). This repository applies each amendment to the provision it names, so every article file reads as it stood on each day, and each changed provision is credited to its amendment.

**Two scripts.** Cyrillic and Latin are equal official scripts (Constitution, Art. 13). The Gazette published the 2007 Constitution in Cyrillic and every amendment in Latin, so an amended article can hold Cyrillic and Latin lines side by side: each line keeps the script of the official text that gave it its words. Nothing is transliterated.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did Article 91 say on 1 January 2020? | `python tools/on.py 2020-01-01 ustav clan-091` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2020-01-01T23:59:59Z" main -- ustav/clan-091.md):ustav/clan-091.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2020-01-01T23:59:59Z" main -- ustav/clan-091.md; git show "$($r):ustav/clan-091.md"` |
| Which amendment wrote each paragraph of Article 91? | `git blame ustav/clan-091.md` |
| Every change to Article 127 (the Judicial Council), word by word | `git log -p --word-diff ustav/clan-127.md` |
| Every amendment in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything Amendment XX changed | `git log --author="Amandman XX " --stat` |
| The whole Constitution on a date | `python tools/on.py 2015-01-01 ustav` |
| The data protection law's definitions | `python tools/on.py 2026-10-01 zakon-o-zastiti-podataka-o-licnosti clan-005` |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Europe/Podgorica, on the day the change took effect**. The adoption date and the Official Gazette publication date are trailers; the in-force day is in `In-force:`, which `tools/on.py` reads.
- **The 2007 Constitution** was adopted on 19 October 2007 and took effect on its proclamation, 22 October 2007 (the Gazette's "Datum stupanja na snagu"; Art. 158 has the constitutional law take effect with it). It was published in Službeni list Crne Gore 1/2007 on 25 October 2007.
- **Amendments I-XVI** and **XVII-XXI** each say they "stupaju na snagu danom proglašenja" (take effect on the day of proclamation): 31 July 2013 (published in 38/2013 on 2 August 2013) and 24 August 2026 (published in 126/2026 on 26 August 2026). So each takes effect two days before its Gazette issue. Amendments proclaimed together are separate commits on the same day, in number order.
- **Ordinary laws** state their own day in their final article. Under the Constitution (Art. 146) a law takes effect no earlier than the eighth day after its publication. The Law on Personal Data Protection (133/2026, 11 September 2026) takes effect on the eighth day, 19 September 2026, and applies six months later, from 19 March 2027 (its Art. 106). Its commit is dated 19 September 2026; until 19 March 2027 the 2008 law it replaces still applies.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day; use `T23:59:59Z` as above, or the tool.

## How it is checked

- **Every amendment's instruction is checked against the Gazette text.** The operation for each amendment is transcribed from its own last paragraph; the build stops unless that paragraph in the Gazette PDF reads word for word as transcribed, and unless the article, paragraph or point it names exists. The replaced text of every operation is logged.
- **The 2026 amendments confirm how the 2013 ones were applied.** Amendment XVII replaces "stav 3 člana 91 Ustava Crne Gore (Amandman IV)": in the build, paragraph 3 of Article 91 after 2013 is exactly Amendment IV's second paragraph, which holds only if Amendment IV's paragraphs took the place of the old paragraph 2. In the same way, the paragraph Amendment XIX deletes (Art. 128, para. 3, from Amendment IX) and the one Amendment XX replaces (Art. 136, para. 3, from Amendment XI) are the ones the build holds, and the caption and chapter title that Amendments XX and VI quote („Tužilački savjet”, „SUD“) are the ones in the 2007 text.
- **The data protection law is the Gazette's text itself**, read from the PDF's text layer: all 106 articles in order, and its final article states the in-force and application days the Gazette's own record gives.
- Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- Health checks: no merge commits on `main`, commit dates never go backwards, nothing dated in the future, and every commit's trailers parse with `git interpret-trailers --parse`.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the amendment or law that made the change, with an e-mail address that cannot exist (`amandman-04@sluzbenilist.invalid`), so `git blame` and `git log --author` name it. The committer is always Lexifina.

- **The first commit** of each act is the act as proclaimed or enacted, credited to it.
- **Credits come only from the source**: each changed provision is credited to the amendment whose instruction names it.
- Blame credits whole lines (one paragraph or numbered point per line). Where an amendment replaced points inside an article (Amendment III: points 13 and 14 of Article 82; Amendment V: point 5 of Article 95), only those lines are credited to it.

## What it does not show

- **How the amendments read on their own.** Each amendment is applied to the provision it names; its promulgation decision and signatures are not files. "Zamjenjuje se stav N ... i dopunjava član" puts all of the amendment's paragraphs in place of paragraph N; "dopunjava se član N" alone (XIV, XV) adds them at the end. A numbered point belongs to the paragraph before it, so "stav 3" counts paragraphs, not points.
- **The constitutional laws for implementing the Constitution and the amendments** (the Ustavni zakon for the 2007 Constitution, and those published in 38/2013 and 126/2026) are separate acts and are not here yet. The draft Amendment XXII (Parliament, October 2026) has not been adopted.
- **The 2008 Law on Personal Data Protection** (79/2008, amended by 70/2009, 44/2012, 22/2017 and 77/2024), which the 2026 law repeals on 19 March 2027 (except its Arts. 35-40a on video surveillance). There is no official consolidated text, the amending laws make dozens of word-level edits, and the text layer of the 2012 amendment splits words, so it is not yet replayed.
- **The Criminal Code** (Krivični zakonik, 70/2003), amended by more than a dozen laws listed by the Gazette, with no official consolidated text. It is not built yet.
- **The Law on Obligations** (Zakon o obligacionim odnosima, 47/2008). Its 2024 amendment (123/2024) replaces "bračni drug" "in each grammatical case" with a longer phrase, so most of the new wording is never printed and would have to be composed; it is not built.
- **Court rulings.** The Constitutional Court has not struck words from the Constitution.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

- The Gazette's act pages (`https://www.sluzbenilist.me/propisi/<id>`) give each act's issue, publication, in-force and application dates and its amending acts; `https://www.sluzbenilist.me/propisi/<id>/download` gives the act's PDF, with a text layer.
- No OCR was run, and no AI model wrote or changed legal text. Claude Opus 5.5 wrote the scripts and chose the sources; see `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions | Names the amending act | Bulk | Notes |
| --- | --- | --- | --- | --- | --- |
| [Službeni list Crne Gore](https://www.sluzbenilist.me/propisi) | Official Gazette and legal information system (PIS) | every act as published, with its amending acts listed | yes | search by title, type and year | Act PDFs have a text layer; page views are images |
| [Skupština Crne Gore: Ustav](https://www.skupstina.me/me/ustav-crne-gore) | Parliament | 2007 text, Amendments I-XVI, drafts of XVII-XXI and XXII (PDF) | yes | no | Its Constitution PDF has an unreadable font encoding and its amendments lose diacritics, so no text is taken from it |

Research guides: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

The texts are official texts of Montenegro, which the Law on Copyright and Related Rights (Zakon o autorskom i srodnim pravima) excludes from copyright protection. They are taken from Službeni list Crne Gore (www.sluzbenilist.me). Lexifina's own contributions are dedicated to the public domain under CC0 1.0; see `LICENSE`.

This repository is not legal advice and is not an official publication.

---

## Crnogorski

Ustav Crne Gore kao istorija u git-u: jedna datoteka po članu, jedan commit po amandmanu, na dan kada je stupio na snagu, sa amandmanom kao autorom. Ustav iz 2007. godine (Službeni list Crne Gore 1/2007, ćirilicom) primijenjen je sa amandmanima I-XVI (2013) i XVII-XXI (2026), svaki na odredbu koju zamjenjuje, dopunjava ili briše, u pismu u kojem je objavljen. Zakon o zaštiti podataka o ličnosti (133/2026) je onakav kakav je donesen. Tekstovi su iz Službenog lista Crne Gore. Ovo nije službeni prečišćeni tekst, niti pravni savjet.
