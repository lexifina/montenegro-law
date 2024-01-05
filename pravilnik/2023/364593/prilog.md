PRILOG 3
UPUTSTVO ZA DOSTAVU PODATAKA O DEPONENTIMA, DEPOZITIMA I DOSPJELIM OBAVEZAMA
1. Svrha Svrha uputstva je utvrđivanje vrste, forme, obima, sadržaja podataka i dokumentacije koje kreditna institucija u kojoj je nastupio zaštićeni slučaj (u daljem tekstu: kreditna institucija) dostavlja Fondu za zaštitu depozita (u daljem tekstu: FZD) za obračun i isplatu garantovanih depozita.
2. Tehnički i organizacioni preduslovi (generisanje .csv datoteka)
2.1. Datoteke U svrhu pripreme isplate garantovanih depozita kreditna institucija u kojoj je nastupio zaštićeni slučaj dužna je da generiše i dostavi FZD-u četiri datoteke u .csv formatu i jednu datoteku u ZIP formatu:
I. bazu matičnih podataka o deponentima (MAT<MB>.csv), II. bazu podataka o depozitima (DPZ<MB>.csv), III. bazu podataka o dospjelim obavezama deponenata (KRD<MB>.csv), IV. bazu podataka o identifikacionim dokumentima, (DOK<MB>.csv) i V. datoteku sa identifikacionim dokumentima u ZIP formatu (pdf, jpg,gif) Oznaka <MB> označava matični broj kreditne institucije, koji se koristi u nazivu datoteka (naziv fajla):
 format datoteke matičnih podataka o deponentima je MAT12345678.csv gdje je
12345678 matični broj kreditne institucije.
 format datoteke podataka o depozitima je DPZ12345678.csv gdje je 12345678
matični broj kreditne institucije.
 format
datoteke
podataka
o
dospjelim
obavezama
deponenata
je
KRD12345678.csv gdje je 12345678 matični broj kreditne institucije.
 format datoteke podataka o identifikacionim dokumentima je DOK12345678.csv
gdje je 12345678 matični broj kreditne institucije.
 format datoteke sa identifikacionim dokumentima je ZIP12345678 gdje je 12345678
