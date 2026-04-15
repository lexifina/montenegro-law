PRILOG 1
SPECIFIKACIJA FORMATA I TEHNIČKI OPIS ZA USLUGU ENP I EENP
Oprema za ENP treba da bude kompatibilan sa sljedećim standardima i specifikacijama: 1) CEN DSRC;
2) GSS;
3) ISO/CEN EFC;
4) A1, CESARE/PISTA, CARDME, AutoPASS;
5) IP67;
6) EN 15509 SL0/SL1;
7) RS232 ili RS422/RS485 interfejs;
8) DSRC komunikacija: EN 12253:2004, EN 12795:2003, EN 12834:2003, EN 13372:2004, EN 16312, EN 15509, EN ISO 14906:2004, ISO/TS 12813: 2009.
Osnovne karakteristike:
1) upis i čitanje transakcija;
2) mogućnost istovremene obrade više transakcija;
3) ograničen pristup od strane operatera;
4) kontrola i upravljanje podacima na uređaju za ENP;
5) skladištenje transakcija;
6) zvučni signal nakon obavljene transakcije.
Zaštita podataka: DES/3-DES algoritam za enkripciju ključeva.
Garancija ispravnosti: vijek trajanja minimum sedam godina.
Arhitektura:
1) karakteristike DSRC komunikacije:
 Pasivni RFID transponder,  Učestalost 5.8 GHz;
2) ASIC komponente:
 analogni strujni modul,  digitalni strujni modul,  RISC 32-bitni procesor,  minimalno 4 kB programske memorije.
Temperaturni uslovi rada:
1) temperatura skladištenja +5 °C do +40 °C;
2) radna temperatura -25 °C do +85 °C.
Napajanje:
1) 3V litijumska baterija;
2) vijek trajanja baterije minimalno sedam godina.
Interna struktura uređaja za ENP DSRC komunikacija je zasnovana na standardu EN 15509. Struktura memorije uređaja za ENP sadrži dva elementa: sistemski i aplikacioni. Sistemski element sadrži podatke koji su u vezi sa samim uređajem i ne odnose se ni na jednu posebnu aplikaciju. Aplikacioni element sadrži podatke u skladu sa EN 15509 standardom nivoa bezbednosti.
Lista atributa aplikacionog elementa:
ID atribut
a
Naziv atributa
Element
Dužin
a
Pristu
p*
0
Oznaka EFC namjene
Provajder ugovora
24B
R/О
Tip ugovora definisan od strane
provajdera
16B
Verzija ECF namjene
8B 15
Broj šasije (VIN)
Identifikacioni broj vozila
17B
R/W 15a
Država registracije
Oznaka države registracije vozila
3B
R/W 15b
Marka i tip vozila
Marka i komercijalni tip vozila
30B
R/W 15c
Emisijska klasa vozila
Euro standard (npr. Euro 4, Euro 6)
10B
R/W 15d
Tehnički najveća dozvoljena
ukupna masa
Tehnički najveća dozvoljena ukupna
masa vozila (kg)
6B
R/W
15e
CO2 emisiona klasa
Specifična CO2 emisija prikazana
klasom
5B
R/W
15f
CO2 emisija u g/tkm
CO2 vrijednost za teška vozila
izražena u g/tkm
6B
R/W
15g
Datum reklasifikacije
Datum promjene kategorije/klase
vozila (format YYYY-MM-DD)
10B
R/W
16
Registarska oznaka vozila
Prijavljena registarska oznaka vozila 17B
R/О 17
Kategorija vozila
Specifična informacija provajdera
usluge vezana za vozilo
1B
R/О
18
Dimenzije vozila
Ukupna dužina vozila
1B
R/О
Ukupna visina vozila
1B
Ukupna širina vozila
1B 19
Osovine vozila
Visina vozila u nivou prve osovine
1B
R/О
Broj osovina vozila
1B 20
Ograničenja mase vozila
6B
R/О 22
Specifične karakteristike vozila
4B
R/О 23
Ime i prezime
Ime i prezime vlasnika ili korisnika
70B
R/W 23a
Adresa
Adresa vlasnika ili korisnika
120B R/W 23b
Datum rođenja
Datum rođenja vlasnika ili korisnika
20B
R/W 23c
JMB
JMB vlasnika ili korisnika
13B
R/W 23d
Naziv
Naziv pravnog lica
70B
R/W 23e
Oblik organizacije
Vrsta organizacije pravnog lica
30B
R/W 23f
Sjedište
Sjedište pravnog lica
120B R/W 23g
PIB
PIB pravnog lica
20B
R/W 24
Identifikaciona oznaka uređaja
Identifikacioni broj uređaja definisan
od strane proizvođača
1 +
4B
R/О 26
Status opreme
Brojač transakcija
2B
R/W 29
Stanje pripejd kredita
Stanje na pripejd računu izraženo u
valuti plaćanja
3B
R/О
30
Valuta plaćanja
Jedinica plaćanja izražena kao
umnožak ili dio zvanične valute
2B
R/О
32
Način plaćanja
Broj ličnog računa (PAN)
10B
R/О
Rok važenja računa na uređaju
2B
Kontrola upotrebe uređaja
2B 33
Podaci o posljednjoj transakciji
Vrijeme transakcije (rezolucija 2s)
4B
R/W
Provajder pri transakciji
3B
Kod lokacije pri transakciji
2B
Kod naplatne trake pri transakciji
1B
Tip transakcije (ulaz/naplata)
1B
Rezultata transakcije
1B
Naplaćena kategorija vozila
1B
Kategorija vozila definsana na
uređaju
1B
Naplaćeni iznos
4B
Provajder ugovora pri transakciji
3B
Tip ugovora pri transakciji
2B
Verzija namjene pri transakciji
1B
Zaštitni kod transakcije
4B
34
Podaci o pretposljednjoj
transakciji
Vrijeme transakcije (rezolucija 2s)
4B
R/W
Provajder pri transakciji
3B
Kod lokacije pri transakciji
2B
Kod naplatne trake pri transakciji
1B
Tip transakcije (ulaz/naplata)
1B
Rezultat transakcije
1B
Naplaćena kategorija vozila
1B
Definisana kategorija vozila
1B
Naplaćen iznos
4B
Provajder ugovor pri transakciji
3B
Tip ugovora pri transakciji
2B
Verzija namjene pri transakciji
1B
Zaštitni kod transakcije
4B 97
Tip ugovora
1 +
2B
R/W
99
Korisnički atribut
1 +
16B
R/W
107
Iznos upozorenja
1 +
3B
R/W
111
Ključ 1 provjere autentičnosti
aplikacionog elementa
1 +
8B
N/A
112
Ključ 2 provjere autentičnosti
aplikacionog elementa
1 +
8B
N/A
113
Ključ 3 provjere autentičnosti
aplikacionog elementa
1 +
8B
N/A
114
Ključ 4 provjere autentičnosti
aplikacionog elementa
1 +
8B
N/A
115
Ključ 5 provjere autentičnosti
aplikacionog elementa
1 +
8B
N/A
116
Ključ 6 provjere autentičnosti
aplikacionog elementa
1 +
8B
N/A
117
Ključ 7 provjere autentičnosti
aplikacionog elementa
1 +
8B
N/A 118
Ključ 8 provjere autentičnosti
aplikacionog elementa
1 +
8B
N/A
120
Ključ za pristup aplikacionom
elementu
1 +
8B
N/A
122
Ključ za umanjenje/uvećanje
pripejd kredita
1 +
8B
N/A
124
Ključ za izmjenu načina
plaćanja (USET)
1 +
16B
N/A * Pristup (R/O=samo čitaj; R/W=čitaj/piši).
PRILOG 2
FORMATI PORUKA ZA RAZMJENU PODATAKA IZMEĐU PRUŽAOCA USLUGE ENP-A I EENP-A I SUBJEKTA ZA NAPLATU PUTARINE
Formati poruke za razmjenu podataka treba da budu u skladu sa EN 15509 standardom. U razmjenu podataka ulazi svaka transakcija (prolazak vozila kroz naplatnu saobraćajnu traku predviđenu za ENP ili EENP) gdje je zabilježen ulazak vozila na dionicu autoputa ili brze saobraćajnice ili naplata putarine pri izlasku sa dionice autoputa ili brze saobraćajnice.
Definisana poruka je preuzeta iz već postojećeg ENP sistema koji je usklađen sa evropskim zahtjevima ENP interoperabilnosti.
Sadržaj polja
Dužina polja
Napomena
Kod autoputa ili brze saobraćajnice
1B
Kod stanice
1B
Kod saobraćajne trake
1B
UTC vrijeme kao ključ
4B
Format: UNIH vrijeme
Jedinstveni broj tekuće transkacije na
konkretnom ENP uređaju
4B
Rezultat transakcije
1B
Korisnički definisana vrijednost
Status transakcije
1B
Korisnički definisana vrijednost
Vrijeme transakcije u sekundama
4B
Format: UNIH vrijeme
Vrijeme transakcije u milisekundama
4B
Kod države provajdera ugovora
2B
Kod pružaoca usluge
2B
Tip ugovora definisan od strane
provajdera
2B
Verzija EFC namjene
1B
ID proizvođača uređaja za ENP
2B
Zemlja izdavanja registarske oznake
2B
Tip alfabeta registarske oznake
1B
Registarska oznaka
11B
Kategorija vozila
1B
ID taga
4B
Broj šasije (VIN)
17B
Marka i tip vozila
30B
Emisiona klasa vozila
10B
Tehnički najveća dozvoljena ukupna
masa
6B
CO2 emisiona klasa
5B
CO2 emisija u g/tkm
6B
Datum reklasifikacije
10B
Ime i prezime vlasnika ili korisnika
70B
Adresa vlasnika ili korisnika
120B
Datum rođenja vlasnika ili korisnika
10B
JMB vlasnika ili korisnika
13B
Naziv pravnog lica i vrsta organizacije
pravnog lica
100B
Sjedište pravnog lica
120B
PIB pravnog lica
20B
Status opreme (brojač transakcija na
uređaju za ENP)
2B
Tip ugovora
2B
Korisnički definisana vrijednost
Stanje pripejd kredita
4B
Valuta plaćanja
2B
Način plaćanja
14B
Rok važenja računa na uređaju za ENP
9B
Format: GGGGMMDD + NULL
karakter
Podaci o posljednjoj transakciji
Vrijeme transakcije (rezolucija 2s)
15B
Format: GGGGMMDDSSMMSS
+ NULL karakter
Kod države pri transakciji
2B
Kod pružaoca usluge pri transakciji
2B
Kod autoputa ili brze saobraćajnice
1B
Korisnički definisana vrijednost
Smjer kretanja
1B
Korisnički definisana vrijednost
Kod naplatne stanice
1B
Korisnički definisana vrijednost
Kod naplatne saobraćajne trake
1B
Tip transakcije (ulaz/naplata)
1B
Rezultat transakcije
1B
Korisnički definisana vrijednost
Naplaćena kategorija vozila
1B
Kategorija vozila definisana na uređaju
za ENP
1B
Naplaćen iznos
2B
Valuta plaćanja
2B
Kod države provajdera ugovora
2B
Kod pružaoca usluge
2B
Tip ugovora definisan od strane
provajdera
2B
Verzija EFC namjene
1B
Zaštitni kod transakcije
4B
Podaci o pretposljednjoj transakciji
Vrijeme transakcije (rezolucija 2s)
15B
Format: GGGGMMDDSSMMSS
+ NULL karakter
Kod države pri transakciji
2B
Kod pružaoca usluge pri transakciji
2B
Kod autoputa ili brze saobraćajnice
1B
Korisnički definisana vrijednost
Smjer kretanja
1B
Korisnički definisana vrijednost
Kod naplatne stanice
1B
Korisnički definisana vrijednost
Kod naplatne saobraćajne trake
1B
Tip transakcije (ulaz/naplata)
1B
Rezultat transakcije
1B
Korisnički definisana vrijednost
Naplaćena kategorija vozila
1B
Kategorija vozila definisana na uređaju
za ENP
1B
Naplaćen iznos
2B
Valuta plaćanja
2B
Kod države provajdera ugovora
2B
Kod pružaoca usluge
2B
Tip ugovora definisan od strane
provajdera
2B
Verzija EFC namjene
1B
Zaštitni kod transakcije
4B
Iznos koji treba naplatiti
2B
PRILOG 3
TEHNIČKI OPIS I SPECIFIKACIJA ENP OPREME
ENP antena komunicira sa uređajem za ENP preko bidirekcionog RF signala učestalosti 5,8 GHz u skladu sa sljedećim DSRC standardima:
1) CEN DSRC 2) RTTT-DSRC i EFC standardi:
 EN 12253:2004
 EN 12795:2003
 EN 12834:2003
 EN 13372:2004
 EN ISO 14906:2004
 GSS ENP antena treba da ima sljedeće tehničke karakteristike:
