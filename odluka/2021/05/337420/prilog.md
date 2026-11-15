Da
Puni naziv
Za zajednički račun unosi se podatak samo za
lice koje je prvopotpisano na zahtjevu za
otvaranje zajedničkog računa
74015:
Šifra opštine
- rezidenta
3!x
Da
Šifra opštine koju utvrdi nadležni organ
Za zajednički račun unosi se podatak samo za
lice koje je prvopotpisano na zahtjevu za
otvaranje zajedničkog računa
74020:
Mjesto sjedišta pravnog lica ili
preduzetnika, odnosno pre-
bivališta fizičkog lica - rezidenta,
odnosno mjesto i država sjedišta
pravnog lica ili prebivališta
fizičkog lica - nerezidenta
35x
Da
Za zajednički račun unosi se podatak samo za
lice koje je prvopotpisano na zahtjevu za
otvaranje zajedničkog računa
74025:
Adresa sjedišta pravnog lica ili
preduzetnika, odnosno adresa
prebivališta fizičkog lica - rezi-
denta, odnosno adresa sjedišta
pravnog lica ili prebivališta
fizičkog lica - nerezidenta
35x
Da
Kada je primjenjivo za nerezidenta unosi se i
adresa privremenog boravišta fizičkog lica u
Crnoj Gori
Za zajednički račun unosi se podatak samo za
lice koje je prvopotpisano na zahtjevu za
otvaranje zajedničkog računa
74030:
Oznaka transakcionog računa
1!n
Da
0 - pravno lice rezident
1- preduzetnik rezident
2 - zajednički račun
3 - fizičko lice rezident
4 - pravno lice nerezident
5 - fizičko lice nerezident
74035:
Šifra djelatnosti pravnog lica ili
preduzetnika - rezidenta,
odnosno djelatnost pravnog lica
- nerezidenta
5!x
35x
Da
Za zajednički račun unosi se
podatak samo za lice koje je prvopotpisano na
zahtjevu za otvaranje zajedničkog računa
Za nerezidenta upisuje se djelatnost - predmet
poslovanja iz izvoda iz registra u koji je upisan,
odnosno iz drugog validnog dokumenta o
osnivanju
74040:
Datum promjene
10!x
Da
Format: DD.MM.YYYY
Status transakcionog računa u
platnom prometu
1!n
Da
0 - uključen
1 - blokirana odobrenja
2 - blokirana zaduženja
3 - blokiran po osnovu prinudne naplate
74045:
4 - ukinut
5 - zabrana raspolaganja sredstvima
8 - privremeno neaktivan
74050:
Vrsta promjene
1!n
Da
0 - novi transakcioni račun
1 - izmjena podataka
9 - ukinut transakcioni račun
74055
Broj ugovora
35x
Da
74060
Datum ugovora
10!x
Da
Format: DD.MM.YYYY
74065
Aktivnost transakcionog računa
1!n
Da
0 - podliježe prinudnoj naplati
2 - ne podliježe prinudnoj naplati
74070
Skraćeni naziv pravnog lica ili
preduzetnika
35x
Da
Za nerezidenta upisuje se, kada je to primjenljivo,
skraćeni naziv pravnog lica iz izvoda iz registra u
koji je upisan, odnosno iz drugog validnog
dokumenta o osnivanju.
Za zajednički račun unosi se podatak samo za
lice koje je prvopotpisano na zahtjevu za
otvaranje zajedničkog računa
2.2.
Poruka SMT 741
Porukom SMT 741 pružaoci platnih usluga iz člana 4 ove odluke obavještavaju se o postojanju greške u dostavljenim podacima. Analiza poruke SMT 740 obuhvata sve dostavljene podatke i nosi u sebi sve otkrivene greške (poruka je
grupna).
Prvi dio poruke
Polje
Element poruke
Format
Obavez- no
Napomena
20
Referenca
16x
Da
TRN poruke SMT741
12
Podtip poruke
3!n
Da
Podtip poruke sopstvenog formata koji se
nalazi u omotnici poruke a to je 741
77E
Sadržaj omotnice poruke koji
odgovara navedenom podtipu
poruke sopstvenog formata
Da
Sadržaj omotnice u poruci sopstvenog formata
čine samo unaprijed standardizovana polja
prema uputstvu
59A
BIC primaoca
4!a2!a2!c[3!c]
Da
54A
BIC pošiljaoca
4!a2!a2!c[3!c]
Da
21
Povezana referenca
16x
Da
TRN poruke SMT740 na koju
se ova poruka odnosi
30
Datum slanja
17!x
Da
Format datuma je:
‘’YYYYMMDD HH:MM:SS’’
Matični broj pravnog lica odnosno
matični broj preduzetnika
JMB fizičkog lica - rezidenta
Identifikacioni broj pravnog lica ili
fizičkog lica - nerezidenta
8n
13n
13x
Da
40
U slučaju zajedničkog računa:
matični brojevi svih pravnih lica
odnosno matični brojevi svih
preduzetnika i JMB fizičkih lica ili
identifikacioni brojevi - imalaca
zajedničkog računa
139 x
Da
Matični brojevi ili JMB ili identifikacioni brojevi
za zajednicki račun pišu se u nizu i odvajaju
zarezom
Drugi dio poruke
Polje
Element poruke
Format
Obavezno
Napomena
79
Polje sopstvenog formata
Da
U ovom redu obavezno samo crtica, polja
sopstvenog formata nemaju dvije tačke na
početku
-->
74110:
Redni broj greške
2!n
Da
74120:
Opis greške
42x
Da
Tekstualni opis greške
---:
PRILOG 2 Poruka SMT 742
Porukom SMT 742 Centralna banka obavještava pružaoce platnih usluga iz člana 4 ove odluke da su primljeni podaci tehnički
ispravni i da transakcioni račun pravnog lica, preduzetnika ili fizičkog lica može biti korišćen u platnom prometu.
Prvi dio poruke
Polje
Element poruke
Format
Obavez- no
Napomena
20
Referenca
16x
Da
TRN poruke SMT742
12
Podtip poruke
3!n
Da
Podtip poruke sopstvenog formata koji se
nalazi u omotnici poruke a to je 742
77E
Sadržaj omotnice poruke koji
odgovara navedenom podtipu
poruke sopstvenog formata
Da
Sadržaj omotnice u poruci sopstvenog formata
čine samo unaprijed standardizovana polja
prema uputstvu
59A
BIC primaoca
4!a2!a2!c[3!c]
Da
54A
BIC pošiljaoca
4!a2!a2!c[3!c]
Da
21
Povezana referenca
16x
Da
TRN poruke SMT740 na koju
se ova poruka odnosi
30
Datum slanja
17!x
Da
Format datuma je:
‘’YYYYMMDD HH:MM:SS’’
Matični broj pravnog lica odnosno
matični broj preduzetnika
JMB fizičkog lica - rezidenta
Identifikacioni broj pravnog lica ili
fizičkog lica - nerezidenta
8n
13n
13x
Da
40
U slučaju zajedničkog računa:
matični brojevi svih pravnih lica
odnosno matični brojevi svih
preduzetnika i JBM fizičkih lica ili
identifikacioni brojevi - imalaca
zajedničkog računa
139x
Da
Matični brojevi ili JMB ili identifikacioni brojevi
za zajednički račun pišu se u nizu i odvajaju
zarezom
Drugi dio poruke
Polje
Element poruke
Format
Obavezno
Napomena
79
Polje sopstvenog formata
Da
U ovom redu obavezno samo crtica, polja sop-
stvenog formata nemaju dvije tačke na početku
74210:
Potvrda ispravnosti
2!a
Da
Fiksno ‘’OK’’