matični broj kreditne institucije.
U .csv formatu tačka-zarez (;) predstavlja graničnik i on se ne smije koristiti u tekstu. Sadržaj čine velika štampana slova i cifre.
2.2. Kodna stranica Kodna stranica datoteka je MSWIN 1250 ili UTF-8.
2.3. Prvi red .csv datoteke Prvi red svake datoteke je naziv kolona:
- za bazu matičnih podataka o deponentima: TIP LICA; ŠIFRA; NAZIV; PREZIME; JMB/MB; ID NEREZIDENTA; ISPRAVA NEREZIDENTA; DATUM RODJENJA; TIP DEPONENTA; MJESTO; ADRESA; PTT; DRŽAVA; DRŽAVLJANSTVO; TELEFON / FAX; EMAIL; KONTAKT.
- za bazu podataka o depozitima: RAČUN; KONTO; TIP DEPOZITA; ŠIFRA DEPONENTA; VALUTA; GLAVNICA VALUTA; KAMATA VALUTA; GLAVNICA EUR; KAMATA EUR; DATUM OBRAČUNA.
- za bazu podataka o dospjelim obavezama deponenata: RAČUN; KONTO; ŠIFRA DEPONENTA; VALUTA; GLAVNICA VALUTA; GLAVNICA EUR.
- za bazu podataka o identifikacionim dokumentima deponenata:
ŠIFRA DEPONENTA, VRSTA DOKUMENTA i IME DATOTEKE - za datoteku identifikacionih dokumenata u ZIP formatu dostaviti kopije identifikacionih dokumenata
2.4. Dostava podataka Dostava podataka obavlja se službeno CD-om ili USB-om.
I. BAZA MATIČNIH PODATAKA O DEPONENTIMA
Baza matičnih podataka o deponentima je popis deponenata kreditne institucije. Ovu bazu treba formirati na osnovu podataka na dan nastupanja zaštićenog slučaja u kreditnoj instituciji (na dan donošenja rješenja o nedostupnosti depozita ili nastupanja zaštićenog slučaja nad kreditnom institucijom).
Sadržaj baze matičnih podatka o deponentima je prikazan Tabelom 1.1
Kolon
a
Naziv
kolona
Sadržaj
Obaveznos
t unosa
Oznaka
A
TIP LICA
Tip lica
Obavezan
FL PL
B
ŠIFRA
DEPONENT
A
Interna šifra deponenta
Obavezan
XXXXAAAAXX
C
NAZIV
Ime deponenta - fizičko
lice ili naziv deponenta -
pravno lice
Obavezan
AAAAAAAA
AAAAA A.D.
D
PREZIME
Prezime deponenta
Obavezan
za fizička
lica
AAAAAAAA
E
JMB/MB
JMB - fizičko lice (13
cifara)
MB - ravno lice (8 cifara)
Obavezno
za rezidente
XXXXXXXXXXXXX
XXXXXXXX
F
ID
NEREZIDEN
TA
Nerezident -
identifikaciona oznaka -
broj PASOSA
Obavezno
za
nerezidente
AXXXAXXXXXXXX
G
ISPRAVA
NEREZIDEN
TA
Naziv isprave
Obavezno
za
nerezidente
AAAAAAAAAAA
H
DATUM
ROĐENJA
Datum rođenja
Obavezan
DD.MM.GGGG
I
TIP
DEPONENT
A
Tip deponenta
Obavezan
1.0 1.9 1.10 1.12
1.14 1.15 1.16 1.17
1.18
1.19
2.0 2.1 2.2 2.3 2.4 2.5
1 Napomena: Za bazu podataka o deponentima neophodno je dostaviti svih 17 kolona, bez obzira na nepostojanje podataka, dakle treba fizički da postoji i svaka prazna kolona.
2.6 2.7 2.8 2.9 2.11
2.12 2.13 2.14 2.15
2.16 2.17 2.18 2.19
J
MJESTO
Mjesto
prebivališta
/
boravišta /sjedište
Obavezan
AAAAAAAAAAA
K
ADRESA
Adresa prebivališta /
boravišta / sjedište
Obavezan
AAAAAAAAXXX
L
PTT
Poštanski broj
prebivališta / boravišta /
sjedište
XXXXX
M
DRŽAVA
Država prebivališta /
boravišta / sjedište
Obavezan
AA
N
DRŽAVLJA
NSTVO
Državljanstvo
nerezidenta
AA
O
TELEFON /
FAX
Telefon / Fax
XXXXXXXXXXXX
P
EMAIL
Email adresa
AAAAAAXXXXX
Q
KONTAKT
Kontakt osoba
AAAAAAAAAAAA
Napomena: X - oznaka u tabeli za cifru; A - oznaka u tabeli sa alfabetski znak.
TIP LICA - Obavezan unos.
FL .....skraćena oznaka za fizička lica;
PL .....skraćena oznaka za pravna lica.
Fizička lica koja obavljaju privrednu djelatnost, kao i advokati, notari, izvršitelji i sl, takođe se vode pod TIP LICA - fizičko lice, skraćena oznaka FL.
Društva bez svojstva pravnog lica i suvlasničke zajednice, takođe se vode pod TIP LICA - pravno lice, skraćena oznaka PL.
Ne smiju se koristiti bilo koji simboli, uključujući sve znake interpukcije. Dakle, polje se ispunjava samo VELIKIM SLOVIMA, skraćenicama FL ili PL.
ŠIFRA DEPONENTA- Obavezan unos.Interna šifra deponenta mora biti jedinstvena. Ograničenje za unos u polju šifre je do 30 simbola. Nijesu dozvoljeni razmaci unutar šifre, navodnici, tačke i ostali specijalni znaci, tj. Šifra se može sastojati od CIFARA I VELIKIH SLOVA.
NAZIV - Obavezan unos. Za fizičko lice se unosi ime, za pravno lice se unosi naziv. Ne smiju se koristiti navodnici i ostali specijalni znaci kod naziva pravnog lica, ali je moguće koristiti tačku (Npr. PLANTAŽE A.D. ili MARKO D.O.O.). Polje se ispunjava VELIKIM SLOVIMA
PREZIME - Obavezan unos samo za fizička lica. Dakle, polje je prazno za pravna lica. Polje se ispunjava VELIKIM SLOVIMA
JMB/MB - Obavezan unos. Za fizička lica se unosi jedinstveni matični broj - trinaest cifra, a za pravna lica se unosi matični broj - osam cifara. Dakle, polje se ispunjava CIFRAMA;
ID NEREZIDENTA - Obavezan unos samo za nerezidente. Dakle, polje je prazno za rezidente. Za identifikaciju i unos nerezidenta koristiti podatke iz pasoša. Oznaka mora biti jedinstvena. Moguća kombinacija CIFARA I VELIKIH SLOVA.
ISPRAVA NEREZIDENTA - Obavezan unos samo za nerezidente. Dakle, polje je prazno za rezidente. Naznačiti naziv isprave (Polje ispuniti VELIKIM SLOVIMA).
DATUM RODJENJA - Obavezan unos samo za fizička lica. Obavezno koristiti format: DD.MM.GGGG Nije dozvoljena upotreba kosih crta (/) ili drigih znakova.
TIP DEPONENTA - Obavezan unos. Zavisno od tipa lica, da li je fizičko ili pravno lice, svakom deponentu treba dodijeliti pripadajuću numeričku oznaku prema kalsifikaciji FZD-a datoj u ovom uputstvu.
1.0; 1.9; 1.10; 1.12; 1.14; 1.15; 1.16; 1.17; 1.18; 1.19 - fizička lica;
2.0; 2.1; 2.2; 2.3; 2.4; 2.5; 2.6; 2.7; 2.8; 2.9; 2.11; 2.12; 2.13; 2.14; 2.15; 2.16; 2.17; 2.18; 2.19 - pravna lica.
MJESTO - Obavezan unos. Mjesto ili naselje. Polje se ispunjava VELIKIM SLOVIMA. ADRESA - Obavezan unos. Ulica i kućni broj. Polje se ispunjava VELIKIM SLOVIMA I CIFRAMA.
PTT - Nije obavezan unos ali, ako se ne unose podaci, kolona L mora postojati i prazna.
DRŽAVA - Obavezan unos. Iz službenog šifarnika država obavezno unijeti alfabetska šifru zemlje - dva simbola. Npr: RS -Srbija; ME- Crna Gora.
DRŽAVLJANSTVO - Nije obavezan unos, ali, ako se ne unose podaci, kolona N mora postojati i prazna. Ako se radi o nerezidentu, službeni šifarnik država - alfabetska oznaka sa dva simbola.
TELEFON / FAX - Nije obavezan unos ali, ako se ne unose podaci, kolona O mora postojati i prazna.
EMAIL - Nije obavezan unos ali, ako se ne unose podaci, kolona P mora postojati i prazna.
KONTAKT - Nije obavezan unos ali, ako se ne unose podaci, kolona Q mora postojati i prazna.
KOLONA I - TIP DEPONENTA - Svakom deponentu treba dodijeliti pripadajuću numeričku oznaku:
Fizička lica
1.0 Dodjeljuje se fizičkim licima kod kojih ne postoji ograničenje raspolaganja i obračuna,
odnosno isplate garantovanih depozita (Deponenti koji imaju pravo na isplatu
garantovanog depozita) u skladu sa članom 6 stav 1 Zakona o zaštiti depozita ("Sl. list
Crne Gore", br. 72/19) (u daljem tekstu: Zakon).
Trajna blokada dodjeljuje se svim fizičkim licima koja nemaju pravo na isplatu garantovanog depozita u skladu sa članom 6 st. 2 Zakona:
1.9 depoziti lica koja direktno ili indirektno učestvuju sa 10% ili više u kapitalu ili
glasačkim pravima u toj kreditnoj instituciji;
1.10 depoziti lica koja su članovi organa upravljanja i/ili stalnih tijela organa
upravljanja kreditne institucije, koji su te funkcije obavljali na dan nastupanja
zaštićenog slučaja ili u periodu posljednjih 12 mjeseci prije nastupanja zaštićenog
slučaja;
1.12 depoziti lica koja su vršila reviziju finansijskih izvještaja kreditne institucije u
periodu 36 mjeseci prije dana nastupanja zaštićenog slučaja;
1.14 depoziti koji proizlaze iz transakcija za koju je pravosnažnom sudskom
odlukom utvrđeno da je povezana sa pranjem novca ili finansiranjem terorizma;
1.15 depoziti lica za koja je, izvještajem o kontroli Centralne banke Crne Gore (u
daljem tekstu: CBCG), utvrđeno da su doprinijeli pogoršanju finansijskog stanja
kreditne institucije;
1.16 depoziti lica koji ne glase na ime, odnosno depoziti čiji vlasnik nije identifikovan
do dana nastupanja zaštićenog slučaja (neimenovani depoziti);
1.17 obaveze iz dužničkih hartija od vrijednosti i drugih finansijskih instrumenata
koje je izdala ili čiju isplatu garantuje kreditna institucija u kojoj je nastupio zaštićeni
slučaj;
1.18 potraživanja klijenata investicionog društva, klijenata kreditne institucije za koje
kreditna institucija pruža investicione usluge i klijenata društva za upravljanje
investicionim fondovima, kada društvo pruža investicione usluge, koje su uključene
u sistem zaštite investitora u skladu sa zakonom kojim se uređuje tržište kapitala;
1.19 instrumenti deponenata kreditne institucije u kojoj je nastupio zaštićeni slučaj,
koji su uključeni u regulatorni kapital kreditne institucije u skladu sa zakonom kojim
se uređuje poslovanje kreditnih institucija.
Pravna lica
2.0 Dodjeljuje se pravnim licima kod kojih ne postoji ograničenje raspolaganja i obračuna,
odnosno isplate garantovanih depozita (Deponenti koji imaju pravo na isplatu
garantovanog depozita) u skladu sa članom 6 st. 1 Zakona.
Trajna blokada dodjeljuje se svim pravnim licima koja nemaju pravo na isplatu garantovanog depozita u skladu sa članom 6 st. 2 Zakona:
2.1 depoziti pravnih lica koja se bave poslovima osiguranja i reosiguranja u skladu
sa zakonom kojim se regulišu poslovi osiguranja i reosiguranja;
2.2 depoziti državnih organa i organizacija i organa i organizacija opštine, odnosno
drugog oblika organizovanja lokalne samouprave;
2.3 depoziti fondova za obavezno zdravstveno, penzijsko i socijalno osiguranje u
skladu sa zakonima kojim se uređuje obavezno zdravstveno, penziono i socijalno
osiguranje;
2.4 depoziti dobrovoljnih penzionih fondova i društava za upravljanje penzionim
fondovima u skladu sa zakonom kojim se uređuje poslovanje dobrovoljnih penzionih
fondova;
2.5 depoziti investicionih društava u skladu sa zakonom kojim se uređuje tržište
kapitala;
2.6 depoziti investicionih fondova i društava za upravljanje investicionim fondovima
u skladu sa zakonom kojim se uređuje tržište kapitala;
2.7 depoziti kreditnih institucija, bez obzira na njihovo sjedište, koji glase na njihovo
ime i koji se vode za njihov račun;
2.8 depoziti finansijskih institucija u skladu sa zakonom kojim se uređuje poslovanje
kreditnih institucija;
2.9 depoziti pravnih lica koja direktno ili indirektno učestvuju sa 10% ili više u
kapitalu ili glasačkim pravima u toj kreditnoj instituciji;
2.11 depoziti matičnih, povezanih i zavisnih društava sa kojima kreditna institucija, u
kojoj je nastupio zaštićeni slučaj, čini grupu;
2.12 depoziti pravnih lica koja su vršila reviziju finansijskih izvještaja kreditne
institucije u periodu 36 mjeseci prije dana nastupanja zaštićenog slučaja;
2.13 depoziti subjekata za zajednička ulaganja u skladu sa zakonom kojim se
uređuje tržište kapitala;
2.14 depoziti koji proizlaze iz transakcija za koju je pravosnažnom sudskom
odlukom utvrđeno da je povezana sa pranjem novca ili finansiranjem terorizma;
2.15 depoziti pravnih lica za koja je, izvještajem o kontroli CBCG, utvrđeno da su
doprinijeli pogoršanju finansijskog stanja kreditne institucije;
2.16 depoziti pravnih lica koji ne glase na ime, odnosno depoziti čiji vlasnik nije
identifikovan do dana nastupanja zaštićenog slučaja (neimenovani depoziti);
2.17 obaveze iz dužničkih hartija od vrijednosti i drugih finansijskih instrumenata
koje je izdala ili čiju isplatu garantuje kreditna institucija u kojoj je nastupio zaštićeni
slučaj;
2.18 potraživanja klijenata investicionog društva, klijenata kreditne institucije za koje
kreditna institucija pruža investicione usluge i klijenata društva za upravljanje
investicionim fondovima, kada društvo pruža investicione usluge, koje su uključene
u sistem zaštite investitora u skladu sa zakonom kojim se uređuje tržište kapitala;
2.19 instrumenti deponenata kreditne institucije u kojoj je nastupio zaštićeni slučaj,
koji su uključeni u regulatorni kapital kreditne institucije u skladu sa zakonom kojim
se uređuje poslovanje kreditnih institucija
U papirnoj formi, kreditna institucija je dužna da dostavi popis:
-
lica koja direktno ili indirektno učestvuju sa 10% ili više u kapitalu ili glasačkim
pravima u toj kreditnoj instituciji;
-
fizičkih lica koja su članovi organa upravljanja i/ili stalnih tijela organa upravljanja
kreditne institucije, koji su te funkcije obavljali na dan nastupanja zaštićenog slučaja
ili u periodu posljednjih 12 mjeseci prije nastupanja zaštićenog slučaja.
-
sva ostala dokumenta neophodna za izradu pojedinačnih rješenja za deponente iz
člana 6 st. 2 Zakona.
II. BAZA PODATAKA O DEPOZITIMA
Bazu podataka o depozitima treba formirati na osnovu podataka na dan nastupanja zaštićenog slučaja.
Sadržaj baze o depozitima čine elementi prikazani u Tabeli 22 Kolon
a
Naziv kolone
Sadržaj
Obaveznos
t unosa
Oznaka
A
RAČUN
Broj računa depozita Obavezan
XXXXXXXXXX
B
KONTO
Račun iz kontnog
plana za kreditne
institucije
Obavezan
XXXXXXXXXX
C
TIP DEPOZITA
Tip depozita
Obavezan
3.0 4.0
5.1 5.2 5.3
5.4
D
ŠIFRA
DEPONENTA
Interna šifra
deponenta imaoca
računa
Obavezan
XXXXXXXXXX
E
VALUTA
Šifra valute
Obavezan
XXX F
GLAVNICA
VALUTA*
Glavnica u valuti
Obavezan
XXXXXXXXXX
G
KAMATA
VALUTA*
Obračun kamata u
valuti
Obavezan
XXXXXXXXXX
H
GLAVNICA
EUR**
Glavnica u eurima
Obavezan
XXXXXXXXXX
I
KAMATE EUR**
Kamata u eurima
Obavezan
XXXXXXXXXX
J
DATUM
OBRAČUNA
Datum zadnjeg
obračuna kamata
Obavezan
DD.MM.GGGG
Napomene: X - oznaka u tabeli za cifru * Standardni numerički format je 99999999999.99 ** Na dan nastupanja zaštićenog slučaja po kursu CBCG
RAČUN - Obavezan unos. Mora biti jedinstven.
KONTO - Obavezan unos. Koristiti kontni plan za kreditne institucije utvrdjen od CBCG.
TIP DEPOZITA - Obavezan unos. Zavisno od tipa depozita, svakom depozitu treba dodijeliti pripadajuću numeričku oznaku prema klasifikaciji FZD-a datoj u ovom uputstvu.
3.0 ........................... zaštićeni depoziti;
4.0 ........................... isključeni depoziti;
5.1 5.2 5.3 5.4 ..... zaštićeni depozit sa privremenom blokadom.
ŠIFRA DEPONENTA - Obavezan unos. Interna šifra deponenta mora biti jedinstvena. Ograničenje za unos u polju šifre je do 30 simbola. Nijesu dozvoljeni razmaci unutar šifre, navodnici, tačke i ostali specijalni znaci, tj. šifra se može sastojati od CIFARA I VELIKIH SLOVA.
VALUTA - Obavezan unos. Brojčana oznaka valute, popunjava se i kada je valuta euro (978).
GLAVNICA VALUTA* - Obavezan unos.Standardni numerički format*.
KAMATA VALUTA* - Obavezan unos. Standardni numerički format*.
2 Napomena: Za bazu podataka o depozitima neophodno je dostaviti svih 10 kolona, bez obzira na nepostojanje podataka, dakle i svaka prazna kolona treba fizčiki da postoji.
GLAVNICA EUR** - Obavezan unos. Standardni numerički format*.
KAMATE EUR** - Obavezan unos. Standardni numerički format*.
DATUM OBRAČUNA - Obavezan unos. Format DD.MM.GGGG
KOLONA B - KONTO - Broj računa iz kontnog plana za kreditne institucije: unosi se broj računa depozita iz kontnog plana za kreditne institucije, iz izvještaja o stanju ukupnih depozita (Mjesečni izvještaj UD) i izvještaja o stanju garantovanih depozita (Mjesečni izvještaj GD).
Uključuju se računi depozita fizičkih lica i pravnih lica klase 1, kategorije 12 - dalje analitike, iz kontnog plana za kreditne institucije, na kojima su knjižene i dospjele obaveze na osnovu kamatnih i nekamatnih troškova, prema fizičkim i pravnim licima.
KOLONA C - TIP DEPOZITA - svakom depozitu treba dodijeliti numeričku oznaku koja mu pripada prema sljedećoj specifikaciji:
3.0 dodjeljuje se svim depozitima kod kojih ne postoji ograničenje isplate, odnosno
zaštićenim depozitima.
4.0 dodjeljuje se svim depozitima kod kojih postoji ograničenje obračuna i isplate,
odnosno isključenim depozitima.
PRIVREMENA BLOKADA
Privremena blokada dodjeljuje se svim depozitima kod kojih postoji privremeno ograničenje obračuna i isplate (na kojima je potrebna dalja obrada):
5.1 Depoziti na zajedničkom računu više vlasnika
Kreditna institucija je dužna da dostavi FZD-u specifikaciju svih ugovora o otvaranju zajedničkog računa i pojedinačno za svaki zajednički račun podatke za sve vlasnike zajedničkog računa (ime i prezime / naziv; JMB / broj pasoša; MB; adresa) i iznos sredstava koja pripadaju pojedinačno svakom vlasniku zajedničkog računa.
5.2 Depoziti kod kojih je deponent nastupao kao zastupnik trećeg lica.
Kreditna institucija je dužna da dostavi FZD-u specifikaciju svih ugovora o otvaranju računa gdje je deponet nastupao kao zastupnik trećeg lica. Kreditna institucija u kojoj je nastupio zaštićeni slučaj dostavlja sve podatke za lice koje je deponent zastupao (ime i prezime / naziv; JMB / broj pasoša; MB; adresa) koje je zastupao deponent kao iznosu sredstava koja pripadaju zastupanom licu.
5.3 Depoziti na kojima je po bilo kom osnovu zasnovano založno pravo.
Kreditna institucija je dužna da dostavi FZD-u specifikaciju svih depozita na kojima je po bilo kom osnovu zasnovano založno pravo. Kreditna institucija u kojoj je nastupio zaštićeni slučaj dostavlja FZD-u dokument kojim se vrši skidanje zaloge na depozitu u svakom pojedinačnom slučaju.
5.4 Depoziti kod kojih postoji ograničenje raspolaganja.
Kreditna institucija je dužna da dostavi FZD-u specifikaciju svih depozita ili dijela depozita ako je nadležni organ na depozitu ili dijelu depozita uveo mjeru ograničenja raspolaganja. Kreditna institucija dostavlja FZD-u dokument kojim se mjera ograničenja raspolaganja ukida u svakom pojedinačnom slučaju.
KOLONA G - KAMATA VALUTA - obračunava se dospjela kamata na dan nastanka zaštićenog slučaja na depozite po viđenju, oročene depozite.
III. BAZA PODATAKA O DOSPJELIM OBAVEZAMA Bazu podataka o dospjelim obavezama deponenata treba formirati na osnovu podataka na dan nastupanja zaštićenog slučaja u kreditnoj instituciji. Kreditna institucija dostavlja PODATKE O DOSPJELIM OBAVEZAMA DEPONENATA - isključivo dospjele obaveze deponenata koji imaju pravo na isplatu garantovanog depozita (dakle unose se dospjele obaveze fizičkih i pravnih lica koja istovremeno imaju i potraživanja od kreditne institucije po osnovu depozita. Ne unose se dospjele obaveze fizičkih i pravnih lica koja nemaju potraživanja od kreditne institucije po osnovu depozita).
Baza podataka o dospjelim obavezama se sastoji od deponenata kreditne institucije koji imaju pravo na isplatu garantovanog depozita i istovremeno imaju dospjelu obavezu (npr. kod fizičkih lica koja imaju pravo na isplatu garantovanog depozita, u ukupan iznos dospjelih obaveza uključuju se obaveze po kreditima, minusna stanja po tekućim računima, obaveze za provizije i naknade, obaveze za dospijeća po kreditnim karticama i sl.).
Sadržaj baze o dospjelim obavezama sastoji se od elemenata prikazanih Tabelom 33
Kolon
a
Naziv kolone
Sadržaj
Obaveznost
unosa
Oznaka
A
RAČUN
Broj računa dospjele
obaveze
Obavezan
XXXXXXXX
XX
B
KONTO
Račun iz kontnog
plana za kreditne insti.
- CBCG
Obavezan
XXXXXXXX
XX
C
ŠIFRA
DEPONENTA
Interna šifra deponenta
imaoca računa
Obavezan
XXXXXXXX
XX
D
VALUTA
Šifra valute
Obavezan
XXX
E
GLAVNICA
VALUTA*
Dospjela obaveza u
valuti
Obavezan
XXXXXXXX
XX
F
GLAVNICA EUR* Dospjela obaveza u
eurima
Obavezan
XXXXXXXX
XX Napomene: X - oznaka u tabeli za cifru * Standardni numerički format je 99999999999.99
RAČUN - Obavezan unos. Mora bit jedinstven.
KONTO - Obavezan unos. Koristi se kontni plan za kreditne institucije utvrdjen od CBCG.
ŠIFRA DEPONENTA - Obavezan unos. Interna šifra deponenta mora biti jedinstvena. Ograničenje za unos u polju šifre je do 30 simbola. Nijesu dozvoljeni razmaci unutar šifre, navodnici, tačke i ostali specijalni znaci, tj. šifra se može sastojati od CIFARA I VELIKIH SLOVA.
VALUTA - Obavezan unos. Brojčana oznaka valute.
GLAVNICA VALUTA - Obavezan unos. Standardni numerički format*.
3 Napomena: Za bazu podataka o dospjelim obavezama neophodno je dostaviti svih 6 kolona, bez obzira na nepostojanje podataka, dakle treba fizički da postoji i svaka prazna kolona. Iznose unositi bez negativnog predznaka. GLAVNICA EUR - Obavezan unos. Standardni numerički format*.
IV. BAZA PODATAKA O IDENTIFIKACIONIM DOKUMENTIMA
Baza podataka o identifikacionim dokumentima odnosi se na bazu za tip deponenta - fizička lica (nepotrebno u ovoj bazi dostavljati podatke o identifikacionim dokumentima lica ovlašćenog za zastupanje pravnog lica).
Sadrzaj baze o identifikacionim dokumentima sastoji se od elemenata prikazanih Tabelom 4.4
Kolon
a
NAZIV
KOLONE
Sadržaj
Obaveznost
unosa
Oznaka
A
ŠIFRA
DEPONENT
A
Interna šifra
deponenta
Obavezan za
fizička lica
XXXXAAAAX
X
B
VRSTA
DOKUMENT
A
Lična karta, pasoš
Obavezan
XXXXaAAAAa
XX
C
IME
DATOTEKE
Ime dokumenta
Obavezan
XXXXAAAAa
XX
ŠIFRA DEPONENTA - Obavezan unos. Interna šifra deponenta mora biti jedinstvena. Ograničenje za unos u polju šifre je do 30 simbola. Nijesu dozvoljeni razmaci unutar šifre, navodnici, tačke i ostali specijalni znaci, tj. šifra se može sastojati od CIFARA I VELIKIH SLOVA.
VRSTA DOKUMENTA - Obavezan unos. Moguća kombinacija CIFARA, MALIH I VELIKIH SLOVA.
IME DATOTEKE - Obavezan unos naziva dokumenta sa ekstenzijom. Ime dokumenta mora biti jedinstveno. Moguća kombinacija CIFARA, MALIH I VELIKIH SLOVA.
V. DATOTEKA SA IDENTIFIKACIONIM DOKUMENTIMA
Datoteka sa skeniranim identifikacionim dokumentima se formira na način da naziv dokumenta mora biti identičan sa poljem "Ime dokumenta" iz baze IV - kolona C. Datoteka se dostavlja u ZIP formatu (ne zipuju se pojedinačno identifikacioni dokumenti već svi idu u jednu ZIP datoteku). Moguća kombinacija CIFARA, MALIH I VELIKIH SLOVA.
Radi kontrole podataka napominjemo:
Skup podataka br. 1 - Tabela 1 - Analitika po SVIM deponentima FL i PL na dan nastupanja zaštićenog slučaja. Broj deponenata odgovara poziciji red I kolona B iz Mjesečnog izvještaja UD. Ukupan iznos depozita u kreditnoj instituciji jednak je poziciji
4 Napomena: Za bazu podataka o identifikacionim dokumentima neophodno je dostaviti sve 3 kolone.
reda I kolona A, Mjesečnog izvještaja UD, a ukupan iznos garantovanih depozita je jednak poziciji reda 5 kolona M Mjesečnog izvještaja GD, na dan nastupanja zaštićenog slučaja.
Skup podataka br. 2 - Tabela 2 - Popis računa depozita i računa dospjelih kamata po depozitima FL i PL, na računima klase 2, kategorije 21, 22 i 23 (stanje obaveza po kamatama na dan nastupanja zaštićenog slučaja). Ukupan iznos depozita u kreditnoj instituciji jednak je poziciji reda I kolona A, Mjesečnog izvještaja UD, a ukupan iznos garantovanih depozita je jednak poziciji reda 5 kolona M Mjesečnog izvještaja GD, na dan nastupanja zaštićenog slučaja.
Skup podataka br. 3 -Tabela 3 - Popis dospjelih obaveza (FL i PL) - na dan nastupanja zaštićenog slučaja. Visina dospjelih obaveza odgovara zbiru pozicija reda I kolone E i kolone H iz Mjesečnog izvještaja GD.