1) opseg učestalosti: 5,795 GHz - 5,815 GHz 2) radne učestalosti:
 Kanal 1: 5.7975 GHz ± 2.5 MHz
 Kanal 2: 5.8025 GHz ± 2.5 MHz
 Kanal 3: 5.8075 GHz ± 2.5 MHz
 Kanal 4: 5.8125 GHz ± 2.5 MHz 3) polarizacija antene: lijevo kružna 4) snaga zračenja: ≤ 33 dBm EIRP 5) brzina prenosa u downlinku: 500 kbit/s 6) brzina prenosa u uplinku: 250 kbit/s 7) radna temperatura: -33 °C do +55 °C 8) temperatura skladištenja: -40 °C do +70 °C 9) nivo zaštite: IP67 (IEC 60529) 10) prosječno vrijeme između otkaza: 130.000 sati
PRILOG 4
ZAHTJEVI ZA KOMPONENTE INTEROPERABILNOSTI I PUTNU INFRASTRUKTURU
1. OPŠTI ZAHTJEVI
1.1. Pouzdanost i dostupnost 1.1.1. Nadzor i održavanje fiksnih ili pokretnih komponenti koje se koriste u EENP-u moraju biti organizovani, sprovođeni i mjerljivo praćeni na način koji obezbjeđuje njihov rad u predviđenim uslovima.
1.1.2. Dizajn EENP sistema mora da omogući funkcionisanje sistema i u slučaju kvara ili otkazivanja komponenti, najmanje u ograničenom režimu rada, i uz najmanje ometanja za korisnike EENP-a.
1.2. Tehnička kompatibilnost U slučaju povezivanja opreme pružalaca usluge EENP-a i opreme subjekta za naplatu putarine tehničke karakteristike te opreme moraju biti međusobno kompatibilne i usklađene sa zahtjevima iz Priloga 6.
1.3. Bezbjednost/privatnost i zaštita podataka o ličnosti 1.3.1. EENP mora da obezbijedi funkcije bezbjednosti koje se odnose na zaštitu podataka koji se čuvaju, obrađuju i prenose između učesnika u području EENP-a. Funkcije bezbijednosti moraju da uključuju potrebne mjere zaštite u obradi podataka kako bi se zaštitila prava i interesi učesnika u EENP-u, a naročito zaštita od rizika ili štete izazvane nedostatkom dostupnosti, povjerljivosti, integriteta, autentičnosti, neopozivosti i zaštite od neovlašćenog pristupa podacima korisnika u evropskom više-korisničkom okruženju, u skladu sa propisima kojima se uređuje obrada podataka o ličnosti.
1.3.2. EENP mora biti usaglašen sa propisima u oblasti zaštite podataka o ličnosti, uključujući i zaštitu tih podataka u elektronskim komunikacijama i međunarodnim standardima u ovoj oblasti.
2. POSEBNI ZAHTJEVI
2.1. Zahtjevi za putnu infrastrukturu 2.1.1. EENP infrastruktura mora da obezbijedi da tačnost podataka o prijavi putarine odgovara zahtjevima režima naplate putarine, kako bi se obezbijedilo jednako i pravično postupanje prema korisnicima EENP-a u pogledu putarina i naknada.
2.1.2. Oprema u vozilu mora da omogući subjektu za naplatu putarine identifikaciju odgovornog pružaoca usluge EENP-a i da redovno prati te informacije, kao i da se automatski deaktivira u slučaju otkrivenih nepravilnosti i ako je moguće da obavijesti pružaoca usluge EENP-a o tim nepravilnostima.
2.1.3. Ako je primjenjivo, oprema EENP-a mora biti projektovana tako da njene komponente interoperabilnosti koriste standarde koje donose evropske organizacije za standardizaciju.
2.1.4. Oprema u vozilu mora biti integrisana na bezbjedan i siguran način i u skladu sa zahtjevima za bezbjedno polje vidljivosti vozača motornog vozila.
2.1.5. Subjekat za naplatu putarine mora da informiše vozače, putem signalizacije ili drugih sredstava, o obavezi plaćanja putarine ili korisničke naknade u okviru područja EENP-a i putevima koji su obuhvaćeni tim područjem.
2.2. Zahtjevi za funkcionisanje i upravljanje 2.2.1. Subjekat za naplatu putarine i pružaoci usluga EENP-a moraju da imaju planove za vanredne situacije radi sprečavanja značajnih poremećaja saobraćajnog toka u slučaju nedostupnosti sistema EENP-a.
2.2.2. Za ocjenjivanje performansi opreme u vozilu koja koristi satelitsku tehnologiju za pozicioniranje, mogu se primjenjivati specifikacije ispitivanja usklađenosti EGNOS/Galileo eCall.
PRILOG 5
USAGLAŠENOST KOMPONENTI INTEROPERABILNOSTI SA SPECIFIKACIJAMA I PRILAGOĐENOST ZA KORIŠĆENJE
Usaglašenost sa specifikacijama
Ocjenjivanje usaglašenosti komponenti interoperabilnosti sa zahtjevima ovog pravilnika i relevantnim tehničkim specifikacijama, prije njihovog stavljanja na tržište, sprovodi proizvođač komponenti interoperabilnosti, koje se koriste u pružanju EENP usluga, ili njegov ovlašćeni predstavnik, u skladu sa zakonom kojim se uređuju tehnički zahtjevi za proizvode i ocjenjivanju usaglašenosti, kao i propisima donijetim na osnovu tog zakona, i to kroz jedan od sljedećih postupaka:
a) internom kontrolom proizvodnje, kojom proizvođač potvrđuje da su komponente proizvedene u skladu sa zahtjevima i tehničkim specifikacijama (modul A);
b) ispitivanjem tipa (modul B), nakon kojeg se izdaje potvrda usaglašenosti sa odobrenim tipom, na osnovu interne kontrole proizvodnje (modul C).
I. Modul A - Interna kontrola proizvodnje
Interna kontrola proizvodnje je postupak ocjenjivanja usaglašenosti kojim proizvođač ispunjava obaveze utvrđene u tač.a), b) i c) ovog modula i na svoju isključivu odgovornost obezbjeđuje i izjavljuje da predmetne komponente interoperabilnosti ispunjavaju sve relevantne tehničke specifikacije i standarde, kao i da je njihova usaglašenost sa specifikacijama i prilagođenost za korišćenje dokazana prije stavljanja na tržište, u skladu sa propisanim postupcima ocjenjivanja usaglašenosti.
a) Tehnička dokumentacija Proizvođač je dužan da pripremi tehničku dokumentaciju. Dokumentacija mora da omogući ocjenjivanje usaglašenosti komponenti interoperabilnosti sa relevantnim zahtjevima i da sadrži odgovarajuću analizu i ocjenu rizika. Tehnička dokumentacija mora da precizira primjenjive zahtjeve i da obuhvati, u onoj mjeri u kojoj je to relevantno za ocjenjivanje, projektovanje, proizvodnju i funkcionisanje komponenti interoperabilnosti. Tehnička dokumentacija mora, gdje god je to primjenjivo, da sadrži najmanje sljedeće elemente:
1) opšti opis komponente interoperabilnosti;
2) idejno rješenje, proizvodne crteže i šeme komponenti, podsklopova, kola i slično;
3) opise i objašnjenja neophodna za razumijevanje tih crteža i šema, kao i
funkcionisanja komponente interoperabilnosti;
4) upućivanje na kategoriju interfejsa utvrđenu u Prilogu 6;
5) listu standarda i/ili drugih relevantnih tehničkih specifikacija, primijenjenih u cjelini ili
djelimično, i opise rješenja koja su usvojena radi ispunjavanja zahtjeva iz ovog
modula;
6) rezultate projektnih proračuna, sprovedenih ispitivanja i slično;
7) izvještaje o ispitivanjima.
b) Proizvodnja Proizvođač je dužan da preduzme sve neophodne mjere kako bi proizvodni proces i njegovo nadgledanje obezbijedili usaglašenost proizvedenih komponenti interoperabilnosti sa tehničkom dokumentacijom iz tačke a) ovog modula, kao i sa zahtjevima propisa koji se na njih primjenjuju.
c) Deklaracija o usaglašenosti sa specifikacijama Proizvođač je dužan da sačini pisanu Deklaraciju o usaglašenosti sa specifikacijama za model komponente interoperabilnosti koju je dužan da, zajedno sa tehničkom dokumentacijom, čuva i stavlja na raspolaganje nadležnim organima u periodu od deset godina nakon što je komponenta interoperabilnosti stavljena na tržište. Deklaracija o usaglašenosti sa specifikacijama mora da identifikuje komponentu interoperabilnosti na koju se odnosi.
Kopija Deklaracije o usaglašenosti sa specifikacijama mora biti stavljena na raspolaganje nadležnim organima na njihov zahtjev.
d) Ovlašćeni predstavnik Obaveze proizvođača iz tačke b) ovog modula može, u njegovo ime i pod njegovom odgovornošću, ispuniti njegov ovlašćeni predstavnik, u skladu sa ovlašćenjem.
II. Modul B - Ispitivanje tipa
1) Ispitivanje tipa je dio postupka ocjenjivanja usaglašenosti u kojem ovlašćeno tijelo ispituje tehničko rješenje komponente interoperabilnosti i potvrđuje da to tehničko rješenje ispunjava propisane zahtjeve.
2) Ispitivanje tipa može da se sprovodi na jedan od sljedećih načina:
- ispitivanjem uzorka, reprezentativnog za planiranu proizvodnju, kompletne komponente interoperabilnosti (tip proizvodnje), - ocjenom adekvatnosti tehničkog rješenja komponente interoperabilnosti ispitivanjem tehničke dokumentacije i pratećih dokaza iz tačke 3 ovog modula, uz ispitivanje uzoraka, reprezentativnih za planiranu proizvodnju, jedne ili više kritičnih komponenti komponente interoperabilnosti (kombinacija tipa proizvodnje i tipa rješenja), - ocjenom adekvatnosti tehničkog rješenja komponente interoperabilnosti ispitivanjem tehničke dokumentacije i pratećih dokaza iz tačke 3 ovo modula, bez ispitivanja uzorka (tip rješenja).
3) Proizvođač podnosi zahtjev za ispitivanje tipa jednom prijavljenom tijelu po svom izboru. Zahtjev iz stava 1 ove tačke, obavezno sadrži:
a) naziv i adresu proizvođača, a ako zahtjev podnosi ovlašćeni predstavnik, i naziv i adresu tog predstavnika;b) pisanu izjavu da zahtjev nije podnijet drugom prijavljenom tijelu;
c) tehničku dokumentaciju koja omogućava ocjenjivanje usaglašenosti komponente interoperabilnosti sa primjenjivim propisanim zahtjevima i koja sadrži odgovarajuću analizu i ocjenu rizika. Tehnička dokumentacija mora da precizira primjenjive zahtjeve i da obuhvati, u onoj mjeri u kojoj je to relevantno za ocjenjivanje, projektovanje, proizvodnju i funkcionisanje komponente interoperabilnosti. Tehnička dokumentacija mora, gdje god je to primjenjivo, da sadrži najmanje sljedeće elemente:
 opšti opis komponente interoperabilnosti;
 idejno rješenje, proizvodne crteže i šeme komponenti, podsklopova, kola i slično;
 opise i objašnjenja neophodna za razumijevanje crteža i šema, kao i funkcionisanje
