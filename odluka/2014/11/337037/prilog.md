105x
Da
Puni naziv
Za zajednički račun unosi se
podatak samo za lice koji je
prvopotpisano na zahtjevu za
otvaranje zajedničkog računa
74015:
Šifra opštine
3!x
Da
Šifra opštine koju utvrdi nadležni
organ
Za zajednički račun unosi se
podatak samo za lice koji je
prvopotpisano na zahtjevu za
otvaranje zajedničkog računa
74020:
Mjesto
35x
Da
Za zajednički račun unosi se
podatak samo za lice koji je
prvopotpisano na zahtjevu za
otvaranje zajedničkog računa
74025:
Adresa
35x
Da
Za zajednički račun unosi se
podatak samo za lice koji je
prvopotpisano na zahtjevu za
otvaranje zajedničkog računa 74030:
Oznaka transakcionog
računa
1!n
Da
0 - pravno lice
1 - preduzetnik
2 - zajednički račun
74035:
Šifra djelatnosti pravnog
lica ili preduzetnika
5!x
Da
Za zajednički račun unosi se
podatak samo za lice koji je
prvopotpisano na zahtjevu za
otvaranje zajedničkog računa 74040:
Datum promjene
10!x
Da
Format: DD.MM.YYYY
74045:
Status transakcionog
računa u platnom
prometu
1!n
Da
0 - uključen
1 - blokirana odobrenja
2 - blokirana zaduženja
3 - blokiran po osnovu
prinudne naplate
4 - ukinut
5 - zabrana raspolaganja
sredstvima
8 - privremeno neaktivan
74050:
Vrsta promjene
1!n
Da
0 - novi transakcioni račun
1 - izmjena podataka
9 - ukinut transakcioni
račun
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
Aktivnost transakcionog
računa
1!n
Da
0 - podliježe prinudnoj
naplati
2 - ne podliježe prinudnoj
naplati
74070
Skraćeni naziv pravnog
lica ili preduzetnika
35x
Da
Za zajednički račun unosi se
podatak samo za lice koji je
prvopotpisano na zahtjevu za
otvaranje zajedničkog računa
2.2. Poruka SMT 741 Porukom SMT 741 pružaoci platnih usluga iz člana 4 ove odluke obavještavaju se o postojanju greške u dostavljenim podacima. Analiza poruke SMT 740 obuhvata sve dostavljene podatke i nosi u sebi sve otkrivene greške (poruka je grupna).
Prvi dio poruke
Polje
Element poruke
Format
Obavezno
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
Podtip poruke sopstvenog formata
koji se nalazi u omotnici poruke a to
je 741
77E
Sadržaj omotnice poruke
koji odgovara
navedenom podtipu
poruke sopstvenog
formata
Da
Sadržaj omotnice u poruci
sopstvenog formata čine samo
unaprijed standardizovana polja
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
TRN poruke SMT740, na koju se
ova poruka odnosi
30
Datum slanja
17!x
Da
Format datuma je:
‘’YYYYMMDD HH:MM:SS’’
40
Matični broj pravnog lica
ili JMB preduzetnika
U slučaju zajedničkog
računa:
matični brojevi svih
pravnih lica i JMB svih
preduzetnika - imalaca
zajedničkog računa
13n
139 x
Da
Da
Matični brojevi ili JMB za zajednicki
racčun pišu se u nizu i odvajaju
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
U ovom redu obavezno samo crtica,
polja sopstvenog formata nemaju
dvije tačke na početku
--> 74110:
Redni broj greške
2!n
Da 74120:
Opis greške
42x
Da
Tekstualni opis greške
---:
PRILOG 2
Poruka SMT 742
Porukom SMT 742 Centralna banka obavještava pružaoce platnih usluga iz člana 4 ove odluke da su primljeni podaci tehnički ispravni i da transakcioni račun pravnog lica ili preduzetnika može biti korišćen u platnom prometu.
Prvi dio poruke
Polje
Element poruke
Format
Obavezno
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
Podtip poruke sopstvenog formata
koji se nalazi u omotnici poruke a to
je 742
77E
Sadržaj omotnice poruke
koji odgovara
navedenom podtipu
poruke sopstvenog
formata
Da
Sadržaj omotnice u poruci
sopstvenog formata čine samo
unaprijed standardizovana polja
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
TRN poruke SMT740, na koju se
ova poruka odnosi
30
Datum slanja
17!x
Da
Format datuma je:
‘’YYYYMMDD HH:MM:SS’’
40
Matični broj pravnog lica
ili JMB preduzetnika
U slučaju zajedničkog
računa:
matični brojevi svih
pravnih lica i JMB svih
preduzetnika - imalaca
zajedničkog računa
13n
139x
Da
Da
Matični brojevi ili JMB za zajednički
račun pišu se u nizu i odvajaju
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
U ovom redu obavezno samo crtica,
polja sopstvenog formata nemaju
dvije tačke na početku
74210:
Potvrda ispravnosti
2!a
Da
Fiksno ‘’OK’’
