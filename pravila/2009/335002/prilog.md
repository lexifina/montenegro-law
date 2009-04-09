Ne popunjava se kod naloga za uplatu 3.
Naziv lica
Naziv i sjedište pravnog lica,
1. naziv-ime (pravnog- fizičkog lica)
čiji se račun
odobrava
odnosno ime, prezime i adresa
prebivališta fizičkog lica
3*35x
2. adresa
3. mjesto 4.
Broj računa
koji se
odobrava
Račun koji će biti odobren
18n
Po odluci kojom se uređuje struktura
računa
18 numeičkih polja (3+13+2)
Ne popunjava se kod naloga za isplatu 5.
Iznos
Iznos sredstava sa dvije cifre iza
decimalnog zareza
12n,nn
Limitiran na 15 znakova (iznos od 12
cifara odvojenih zarezom od dvije
naredne cifre (decimale) 6.
Svrha
transfera
Namjera, odnosno osnov
transfera
3*35x
Popunjava inicijator
7.
Šifra
transfera
Oblik transfera
3n
Popunjava se po potrebi
8.
Model (broj
modela
poziva na
broj
zaduženja)
Popunjava nalogodavac po
modulu 97. Upisivanje
kontrolnog broja nije uslov za
izvršenje naloga.
2n
Polje od 2 numerička znaka
9.
Poziv na
broj
zaduženja
Podaci koji bliže objašnjavaju
poslovne promjene lica koje se
zadužuje
20x
Ne može biti veći od 20 znakova
10.
Model (broj
modela
poziva na
broj
odobrenja)
Popunjava nalogodavac po
modulu 97. Upisivanje
kontrolnog broja nije uslov za
izvršavanje naloga
2n
Polje od 2 numerička znaka
Ne popunjava se kod naloga za isplatu
11.
Poziv na
broj
odobrenja
Podaci koji bliže objasnjavaju
poslovne promjene povjerioca
20x
Ne može biti veći od 20 znakova
Ne popunjava se kod obrasca za isplatu 12.
Datum
valute
Datum kada nalog treba izvršiti
DDMMGG
Popunjava inicijator 13.
Mjesto i
datum
podnoše-nja
naloga
Mjesto i datum podnošenja
naloga
DDMMGG
Popunjava inicijator
14.
Hitnost
Polje "Hitno" popunjava
inicijator
X
Popunjava inicijator - ako se popuni sa
X dobija karakter hitnosti
PRILOG 3 PORUKE U SWIFT FORMATU Poruke
Namjena MT 102
Grupni kreditni transfer (Multiple Customer Credit Transfer): koristi se za višestruke
transfere više klijenata u okviru jedne poruke u DNS sistemu MT 103
Pojedinačni kreditni transfer (Single Customer Credit Transfer): koristi se za pojedinačni
transfer za račun klijenta učesnika u RTGS sistemu MT 202
Transfer sredstava između finansiskih institucija (General Financial Institution Transfer):
koristi se za pojedinačni transfer između učesnika u RTGS sistemu MT 900
Potvrda o zaduženju računa (Confirmation of Debit): koristi se kao potvrda o zaduženju
računa učesnika poslije izvršenog transfera (MT 103 ili MT 202) MT 910
Potvrda o odobrenju računa (Confirmation of Credit): koristi se kao potvrda o odobrenju
računa učesnika poslije izvršenog transfera (MT 103 ili MT202) MT 920
Zahtjev o stanju računa i za slanje izvještaja (Request for Balance and Interim Transactions Reports): koristi se kao zahtjev za informacije o stanju računa učesnika u određenom
trenutku ili kao zahtjev za slanje izvještaja MT 940
Izvještaj o izvršenim transferima na računu učesnika (Customer Statement Message): sadrži
informacije o izvršenim transferima u RTGS sistemu MT 941
Trenutno stanje sredstava na računu učesnika (Balance Report): koristi se za slanje informacija o stanju računa, kao odgovor na zahtjev MT 920 kojim se zahtijeva informacija
o stanju računa u određenom momentu MT 942
Privremeni izvještaj o izvršenim transferima (Participant Interim Transaction Report):
sadrži podatke o transferima od prethodno dostavljenog privremenog ili dnevnog izvještaja.
Za račune državnih institucija ima karaker redovnih izvještaja za njihove uplatne račune
MT 950
Izvještaj o izvršenim dnevnim transferima sa računa učesnika (Statement Message): sadrži
informacije o izvršenim transferima u RTGS sistemu MT 970
Izvještaj o izvršenim transferima u DNS sistemu (Netting Statement): sadrži informacije o
izvršenim transferima u DNS sistemu u određenom klirinškom periodu MT 972
Privremeni izvještaj o izvršenim transferima u DNS sistemu (Interim Netting Statement):
sadrži informacije o izvršenim transferima u DNS sistemu MT 973
Zahtjevi za izvještaje iz DNS sistema (Netting Request Message): koristi se kao zahtjev za
slanje izvještaja o izvršenim transferima u DNS sistemu MT 985
Upit o statusu računa (Query Message): koristi se kao upit o statusu računa, o porukama u
redu za čekanje, setovanom limitu i totali transfera u DNS sistemu MT 986
Odgovor na upit o statusu (Report on Account Requests): korisi se da učesniku da odgovor
postavljen upitom MT 985 MT 991
Izvještaj o dnevnom iznosu naknade Centralnoj banci (Request for Payment of Changes,
Interest and Other Expenses) za izvršavanje transfera u RTGS sistemu i DNS sistemu
MT 192
Zahtjev za opoziv (Request for Cansellation) prethodno poslate i do tog momenta
neizvršene poruke MT 103 ili MT 102 MT 292
Zahtjev za opoziv (Request for Cansellation) prethodno poslate i do tog momenta
neizvršene poruke MT 202 MT 195
Upit o statusu (Queries to Transfer) prethodno poslate poruke MT 103 ili MT 102
MT 295
Upit o statusu (Queries to Transfer) prethodno poslate poruke MT 202 MT 196
Odgovor (Reports on Transfers) na upit MT 195 ili informacija sistema o statusu prethodno
poslate poruke MT 103 ili MT 102 MT 296
Odgovor (Reports on Transfers) na upit MT 295 ili informacija sistema o statusu prethodno
poslate poruke MT 202 MT 999
Poruka slobodnog formata 1. Struktura poruke
1.1. Zaglavlje poruke
Svaka instrukcija sadrži informaciju o učesniku u međubankarskom transferu kao pošiljaocu ili
primaocu poruke za/od RTGS sistema i o samom RTGS sistemu.
Primjer "Zaglavlja poruke" dat je u narednoj tabeli:
Učesnik à RTGS sistem
Br. blo.
Naziv polja
Učesnik à RTGS sistem
1:
Pošiljalac
HBBAMEPGXXX
Hipotekarna banka AD
Podgorica
2:
Tip poruke
103
2:
Primalac
CBCGMEPGXXXX
RTGS - sistem Podgorica
RTGS sistem à Učesnik
Br. blo.
Naziv polja
RTGS sistem à Učesnik
1:
Pošiljalac
CBCGMEPGXXXX
RTGS - sistem Podgorica
2:
Tip poruke
103
2:
Primalac
HBBAMEPGXXX
Hipotekarna banka AD
Podgorica
1.2. Karakteri koji definišu format poruke:
Struktura SWIFT polja:
Vrsta karaktera
Opis
Primjeri
n
Numeričko polje
18n - numeričko polje do 18 karaktera
!
Iza nekog broja predstavlja fiksnu dužinu
određenu tim brojem
18!n - polje od fiksno 18 numeričkih karaktera
a
Isključivo slovno polje (velika slova)
4!a - fiksno četiri slovna karaktera
d
Decimalno polje
15d - numeričko polje sa dvije decimale do 15 karaktera
(12n,nn)
x
Slovno,numeričko i znakovno polje
35x - predstavlja do 35 slovno, numeričkih i znakovnih
karaktera
c
Slovno numeričko polje
3c - polje koje ima 3 slovna, 3 numerička ili 3 slovno
numerička karaktera
3*35x
Prvi broj određuje broj linija a drugi broj
karaktera po liniji
3*35x - 3 linije od kojih svaka ima do 35 karaktera
[ ]
Polja u uglastim zagradama su opciona polja
[1!a] - polje u određenim uslovima ima fiksno jedan karakter
dok u drugim uslovima se ne popunjava
à
----I
Polja koja se nalaze između ova dva znaka
mogu se ponavljati više puta
Dozvoljeni karakteri u SWIFT-u:
a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0123456789 / - ? : ( ) . , + { }
1.3. Prioritet
Polje :113: nalazi se u trećem bloku i određuje prioritet transfera.
Za transfere u RTGS sistemu prioritet se kreće između 0001 - 0099. Vrijednost 0001 je za najveći prioritet dok je najniži prioritet 0099. Za transfere u DNS sistemu prioritet je 0100.
1.4. ACK/NAK potvrda
ACK/NAK potvrda postoji samo u XML formatu.
ACK potvrda se šalje učesniku u slučaju uspješnog predprocesiranja poruke.
NAK potvrda se šalje učesniku u slučaju greške tokom predprocesiranja poruke.
1.5.Tabela poruka koje se koriste u RTGS sistemu
Poruke koje učesnk šalje RTGS sistemu
Poruke koje RTGS sistem šalje učesniku MT 102
MT 196 MT 103
MT 900, MT 910, MT 196 MT 202
MT 900, MT 910, MT 296 MT 985
MT 986 MT 920
MT 940, MT 941, MT 942, MT 950 MT 192
MT 196 MT 195
MT 196 MT 292
MT 296 MT 295
MT 296 MT 999
MT 999
MT 991
2. Formati poruka transfera sredstava
2.1. Poruka MT 102 - višestruki transfer sredstava za račun više
klijenata učesnika u DNS sistemu
Grupni kreditni transfer (Multiple Customer Credit Transfer) koristi se za višestruke transfere sredstava za račun više klijenata (za račun učesnika u DNS sistemu). Svi transferi u jednoj poruci moraju imati isti datum valute, pri čemu je učesnik pošiljalac isti za sva zaduženja, a učesnik primalac je isti za sva odobrenja. Zbir pojedinačnih transfera mora da odgovara iznosu u polju 32A.
Raspored elemenata je sljedeći:
Polje
Elementi naloga za transfer
Format
Obavezno
Napomena
Pošiljalac
da
Primalac
da 113
Prioritet sa vrijednošću 100 određuje da će se
transfer izvršiti u DNS sistemu
4n
da
Primjer:
113:0100 20
Referenca poruke
16x
da
TRN y SWIFT-y 23
CREDIT
6!a
da
CREDIT 26T
Tip koda transfera
3!c
Podrazumijeva se vrijednost 001 71A
SHA
3!a
à
21
Referenca transfera
16x
da
32B
Šifra valute (EUR) i
iznos (12n,nn)
3!a15d
da
Primjer:
32B:EUR100,00 50K
Račun klijenta koji se zadužuje (3n-13n-2n)
/18!n 3*35x
da
Primjer:
:50K:/580000000000123475
KLIJENT BANKE A
Ul.Slobode br.2
PODGORICA
Naziv klijenta:
- naziv-ime (pravnog - fizičkog lica),
- adresa ,
- mjesto
59
Račun klijenta koji se odobrava (3n-13n-2n)
/18!n 3*35x
da
Primjer:
:59:/570000000000873444
KLIJENT BANKE B
Ul. Balšićeva br.5
BUDVA
Naziv klijenta:
- naziv-ime (pravnog - fizičkog lica),
- adresa
- mjesto
70
Informacije o doznačenju sredstava :
-
šifra transfera (SIF- 3n)
-
kod polja PBZ iza koga slijede model
poziva na broj zaduženja i poziv na
broj zaduženja odvojeni crticama
-
kod polja PBO iza koga slijede model
poziva na broj odobrenja i poziv na
broj odobrenja odvojeni crticama
4*35x (SIF-3n
PBZ-2n-20x
PBO-2n-20x)
da
Primjer predloženog formata:
:70:SIF-120
PBZ-00-12345
PBO-00-4567-2008
77B
Svrha transfera
3*35x
da
Primjer:
:77B: UPLATA PO FAKTURI BR.
4567
----I
32A
- Datum valute (YYMMDD),
- šifra valute (za euro EUR) i
- iznos - zbir svih transakcija (12n,nn)
6!n3!a15d
da
Primjer (za 10 naloga po 20,00
eura):
:32A:0907029EUR200,00
53A
Učesnik čiji se račun zadužuje:
/D/ Račun učesnika
/D/18!n 4!a2!a2!c[3!c]
da
Primjer:
:53A:/D/907000000005800138
CKBCMEPG
BIC učesnika 54A
Učesnik čiji se račun odobrava:
/C/ Račun učesnika
/C/18!n 4!a2!a2!c[3!c]
da
Primjer:
:54A:/C/907000000005700131
PDBPMEPG
BIC učesnika 72
Informacije od pošiljaoca primaocu sa kodom
transakcije
Na početku se unosi kod CODTYPTR/001 ili
BNF , na početku ostalih redova idu obavezno
dvije crtice //
6*36
CODTYPRT/001
-
Šematski prikaz realizacije poruke MT 102
MT 102 (1) MT 102 (3)
MT 196 (2)
Učesnik B
DNS sistem
Učesnik A
-
Šematski prikaz kada poruka MT 102 nije izvršena jer:
a/ došlo je do greške pri procesiranju poruke b/ nije bilo dovoljno sredstava za realizaciju.
MT 102
MT 196
2.2. Poruka MT 103 - transfer sredstava za račun klijenta učesnika u RTGS sistemu Pojedinačni kreditni transfer (Single Customer Credit Transfer) koristi se za pojedinačni prenos sredstava kada se kao pošiljalac, primalac ili i pošiljalac i primalac pojavljuje klijent učesnika u RTGS sistemu.
Raspored elemenata je sljedeći:
Polje
Elementi naloga za transfer
Format
Obavezno
Napomena
Pošiljalac
da
Primalac
da 113
Za transfere u RTGS sistemu prioritet se kreće
izmedju 0010 - 0099. Vrijednost 0010 je za
najveći prioritet, ukoliko nije naveden
podrazumijeva se 0099
4n
Primjer:
113:0099
20
Referenca poruke
16x
da
TRN y SWIFT-y 23B
CRED
4!c
da
CRED 23E
SDVA
4!c
da
SDVA 26T
Tip koda transakcije
3!c
Podrazumijeva se vrijednost 001 32A
Datum valute (YYMMDD),
Šifra valute (EUR) i
Iznos (12n,nn)
6!n3!a15d
da
Primjer:
:32A:090123EUR453,69
50K
Račun klijenta koji se zadužuje (3n-13n-2n)
/18!n 3*35x
da
Primjer:
:50K:/580000000000123475
KLIJENT BANKE A
Ul.Slobode br.23
PODGORICA
Naziv klijenta koji se zadužuje:
- naziv-ime (pravnog - fizičkog lica),
- adresa
- mjesto
53A
Učesnik čiji se račun zadužuje:
/D/ Rračun učesnika
/D/18!n 4!a2!a2!c[3!c]
da
Primjer:
:53A:/D/907000000005800138
CKBCMEPG
BIC učesnika 57A
Učesnik čiji se račun odobrava :
/C/ Račun učesnika
/C/18!n 4!a2!a2!c[3!c]
da
Primjer:
:57A:/C/907000000005700131
PDBPMEPG
BIC učesnika 59
Račun klijenta koji se odobrava (3n-13n-2n)
/18!n 3*35x
da
Primjer:
:59:/570000000000873444
KLIJENT BANKE B
Ul.Balšićeva br.8
PODGORICA
Naziv klijenta koji se odobrava:
- naziv-ime (pravnog - fizičkog lica),
- adresa
- mjesto 70
Informacije o doznačenim sredstvima :
-
šifra transfera (SIF- 3n),
4*35x
SIF-3n
Primjer predloženog formata:
SIF-132
Učesnik A
DNS sistem
-
kod polja PBZ iza koga slijede model
poziva na broj zaduženja i poziv na
broj zaduženja odvojeni crticama
-
kod polja PBO iza koga slijede model
poziva na broj odobrenja i poziv na
broj odobrenja odvojeni crticama
PBZ-2n-20x
PBO-2n-20x
da
PBZ-05-02731266
PBO-05-35092-09-001-4000247
71A
SHA
3!a
Da
72
Svrha transfera
Na početku se unosi kod CODTYPTR/001 ili
BNF , na početku ostalih redova idu obavezno
dvije crtice//
3*35x
da
Primjer:
:72:/ CODTYPRT/001
//carinski dug
NAPOMENA: Kod uplate javnih prihoda, polje 70 poruke MT 103 popunjava se na sljedeći način:
70
Informacije o doznačenim sredstvima :
-
broj uplatnih računa (Poreske uprave,
Uprave carina , MUP-a ili Centralnog
računa Državnog trezora)
-
šifra transfera (SIF- 3n),
-
kod polja PBZ iza koga slijede model
poziva na broj zaduženja i poziv na
broj zaduženja odvojeni crticama
-
kod polja PBO iza koga slijede model
poziva na broj odobrenja i poziv na
broj odobrenja odvojeni crticama
4*35x
TC-18!n
SIF-3n
PBZ-2n-20x
PBO-2n-20x
da
Primjer predloženog formata:
:70:/ TC/805000000000095502
SIF-132
PBZ-05-02731266
PBO-05-35092-09-001-4000247
-
Šematski prikaz realizacije poruke MT 103
MT 103 (1) MT 103 (3)
MT 900 (2) MT 910 (4)
-
Šematski prikaz kada poruku MT 103 nije moguće izvršiti jer:
a/ došlo je do greške pri procesiranju poruke;
b/ nema dovoljno sredstava na računu učesnika (poruka sa prioritetom od 10 -49 evidentira se u redu za čekanje);
c/ nema dovoljno sredstava na računu učesnika (poruka sa prioritetom od 50-99 se automatski odbija).
MT 103
MT 196
2.3. Poruka MT 202 - transfer sredstava između učesnika u RTGS
sistemu
Poruka MT 202 koristi se za transfer sredstava između učesnika u RTGS-u.
Učesnik B
RTGS sistem
Učesnik A
Učesnik A
RTGS sistem Raspored elemenata je sljedeći:
Polje
Element naloga za transfer
Format
Obavezno
Napomena
Pošiljalac
da
Primalac
da 113
Za transfere u RTGS sistemu prioritet se kreće
između 0010 - 0099. Vrijednost 0010 je za
najveći prioritet, ukoliko nije naveden prioritet
podrazumijeva se 0099
4n
da
Primjer:
113:0099
20
Referenca poruke
16x
da
TRN y SWIFT-y
21
Povezana referenca
16x
da
Referenca na koju se ova poruka
odnosi ili kod NONREF 32A
Datum valute (YYMMDD),
šifra valute (EUR) i
iznos (12n,nn)
6!n3!a15d
da
Primjer:
32A:090126EUR150,39
53A
Učesnik čiji se račun zadužuje:
/D/ Račun učesnika
/D/18!n 4!a2!a2!c[3!c]
da
Primjer:
:53A:/D/907000000005800138
CKBCMEPG
BIC učesnika 58A
Učesnik čiji se račun odobrava::
/C/ Račun učesnika
/C/18!n 4!a2!a2!c[3!c]
da
Primjer:
:58A:/C/907000000005700131
PDBPMEPG
BIC učesnika 72
Na početku se unosi kod CODTYPTR/001 ili
BNF
Informacije o doznačenim sredstvima :
- kod tipa transfera
-
šifra transfera (SIF- 3n)
-
kod polja PBZ iza koga slijede model
poziva na broj zaduženja i poziv na
broj zaduženja odvojeni crticama
-
kod polja PBO iza koga slijede model
poziva na broj odobrenja i poziv na
broj odobrenja odvojeni crticama
-
svrha transfera
( na početku redova 2-5 obavezno se unose
dvije kose crtice// )
5*35x
(001)
SIF-3n
PBZ-2n20x
PBO-2n20x
35x
da
Primjer predloženog formata:
:72:/CODTYPRT/001
//SIF-383
//PBZ-00
//PBO-00-00-401-0115296-2
// UPLATA RATE KREDITA
-
Šematski prikaz realizacije poruke MT 202
MT 202 (1) MT 202 (3)
MT 900 (2) MT 910 (4)
-
Šematski prikaz kada poruka MT 202 nije moguće izvršiti jer:
a/ došlo je do greške pri procesiranju poruke;
b/ nema dovoljno sredstava na računu učesnika (poruka sa prioritetom od 10 -49 evidentira se u redu za čekanje);
Učesnik B
RTGS sistem
Učesnik A c/ nema dovoljno sredstava na računu učesnika (poruka sa prioritetom od 50-99 se automatski odbija).
MT 202
MT 296
3. Kategorija 9 - Potvrda o prijemu, statusu računa i izvještaji
3.1. Poruka MT 900 - potvrda o zaduženju računa Poruka MT 900 koristi se kao potvrda o zaduženju računa poslije izvršenog transfera (MT 103 ili MT 202). Poruku šalje RTGS sistem učesniku.
Raspored elemenata je sljedeći:
Polje
Element poruke
Format
Obavezn
o
Napomena
Pošiljalac
da
Primalac
da 20
Referenca poruke
16x
da
TRN y SWIFT-y 21
Povezana referenca
16x
d a
TRN poruke na koju se potvrda
odnosi 25:
Račun učesnika koji se zadužuje
18!n
da
:25:907000000005800138 32A
- Datum valute - (YYMMDD),
- šifra valute - (EUR),
- iznos - (12n,nn)
6!n3!a15d
da
Primjer:
:32A:090123EUR453,69
52A
BIC učesnika koji izvršava transfer za nekog
drugog učesnika
4!a2!a2!c[3!c]
:52A:CBCGMEPGRTG
72
Informacije od pošiljaoca primaocu
6*35
3.2. Poruka MT 910 - potvrda o odobrenju računa Poruka MT 910 koristi se kao potvrda o odobrenju računa poslije izvršenog transfera (MT 103 ili MT 202). Poruku šalje RTGS sistem učesniku čiji se račun odobrava.
Raspored elemenata je sljedeći:
Polje
Element poruke
Format
Obavez-no
Napomena
Pošiljalac
da
Primalac
da 20
Referenca poruke
16x
da
TRN y SWIFT-y 21
Povezana referenca
16x
da
TRN poruke na koju se potvrda
odnosi 25
Račun učesnika koji se odobrava
18!n
da
:25:907000000005700131 32A
Datum valute (YYMMDD),
šifra valute (EUR),
iznos (12n,nn).
6!n3!a15d
da
Primjer:
:32A: 090123EUR453.69
52A
Račun učesnika čiji se račun zadužuje
BIC učesnika čiji se račun zadužuje
18!n 4!a2!a2!c[3! c]
da
Primjer:
:52A:/D/907000000005800138
FFBMMEPG 72
Informacije od pošiljaoca primaocu
6*35
Učesnik A
RTGS sistem 3.3. Poruka MT 920 - zahtjevi o stanju računa i za slanje izvještaja
Poruka MT 920 koristi se kao zahtjev za informaciju o stanju računa u određenom trenutku ili kao zahtjev za slanje izvještaja o izvršenim transferima učesnika. Ovu poruku učesnik šalje RTGS sistemu.
Raspored elemenata je sljedeći:
Polje
Element poruke
Format
Obavezno
Napomena
Pošiljalac
da
Primalac
da 20
Referenca poruke
16x
da
TRN y SWIFT-y à 12
Identifikuje tip poruke za koju se šalje zahtjev
3!n
da
Mora postojati jedan od sljedećih
tipova poruke: 940,941,942
ili 950 25
Broj računa na koji se poruka odnosi
18!n
da
907000000005800138 34F
- šifra valute (EUR)
- oznaka D (za zaduženje) ili prazno
- limit ispod koga transakcija ne ulazi u
izveštaj (12n,nn)
3!a[1!a]15d
Primjer:
:34F:EURD10,
34F
- šifra valute (EUR)
- oznaka C (za odobrenje) ili prazno
- limit ispod koga transakcija ne ulazi u
izveštaj (12n,nn)
3!a[1!a]15d
Primjer:
:34F:EURC10,
------I
Ako su prisutna 2 polja 34F, prvo polje 34F mora sadržati oznaku D, a drugo polje 34F mora sadržati oznaku C, a ako je prisutno jedno polje 34F ne smiju se koristiti oznake C ili D - podrazumijeva se debitni limit.
-
Šematski prikaz odgovora na zahtjev poruke MT 920
MT 920
MT 940, MT 941, MT 942, MT950
3.4. Poruka MT 940 - izvještaj o izvršenim transferima učesnika Poruka MT 940 je dnevni izvještaj o izvršenim transferima učesnika , a odgovor je i na poslati zahtjev MT 920. Poruku MT 940 RTGS sistem šalje učesniku.
Raspored elemenata je sljedeći:
Polje
Element poruke
Format
Obavezno
Napomena
Pošiljalac
da
Primalac
da 20
Referenca poruke
16x
da
TRN y SWIFT-y 25
Broj računa
18!n
da
Broj računa čiji izvještaj se šalje 28C
Broj izvještaja / broj strane pripad. Izvještaja
5n[/3n]
da 60F
Početno stanje u obliku;
- dugovno / potražno - D/C
- datum - GGMMDD
- šifra valute - EUR
- iznos - (12n,nn)
1!a6!n3!a15d
da
Primjer:
:60F:C090628EUR1000,
à 61
Prva linija izvještaja:
- datum valute - YYMMDD,
6!n
Učesnik A
RTGS sistem
- duguje (D), potražuje (C) ….,
- iznos (12n,nn),
- kod za identif. tipa transakcije,
- referenca za vlasnika računa,
- referenca inst. koja servisira račun
Druga linija izvještaja:
- broj računa koji je izazvao promjenu
2a 15d 1!a3!c 16x [//16x]
18!n
86
- prvi red - račun dužnika (kod MT 103-polje
50K i kod MT 202 polje 53A)
- drugi red - račun povjerioca (kod MT 103-
polje59 i kod MT 202 polje 58A)
- sljedeće 4 linije izvještaja su polje 70 poruke
MT103.
6*35x
------I 62F
Zaključno stanje:
- dugovno / potražno - D/C
- datum - GGMMDD
- šifra valute - EUR
- iznos - (12n,nn)
1!a6!n3!n15d
da
Primjer:
:62F:C091010EUR1000,
3.5. Poruka MT 941 - trenutno stanje sredstava na računu Poruka MT 941 koristi se za slanje informacija o stanju računa u određenom trenutku, kao odgovor na zahtjev MT 920 .
Raspored elemenata je sljedeći:
Polje
Element poruke
Format
Obavezno
Napomena
Pošiljalac
da
Primalac
da 20
Referenca poruke
16x
da
TRN y SWIFT-y 21
Odnosna referenca
16x
da
Odnosi se na referencu poruke MT
920 koja je inicirala zahtjev 25
Broj računa
18!n
da
Broj računa na koji se poruka odnosi 28
Broj stanja / broj sekvence
5n[/2n]
da 60F
Početno stanje u obliku;
- dugovno / potražno - D/C,
- datum - GGMMDD,
- šifra valute - EUR,
- iznos (12n,nn).
1!a6!n3!a15d
da
Primjer:
:60F:C090628EUR595771,00
9 0D
- Broj transfera zaduženja,
- oznaka valute,
- vrijednost transfera zaduženja
5n3!a15d
da
Primjer:
:90D:8EUR385920,00
9 0C
-Broj transfera odobrenja,
- oznaka valute
- vrijednost transfera odobrenja
5n3!a15d
da
Primjer:
:90C:5EUR450000,00
62F
Zaključno stanje u vrijeme kreiranja izvještaja :
- dugovno / potražno - D/C
- datum - GGMMDD
- šifra valute - EUR
- iznos (12n,nn).
1!a6!n3!n15d
da
Primjer:
:62F:C091111EUR659851,00
64
Raspoloživo stanje:
- dugovno / potražno - D/C
- datum - GGMMDD
- šifra valute - EUR
- iznos (12n,nn).
1!a6!n3!a15d
Primjer (za slučaj da je za kliring
rezervisano 179.226,00 EUR) :
:64:C091111EUR480625,00
3.6. Poruka MT 942 - privremeni izvještaj o izvršenim transferima učesnika Poruka MT 942 sadrži podatke o transferima od prethodno dostavljenog privremenog ili dnevnog izvještaja, kao odgovor na zahtjev MT 920.
Raspored elemenata je sljedeći:
Polje
Element poruke
Format
Obavez-
no
Napomena
Pošiljalac
da
Primalac
da 20
Referenca poruke
16x
da
TRN y SWIFT-y 21
Odnosna referenca
16x
Odnosi se na referencu poruke MT
920 koja je inicirala zahtjev 25
Broj računa
18!n
da
Broj računa na koji se poruka odnosi 28C
Broj izvještaja / broj strane pripad. izvještaja
5n[/3n]
da
34F
- Šifra valute - EUR,
- dugovno - D ili prazno,
- limit ispod koga transfer ne ulazi u izvod
(12n,nn)
3!a[1!a]15d
da
Primjer:
:34F:EURD10,00
34F
- Šifra valute - EUR,
- potražno - C ili prazno,
- limit ispod koga transfer ne ulazi u izvještaj
(12n,nn)
3!a[1!a]15d
Primjer:
:34F:EURC10,00
13D
Datum i vrijeme slanja
YYMMDDHHMM+0100
6!n4!n1!4!n
da
Primjer:
0908261050+0100 à
61
Linija izvještaja:
- datum valute - YYMMDD
- duguje (D), potražuje (C), očekivani dugovni
promet (ED), očekivani potražni promet (EC)
- iznos
- kod za identif. tipa transfera
- referenca za vlasnika računa
- referenca inst. koja servisira račun
- broj računa
6!n 2a
15d 1!a3!c 16x [//16x] 18!n
86
- prvi red - račun dužnika (kod MT 103-polje 50K
i kod MT 202 polje 53A)
- drugi red - račun povjerioca (kod MT 103-
polje59 i kod MT 202 polje 58A)
- sljedeće 4 linije izvoda su polje 70 poruke
MT103.
6*65
------I
9 0D
- broj transfera zaduženja,
- šifra valute,
- vrijednost zaduženja.
5n3!a15d
Primjer:
:90D:2EUR2000,00
90C
- broj transfera odobrenja,
- šifra valute,
- vrijednost odobrenja.
5n3!a15d
Primjer:
:90C:8EUR1000,00
Ako su prisutna 2 polja 34F, prvo polje 34F mora sadržati oznaku D, a drugo polje 34F mora sadržati oznaku C, a ako je prisutno jedno polje 34F ne popunjava se oznaka C ili D - podrazumijeva se debitni limit.
3.7. Poruka MT 950 - izvještaj o izvršenim transferima Poruka MT 950 je izvještaj o izvršenim transferima sa računa na kraju radnog dana, po izboru učesnika.
Raspored elemenata je sljedeći:
Polje
Elemenat poruke
Format
Obavezno
Napomena
Pošiljalac
da
Primalac
da 20
Referenca poruke
16x
da
TRN y SWIFT-y
25
Broj računa učesnika
18!n
da
Broj računa čiji izvještaj se šalje
28C
Broj izvještaja / broj strane pripad. izvještaja
5n[/3n]
da 60F
Početno stanje u obliku:
- dugovno / potražno - D/C,
- datum - GGMMDD,
- šifra valute - EUR,
- iznos (12n,nn).
1!a6!n3!a15d
da
Primjer:
:60F:C090628EUR1000,00
à
61
Linija izvještaja:
- datum valute - YYMMDD,
- duguje (D), potražuje (C) …,
- iznos,
- kod za identif. tipa transfera,
- referenca za vlasnika računa,
- referenca inst. koja servisira račun.
- broj računa
6!n 2a 15d 1!a3!c 16x [//16x] 18!n
------I 62F
Zaključno stanje sa vremenom slanja:
- dugovno / potražno - D/C,
- datum - GGMMDD,
- šifra valute - EUR,
- iznos (12n,nn).
1!a6!n3!n15d
da
Primjer:
:62F:C090628EUR18910,00
3.8. Poruka MT 970 - izvještaj o izvršenim transferima u DNS sistemu i MT 972- privremeni izvještaj o izvršenim
transferima u DNS sistemu
Poruka MT 970 je izvještaj o izvršenim transferima u DNS sistemu. Šalje se automatski na kraju sesije, dok se MT 972 šalje na zahtjev i obuhvata transfere od poslednjeg MT 970 ili MT 972.
Raspored elemenata je sljedeći:
Polje
Element poruke
Format
Obavezno
Napomena
Pošiljalac
da
Primalac
da 20
Referenca poruke
16x
da
TRN y SWIFT-y 25
Broj računa učesnika
18!n
da
Broj računa čiji izvod se šalje 28C
Broj izvještaja / broj strane pripad. izvještaja
5n[/3n]
da 60F
Početno stanje u obliku:
- dugovno / potražno - D/C,
- datum - GGMMDD,
-šifra valute - EUR,
- iznos (12n,nn).
1!a6!n3!a15d
da
Primjer:
:60F:C090126EUR0,
à 61
Prva linija izvještaja:
- datum valute - YYMMDD,
- duguje (D), potražuje (C) ….,
- iznos - (12n,nn),
- kod za identif. tipa transfera,
- referenca za vlasnika računa
- referenca inst. koja servisira račun
Druga linija izvještaja:
- BIC kod
6!n 2a 15d 1!a3!c 16x [//16x]
4!a2!a2!c[3!c]
:
61:090126D53,30S102890560
000003832c//24416664
HBBAMEPG ------I 62F
Zaključno stanje u obliku:
- dugovno / potražno - D/C,
- datum - GGMMDD,
- šifra valute - EUR,
- iznos (12n,nn).
1!a6!n3!a15d
da
Primjer:
:62F:C090126EUR1592,76
3.9. Poruka MT 973 - zahtjevi za izvještaje iz DNS sistema
Poruka MT 973 se koristi kao zahtjev za informacije o stanju računa u DNS sistemu ili zahtjev za slanje izvještaja o transferima izvršenim u DNS sistemu.
Raspored elemenata je sljedeći:
Polje
Element poruke
Format
Obavezno
Napomena
Pošiljalac
da
Primalac
da 20
Referenca poruke
16x
da
TRN y SWIFT-y à 12
Tip poruke koja se zahtijeva
3!n
da
Broj odgovarajuće poruke
MT970 ili MT972 25
Broj računa na koji se poruka odnosi
18!n
da -----I
-
Šematski prikaz odgovora na zahtjev poruke MT 973
MT 973
MT 970, MT 972
3.10. Poruka MT 985 - upit o statusu računa
Učesnik šalje poruku MT 985 za upit o statusu računa učesnika na koju sistem dgovora porukom
MT 986.
Raspored elemenata je sljedeći:
Polje
Element poruke
Format
Obavezno
Napomena
20
Referenca poruke
16x
da
TRN y SWIFT-y 57A
BIC kod RTGS sistema
4!a2!a2!c[3!c]
Primjer:
:57A:CBCGMEPGIPS 59
Račun učesnika na koji se odnosi upit
/18!n
4!a2!a2!c[3!c]
da
Polje "račun na koji se odnosi upit" (/18!
n) nije obavezno za sljedeće upite:
PCLT, TTLS i TTLD
Primjer:
:59:ATLMMEP2
BIC učesnika
75
Zahtjevi
Opis formata u
zavisnosti od
zahtjeva:
da
Vrste zahtjeva:
4!a
STAT - status račna
4!a
SQDC - izvještaj o redu za čekanje
4!a
PCLT - setovani limit za kliring
4!a
[6!n/]16x
- TTLS - totali serije u DNS sistemu
- YYMMDD, kosa crta a posle nje sesija
(primer MORNING,EVENING ili
FINAL)
Učesnik A
RTGS sistem
3.11. Poruka MT 986 - odgovor na upit o statusu
Porukom MT 986 šalje se odgovor na upit poslat porukom MT 985.
Odgovori koje podržava RTGS sistem dati su u polju 79.
Raspored elemenata je sljedeći:
Polje
Element poruke
Format
Obavezno
Napomena
Pošiljalac
da
Primalac
da 20
Referenca poruke
16x
da
TRN y SWIFT-y 21
Referenca poruke na koju se odgovor
odnosi
16x
da
59
Račun učesnika na koji se odnosi odgovor
/18!n
4!a2!a2!c[3!c]
da
Primjer:
:59:PDBPMEPG
BIC učesnika 79
Odgovor
da
Mogući odgovori na upit STAT:
4!a[/6!n4!n1!x4!n]
STAT/
Mogući odgovori na upit o statusu
(drugi red odgovora):
-
račun nije blokiran
-
račun je blokiran za zaduženje
-
račun je blokiran za odobrenje
-
račun je blokiran
2!a
2!a
2!a
2!a
AA - kod
DA - kod
AC - kod
DC - kod
Mogući odgovori na upit SQDC:
- Suma i broj suspendovanih transfera koje
zadužuju račun
- Suma i broj suspendovanih transfera koje
odobravaju račun
- Suma i broj suspendovanih transfera u
redu za čekanje koje zadužuju račun
- Suma i broj suspendovanih transfera u
redu za čekanje koje odobravaju račun
-
Suma i broj transfera koje su
zamrzle zaduženje računa
- Suma i broj transfera koje su zamrzle
odobrenje računa
-Tekuće saldo na računu (CC potražno ili
CD dugovno)
- Raspoloživo stanje na računu (AC
potražno ili AD dugovno)
4!a[/6!n4!n1!x4!n]
2!a3!a15d[/5n]
2!a3!a15d[/5n]
2!a3!a15d[/5n]
2!a3!a15d[/5n]
2!a3!a15d[/5n]
2!a3!a15d[/5n]
2!a3!a15d[/5n]
2!a3!a15d[/5n]
SQDC/
Mogući odgovori na upit (drugi red
odgovora):
SDEUR153994,21/14 (kod SD)
SCEUR0,/0 (kod SC)
EDEUR153994,21/14 (kod ED)
ECEUR0,/0 (kod EC)
LDEUR0,/0 (kod LD)
LCEUR0,/0 (kod LC)
CCEUR1988850,07/3 (kod CC,CD)
ADEUR1988850,07/3 (kod
AC,AD)
Odgovor na upit o setovanom limitu :
PLCT/datum i vrijeme
-
račun na koji se odgovor odnosi
-
datum, valuta, setovani limit
-
datum, valuta, vrij. polja je 0
-
datum, valuta ,neto pozicija u
tekućoj sesiji
-
tekuća sesija
4!a[/6!n4!n1!x4!n]
/18!n
6!n3!a15d 6!n3!a15d 1!a6!n3!a15d
PCLT/0901260901+0000
/907000000005800138
090126EUR150000,
090126EUR0,
C090126EUR0,
MORNING
Odgovori na upite TTLS sadrže podatke o
zahtjevu u prvom redu,broj primljenih
poruka u drugom redu, broj prihvaćenih,
poravnatih ,na čekanju i odbijenih poruka.
Datum i sekcija
4!a[/6!n4!n1!x4!n]
5d/5d/5d
17d/5d/5d 17d/5d/5d 17d/5d/5d 17d/5d/5d
6!n16x
TTLS/
4. Kategorija n - Zajedničke grupne poruke
4.1. Poruka MT n91 - Izvještaj o dnevnom iznosu naknade Centralnoj banci za izvršavanje transfera u RTGS sistemu
i DNS sistemu
Poruka MT 991 se šalje kao Izvještaj o dnevnom iznosu naknade Centralnoj banci za izvršavanje transfera u RTGS sistemu i DNS sistemu.
Raspored elemenata je sljedeći:
Polje
Elemenat poruke
Format
Obavezno
Napomena
Pošiljalac
da
Primalac
da 20
Referenca poruke
16x
da
TRN y SWIFT-y 21
Povezana referenca
16x
d a
NONREF 32B
Šifra valute (EUR)
Iznos (12n,nn)
3!a15d
da
Primjer:
:32B:EUR6,76 52A
Račun učesnika koji se zadužuje
BIC učesnika
[/1!a][/18!n] 4!a2!a2!c[3!c]
da
Primjer:
:52A:PDBPMEPG 57A
Račun Centralne banke Crne Gore kojoj se
plaća naknada
BIC Centralne banke Crne Gore
[/1!a][/18!n] 4!a2!a2!c[3!c]
da
Primjer:
:57A:CBCGMEPG 71B
Detalji o zaduženju
6*35
da
72
Informacije od pošiljaoca primaocu
6*35
:72:/INT/
4.2. Poruka MT n92 - zahtjev za opoziv poruke Poruka MT 192 se koristi kao zahtjev za opoziv prethodno poslate poruke MT 103 i MT 102 , a poruka MT 292 kao zahtjev za opoziv poruke MT 202.
Poruka se može opozvati samo dok još nije izvršena.
Raspored elemenata je sljedeći:
Polje
Elemenat poruke
Format
Obavezno
Napomena
Pošiljalac
da
Primalac
da 20
Referenca poruke
16x
da
TRN y SWIFT-y 21
Povezana referenca
16x
d a
TRN poruke na koju se zahtjev
odnosi
11S
MT broj
3!n 6!n [4!n6!n]
da
Primjer:
11S:103
090104
4444666666
Datum - GGMMDD
Broj serije i sekvence orginalne poruke 79
BIC učesnika koji je poslao poruku
4!a2!a2!c[3!c] 6!n
da
Primjer:
:79: PDBPMEPG
090104
Datum valute - GGMMDD
-
Šematski prikaz zahtjeva MT 192 za opoziv poruke MT102 i MT103
MT 192
MT 196
-
Šematski prikaz zahtjeva MT 292 za opoziv poruke MT202
MT 292
MT 296
4.3. Poruka MT n95 - upiti o prethodno poslatim porukama Poruka MT 195 se koristi za upit o prethodno poslatoj poruci MT 103 i MT 102 , a poruka MT 295 je upit o prethodno poslatoj poruci MT 202.
Raspored elemenata je sljedeći:
Polje
Elemenat poruke
Format
Obavezno
Napomena
Pošiljalac
da
Primalac
da 20
Referenca poruke
16x
da
TRN y SWIFT-y 21
Povezana referenca
16x
d a
TRN poruke na koju se upit odnosi 75
Upiti
4!a
da
Zahtjevi koji su predviđeni:
STAT - Status poruke
PRTY - Promjena prioriteta
DUPL - Kopija poruke
Učesnik A
RTGS sistem
Učesnik A
RTGS sistem 77A
Ovo polje se koristi samo kada želimo da
promijenimo prioritet (ako je u polju :75: kod
PRTY)
4!c
Ovo polje
je
obavezno
samo za
upit PRTY,
Primjer:
77A:0020
11S
MT broj
3!n 6!n [4!n6!n]
Primjer:
:11S:103
090104
4444666666
Datum - GGMMDD
Serija i sekvenca orginalne poruke
79
BIC učesnika koji je poslao poruku
4!a2!a2!c[3!c] 6!n
Primjer:
:79: PDBPMEPG
090104
Datum valute
-
Šematski prikaz upita MT 195 za prethodno poslate poruke MT102 i MT103
MT 195
MT 196
-
Šematski prikaz upita MT 295 za poslatu poruku MT202
MT 295
MT 296
4.4. Poruka MT n96 - odgovor na zahtjeve i upite Poruka MT 196 je odgovor na zahtjeve i upite prethodno poslatoj poruci MT 192 i MT 195 , a poruka MT 296 je odgovor na zahtjeve i upite prethodno poslatoj poruci MT 292 i MT 295.
Pored navedenog sistem automatski generiše poruku MT196 i MT296. Generisanom porukom MT196 sistem informiše učesnika:
- o prethodno poslatoj poruci MT102, - nemogućnosti realizacije MT103, a porukom MT296 o nemogućnosti realizacije MT202.
Raspored elemenata je sljedeći:
Polje
Element poruke
Format
Obavezno
Napomena
Pošiljalac
da
Primalac
da
20
Referenca poruke
16x
da
TRN y SWIFT-y
21
Povezana referenca
16x
d a
TRN iz polja 20: poruke n95 na koju se pravi
odgovor
76
Odgovori
4!a[/6!n4!n1!x4!n]
da
Odgovori na zahtjeve:
STAT - statusi dati u narednoj tabeli
Učesnik A
RTGS sistem
Učesnik A
RTGS sistem
4c[/6!n4!n1!x4!n]
DUPL - kopija poruke
PRTY - promjena prioritete
CANC - poruka je opozvana
ERRC - poruka o grešci u zahtjevu 77A
Tekstualni opis odgovora
(odnosi se na grešku
zahtjeva ili upita)
3*35x
Ukoliko odgovor sadrži grešku u prvom redu se
dobije kod a u druga dva opis greške
11R
MT broj - broj poruke
3!n
6!n
[4!n6!n]
da
Primjer:
:11R:202
090628
4444666666
Datum - GGMMDD
Serija i sekvenca orginalne
poruke
Kopija najmanje svih
obaveznih polja originalne
poruke
Na upit o statusu (STAT) polje 76 može da sadrži sljedeće odgovore:
STAT/datum,vrijeme - prvi red odgovora REJT /datum,vrijeme - drugi red odgovora
Poruka je opozvana porukom MT n92 koju je poslao
učesnik STAT/datum,vrijeme - prvi red odgovora CANC/datum,vrijeme - drugi red odgovora
Poruka je opozvana po pravilima RTGS sistema CBCG,
šalje se i kad CBCG odbije poruku bez zahtjeva STAT EXEC
Transfer se upravo izvršava STAT SETL
Transfer je izvršen
STAT ERRC
Došlo je do greške pri procesiranju poruke STAT WAIT
Poruka je u redu za čekanje STAT SUSP
Poruka je suspendovana STAT ERRP
Došlo je do greške STAT NETR
Poruka je prihvaćena za kliring. Učesnik može da je
opozove.
STAT NETS
Poruka je poravnata poslije procedure kliringa. Opoziv
nije moguć.
Na upit o kopiji poruke (DUPL) polje 76 može da sadrži sljedeće odgovore:
DUPL - prvi red poruke OK - drugi red poruke
Tražena poruka će biti kopirana DUPL ERRC
Graška u toku kopiranja transfera
Na upit o kopiji promjeni prioriteta (PRTY) polje 76 može da sadrži sljedeće odgovore:
PRTY - prvi red poruke <izmij. prioritet> - drugi red poruke
Prioritet transfera je promijenjen PRTY ERRC
Greška u promjeni prioriteta
Na zahtjev za opoziv poruke (CANC) polje 76 može da sadrži sljedeće odgovore:
CANC - transfer je opozvan OK - drugi red poruke
Transfer je opozvan CANC ERRC
Greška u zahtjevu procesiranja
Poruka o grešci kao odgovor na upit MTn95 ili MTn92 u polju 76 daje samo jedan red sa kodom ERRC dok u polju 77A daje opis greške.
4.5. Poruka MT n99 - poruka slobodnog formata Poruka MT 999 je poruka slobodnog formata.
Raspored elemenata je sljedeći:
Polje
Elemenat poruke
Format
Obavezno
Napomena
Pošiljalac
da
Primalac
da 20
Referenca poruke
16x
da
TRN y SWIFT-y 21
Povezana referenca
16x 79
Tekst poruke:
35*50x
da
/TEXTMESSAGE/BIC
/11!c/4!a2!a2!c[3!c]
34*50x
Primjer:
/TEXTMESSAGE/ PDBPMEPG
Promjena korisničkog statusa:
/SETUSERLOCK/ kod koris. čiji
status se mijenja
/DIRECTION/
/STATUS/ status koji se dodjeljuje
/11!c/12x
2*50
Primjer:
:79:/SETUSERLOCK/LLLLLL
/DIRECTION/
/STATUS/00
Setovanje limita računa:
/SETACCOUNTLIMIT/CLEARING
/STATUS/
/ACTION/
/DIRECTION/I (za povećanje) ili D
(za smanjenje limita)
/ACCAUNT/ broj računa
/AMOUNT/ iznos - novi limit
15/!c/16x
5*50
Primjer:
/SETACCOUNTLIMIT/CLEARING
/STATUS/
/ACTION/
/DIRECTION/I
/ACCAUNT/ 907000000005050134
/AMOUNT/ 1000,00
Zahtjev za izvještaj o periodu radnog
dana:
/GETBUSINESSDAYPERIOD/
/20!C/
-
Šematski prikaz poruke slobodnog formata
MT 999
MT 999
PRILOG 4
_________________ štambilj učesnika
PRIJAVA LICA OVLAŠĆENIH ZA KONTAKT SA CENTRALNOM BANKOM CRNE GORE PO POSLOVIMA IZVRŠAVANJA TRANSFERA U RTGS SISTEMU
____________________________________________________________
( pun naziv učesnika iz potvrde o registraciji u CRPS)
Matični broj učesnika: ______________________________
Učesnik A
RTGS sistem
Za kontakt sa Centralnom bankom Crne Gore po poslovima izvršavanja transfera u RTGS sistemu ovlašćena lica su:
1. Ime i prezime:____________________________________________
Broj telefona i telefaksa: _______________________________
E-mail adresa: _____________________________
Svojeručan potpis ovlašćenog lica za kontakt ______________________
2. Ime i prezime:___________________________________________
Broj telefona i telefaksa: ________________________________
E-mail adresa: _____________________________
Svojeručan potpis ovlašćenog lica za kontakt: ____________________
Mjesto i datum: __________________________
_____________________
pečat i potpis lica ovlašćenog za zastupanje
_________________ štambilj učesnika
PRIJAVA LICA OVLAŠĆENIH ZA KONTAKT SA CENTRALNOM BANKOM CRNE GORE PO POSLOVIMA IZVRŠAVANJA TRANSFERIMA U DNS SISTEMU
________________________________________________________________
( pun naziv učesnika iz iz potvrde o registraciji u CRPS)
Matični broj učesnika: ______________________________
Za kontakt sa Centralnom bankom Crne Gore po poslovima izvršavanja transfera u DNS sistemu ovlašćena lica su:
1. Ime i prezime:____________________________________________
Broj telefona i telefaksa: _______________________________
E-mail adresa: _____________________________
Svojeručan potpis ovlašćenog lica za kontakt ______________________
2. Ime i prezime:___________________________________________
Broj telefona i telefaksa: ________________________________
E-mail adresa: _____________________________
Svojeručan potpis ovlašćenog lica za kontakt: ____________________
Mjesto i datum: __________________________
_____________________
pečat i potpis lica
ovlašćenog za zastupanje
PRILOG 5
_________________ štambilj učesnika
PRIJAVA LICA
OVLAŠĆENOG ZA SIGURNOST I ZAŠTITU KOMUNIKACIJE
SA RTGS SISTEMOM I DNS SISTEMOM
____________________________________________________________
( pun naziv učesnika iz potvrde o registraciji u CRPS)
Matični broj učesnika: ______________________________
Ovlašćeno lice zaduženo za sigurnost i zaštitu komunikacije sa RTGS sistemom i DNS sistemom je:
1. Administrator zaštite
Ime i prezime:____________________________________________
Broj telefona i telefaksa: _______________________________
E-mail adresa: _____________________________
Svojeručan potpis ovlašćenog lica za kontakt ______________________
Mjesto i datum: __________________________
_____________________
pečat i potpis lica ovlašćenog za zastupanje
PRILOG 6
SPECIFIKACIJA
hardverske opreme potrebne za povezivanje sa RTGS sistemom
Za povezivanje sa RTGS sistemom učesnik je dužan da obezbijedi jedan personalni računar za instalaciju File Adaptera (ili RCCC
komponente ili Controller Workplace, zavisno za koji način konekcije se učesnik odluči) najmanje sljedećih karakteristika:
a)
IBM PC kompatibilan računar,
b)
procesor klase Pentium CPU 366 MHz,
c)
RAM 256,
d)
slobodan prostor na hard disku 40 MB,
e)
VGA rezolucija grafičkog podsistema,
f)
Microsoft kompatibilan miš.
PRILOG 7
___________________ štambilj učesnika
OBAVJEŠTENJE O PROMJENI PRIORITETA PORUKE U RTGS SISTEMU
Naziv učesnika:
Račun učesnika:
Tip poruke čija se promjena prioriteta traži:
(MT202, MT103)
Postojeći prioritet poruke:
Zahtijevani prioritet poruke:
Referenca poruke/polje 20:
Iznos transfera:
Mjesto i datum:
_____________________
Pečat i potpis lica
ovlašćenog za zastupanje
_____________________
PRILOG 8
___________________ štambilj učesnika
OBAVJEŠTENJE O OPOZIVU PORUKA ZA TRANSFER U RTGS SISTEMU
Naziv učesnika:
Račun učesnika:
Tip poruka čiji se opoziv traži:
(MT103, MT202)
Referenca poruke/polje 20:
Iznos transfera:
Mjesto i datum:
_____________________
Pečat i potpis lica
ovlašćenog za zastupanje
_____________________
___________________ štambilj učesnika
OBAVJEŠTENJE O OPOZIVU PORUKA ZA TRANSFER U DNS SISTEMU
Naziv učesnika:
Račun učesnika:
Tip poruka čiji se opoziv traži:
( MT102)
Referenca poruke/polje 20:
Iznos transfera:
Mjesto i datum:
_____________________
Pečat i potpis lica
ovlašćenog za zastupanje
_____________________
PRILOG 9
___________________
štambilj učesnika
OBAVJEŠTENJE O UTVRĐIVANJU ILI PROMJENI LIMITA ZA NEGATIVNU NETO POZICIJU IZ MULTILATERALNOG OBRAČUNA U DNS SISTEMU
Naziv učesnika:
Račun učesnika:
Iznos limita za negativnu neto poziciju u €:
Mjesto i datum:
_____________________
Pečat i potpis lica
ovlašćenog za zastupanje
_____________________
PRILOG 10
___________________ štambilj učesnika
ZAHTJEV ZA PONOVNO SLANJE PORUKA IZ RTGS SISTEMA
Naziv učesnika:
Račun učesnika:
Tip poruka koje treba ponovo poslati:
Referenca poruke/polje 20:
Iznos transfera:
Mjesto i datum:
_____________________
Pečat i potpis lica
ovlašćenog za zastupanje
_____________________
___________________ štambilj učesnika
ZAHTJEV ZA PONOVNO SLANJE PORUKA IZ DNS SISTEMA
Naziv učesnika:
Račun učesnika:
Tip poruka koje treba ponovo poslati:
Referenca poruke/polje 20:
Iznos transfera:
Mjesto i datum:
_____________________
Pečat i potpis lica
ovlašćenog za zastupanje
_____________________
PRILOG 11
___________________ štambilj učesnika
REKLAMACIJE TRANSFERA IZVRŠENIH U RTGS SISTEMU
Naziv učesnika:
Račun učesnika:
Predmet reklamacije:
Spisak priložene dokumentacije:
SWIFT format poruke kojom je transfer izvršen, referenca poruke, ostale poruke koje su u vezi sa spornim transferom, izvod o izvšenom međubankarskom transferu i sl.
Mjesto i datum:
_____________________
Pečat i potpis lica
ovlašćenog za zastupanje
_____________________
___________________ štambilj učesnika
REKLAMACIJE TRANSFERA IZVRŠENIH U DNS SISTEMU
Naziv učesnika:
Račun učesnika:
Predmet reklamacije:
Spisak priložene dokumentacije:
SWIFT format poruke kojom je transfer izvršen, referenca poruke, ostale poruke koje su u vezi sa spornim transferom, izvod o izvšenom međubankarskom transferu i sl.
Mjesto i datum:
_____________________
Pečat i potpis lica
ovlašćenog za zastupanje
_____________________
PRILOG 12
ZAHTJEV ZA PRODUŽENJE RADA RTGS SISTEMA
Naziv učesnika:
Račun učesnika:
Razlog produženja rada:
Vrijeme produženja rada u minutima:
Mjesto i datum:
_____________________
Pečat i potpis lica
ovlašćenog za zastupanje
_____________________
ZAHTJEV ZA PRODUŽENJE RADA DNS SISTEMA
Naziv učesnika:
Račun učesnika:
Razlog produženja rada:
Vrijeme produženja rada u minutima:
Mjesto i datum:
_____________________
Pečat i potpis lica
ovlašćenog za zastupanje