komponente interoperabilnosti;
 listu
usklađenih
standarda
i/ili
drugih
relevantnih
tehničkih
specifikacija,
primijenjenih u cjelini ili djelimično i opise rješenja koji se primjenjuju radi
ispunjavanja osnovnih propisanih zahtjeva kada usklađeni standardi nisu u
potpunosti primijenjeni. U slučaju djelimične primjene usklađenih standarda,
tehnička dokumentacija mora da precizira djelove koji su primijenjeni,
 rezultate projektnih proračuna, sprovedenih ispitivanja i slično,
 izvještaje o ispitivanjima;
d) reprezentativne uzorke za planiranu proizvodnju. Prijavljeno tijelo može da zahtijeva dodatne uzorke ako su potrebni za sprovođenje ispitivanja;
e) prateće dokaze o adekvatnosti tehničkog rješenja, u kojima se navode korišćena dokumentacija, posebno u slučaju kada relevantni usklađeni standardi i/ili tehničke specifikacije nisu u potpunosti primijenjeni. Prateći dokazi obuhvataju, gdje je potrebno, rezultate ispitivanja koje je sprovela odgovarajuća laboratorija proizvođača ili druga ispitna laboratorija u njegovo ime i pod njegovom odgovornošću.
4) Prijavljeno tijelo je dužno da:
U pogledu komponente interoperabilnosti:
4.1. ispita tehničku dokumentaciju i prateće dokaze radi ocjenjivanja adekvatnosti tehničkog rješenja komponente interoperabilnosti;
U pogledu uzorka/uzoraka:
4.2. provjeri da li su uzorci proizvedeni u skladu sa tehničkom dokumentacijom i identifikuje elemente koji su projektovani u skladu sa primjenjivim odredbama relevantnih usklađenih standarda i/ili tehničkih specifikacija, kao i elemente koji su projektovani bez primjene tih odredbi;
4.3. sprovede ili obezbijedi sprovođenje odgovarajućih ispitivanja i testiranja, radi provjere da li je proizvođač rješenja iz relevantnih usklađenih standarda i/ili tehničkih pravilno primijenio;
4.4. sprovede ili obezbijedi sprovođenje odgovarajućih ispitivanja i testiranja radi provjere da li rješenja koja je usvojio proizvođač, u slučaju kada relevantni usklađeni standardi i/ili tehničke specifikacije nisu primijenjeni, ispunjavaju odgovarajuće bitne zahtjeve propisa; 4.5. usaglasi sa proizvođačem mjesto na kojem će se ispitivanja i testiranja sprovoditi. 5) Prijavljeno tijelo je dužno da sačini izvještaj o ocjenjivanju, koji sadrži aktivnosti sprovedene u skladu sa tačkom 4 ovog modula i rezultate tih aktivnosti. Ne dovodeći u pitanje obaveze prema nadležnim tijelima za notifikaciju, prijavljeno tijelo može da objavi sadržaj tog izvještaja, u cjelini ili djelimično, samo uz saglasnost proizvođača.
6) Ako tip komponente ispunjava propisane zahtjeve , prijavljeno tijelo izdaje proizvođaču Sertifikat o ispitivanju tipa. Sertifikat mora da sadrži naziv i adresu proizvođača, zaključke ispitivanja, uslove (ako postoje) za njegovu validnost i potrebne podatke za identifikaciju odobrenog tipa. Sertifikat može da sadrži priloge.
Sertifikat mora da sadrži sve relevantne informacije koje omogućavaju ocjenjivanje usaglašenosti proizvedenih komponenti interoperabilnosti sa ispitivanim tipom, kao i sprovođenje kontrole u toku upotrebe.
Ako tip komponente ne ispunjava primjenjive propisane zahtjeve, prijavljeno tijelo odbiće izdavanje Sertifikata o ispitivanju tipa i o tome obavještava podnosioca zahtjeva, uz navođenje detaljnih razloga za odbijanje.
7) Prijavljeno tijelo je dužno da prati sve promjene u opštepriznatom stanju tehničkog razvoja koje ukazuju da odobreni tip možda više ne ispunjava primjenjive propisane zahtjeve i da utvrdi da li te promjene zahtijevaju dodatna ispitivanja. U tom slučaju prijavljeno tijelo obavještava proizvođača.
Proizvođač je dužan da obavijesti prijavljeno tijelo koje čuva tehničku dokumentaciju koja se odnosi na Sertifikat o ispitivanju tipa o svim izmjenama odobrenog tipa koje mogu da utičuna usaglašenost komponente interoperabilnosti sa bitnim zahtjevima propisa ili na uslove validnosti tog sertifikata. Takve izmjene zahtijevaju dodatno odobrenje i dopunu Sertifikate o ispitivanju tipa.
8) Svako prijavljeno tijelo je dužno da obavijesti svoje nadležno tijelo za notifikaciju o izdatim ili povučenim Sertifikatima o ispitivanju tipa i/ili njihovim dopunama, kao i da periodično ili na zahtjev dostavi nadležnom tijelu listu sertifikata i/ili njegovih dopuna koje su odbijene, suspendovane ili na drugi način ograničene.
Svako prijavljeno tijelo je dužno da obavijesti druga prijavljena tijela o Sertifikatima o ispitivanju tipa i/ili njihovim dopunama koje je odbilo, povuklo, suspendovalo ili na drugi način ograničilo, kao i da, na zahtjev drugih prijavljenih tijela, obezbijedi podatke o sertifikatima i/ili dopunama koje je izdalo.
Na zahtjev nadležnih organa i drugih prijavljenih tijela prijavljeno tijelo dužno je dostaviti kopije Sertifikata o ispitivanju tipa i/ili njihovih dopuna, a nadležnim organima i tehničku dokumentaciju i rezultate ispitivanja koje je sprovelo. Prijavljeno tijelo je dužno da čuva primjerak Sertifikata o ispitivanju tipa, njegovih priloga i dopuna, kao i tehnički dosije sa dokumentacijom koju je dostavio proizvođač, sve do isteka roka važenja sertifikata.
9) Proizvođač je dužan da čuva primjerak Sertifikata o ispitivanju tipa, njegove priloge i dopune, zajedno sa tehničkom dokumentacijom i da ih stavi na raspolaganje nadležnim organima u periodu od deset godina od dana stavljanja komponenta interoperabilnosti na tržište.
10) Ovlašćeni predstavnik proizvođača može da podnese zahtjev iz tačke 3 ovog modula u kom slučaju je dužan da ispunjava obaveze iz tač. 7 i 9 ovog modula, u skladu sa ovlašćenjem.
III. Modul C - Usaglašenost sa tipom na osnovu interne kontrole proizvodnje
1) Usaglašenost sa tipom na osnovu interne kontrole proizvodnje je dio postupka ocjenjivanja usaglašenosti kojim proizvođač ispunjava obaveze utvrđene u tač. 2 i 3 ovog modula i izjavljuje da su predmetne komponente interoperabilnosti usaglašene sa tipom opisanim u Sertifikatu o ispitivanju tipa i da ispunjavaju propisane zahtjeve.
2) Proizvodnja Proizvođač je dužan da preduzme sve neophodne mjere kako bi proizvodni proces i njegovo nadgledanje obezbijedili usaglašenost proizvedenih komponenti interoperabilnosti sa odobrenim tipom opisanim u Sertifikatu o ispitivanju tipa, kao i sa propisanim zahtjevima.
3) Znak usaglašenosti i Deklaraciju o usaglašenosti sa specifikacijama 3.1. Proizvođač je dužan da na svaku pojedinačnu komponentu interoperabilnosti, koja je usaglašena sa tipom opisanim u Sertifikatu o ispitivanju tipa i ispunjava primjenjive propisane zahtjeve, stavi znak usaglašenosti utvrđenu zakonom kojim se propisuju tehnički zahtjevi za proizvode i ocjenjivanje usaglašenosti i propisima donijetim na osnovu tog zakona.
3.2. Proizvođač je dužan da sačini pisanu Deklaraciju o usaglašenosti sa specifikacijama za svaki model komponente interoperabilnosti i da je stavi na raspolaganje nadležnim organima u periodu od deset godina od dana stavljanja komponente interoperabilnosti na tržište. Deklaracija o usaglašenosti sa specifikacijama mora da identifikuje model komponente interoperabilnosti na koji se odnosi.
Kopija Deklaracije o usaglašenosti sa specifikacijama stavlja se na raspolaganje nadležnim organima na njihov zahtjev.
4) Ovlašćeni predstavnik Obaveze proizvođača utvrđene u tački 3 ovog modula može, u njegovo ime i pod njegovom odgovornošću, izvršavati njegov ovlašćeni predstavnik, u skladu
sa ovlašćenjem.
IV. Specifikacije ispitivanja
Ocjenjivanje usaglašenosti implementacije sa zahtjevima iz Modula A ovog priloga i relevantnim tehničkim specifikacijama i standardima može se vršiti primjenom sljedećih specifikacija ispitivanja:
- za tehničku dokumentaciju iz Modula A ovog priloga, koja se odnosi na DSRC transakcije naplate: EN 15876-1:2016, ETSI TS 102 708-1-1:2010, ETSI TS 102 708-1- 2:2010, ETSI TS 102 708-2-1:2013 i ETSI TS 102 708-2-2:2018;
- za proizvodnju iz Modula A ovog priloga, koja se odnosi na provjere usklađenosti transakcija u realnom vremenu: EN ISO 13143-1:2016;
- za Deklaraciju o usaglašenosti sa specifikacijama iz Modula A ovog priloga, koja se odnosi na dopunu lokalizacije: EN ISO 13140-1:2016.
V. Prilagođenost za korišćenje (interoperabilnost usluge)
Prilagođenost za korišćenje komponenti interoperabilnosti ocjenjuje se kroz njihovo praktično funkcionisanje ili upotrebu, koje su reprezentativno integrisane u sistem EENP-a subjekta za naplatu putarine na čijem području vozila moraju koristiti opremu u vozilu, tokom unaprijed određenog perioda. Ocjenjivanje prilagođenosti za korišćenje obuhvata unaprijed definisana ispitivanja u izjavi o području EENP-a. Subjekat za naplatu putarine ili njegov ovlašćeni predstavnik, kao i pružalac usluge EENP-a, proizvođač ili njegov ovlašćeni predstavnik i prijavljeno tijelo kojem se pružalac usluge EENP-a obratio, dužni su da sprovedu svaku fazu ocjenjivanja prilagođenosti za korišćenje na osnovu mjerljivih kriterijuma ili parametara definisanih u izjavi o području EENP-a.
U cilju sprovođenja ocjenjivanja putem iskustva iz stvarne upotrebe, sa ciljem dokazivanja interoperabilnosti komponenti u praksi, proizvođač, pružalac usluge EENP-a ili njihov ovlašćeni predstavnik dužni su da neposredno sarađuju sa subjektom za naplatu putarine ili da se obrate prijavljenom tijelu, u skladu sa zahtjevima iz tač. a) i b) ovog poglavlja. Subjekat za naplatu putarine može da zahtijeva da se ispitivanja sprovedu korišćenjem infrastrukture koju obezbjeđuje, bez obzira da li pružalac usluge EENP-a sarađuje neposredno sa subjektom za naplatu putarine ili se obratio prijavljenom tijelu.
1) a) Ako pružalac usluge EENP-a neposredno sarađuje sa subjektom za naplatu
putarine na čijem području vozilo mora da koristi opremu u vozilu:proizvođač,
pružalac usluge EENP-a ili njihov ovlašćeni predstavnik dužni su da:
 obezbijede sprovođenje ispitivanja ili stave u upotrebu jedan ili više uzoraka
