# How this repository was made (Montenegro)

This file is written by the build on 2026-10-29, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Službeni list Crne Gore (Official Gazette of Montenegro, PIS) | <https://www.sluzbenilist.me/propisi> | 2026-10-29 | Official texts, not protected by copyright (Zakon o autorskom i srodnim pravima) |
| Skupština Crne Gore (Parliament) | <https://www.skupstina.me/me/ustav-crne-gore> | 2026-10-29 | Official texts, not protected by copyright |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `ustav` | Ustav Crne Gore | 3 | 2007-10-22 to 2026-08-24 |
| `zakon-o-zastiti-podataka-o-licnosti` | Zakon o zaštiti podataka o ličnosti | 1 | 2026-09-19 to 2026-09-19 |

The build made 23 commits:

| Commits | Kind |
| ---: | --- |
| 2 | first version of an act |
| 21 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `buduce`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 23 laws in the record.
- 27 tags.

## Dates

Each commit is dated at noon (Europe/Podgorica) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Ustav Crne Gore art. 146: a law or other regulation is published before it takes effect and takes effect no earlier than the eighth day after its publication; each act's own final article states its day. The Constitution and its amendments take effect on proclamation. https://www.sluzbenilist.me/propisi/297951

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `c3e2cbd1f59f1b98ca01c841872da7d26eb3f1627f3e82ebb19ab514413c80cd` (526226 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

4 versions of 2 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Constitution: there is no official consolidated text. Officially it is the 2007 text (Službeni list CG 1/2007) plus Amendments I-XVI (38/2013) and XVII-XXI (126/2026), each 'sastavni dio Ustava'. Each amendment is applied by its own last paragraph ('Ovim amandmanom zamjenjuje se ...'), transcribed as an operation and checked word for word against that paragraph on every build.
- Script: the gazette published the 2007 Constitution in Cyrillic and the amendments in Latin; both scripts are official (Constitution art. 13). Every provision keeps the script of the text that gave it its words, so an amended article can mix Cyrillic and Latin lines. Nothing is transliterated.
- 'Zamjenjuje se stav N ... i dopunjava' puts all of the amendment's paragraphs in place of stav N. Amendment XVII (2026) confirms this for Amendment IV: the 'stav 3 člana 91 (Amandman IV)' it replaces is IV's second paragraph. 'Dopunjava se član N' alone (XIV, XV) adds the paragraphs at the end of the article.
- A numbered point ('1) ...') belongs to the paragraph before it, so 'stav 3' counts paragraphs, not points (Amendment XIX deletes stav 3 of art. 128, the last paragraph after the points of stav 1).
- In-force days: the 2007 Constitution took effect on its proclamation, 22 October 2007 (gazette 'Datum stupanja na snagu'; art. 158 with the constitutional law). Each batch of amendments says it 'stupa na snagu danom proglašenja': 31 July 2013 (published 2 August 2013) and 24 August 2026 (published 26 August 2026).
- Article captions (the bold heading above 'Član N') are the second line of the article file ('## ...'); Amendments II and XX replace a caption ('naziv člana'). Part and chapter headings are units of their own (dio-N, dio-N-poglavlje-M); Amendment VI renames chapter 5 of Part Three from 'СУД' to 'SUDSTVO'.
- Letter-spaced headings ('5. С У Д') are joined into one word; runs of spaces are collapsed. Otherwise the gazette's words, punctuation and spelling are kept, including 'Ustavnog suda,vrhovnog' in Amendment III.
- Left out: the promulgation decisions printed before each text, the signatures, and the two constitutional laws for implementing the amendments (Ustavni zakon, 38/2013 and 126/2026), which are separate acts. The draft Amendment XXII (Skupština, October 2026) is not adopted and is not included.
- Law on Personal Data Protection (2026): the new law (Službeni list CG 133/2026, published 11 September 2026) is built as enacted. It takes effect on the eighth day after publication, 19 September 2026 (art. 106; gazette 'Datum stupanja na snagu'), the commit date, and applies from 19 March 2027, six months later (gazette 'Datum početka primjene'); art. 104 defers some provisions to EU accession.
- The 2008 Law on Personal Data Protection (79/2008, amended 70/2009, 44/2012, 22/2017, 77/2024), which the 2026 law repeals on its application day (art. 105, except arts. 35-40a on video surveillance), is not built yet: no consolidated official text exists, 44/2012 makes dozens of word-level edits across some 40 articles, and its PDF text layer splits words ('zloupo trebe', 'nad zornom', 'brisa nje'), so an exact replay would need hand-corrected words.
- Not built: the Criminal Code (Krivični zakonik, 70/2003), with more than a dozen amending laws on the gazette's record and no official consolidated text (over the 45-minute budget per act); and the Law on Obligations (Zakon o obligacionim odnosima, 47/2008; amended 22/2017, 123/2024, 94/2026, 117/2026), because 123/2024 replaces 'bračni drug' 'u različitom padežu' (in each grammatical case), so the new words in most cases are not printed in the gazette and would have to be composed.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Opus 5.5, claude-opus-5-5) wrote Lexifina's code and transcribed each amendment's instruction paragraph into an operation table, which the code checks against the gazette's own words. No model wrote or edited legal text, and no model runs at parse or git-build time.
