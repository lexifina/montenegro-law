PRILOG 1
OPŠTI ASPEKTI SISTEMA ZA RAZMJENU PORUKA TAHONET
Uvod Asinkroni interfejs je proces u kojem se poruka kao odgovor na zahtjev vraća novom HTTP vezom.
Opšte pretraživanje je poruka sa zahtjevom koju država članica upućuje svim drugim državama članicama.
Tijelo koje izdaje karticu je tijelo koje je država članica ovlastila za izdavanje tahografskih kartica i upravljanje njima.
Centralno čvorište je informacijski sistem koji omogućava usmjeravanje poruka sistema TAHOnet među državama članicama.
Nacionalni sistem je informacioni sistem uspostavljen u svakoj državi članici za slanje i obradu poruka sistema TAHOnet te odgovaranje na njih.
Sinhroni interfejs je proces u kojem se poruka kao odgovor na zahtjev vraća istom HTTP vezom kojom je poslat zahtjev.
Država članica koja upućuje zahtjev je država članica koja upućuje zahtjev ili obaviještenje, koji se zatim prosljeđuju odgovarajućoj državi članici koja odgovara na zahtjev.
Država članica koja odgovara na zahtjev je država članica kojoj se upućuje zahtjev ili obaviještenje iz sistema TAHOnet.
Ciljano pretraživanje je poruka sa zahtjevom koji država članica upućuje jednoj državi članici.
Tahografska kartica je kartica vozača ili kartica radionice u skladu sa članom 2 tač. (f) i (k) Regulative (EU) br. 165/2014.
Sistem transevropskih usluga za telematiku među upravama (Testa) je platforma za telekomunikaciono međupovezivanje radi sigurne razmjene informacija među javnim upravama u Uniji.
Direktan pristup TAHOnetu je povezivanje nacionalne elektronske evidencije, pomoću priključka na mrežu Testa kojom upravlja država članica u kojoj je ta evidencija smještena, na sistem za razmjenu poruka TAHOnet.
Indirektan pristup TAHOnetu je povezivanje nacionalne elektronske evidencije, pomoću priključka na mrežu Testa kojom upravlja država članica u kojoj ta evidencija nije smještena, na sistem za razmjenu poruka TAHOnet.
1. Arhitektura Sistem za razmjenu poruka TAHOnet sastoji se od sljedećih dijelova:
1.1. Centralnog čvorišta, koje mora biti u mogućnosti primiti zahtjev države članice koja ga upućuje te ga provjeriti i obraditi prosljeđivanjem državama članicama koje odgovaraju na zahtjev. Centralno čvorište mora pričekati odgovor svih država članica, konsolidovati sve odgovore i konsolidovani odgovor proslijediti državi članici koja upućuje zahtjev.
▼M1 Sve poruke sistema TAHOnet prosljeđuju se putem centralnog čvorišta.
1.2. Nacionalnih sistema država članica, koji moraju biti opremljeni interfejsom koje je u mogućnosti slati zahtjeve centralnom čvorištu i primati odgovarajuće odgovore. Nacionalni sistemi mogu za prenos poruka centralnom čvorištu i primanje poruka iz njega upotrebljavati softver koji je vlasništvo proizvođača ili komercijalni softver.
2. Upravljanje 2.1. Centralnim čvorištem upravlja Komisija, koja je odgovorna za tehnički rad i održavanje centralnog čvorišta.
▼M1 2.2. U centralnom čvorištu podaci se pohranjuju najduže šest mjeseci, osim evidencionih i statističkih podataka te podataka o usmjeravanju navedenih u Prilogu 7 ovog pravilnika. ▼B 2.3. Centralno čvorište ne smije omogućavati pristup ličnim podacima, osim u slučaju ovlaštenog osoblja Komisije ako su ti podaci potrebni u svrhu praćenja, održavanja i otklanjanja poteškoća.
2.4. Države članice odgovorne su za:
2.4.1. uspostavu nacionalnih sistema i upravljanje njima, uključujući povezivanje sa centralnim čvorištem;
2.4.2. instaliranje i održavanje hardvera i softvera svojih nacionalnih sistema, bilo softvera koji je vlasništvo proizvođača ili komercijalnog softvera;
2.4.3. ispravnu interoperabilnost svojih nacionalnih sistema sa centralnim čvorištem, uključujući upravljanje porukama o pogrešci primljenima od centralnog čvorišta;
2.4.4. preduzimanje svih mjera za osiguravanje povjerljivosti, cjelovitosti i dostupnosti informacija;
2.4.5. djelovanje nacionalnih sistema u skladu sa niovima usluga navedenima u Prilogu 6 ovog pravilnika.
2.5. Internetski portal MOVEHUB Komisija osigurava mrežnu aplikaciju sa sigurnim pristupom, koja se naziva "internetski portal MOVEHUB" i omogućava barem sljedeće usluge:
(a) statistiku dostupnosti usluga sistema država članica;
(b) obavijesti o održavanju centralnog čvorišta i nacionalnih sistema država članica;
(c) skupna izvještaja;
(d) upravljanje kontaktima;
(e) XSD sheme.
2.6. Upravljanje kontaktima ▼M1 2.6.1. Funkcija upravljanja kontaktima omogućava svakoj državi članici upravljanje podacima za kontakt u pogledu političkih, poslovnih, operativnih i tehničkih kategorija te države članice, pri čemu je nadležno tijelo svake države članice odgovorno za održavanje svojih kontakata. Pregledavanje podataka za kontakt iz drugih država članica mora biti moguće, ali ne i njihovo uređivanje.
▼M1 -----
▼B
PRILOG 2
FUNKCIJE SISTEMA ZA RAZMJENU PORUKA TAHONET
1. Sistem za razmjenu poruka TAHOnet mora omogućavati sljedeće funkcije:
1.1. Provjera izdatih kartica (Check Issued Cards - CIC): omogućava državi članici koja upućuje zahtjev da pošalje zahtjev za provjeru kartica jednoj državi članici koja odgovara na zahtjev ili svima njima radi utvrđivanja posjeduje li već podnositelj zahtjeva karticu vozača koju su izdale države članice koje odgovaraju na zahtjev. Države članice koje odgovaraju na zahtjev odgovaraju slanjem odgovora o provjeri izdatih kartica.
1.2. Provjera statusa kartice (Check Card Status - CCS): omogućava državi članici koja upućuje zahtjev da slanjem zahtjeva za provjeru statusa kartice zatraži od države članice koja odgovara na zahtjev pojedinosti o kartici koju je izdao ovaj drugi. Država članica koja odgovara na zahtjev odgovara slanjem odgovora o provjeri statusa kartice.
▼M1 1.3. Promjena statusa kartice (Modify Card Status - MCS): omogućava državi članici koja upućuje zahtjev da upućivanjem zahtjeva za promjenu statusa kartice obavijesti državu članicu koja odgovara na zahtjev da se status kartice koju je izdao ovaj drugi promenio. Odmah nakon ažuriranja evidencije ili odbijanja obavijesti država članica koja odgovara na zahtjev odgovara na primljeni zahtjev za promjenu statusa kartice upućivanjem odgovora na zahtjev za promjenu statusa kartice, pritom navodeći rezultat ažuriranja i trenutačni status kartice (kako je zabilježeno u evidenciji tahografskih kartica). Taj se odgovor šalje najkasnije deset kalendarskih dana nakon što je poslato obavještenje o zahtjevu. U svakom slučaju zahtjev ili odgovor za promjenu statusa kartice potvrđuje se potvrdom promjene statusa kartice.
▼B 1.4. Kartica izdata na osnovu vozačke dozvole (Issued Card Driving License - ICDL): omogućava državi članici koja upućuje zahtjev da zahtjevom za karticu izdatu na osnovu vozačke dozvole obavijesti državu članicu koja odgovara na zahtjev da je prvospomenuta država izdala karticu na osnovu vozačka dozvola koju je izdao ovaj drugi. Država članica koja odgovara na zahtjev odgovara slanjem odgovora na karticu izdatu na osnovu vozačke dozvole.
2. Uključit će se i druge vrste poruka koje se smatraju prikladnima za efikasno funkcioniranje sistema TAHOnet, primjerice obavještenje o pogreškama.
3. Nacionalni sistemi moraju prepoznavati statuse kartica navedene u Dodatku ovom Prilogu kada se koriste bilo kojom od funkcija opisanih u tački 1. Međutim, države članice ne moraju primjenjivati administrativni postupak koji se koristi svim navedenim statusima. 4. Kada država članica primi odgovor ili obavještenje sa statusom koji se ne upotrebljava u njenim administrativnim postupcima, nacionalni sistem mora pretvoriti status iz primljene poruke u odgovarajuću vrijednost u tom postupku. Država članica koja odgovara na zahtjev ne smije odbiti tu poruku ako je status u poruci naveden u Dodatku ovom Prilogu. ▼M1 5. Status kartice naveden u Dodatku ovom Prilogu ne smije se upotrebljavati kako bi se odredilo je li kartica važeća za vožnju. Kada država članica pretražuje evidenciju države članice koja je izdala karticu pomoću funkcije CCS ili CIC, odgovor sadrži posebno polje "važeća za vožnju". Nacionalni administrativni postupci moraju biti takvi da odgovori funkcije CCS ili CIC uvijek sadrže odgovarajuću vrijednost "važeća za vožnju".
▼B
Dodatak Statusi kartica
Status kartice
Definicija
Podnesen
zahtjev
Tijelo koje izdaje karticu primilo je zahtjev za izdavanje kartice
vozača. Ta je informacija zabilježena i pohranjena u bazu podataka
s generiranim ključevima za pretraživanje.
Odobrena
Tijelo koje izdaje karticu odobrilo je zahtjev za izdavanje
tahografske kartice.
Odbijena
Tijelo koje izdaje karticu nije odobrilo zahtjev.
Personalizovana Tahografska kartica je personalizovana.
Poslana
Nacionalno tijelo poslalo je karticu vozača dotičnom vozaču ili
agenciji koja je dostavlja.
Uručena
Nacionalno tijelo predalo je karticu vozača dotičnom vozaču.
Oduzeta
Nadležno tijelo oduzelo je vozaču karticu vozača.
Povučena
Kartica vozača privremeno je oduzeta vozaču.
Poništena
Tijelo koje izdaje karticu odlučilo je poništiti karticu vozača. Kartica
je trajno poništena.
Vraćena
Tahografska kartica vraćena je tijelu koje izdaje karticu i prijavljeno
je da više nije potrebna.
Izgubljena
Tijelu koje izdaje karticu prijavljen je gubitak tahografske kartice.
Ukradena
Tijelu koje izdaje karticu prijavljena je krađa tahografske kartice.
Ukradena kartica smatra se izgubljenom.
Neispravna
Tijelu koje izdaje karticu tahografska kartica prijavljena je kao
neispravna.
Istekla
Isteklo je period važenja tahografske kartice.
Nadomještena Tahografska kartica koja je prijavljena kao izgubljena, ukradena ili
neispravna nadomještena je novom karticom. Podaci na novoj
kartici isti su kao na staroj, osim broja indeksa zamjene kartice, koji
je uvećan za jedan.
Obnovljena
Tahografska kartica je obnovljena zbog promjene administrativnih
podataka ili istekao period važenja. Broj nove kartice jednak je
broju stare kartice, osim broja indeksa obnove kartice, koji je
uvećan za jedan.
U postupku
zamjene
Tijelo koje je izdalo karticu vozača primilo je obavještenje da je
pokrenut postupak za zamjenu te kartice karticom vozača koju
izdaje tijelo druge države članice.
Zamijenjena
Tijelo koje je izdalo karticu vozača primilo je obavijest da je završen
postupak za zamjenu te kartice karticom vozača koju izdaje tijelo
druge države članice.
PRILOG 3
ODREDBE U POGLEDU PORUKA SISTEMA ZA RAZMJENU PORUKA TAHONET
1. Opšti tehnički zahtjevi 1.1. Centralno čvorište osigurava sinhroni i asinhroni interfejs za razmjenu poruka. Države članice mogu izabrati najprikladniju tehnologiju interfejsa za vlastite aplikacije.
1.2. Sve poruke razmijenjene između centralnog čvorišta i nacionalnih sistema moraju biti kodirane prema standardu UTF-8.
1.3. Nacionalni sistemi moraju omogućivati primanje i obradu poruka koje sadržavaju grčka ili ćirilična slova.
2. Struktura XML poruka i definicija sistema (XSD) 2.1. Opšta struktura XML poruka mora biti u skladu s formatom definisanim XSD shemama ugrađenima u centralno čvorište.
2.2. Centralno čvorište i nacionalni sistemi šalju i primaju poruke koje su u skladu s XSD shemom poruke.
▼M1 2.3. Nacionalni sistemi moraju omogućavati slanje, primanje i obradu svih poruka koje odgovaraju bilo kojoj od funkcija navedenih u Prilogu 2 ovog pravilnika.
▼B 2.4. XML poruke obuhvaćaju barem minimalne zahtjeve utvrđene u Dodatku ovom Prilogu. ▼M1
___________________
Dodatak Minimalni zahtjevi za sadržaj XML poruka
Standardno zaglavlje
Obvezno
Verzija
Službena verzija XML specifikacija navodi se u nazivnom prostoru (namespace) definisanom u XSD shemi poruke i u atributu verzija u elementu zaglavlja svake XML poruke. Broj verzije ("n.m.") definiše se kao fiksna vrijednost pri svakom
generisanju datoteke s XML definicijom sistema (xsd).
Da
Ispitni
identifikator
Neobvezna identifikacijska oznaka za ispitivanje. Inicijator ispitivanja popunjava identifikacijsku oznaku i svi sudionici u radnom tijeku prosljeđuju odnosno vraćaju istu identifikacijsku oznaku. U produkciji se ignoriše i ne upotrebljava ako je
navedena.
Ne
Tehnički
identifikator
Univerzalni jedinstveni identifikator (UUID) za jedinstvenu identifikaciju svake pojedinačne poruke. Pošiljatelj generiše UUID i popunjava ovaj atribut. Ti se podaci ne upotrebljavaju
ni u kakvom poslovnom svojstvu.
Da
Identifikator
radnog toka
Identifikator radnog toka je univerzalni jedinstveni identifikator (UUID) i generiše ga država članica koja upućuje zahtjev. Ta se identifikacijska oznaka zatim upotrebljava u svim
porukama za povezivanje radnog toka.
Da
Vrijeme
slanja
Datum i vrijeme (u UTC formatu) kada je poruka poslata.
Da
Prekoračenje
vremena
Neobavezni atribut datuma i vremena (u UTC formatu). Ova se vrijednost utvrđuje isključivo za proslijeđene zahtjeve u središnjem čvorištu i izračunava se na osnovu datuma i vremena zaprimanja početnog zahtjeva u čvorištu. Time se državu članicu koja odgovara na zahtjev obavještava o trenutku prekoračenja vremena za zahtjev. Ta vrijednost nije potrebna za početne zahtjeve poslate u središnje čvorište ni
u porukama odgovora.
Ne
Pošiljatelj
Oznaka ISO 3166-1 alpha-2 države članice koja šalje poruku
ili "EU".
Da
Primatelj
Oznaka ISO 3166-1 alpha-2 države članice kojoj se šalje
poruka ili "EU".
Da
Zahtjev za provjeru izdatih kartica
Obvezno
Prezime
Prezime vozača.
Da
Ime
Ime vozača.
Ne
Datum rođenja
Datum rođenja vozača.
Da
Mjesto rođenja
Mjesto rođenja vozača.
Ne
Broj
vozačke
dozvole
Broj vozačke dozvole vozača.
Ne
Zemlja
izdavanja
vozačke dozvole
Zemlja u kojoj je vozaču izdana vozačka
dozvola.
Ne
Odgovor na zahtjev za provjeru izdanih kartica
Obvezno
Oznaka statusa
Oznaka statusa odgovora.
Da
Poruka o statusu
Opis statusa s objašnjenjem.
Ne
Mehanizam
pretraživanja
Podatak
je
li
kartica
pronađena
NYSIIS
pretraživanjem ili prilagođenim pretraživanjem.
Da
Pronađene pojedinosti vozača
Da, ako je
vozač
pronađen
Prezime
Prezimena pronađenih vozača.
Da
Ime
Imena pronađenih vozača.
Ne
Datum rođenja
Datumi rođenja pronađenih vozača.
Da
Mjesto rođenja
Mjesta rođenja pronađenih vozača.
Ne
Pojedinosti kartice
Da, ako je
vozač
pronađen
Broj kartice
Broj pronađene kartice.
Da
Status kartice
Status pronađene kartice.
Da
Važeća za vožnju
Pronađena kartica je/nije važeća za vožnju.
Da
Tijelo koje je izdalo
karticu
Ime tijela koje je izdalo pronađenu karticu.
Da
Datum
početka
važenja kartice
Datum početka važenja pronađene kartice.
Da
Datum isteka kartice
Datum isteka pronađene kartice.
Da
Datum
promjene
statusa kartice
Datum kada je pronađena kartica zadnji put
promijenjena.
Da
Privremena kartica
Pronađena kartica je privremena kartica.
Ne
Pojedinosti vozačke dozvole
Da, ako je
kartica vozača
pronađena
Broj
vozačke
dozvole
Broj vozačke dozvole pronađenog vozača.
Da
Zemlja
izdavanja
vozačke dozvole
Zemlja u kojoj je pronađenom vozaču izdana
vozačka dozvola.
Da
Status
vozačke
dozvole
Status vozačke dozvole pronađenog vozača.
Ne
Datum
izdavanja
vozačke dozvole
Datum izdavanja vozačke dozvole pronađenog
vozača.
Ne
Datum
isteka
vozačke dozvole
Datum isteka vozačke dozvole pronađenog
vozača.
Ne
Pojedinosti kartice radionice
Da, ako je
pronađena
kartica
radionice
Ime radionice
Ime radionice kojoj je izdana pronađena kartica.
Da
Adresa radionice
Adresa radionice kojoj je izdana pronađena
kartica.
Da
Zahtjev za provjeru statusa kartice
Obvezno
Broj kartice
Broj kartice čije se pojedinosti zahtijevaju.
Da
Odgovor na zahtjev za provjeru statusa kartice
Obvezno
Oznaka statusa
Oznaka statusa odgovora.
Da
Poruka o statusu
Opis statusa s objašnjenjem.
Ne
Pojedinosti zahtijevane kartice
Da, ako je
zahtijevana
kartica
pronađena
Broj kartice
Broj zahtijevane kartice.
Da
Status kartice
Status zahtijevane kartice.
Da
Važeća
za
vožnju
Zahtijevana kartica je/nije važeća za vožnju.
Da
Tijelo
koje
je
izdalo karticu
Ime tijela koje je izdalo zahtijevanu karticu.
Da
Datum
početka
važenja kartice
Datum početka važenja zahtijevane kartice.
Da
Datum
isteka
kartice
Datum isteka zahtijevane kartice.
Da
Datum promjene
statusa kartice
Datum kada je zahtijevana kartica zadnji put
promijenjena.
Da
Privremena
kartica
Zahtijevana kartica je privremena kartica.
Ne
Kartica radionice
Da, ako je
pronađena
kartica
radionice
Ime radionice
Ime radionice kojoj je kartica izdana.
Da
Adresa radionice
Adresa radionice kojoj je kartica izdana.
Da
Pojedinosti imatelja kartice
Prezime
Prezime vozača kojem je kartica izdana.
Da
Ime
Ime vozača kojem je kartica izdana.
Ne
Datum rođenja
Datum rođenja vozača kojem je kartica izdana.
Da
Mjesto rođenja
Mjesto rođenja vozača kojem je kartica izdana.
Ne
Pojedinosti vozačke dozvole
Da, ako je
kartica
vozača
pronađena
Broj
vozačke
dozvole
Broj vozačke dozvole vozača kojem je kartica
izdana.
Da
Zemlja izdavanja
vozačke dozvole
Zemlja koja je izdala vozačku dozvolu vozaču
kojem je kartica izdana.
Da
Status
vozačke
dozvole
Status vozačke dozvole vozača kojem je kartica
izdana.
Ne
Datum izdavanja
vozačke dozvole
Datum izdavanja vozačke dozvole vozaču kojem je
kartica izdana.
Ne
Datum
isteka
vozačke dozvole
Datum isteka vozačke dozvole vozača kojem je
kartica izdana.
Ne
Zahtjev za promjenu statusa kartice
Obvezno
Broj kartice
Broj kartice čiji se status promijenio.
Da
Novi
status
kartice
Novi status nakon promjene statusa kartice.
Da
Datum promjene
statusa kartice
Datum i vrijeme kad je promijenjen status kartice.
Da
Prijavitelj
Tijelo
Ime tijela koje je promijenilo status kartice.
Da
Adresa nadležnog
tijela
Adresa nadležnog tijela koje je promijenilo status
kartice.
Da
Prezime
Prezime osobe koja je promijenila status kartice.
Ne
Ime
Ime osobe koja je promijenila status kartice.
Ne
Telefon
Telefonski broj osobe koja je promijenila status
kartice.
Ne
Adresa e-pošte
Adresa e-pošte osobe koja je promijenila status
kartice.
Ne
Potvrda promjene statusa kartice
Obvezno
Oznaka statusa
Oznaka statusa potvrde.
Da
Poruka o statusu
Opis statusa s objašnjenjem.
Ne
Vrsta potvrde
Vrsta
potvrde:
potvrda
zahtjeva
ili
potvrda
odgovora
Da
Odgovor na zahtjev za promjenu statusa kartice
Obvezno
Oznaka statusa
Oznaka statusa odgovora.
Da
Poruka o statusu
Opis statusa s objašnjenjem.
Ne
Broj kartice
Broj zahtijevane kartice vozača.
Da
Status kartice
Status zahtijevane kartice kako je zabilježeno u
evidenciji tahografskih kartica.
Da
Zahtjev za karticu izdanu na temelju vozačke dozvole
Obvezno
Broj kartice
Broj izdane kartice.
Da
Broj
vozačke
dozvole
Broj strane vozačke dozvole koja je upotrijebljena
za podnošenje zahtjeva za karticu vozača.
Da
Prezime
Prezime vozača kojem je kartica izdana.
Da
Ime
Ime vozača kojem je kartica izdana.
Ne
Datum rođenja
Datum rođenja vozača kojem je kartica izdana.
Da
Mjesto rođenja
Mjesto rođenja vozača kojem je kartica izdana.
Ne
Odgovor na karticu izdanu na temelju vozačke dozvole
Obvezno
Oznaka statusa
Oznaka statusa odgovora.
Da
Poruka o statusu
Opis statusa s objašnjenjem.
Ne
▼B
PRILOG 4
USLUGE TRANSLITERACIJE I SISTEMA NYSIIS (NEW YORK STATE IDENTIFICATION AND INTELLIGENCE SYSTEM)
1. Algoritam NYSIIS koji se primjenjuje u centralnom čvorištu upotrebljava se za kodiranje imena svih vozača u nacionalnoj evidenciji.
2. Pri traženju kartice putem funkcije CIC (provjera izdanih kartica) kao primarni mehanizam pretraživanja upotrebljavaju se ključevi NYSIIS.
3. Osim toga, države članice mogu upotrebljavati prilagođen algoritam za dobivanje dodatnih rezultata.
4. Uz rezultate pretraživanja navodi se mehanizam pretraživanja koji je upotrijebljen za pronalaženje podatka, to jest pretraživanje pomoću NYSIIS-a ili prilagođeno pretraživanje. 5. Ako država članica odluči zabilježiti obavještenje o karticama izdatima na osnovu vozačke dozvole (ICDL), tada se ključevi NYSIIS koji se nalaze u obavještenju bilježe kao dio podataka o karticama izdatima na osnovu vozačke dozvole.
5.1. Pri pretraživanju podataka o karticama izdanima na temelju vozačke dozvole država članica upotrebljava ključeve NYSIIS za ime podnositelja zahtjeva.
PRILOG 5
SIGURNOSNI ZAHTJEVI
1. Za razmjenu poruka između centralnog čvorišta i nacionalnih sistema upotrebljava se protokol HTTPS.
2. U nacionalnim sistemima upotrebljavaju se certifikati PKI koje izdaje Komisija za potrebe zaštite prenosa poruka između nacionalnih sistema i centralnog čvorišta.
3. Nacionalni sistemi primjenjuju, kao minimum, certifikate s hash algoritmom potpisa SHA-2 (SHA-256) i dužinom javnog ključa od 2 048 bita.
PRILOG 6
NIVOI USLUGA
1. Nacionalni sistemi moraju pružati sljedeće minimalne nivoe usluga:
1.1. Moraju biti dostupni 24 sata dnevno, sedam dana u nedelji.
1.2. Njihova se dostupnost prati porukama koje centralno čvorište šalje u redovinim vremenskim razmacima (heartbeat messages).
1.3. Njihova stopa dostupnosti mora iznositi 98 %, u skladu sa sljedećom tablicom (iznosi su zaokruženi na najbližu prikladnu jedinicu):
Dostupnost od
znači nedostupnost od
dnevno
mjesečno
godišnje
98 %
pola sata
15 sati
7,5 dana Države članice podstiču se da poštuju dnevnu stopu dostupnosti. Međutim, poznato je da je prilikom određenih nužnih aktivnosti, primjerice tokom održavanja sistema, sistem nedostupan više od 30 minuta. Mjesečne i godišnje stope dostupnosti obvezne su.
▼M1 1.4. Moraju odgovoriti na najmanje 98 % zahtjeva koji su im proslijeđeni u jednom kalendarskom mjesecu i biti u stanju obraditi zahtjeve brzinom od šest poruka u sekundi. 1.5. Pri slanju odgovora funkcija CIC, CCS i ICDL te potvrda MCS u skladu s Prilogom 8., na zahtjeve moraju odgovoriti u roku od deset sekundi.
Prekoračenje vremena za zahtjeve (vrijeme u kojem podnositelj zahtjeva može čekati odgovor) ne smije biti duži od 20 sekundi.
1.6. Odgovor na promjenu statusa kartice šalje se u roku od deset kalendarskih dana od slanja zahtjeva za promjenu statusa kartice.
1.7. Nacionalni sistemi neće čvorištu TAHOneta slati više od dva zahtjeva u sekundi.
1.8. Svaki nacionalni sistem mora biti u stanju prevladati potencijalne tehničke probleme centralnog čvorišta ili nacionalnih sistema u ostalim državama članicama. One uključuju, ali nisu ograničene na sljedeće:
(a) gubitak veze sa centralnim čvorištem;
(b) slučajeve kada nema odgovora na zahtjev;
(c) primanje odgovora nakon prekoračenja vremena poruke;
(d) primanje nezatraženih poruka;
(e) primanje neispravnih poruka.
▼M1 ----- ▼B 2.Centralno čvorište mora:
2.1. omogućiti stopu dostupnosti od 98 %;
2.2. obavještavati nacionalne sisteme o svim pogreškama, bilo porukom odgovora ili namjenskom porukom o pogrešci. Nacionalni sistemi moraju primiti te namjenske poruke o pogrešci i imati eskalacijski tok rada za preduzimanje odgovarajućih mjera za ispravljanje prijavljene pogreške.
▼M1 Komisiji se na zahtjev upućuju pojedinosti o eskalacijskom postupku.
▼B 3.Održavanje Države članice putem mrežne aplikacije obavještavaju druge države članice i Komisiju o svim uobičajenim postupcima održavanja najmanje nedelju dana prije početka tih postupaka ako je to tehnički moguće.
PRILOG 7
PODACI ZA EVIDENTIRANJE I STATISTIČKU OBRADU PRIKUPLJENIH PODATAKA
U CENTRALNOM ČVORIŠTU
▼M1 U ovom Prilogu navedeni su detalji o evidencijskim i statističkim podacima te podacima o usmjeravanju koji su prikupljeni u centralnom čvorištu, a ne u državama članicama.
▼B Evidentiranje i statistička obrada prikupljenih podataka u centralnom čvorištu 1. Kako bi se osigurala privatnost, podaci za statističke svrhe su anonimni. Identifikacijski podaci koji se odnose na određenu karticu, vozača ili vozačku dozvolu ne smiju biti dostupni za statističke svrhe.
2. Evidencijske informacije moraju sadržavati podatke o svim transakcijama za potrebe nadzora i otklanjanja grešaka te omogućiti pripremu statistika o tim transakcijama.
▼M1 3. Lični se podaci ne smiju zadržavaju u datotekama duže od šest mjeseci nakon dovršetka transakcije. Statistički i anonimizirani podaci o usmjeravanju čuvaju se neograničeno.
▼B 4. ►M1 Statistički podaci koji se upotrebljavaju za izvješćivanje među ostalim sadržavaju: ◄ (a) državu članicu koja upućuje zahtjev;
(b) državu članicu koja odgovara na zahtjev;
(c) vrstu poruke;
(d) oznaku statusa odgovora;
(e) datum i vrijeme poruka;
(f) vrijeme odgovora.
PRILOG 8
UPOTREBA SISTEMA ZA RAZMJENU PORUKA TAHONET
1. Izdavanje kartica vozača 1.1. Ako podnositelj zahtjeva za karticu vozača ima vozačku dozvolu izdatu u državi članici različitoj od one u kojoj je podnesen zahtjev, država članica u kojoj je podnesen zahtjev pokreće opšte pretraživanje za provjeru izdate kartice (Check Issued Card, CIC).
1.2. Država članica koja izdaje karticu vozača vozaču koji ima vozačku dozvolu izdatu u drugoj državi članici s pomoću funkcije kartice izdate na osnovu vozačke dozvole (Issued Card Driving Licence, ICDL) odmah obaveštava potonjeg da je vozačka kartica izdata. ▼M1 1.3. Ako podnositelj zahtjeva za karticu vozača ima vozačku dozvolu izdatu u državi članici u kojoj je podnesen zahtjev, ta država članica provjerava je li u nacionalnoj evidenciji prethodno zabilježena obavijest ICDL. Ta se provjera najprije sprovodi pretraživanjem obavijesti na osnovu broja vozačke dozvole, a zatim na osnovu ključeva NYSIIS i datuma rođenja. Ako je obavijest pronađena, država članica upućuje ciljano pretraživanje CIC ili CCS državi članici koja je poslala obavijest ICDL.
▼B 1.4. Svaka obavijest ICDL bilježi se u nacionalnoj evidenciji države članice koja je prima. 1.5. Države članice provode opće pretraživanje CIC za najmanje 30 % zahtjeva koje su podnijeli vozači koji imaju dozvolu izdatu u toj državi članici.
▼M1 1.6. Države članice mogu odlučiti da u svoje nacionalne evidencije neće unijeti obavijesti ICDL primljene u skladu sa tačkama 1.3., 1.4. i 1.5. U tom slučaju one obavljaju opšte pretraživanje CIC za svaki primljeni zahtjev.
▼B 1.7. Države članice obavještavaju Komisiju najkasnije do datuma primjene ovog Pravilnika o tome hoće li bilježiti obavijesti ICDL u svojim nacionalnim evidencijama ili će slijediti postupak iz tačke 1.6.
1.8. Države članice koje pet godina ili manje prije datuma primjene ove Uredbe nisu bilježile obavijesti ICDL u svojim nacionalnim evidencijama kako je utvrđeno u tački 1.4. provode opće pretraživanje CIC za 100 % zahtjeva, osim za vozačke dozvole za koje nije zabilježena obavijest ICDL; u tom se slučaju primjenjuje tačka 1.3.
1.9. Obveza iz tačke 1.8. primjenjuje se za period od pet godina od datuma efikasne primjene bilježenja obavijesti ICDL u nacionalnoj evidenciji svake države članice.
2. Poništene, povučene ili ukradene kartice vozača 2.1. Ako je u skladu s članom 26. stavom 7. i članom 29. stavom 2. Regulative (EU) br. 165/2014 kartica vozača poništena, povučena ili proglašena ukradenom u državi članici koja je nije izdala, nadležno tijelo mora:
▼M1 (a) provjeriti stvarni status kartice slanjem zahtjeva CCS državi članici koja ju je izdala. Ako je broj kartice nepoznat, upućuje se ciljano pretraživanje CIC;
▼B (b) putem sistema za razmjenu poruka TAHOnet poslati obavijest o promjeni statusa kartice (Modify Card Status, MCS) državi članici koja ju je izdala.
3. Zamjena kartica vozača 3.1. Ako imatelj kartice vozača podnese zahtjev za zamjenu kartice vozača u državi članici koja je nije izdala, nadležno tijelo države u kojoj je zahtjev podnesen provjerava stvarni status kartice slanjem zahtjeva CCS državi koja ju je izdala.
▼M1 3.2. Nakon što se status kartice vozača provjeri i utvrdi se da je važeća za zamjenu, nadležno tijelo države članice u kojoj je zahtjev podnesen putem sistema za razmjenu poruka TAHOnet šalje obavijest MCS državi članici koja ju je izdala.
▼B 3.3. Države članice koje obnavljaju ili zamjenjuju karticu vozača koji ima vozačku dozvolu izdanu u drugoj državi članici s pomoću funkcije ICDL odmah obavještava državu članicu koja ju je izdala da je kartica vozača obnovljena ili zamijenjena.
▼M1
OBRAZAC 1
ZAHTJEV ZA INDIREKTNI PRISTUP TAHONETU
_______________________________________________________
[Skraćeno ime nadležnog tijela koje traži indirektni pristup TAHOnetu]
iz
_____________
[ime zemlje koja ___________________________ traži indirektan pristup TAHOnetu]
potpisao je ugovor sa
____________________________
[skraćeno ime nadležnog tijela koje ____________________________
pruža indirektni pristup TAHOnetu]
radi ostvarivanja indirektnog pristupa TAHOnetu preko
_________________________________________ [ime zemlje koja pruža indirektni pristup TAHOnetu].
Ugovor kojim _________________________________________
[ime zemlje koja pruža indirektni pristup TAHOnetu]
pruža indirektni pristup
TAHOnetu za
________________________________________
[ime zemlje koja traži indirektni pristup TAHOnetu]
priložen je ovom zahtjevu.
Navedene su sljedeće informacije:
(a) tijelo nadležno za pristup TAHOnetu u
_____________________________
[naziv zemlje koja traži _______________________ ;
indirektni pristup TAHOnetu] (b) osoba za kontakt za TAHOnet u
_______________________
[nadležno tijelo iz tačke (a)]
(ime, funkcija, adresa,
e-pošte, telefonski broj i adresa);
(c) ime i funkcija drugih odgovornih subjekata u odnosu na TAHOnet; d) osobe za kontakt iz odgovornih subjekata iz tačke (c) (ime, funkcija, adresa e-pošte, telefonski broj);
(d) osoba za kontakt u odgovornom subjektu iz tačke (c) (ime, funkcija, adresa e-pošte, telefonski broj).
Potpis
_______________________________________________
[predstavnik nadležnog tijela koje zahtijeva indirektni pristup TAHOnetu]