reprezentativnih za komponente interoperabilnosti, u skladu sa zahtjevima subjekta
za naplatu putarine;
 prate način rada komponenti interoperabilnosti u stvarnoj upotrebi, putem postupka
koji je usaglašen i pod nadzorom subjekta za naplatu putarine;
 dostave dokaze subjektu za naplatu putarine da komponente interoperabilnosti
ispunjavaju sve zahtjeve interoperabilnosti tog subjekta;
 sačine Deklaraciju o prilagođenosti za korišćenje, nakon pribavljanja Sertifikata o
prilagođenosti za korišćenje kojeg obezbjeđuje subjekat za naplatu putarine.
Deklaracija o prilagođenosti za korišćenje obuhvata ocjenu subjekta za naplatu
putarine o prilagođenosti za korišćenje komponenti interoperabilnosti EENP-a u
okviru područja EENP-a tog subjekta;
2) subjekat za naplatu putarine je dužan da:
 jasno definiše program za potvrđivanje ispravnosti putem iskustva iz stvarne
upotrebe;
 odobri postupak za praćenje načina rada u stvarnoj upotrebi u svom području
naplate putarine i sprovede posebne provjere;
 ocijeni interoperabilnost tokom rada u okviru svog sistema;
 obezbjedi Sertifikat o prilagođenosti za korišćenje u svom području naplate putarine
u slučaju uspješnog načina rada komponenti interoperabilnosti.
b) Ako se pružalac usluge EENP obrati prijavljenom tijelu:
1) proizvođač, pružalac usluge EENP-a ili njihov ovlašćeni predstavnik dužni su da:
 obezbijede sprovođenje ispitivanja ili stave u upotrebu jedan ili više uzoraka
reprezentativnih za komponente interoperabilnosti, u skladu sa zahtjevima i
specifikacijama subjekta za naplatu putarine;
 prate način rada komponenti interoperabilnosti u stvarnoj upotrebi, putem postupka
koji je odobren i pod nadzorom prijavljenog tijela;
 dostave prijavljenom tijelu dokaze da komponente interoperabilnosti ispunjavaju sve
zahtjeve interoperabilnosti subjekta za naplatu putarine, uključujući rezultate
dobijene kroz iskustvo iz stvarne upotrebe;
 sačine Deklaraciju o prilagođenosti za korišćenje, nakon pribavljanja Sertifikata o
prilagođenosti za korišćenje izdatog od strane prijavljenog tijela. Deklaracija o
prilagođenosti za korišćenje obuhvata ocjenu prijavljenog tijela o prilagođenosti za
korišćenje komponenti interoperabilnosti EENP-a u okviru područja i okruženja
EENP-a odabranog subjekta za naplatu putarine, a posebno u slučaju kada su u
pitanju interfejsi, u odnosu na tehničke specifikacije, naročito specifikacije
funkcionalne prirode, koje treba provjeriti.
2) prijavljeno tijelo je dužno da:
 uzme u obzir Deklaraciju o usaglašenosti sa specifikacijama, kao i zahtjeve
utvrđene u izjavi o području EENP-a subjekta za naplatu putarine;
 organizuje saradnju sa subjektom za naplatu putarine kojeg je izabrao proizvođač;
 provjeri tehničku dokumentaciju i program za potvrđivanje ispravnosti kroz iskustvo
iz stvarne upotrebe;
 odobri postupak praćenja načina rada u stvarnoj upotrebi i sprovede posebni
nadzor;
 ocijeni interoperabilnost u stvarnoj upotrebi sa sistemima i operativnim procesima
subjekta za naplatu putarine;
 izda Sertifikat o prilagođenosti za korišćenje u slučaju uspješnog načina rada
komponenti interoperabilnosti;
 izda izvještaj sa obrazloženjem u slučaju neuspješnog način rada komponenti
interoperabilnosti. Izvještaj mora da obuhvati i probleme koji mogu nastati zbog
neusaglašenosti sistema i procesa subjekta za naplatu putarine sa relevantnim
standardima i tehničkim specifikacijama. Ako je primjereno, izvještaj sadrži i
preporuke u cilju rješavanja tih problema.
VI. SADRŽAJ DEKLARACIJE O USAGLAŠENOSTI SA SPECIFIKACIJAMA I DEKLARACIJE O PRILAGOĐENOSTI ZA KORIŠĆENJE
1) Sadržaj Deklaracije o usaglašenosti sa specifikacijama Deklaracijom o usaglašenosti sa specifikacijama potvrđuje se da je dokazano ispunjavanje zahtjeva iz zakona kojim se uređuju o tehnički zahtjevi za proizvode i ocjenjivanju usaglašenosti, kao i propisima donijetim na osnovu tog zakona.
Deklaracija o usaglašenosti sa specifikacijama mora imati sadržaj obrasca iz tačke 2 ovog poglavlja, elemente propisane u relevantnim modulima iz ovog priloga i kontinuirano se ažurirati. Deklaracija o usaglašenosti sa specifikacijama mora biti prevedena na jezik ili jezike koje zahtijeva država na čijem se tržištu komponenta interoperabilnosti stavlja u promet ili čini dostupnom.
Sastavljanjem Deklaracije o usaglašenosti sa specifikacijama proizvođač preuzima odgovornost za usaglašenost komponente interoperabilnosti.
2) Sadržaj obrasca Deklaracije o usaglašenosti sa specifikacijama
1)
Br……………….…………………
(jedinstvena
identifikacija
komponente interoperabilnosti) 2) Naziv i adresa proizvođača ili njegovog ovlašćenog predstavnika:
3) Ova deklaracija o usaglašenosti sa specifikacijama se izdaje pod isključivom odgovornošću proizvođača (ili instalatera):
4) Predmet deklaracije (identifikacija komponente interoperabilnosti koja omogućava sljedivost; po potrebi može sadržavati i fotografiju):
5) Predmet deklaracije opisan u ovom obrascu usaglašen je sa relevantnim zakonodavstvom
o usaglašavanju:………………………………………………………………………………………. .
6) Reference na relevantne usklađene standarde koji su korišćeni ili reference na specifikacije u odnosu na koje se proglašava usaglašenost:
7) Ako je primjenjivo, prijavljeno tijelo……………………………………….…………….(naziv, broj)………………………………..je
sprovelo………………………………(opis intervencije)……….i izdalo Sertifikat:………………………………………………………… 8) Dodatne informacije:
Potpisano za i u ime:……………………………………………………………………………...… (mjesto i datum izdavanja):
(ime, funkcija):
(potpis):
3) Deklaracije o usaglašenosti sa specifikacijama i prilagođenosti za korišćenje i prateća dokumenta moraju imati datum i potpis.
Deklaracije iz stava 1 ove tačke moraju biti napisane na istom jeziku kao i uputstva i moraju da sadrže sljedeće:
a) propise donijete na osnovu zakona kojim se uređuju tehnički zahtjevi za proizvode i ocjenjivanju usaglašenosti;
b) naziv i adresu proizvođača, pružaoca EENP-a ili ovlašćenog predstavnika (naziv privrednog subjekta i sjedište, a u slučaju ovlašćenog predstavnika, oznaku proizvođača ili projektanta);
c) opis komponenata interoperabilnosti (brend, tip, verzija, itd.);
d) opis primijenjenih postupaka za sačinjavanje Deklaracije o usaglašenosti sa specifikacijama ili Deklaracije o prilagođenosti za korišćenje;
e) sve relevantne zahtjeve koje ispunjavaju komponente interoperabilnosti, posebno uslove korišćenja;
f) kada je to primenjivo, naziv i adresu subjekta za naplatu putarine koji je uključen u postupak radi postizanja usklađenosti sa specifikacijama ili procjenu prilagođenosti za korišćenje;
g) po potrebi, pozivanje na tehničke specifikacije;
h) identifikaciju potpisnika ovlašćenog za ugovaranje obaveza u ime proizvođača ili njegovog ovlašćenog predstavnika.
PRILOG 6
JEDINSTVENI ELEKTRONSKI INTERFEJS SERVISA EENP I KOMUNIKACIONI PROTOKOLI
Pružaoci usluge EENP-a i subjekat za naplatu putarine dužni su da koriste sljedeće elektronske interfejse:
1. Elektronske radio interfejse pored puta između opreme u vozilu pružaoca usluge EENP- a i fiksne ili mobilne opreme subjekta za naplatu putarine, a kojinaročito podržavaju:
a) transakcije naplate putem komunikacionog sistema kratkog dometa (DSRC), u skladu sa sljedećim zahtjevima:
 oprema u vozilu pružaoca usluge EENP-a mora da podržava standard EN
15509:2014, kao i odredbe ETSI ES 200674-1 V2.4.1 koje se odnose na
interoperabilnost;
 fiksna i mobilna oprema subjekta za naplatu putarine mora da podržava standard
EN 15509:2014;
b) provjeru usklađenosti transakcija u realnom vremenu, u skladu sa standardom EN ISO 12813:2015;
c) dopunske funkcije lokalizacije (gdje je primjenjivo), u skladu sa standardom EN ISO 13141:2015.
Oprema u vozilu za EENP mora biti u skladu sa stavom 1 ovog priloga. Oprema u vozilu za EENP koju koriste laka teretna vozila mora biti u skladu sa stavom 1 tačka a) ovog priloga.
Subjekat za naplatu putarine može, u skladu sa svojim potrebama, u svojoj fiksnoj ili mobilnoj opremi na putu primjenjivati bilo koju podršku iz st. 1 i 2 ovog priloga.
Ako subjekat za naplatu putarine primijeni novu verziju standarda za interfejs između opreme na putu i opreme u vozilu, interfejs mora da nastavi da podržava prethodnu verziju standarda u ograničenom vremenskom periodu, kako bi se obezbijedila stalna kompatibilnost sistema elektronske naplate putarine sa opremom u vozilu koja je u upotrebi. Trajanje tog ograničenog vremenskog perioda subjekat za naplatu putarine objavljuje u svojoj izjavi o području EENP-a i ne može biti kraće od dvije godine.
2) Elektro-optički sistemi za snimanje kojim raspolaže fiksna ili mobilna oprema subjekta za naplatu putarine, a koji omogućavaju automatsko prepoznavanje registarskih oznaka vozila (ANPR), koriste se u sistemima za naplatu putarine u kojima posjedovanje i korišćenje opreme u vozilu nije obavezno.
3) Elektronski interfejsi između odgovarajućih pozadinskih sistema.
Subjekat za naplatu putarine primjenjuje samo one aspekte interfejsa koji su povezani sa tehnologijom koja se koristi na području EENP-a pod njegovom nadležnošću (GNSS, DSRC i/ili ANPR).
3.1. Pružaoci usluge EENP-a i subjekat za naplatu putarine dužni su da uspostave i primjenjuju pozadinske interfejse, nezavisno od tehnologije koja se koristi u području EENP-a, koji omogućavaju:
a) slanje informacija radi podrške rješavanju problema u radu, od subjekta za naplatu putarine ka pružaocima usluge EENP-a;
b) razmjenu evidencije korisnika EENP-a, između pružalaca usluge EENP-a i subjekta za naplatu putarine;
c) razmjenu povjerljivih informacija;
d) razmjenu podataka za obračun putarine;
e) po potrebi, razmjenu zahtjeva za plaćanje u skladu sa poslovnim modelom.
3.2. Pružaoci usluge EENP-a i subjekat za naplatu putarine dužni su da uspostave i primjenjuju pozadinske interfejse za područja EENP-a u kojima se primjenjuje GNSS tehnologija, koji obuhvataju:
a) podnošenje i potvrđivanje prijava putarine utvrđenih globalnim navigacionim satelitskim sistemom (GNSS);
b) u zavisnosti šta je primjenjivo, informacije o obavljenim uplatama putarine u skladu sa poslovnim modelom;
c) u zavisnosti šta je primjenjivo, razmjenu podataka o obračunu putarine u skladu sa poslovnim modelom.
3.3. Pružaoci usluge EENP-a i subjekat za naplatu putarine dužni su da uspostave i primjenjuju pozadinske interfejse za područja EENP-a u kojima se primjenjuje DSRC tehnologija, koji obuhvataju:
a) razmjenu podataka o obračunu putarine;
b) po potrebi, razmjenu zahtjeva za plaćanje utvrđenih putem komunikacionog sistema kratkog dometa (DSRC).
3.4. Pružaoci usluge EENP-a i subjekat za naplatu putarine dužni su da uspostave i primjenjuju pozadinske interfejse za područja EENP-a u kojima se primjenjuje ANPR tehnologija, koji u zavisnosti šta je primjenjivo obuhvataju:
a) razmjenu podataka o obračunu putarine;
b) razmjenu zahtjeva za plaćanje utvrđenih ANPR-om.
Elektronski interfejsi za DSRC i GNSS sisteme između pozadinskih sistema subjekta za naplatu putarine i pružaoca usluge EENP-a moraju biti u skladu sa standardom CEN/TS 16986:2016, sa ispravkom CEN/TS 16986:2016/AC:2017, najkasnije pet godina od dana stupanja na snagu ovog pravilnika.
Ako subjekat za naplatu putarine ili pružalac usluge EENP-a primijeni novu verziju standarda, dužan je da, tokom ograničenog vremenskog perioda, koji ne može biti kraći od dvije godine, nastavi da podržava razmjenu podataka kompatibilnu sa prethodnom verzijom standarda, kako bi se obezbijedila stalna kompatibilnost pozadinskih sistema.
PRILOG 7
SADRŽAJ IZJAVE O PODRUČJU EENP-A
Izjava o području EENP mora da sadrži sljedeće informacije:
1) Dio o proceduralnim uslovima, koji mora biti nediskriminatorski i obuhvatati najmanje: a) politiku upravljanja transakcijama naplate putarine (uključujući parametre autorizacije, podatke za obračun putarine, crne liste);
b) procedure i ugovor o nivou usluge, uključujući format za razmjenu podataka o prijavi ili obračunu putarine, rokove i učestalost prenosa podataka o prijavi putarine, prihvatljiv procenat propuštenih/pogrešnih naplata, tačnost podataka o prijavi putarine, performanse operativne dostupnosti;
c) politiku izdavanja računa;
d) politiku plaćanja;
e) referencu na relevantno tijelo za mirenje i njegove nadležnosti u vezi sa sporovima koji se odnose na naknadu za pružaoce usluge EENP-a i glavnom pružaocu usluga;
f) komercijalne uslove.
1.1. Dio o komercijalnim uslovima mora da obuhvati najmanje sljedeće elemente primjenjive na pružaoce usluga EENP-a:
a) sve primjenjive fiksne naknade zasnovane na troškovima koje snosi subjekat za naplatu putarine za obezbjeđivanje, funkcionisanje i održavanje sistema usklađenog sa EENP-om. Subjekat za naplatu putarine ne može nametnuti pružaocima usluga EENP-a fiksne naknade zasnovane na ovim troškovima ako su troškovi obezbjeđivanja, funkcionisanja i održavanja sistema usklađenog sa EENP-om uključeni u putarinu;
b) sve primjenjive fiksne naknade koje pružaoci usluga EENP-a treba da plate, zasnovane na troškovima postupka akreditacije, uključujući troškove ocjenjivanja usaglašenosti sa specifikacijama ili prilagođenosti za korišćenje komponenti interoperabilnosti;
c) sve primjenjive zahtjeve za bankarskom garancijom ili ekvivalentnim finansijskim instrumentom, koji ne može preći prosječan mjesečni iznos transakcija naplate putarine koji pružalac usluge EENP-a plaća za to područje naplate putarine. Ovaj iznos se određuje na osnovu ukupnog iznosa transakcija naplate putarine koje je pružalac usluge EENP-a platio za to područje u prethodnoj godini. Za nove pružaoce usluga EENP-a i za nova područja naplate putarine, iznos se određuje na osnovu očekivanog prosječnog iznosa transakcija naplate putarine koje pružalac usluge EENP-a treba da plati za to područje u obračunskom periodu, na osnovu broja ugovora i prosječne putarine po ugovoru procijenjene u poslovnom planu pružaoca usluga EENP-a za konkretno područje naplate putarine.
1.2. Komercijalni uslovi moraju, kao minimum, da obuhvate i opis elemenata koji se koriste za određivanje fiksne i/ili varijabilne naknade koju subjekat za naplatu putarine plaća pružaocu usluge EENP-a. Naknada može varirati u zavisnosti od sljedećih elemenata: a) iznosa putarine koju je pružalac usluge EENP-a naplaćuje u ime subjekta za naplatu putarine;
b) broja aktivnih komada opreme u vozilu koje je obezbijedio pružalac usluge EENP-a, a koji se koriste u području EENP-a subjekta za naplatu putarine;
c) gdje je primjenjivo, broja transakcija naplate putarine ili drugog pokazatelja troškova mobilne komunikacije između opreme u vozilu i pozadinskog sistema pružaoca usluge EENP-a;
d) računa koje pružalac usluge EENP-a izdaje korisnicima EENP-a za putarine koje duguju za korišćenje odgovarajućeg područja EENP-a;
e) karakteristika drugih usluga koje je subjekat za naplatu putarine povjerio pružaocu usluge EENP-a.
1.3. Izjava o području EENP-a mora da sadrži i opis posebnih zahtjeva i obaveza glavnog pružaoca usluge, koji se razlikuju od obaveza pružalaca usluga EENP-a i koji opravdavaju eventualne razlike u naknadi glavnog pružaoca usluge u odnosu na pružaoce usluga EENP-a.
2) Dio kojim se unaprijed definišu koraci akreditacije pružaoca usluge EENP-a za pristup području EENP-a i okvirno trajanje postupka akreditacije, a sadrži:
a) cjelokupan postupak ocjenjivanja usaglašenosti sa specifikacijama i prilagođenosti za korišćenje komponenti interoperabilnosti;
b) listu potrebnih sertifikata, laboratorijskih i terenskih ispitivanja i njihove okvirne troškove; c) mjerljive kriterijume ili parametre koji ukazuju na usaglašenost sa specifikacijama;
d) reference na sve primjenjive međunarodne ili evropske standarde koji se odnose na elektronsku naplatu putarine i izuzetke od njihove primjene u području EENP-a;
e) preciziranje svih tehničkih zahtjeva koji su specifični za područje EENP-a, a koji nisu obuhvaćeni međunarodnim ili evropskim standardima.
Isti postupak prihvatanja primjenjuje se na sve pružaoce usluga EENP-a.
3) Dio o podacima za obračun putarine.
PRILOG 8
MINIMALNI KRITERIJUMI PODOBNOSTI ZA PRIJAVLJENA TIJELA
1) Za potrebe notifikacije, tijelo za ocjenjivanje usaglašenosti, odnosno tijelo ovlašćeno da sprovodi
ili
nadzire
postupak
ocjenjivanja
usaglašenosti
sa
specifikacijama
i prilagođenošću za korišćenje komponenti interoperabilnosti, mora da ispunjava kriterijume utvrđene ovim prilogom.
Tijelo za ocjenjivanje usaglašenosti, mora biti akreditovano u skladu sa zakonom kojim se uređuju tehnički zahtjevi za proizvode i ocjenjivanju usaglašenosti, kao i propisima donijetim na osnovu tog zakona.
2) Tijelo za ocjenjivanje usaglašenosti mora biti osnovano u skladu sa zakonom sa pravnim subjektivitetom.
3) Tijelo za ocjenjivanje usaglašenosti mora biti nezavisno od organizacije ili proizvoda koji ocjenjuje.
Tijelo koje pripada privrednom udruženju ili strukovnom udruženju koja predstavlja privredna društva uključena u projektovanje, proizvodnju, isporuku, montažu, korišćenje ili održavanje proizvoda koje ocjenjuje, može se smatrati tijelom za ocjenjivanje usaglašenosti, pod uslovom da je dokazana njegova nezavisnost i odsustvo sukoba interesa.
4) Tijelo za ocjenjivanje usaglašenosti njegovo najviše rukovodstvo i zaposleni odgovorni za sprovođenje zadataka ocjenjivanja usaglašenosti ne mogu biti projektanti, proizvođači, dobavljači, instalateri, kupci, vlasnici, korisnici ili lica koja održavaju proizvode koje ocjenjuju, ni njihovi ovlašćeni predstavnici. Ovo ne sprečava korišćenje ocijenjenih proizvoda koji su neophodni za rad tijela za ocjenjivanje usaglašenosti ili njihovo korišćenje u lične svrhe.
Tijelo za ocjenjivanje usaglašenosti, njegovo najviše rukovodstvo i zaposleni odgovorni za sprovođenje ocjenjivanja usaglašenosti ne smiju biti direktno uključeni u projektovanje, proizvodnju ili izgradnju, prodaju, instalaciju, korišćenje ili održavanje tih proizvoda, ni zastupati strane koje se obavljaju te aktivnosti, kao ni biti uključeni ni u jednu aktivnost koja može dovesti u pitanje njihovu nezavisnost ili integritet u vezi sa aktivnostima ocjenjivanja usaglašenosti za koje su prijavljeni. Ovo ograničenje se posebno odnosi na konsultantske usluge.
Tijela za ocjenjivanje usaglašenosti moraju da obezbijede da aktivnosti njihovih podružnica ili podizvođača ne utiču na povjerljivost, objektivnost ili nepristrasnost njihovih aktivnosti ocjenjivanja usaglašenosti.
5) Tijela za ocjenjivanje usaglašenosti i njihovi zaposleni moraju da sprovode aktivnosti ocjenjivanja usaglašenosti sa najvećim stepenom profesionalnog integriteta i sa potrebnom tehničkom stručnošću u odgovarajućoj oblasti, moraju da budu nezavisni od svih pritisaka i podsticaja, naročito finansijskih, koji bi mogli da utiču na njihovo prosuđivanje ili rezultate aktivnosti ocjenjivanja usaglašenosti, posebno u odnosu na lica ili grupe lica koja imaju interes u ishodu tih aktivnosti.
6) Tijelo za ocjenjivanje usaglašenosti mora biti sposobno da sprovodi sve zadatke ocjenjivanja usaglašenosti na osnovu zakona kojim se uređuju tehnički zahtjevi za proizvode i ocjenjivanju usaglašenosti i propisima donijetim na osnovu tog zakona, a u vezi sa kojima je prijavljeno, bez obzira da li te zadatke obavlja neposredno ili se obavljaju u njegovo ime i pod njegovom odgovornošću.
Tijelo za ocjenjivanje usaglašenosti u svakom trenutku, za svaki postupak ocjenjivanja usaglašenosti i za svaku vrstu ili kategoriju proizvoda u vezi sa kojom je prijavljeno, mora da ima na raspolaganju:
a) zaposlebe sa tehničkim znanjem i dovoljnim i relevantnim iskustvom za obavljanje zadataka ocjenjivanja usaglašenosti;
b) opise procedura kojima se uređuje način sprovođenja ocjenjivanja usaglašenosti, čime se obezbjeđuje transparentnost i mogućnost ponavljanja tih procedura.
c) odgovarajuće politike i procedure kojima se jasno razlikuju zadaci koje obavlja kao prijavljeno tijelo od drugih aktivnosti; i d) procedure za sprovođenje aktivnosti koje uzimaju u obzir veličinu privrednog subjekta, sektor u kojem posluje, strukturu, stepen složenosti tehnologije proizvoda i tip proizvodnog procesa (serijski ili velike proizvodnje)..
Tijelo za ocjenjivanje usaglašenosti mora biti sposobno da na odgovarajući način obavlja tehničke i administrativne zadatke povezane sa aktivnostima ocjenjivanja usaglašenosti i mora da imati pristup neophodnoj opremi i objektima.
7) Zaposleni odgovoran za sprovođenje aktivnosti ocjenjivanja usaglašenosti mora da ima: a) završenu odgovarajuću tehničku i stručnu obuku koja obuhvata sve aktivnosti ocjenjivanja usaglašenosti za koje je tijelo za ocjenjivanje usaglašenosti prijavljeno;
b) zadovoljavajuće znanje o zahtjevima ocjenjivanja koje sprovodi i odgovarajuće ovlašćenje da ga obavlja;
c) dovoljno znanja i razumijevanja bitnih zahtjeva, primjenjivih standarda i relevantnih zahtjeva iz zakona kojima se uređuju tehnički zahtjevi za proizvode i ocjenjivanju usaglašenosti , kao i propisa donijetih na osnovu tog zakona ; i d) sposobnost da sastavlja sertifikate, evidencije i izvještaje kojima se dokazuje da su ocjenjivanja sprovedena.
8) Tijelo za ocjenjivanje usaglašenosti , njegovo najviše rukovodstvo i zaposleni koji sprovode ocjenjivanja mora da budu nepristrasni i primanja tog rukovodstva i zaposlenih ne smiju da zavise od broja sprovedenih ocjenjivanja ni od njihovih rezultata.
9) Tijela za ocjenjivanje usaglašenosti moraju da imaju osiguranje od odgovornosti, ako odgovornost nije preuzela država u skladu sa zakonom ili ako nadležni državni organ nije odgovoran za sprovođenje ocjenjivanja usaglašenosti.
10) Zaposleni tijela za ocjenjivanje usaglašenosti moraju da čuvaju poslovnu tajnu u vezi sa sviminformacijama do kojih dođu prilikom obavljanja svojih zadataka. Ovo ne ograničava dostavljanje informacija nadležnim organimadržave u kojoj se aktivnosti sprovode. Vlasnička prava moraju biti zaštićena.
11) Tijela za ocjenjivanje usaglašenosti moraju
da učestvuju u aktivnostima standardizacije ili obezbijede da zaposleni koje sprovodi ocjenjivanje bude upoznato sa tim aktivnostima, kao i sa aktivnostima koordinacione grupe prijavljenih tijela osnovane na osnovu relevantnog zakonodavstva EU, kao i da primjenjuju kao opšte smjernice administrativne odluke i dokumenta te koordinacione grupe.
PRILOG 9
ZAHTJEVI ZA KLASIFIKACIJU VOZILA
1. Opšte odredbe 1.1. Subjekat za naplatu putarine objavljuje korelaciju između skupa parametara klasifikacije vozila koji se koriste i svojih tarifnih klasa vozila za svaki tarifni režim koji se primjenjuje u području EENP-a za koje je nadležan, najmanje tri mjeseca prije početka primjene tog tarifnog režima. Ova obaveza ne odnosi se na izmjene koje subjekat za naplatu putarine vrši na pojedinačnim tarifama unutar jednog tarifnog režima.
1.2. Subjekat za naplatu putarine objavljuje usklađenost svojih tarifnih klasa vozila sa svojom strukturom tarifa za svaki tarifni režim koji se primjenjuje u području EENP-a za koje je nadležan, kao i da ažurira tu objavu u slučaju promjene usklađenosti.
2. Parametri klasifikacije vozila 2.1. Subjekat za naplatu putarine može da koristi parametre klasifikacije vozila i to:
a) bilo koji parametar klasifikacije vozila koji se može izmjeriti njegovom opremom pored puta; ili b) parametre vozila koji su navedeni u saobraćajnoj dozvoli i standardizovani u tački 8.4 standarda EN ISO 14906:2018.
Ako se koristi, oprema u vozilu je obavezna samo za podršku skladištenju i prenosu mogućih parametara klasifikacije vozila, koji se mogu preuzeti iz te opreme putem namjenske komunikacije kratkog dometa (DSRC) na frekvenciji 5,8 GHz, kako je definisano standardima EN 15509:2014 i ETSI ES 200674-1 V2.4.1. Za sisteme zasnovane na GNSS-u bilo koji parametar vozila može se preuzeti iz opreme u vozilu korišćenjem CEN-DSRC, kako je definisano standardom EN ISO 12813:2019.
2.2. Tokom vožnje u području naplate putarine, oprema u vozilu mora omogućiti razmjenu statusne informacije i kada je primjenjivo, svoje parametre klasifikacije vozila sa opremom za nadzor prijave putarine subjekta za naplatu putarine, na način kako je definisano u Prilogu 6 ovog pravilnika.
3. Novi tarifni režimi 3.1. Ako se novi tarifni režim zasniva na parametrima klasifikacije vozila koji su u upotrebi u najmanje jednom području EENP-a, pružaoci usluga EENP-a moraju da primjenjuju novi tarifni režim od dana njegovog stupanja na snagu.
3.2. Ako se novim tarifnim režimom uvodi jedan ili više novih parametara klasifikacije vozila, država u kojoj je vozilo registrovano mora o tome da obavijesti druge države i pružaoce usluge EENP-a aktivne u predmetnom području EENP-a, najmanje šest mjeseci unaprijed.
OBRAZAC 1
OBAVJEŠTENJE O NEPLAĆANJU PUTARINE
.........................................................................................
.........................................................................................
.........................................................................................
[Ime i prezime (naziv), adresa i broj telefona pošiljaoca]
................................................................................
................................................................................
................................................................................
[Ime i adresa primaoca]
PISANO OBAVJEŠTENJE
u vezi sa neplaćanjem putarine na teritoriji Crne Gore
Strana 2
Dana ....................................... neplaćanje putarine vozilom registarske
(datum)
oznake..........................
marke..................................
tipa.................................................
utvrđeno
je
od
strane.......................................................................................................
(naziv nadležnog organa)
[Opcija 1](1)
Vi ste registrovani kao vlasnik ili korisnik vozila navedenog iznad.
[Opcija 2](1)
Vlasnik ili korisnik vozila je naveo da ste Vi upravljali vozilom kada je
izvršeno neplaćanje putarine.
Relevantni detalji o neplaćanju putarine opisani su na strani 3 ovog
obavještenja.
Novčana kazna za neplaćanje putarine iznosi ............... EUR
Iznos putarine koji je potrebno platiti iznosi ............... EUR
Rok
za
plaćanje
je
.........................................,...................................................................
Ako ne platite novčanu kaznu(1)/putarinu(1) u roku od ......... dana od dana prijema ovog obavještenja, potrebno je da popunite priloženi Obrazac za odgovor (stana 4 ovog obavještenja) i da ga u roku od 30 dana od dana prijema ovog obavještenja dostavite na adresu iz Obrasca za odgovor.
Ovo obavještenje se obrađuje u skladu sa zakonom Crne Gore, na čijoj
teritoriji je došlo do neplaćanja putarine.
Strana 3
Relevantni detalji o neplaćanju putarine
(a) Podaci o vozilu kojim je počinjeno neplaćanje putarine:
Registarska oznaka: ..................................................................................
Država registracije: ...................................................................................
Marka i tip: ...............................................................................................
(b) Podaci o neplaćanju putarine:
Mjesto, datum i vrijeme na kojem je došlo do neplaćanja putarine:
...................................................................................................................
...................................................................................................................
...................................................................................................................
Priroda i pravna kvalifikacija neplaćanja putarine:
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
Detaljan opis neplaćanja putarine:
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
Upućivanje na relevantne pravne odredbe:
...................................................................................................................
...................................................................................................................
Opis dokaza o neplaćanju putarine ili upućivanje na njega:
...................................................................................................................
...................................................................................................................
...................................................................................................................
(c) Podaci o uređaju kojim je utvrđeno neplaćanje putarine(2):
Podaci o uređaju:
...................................................................................................................
...................................................................................................................
Identifikacioni broj uređaja:
...................................................................................................................
Datum isteka posljednjeg baždarenja:
...................................................................................................................
2 Ako uređaj nije korišćen, ne ispunjava se
Strana 4
Obrazac za odgovor
(popuniti velikim štampanim slovima)
A. Podaci o vozaču:
- Ime i prezime:
...........................................................................................................
...........................................................................................................
- Mjesto i datum rođenja:
...........................................................................................................
...........................................................................................................
- Broj vozačke dozvole........................, izdata (datum)......................,
u (mjesto izdavanja)...........................................................................
- Adresa: ..............................................................................................
...........................................................................................................
...........................................................................................................
B. Pitanja:
1. Da li je vozilo, marke.............................., registarske oznake .........
................................. registrovano na Vaše ime? ...................da/ne(1)
Ako nije, navedite podatke o vlasniku saobraćajne dozvole:
.............................................................................................................
[ime, prezime, adresa]
2. Da li priznajte da niste platili putarinu? da/ne(1) 3. Ako ne priznajte, navedite razloge:.................................................
...........................................................................................................
...........................................................................................................
...........................................................................................................
Popunjen obrazac dostavite u roku od 30 dana od dana prijema ovog obavještenja nadležnom organu:...............................................................
na adresu ...................................................................................................
Ime i prezime:.........................................................
Svojeručni potpis:....................................................
Strana 5
OBAVJEŠTENJE O NASTAVKU POSTUPKA
(Ako obavještenje šalje subjekat za naplatu putarine u skladu sa članom 23n Zakona o putevima ("Službeni list CG", br. 82/20, 140/22 i ______))
Ako utvrđena putarina nije plaćena u roku navedenom u ovom obavještenju ili nisu dostavljeni vjerodostojni podaci o identitetu vozača,
subjekat za naplatu putarine može da pokrene prekršajni postupak i/ili postupak prinudne naplate putarine kod nadležnog organa na teritoriji
Crne Gore.
Ako se predmet ne nastavi, bićete obaviješteni u roku od 60 dana od dana
prijema Obrasca za odgovor ili dokaza o plaćanju putarine.(1)
Ako se predmet nastavi, primjenjuje se sljedeći postupak:
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
...................................................................................................................
[popunjava se kakav će biti dalji postupak. Ti detalji naročito uključuju:
naziv i adresu organa ili subjekta nadležnog za rješavanje predmeta, rok za plaćanje, naziv i adresu nadležnog organa za pravni lijek, kao i rok za
podnošenje pravnog lijeka]
Protiv odluke o nastavku predmeta nije propisana mogućnost podnošenja
pravnog lijeka.
Ovo obavještenje samo po sebi ne proizvodi pravne posljedice.
Strana 6
Izjava o zaštita podataka
U skladu sa Regulativom (EU) 2016/679 imate pravo da zahtijevate pristup svojim ličnim podacima, kao i njihov ispravak ili brisanje, ograničavanje njihove obrade, pravo na podnošenje prigovora na obradu tih podataka, kao i pravo na prenosivost podataka. Takođe, imate pravo da podnesete prigovor [naziv i adresa relevantnog nadzornog organa].
U skladu sa propisima o zaštiti podataka o ličnosti imate pravo da od rukovaoca obrade zahtijevate pristup svojim ličnim podacima, kao i njihov ispravak ili brisanje i ograničavanje njihove obrade. Takođe, imate pravo da podnesete prigovor [naziv i adresa relevantnog nadzornog organa].
