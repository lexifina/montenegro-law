PRILOG 1
NAČIN IZRADE METAPODATAKA ZA SKUP PROSTORNIH PODATAKA I SERVISE PROSTORNIH PODATAKA
Prilikom izrade metapodataka za skup prostornih podataka i servise prostornih podataka određuje se:
1.1. naziv izvora koji treba da bude jedinstven, a polje vrijednosti ovog elementa metapodataka je slobodan tekst;
1.2. opisni rezime izvora, a polje vrijednosti ovog elementa metapodataka je slobodan tekst; 1.3. opis metapodataka, a polje vrijednosti ovog elementa metapodataka objašnjeno je u Prilogu 2 tačka 1 ovog pravilnika;
1.4. adresa izvora koja predstavlja vezu sa izvorom i/ili vezu sa dodatnim informacijama o izvoru podataka, a polje vrijednosti ovog elementa metapodataka je niz znakova - usklađeni lokator resursa (u daljem tekstu: URL);
1.5. jedinstveni identifikator izvora koji označava izvor podataka, a polje vrijednosti ovog elementa metapodataka je obavezna oznaka niza znakova koju obično dodjeljuje vlasnik podatka i prostor naziva niza znakova koji jedinstveno određuju kontekst identifikacijske oznake;
1.6. povezani izvori ako je izvor servisa prostornih podataka onaj element metapodataka koji određuje, kad je to primjenjivo, ciljani skup(ovi) prostornih podataka servisa kroz njihov URI, a polje vrijednosti ovog elementa metapodatka je obavezna oznaka niza znakova koju obično dodjeljuje vlasnik podataka i prostor naziva niza podataka koji jedinstveno označava kontekst identifikacijske oznake;
1.7. jezik izvora koji se upotrebljavaju u izvoru, a polje vrijednosti ovog elementa metapodatka ograničeno je na jezike određene u standardu MEST ISO 639-2;
2.1. kategorija oblasti koja predstavlja sistem klasifikacije na visokom nivou koji pomaže pri grupisanju i traženju raspoloživih izvora prostornih podataka na temelju oblasti, a polje vrijednosti ovog elementa metapodataka određeno je u Prilogu 2 tačka 2.
2.2. vrste servisa prostornih podataka kao pomoć prilikom traženja raspoloživih servisa prostornih podataka, poseban servis kategorizovan je u samo jednoj kategoriji, a polje vrijednosti ovog elementa metapodataka određeno je u Prilogu 2 tačka 3.
3.1. vrijednost ključne riječi koja se koristi za opisivanje subjekta i pomažu prilikom sužavanju pretraživanja cijelog teksta i omogućavaju strukturno traženje prema ključnoj riječi, a polje vrijednosti ovog elementa metapodataka je slobodan tekst.
3.2. izvorni kontrolisani rječnik se navodi ako vrijednost ključne riječi dolazi iz kontrolisanog rječnika (tezaurus, ontologija), na primjer GEMET, a navod bi trebalo da sadrži barem naslov i važne datume (datum izdavanja, datum poslednje promjene ili nastanka) izvornog kontrolisanog rječnika.
4.1. geografski granični okvir koji je izražen kao granični pravougaonik, a granični pravougaonik izražava se zapadnim i istočnim geografskim dužinama, sjevernim i južnim geografskim širinama u decimalama sa tačnošću od najmanje dvije decimale.
5. vremenska referenca koja se poziva na zahtjev o potrebi informacije o vremenskoj dimenziji podataka (vrijeme unošenja i važenja podataka; i način i vrijeme ažuriranja podataka), a navodi se najmanje jedan element metapodataka navedenih u tačkama od 5.1. do 5.4.
Polje vrijednosti elemenata metapodataka navedenih u tačkama od 5.1. do 5.4. je skup podataka. Svaki datum odnosi se na sistem vremenske reference i izražava se u obliku koji je usklađen sa tim sistemom. Zadati sistem odnosa je gregorijanski kalendar sa datumima koji se izražavaju u skladu sa standardom ISO 8601.
5.1. vremenski raspon koji određuje vremensko razdoblje sadržaja izvora, i može se izraziti kao nešto od dolje navedenog:
 pojedinačni datum;
 interval datuma izraženih početnim datumom i konačnim datumom razdoblja; ili
 kombinacijom pojedinačnih datuma i intervala datuma.
5.2. datum objavljivanja dostupnosti izvora ili datum od kada postaje validan, a može postojati nekoliko datuma objavljivanja.
5.3. datum posljednje promjene izvora, u slučaju da je izvor bio mijenjan i postoji samo jedan datum posljednje promjene.
5.4. datum nastanka i postoji samo jedan datum nastanka.
6.1. porijeklo sa podacima o istoriji postupka i/ili ukupnom kvalitetu skupova prostornih podataka, prema potrebi, mogu uključivati podatke o tome da li je skup podataka provjeren ili da li mu je osiguran kvalitet, radi li se o službenoj verziji (ako postoji nekoliko verzija), kao i ima li pravnu validnost, a polje vrijednosti ovog elementa metapodataka je slobodan tekst. 6.2. prostornu rezoluciju koja se odnosi na broj detalja skupa podataka. Izražava se kao skup "od nula do mnogo" rezolucijske udaljenosti (uobičajeno za rasterske podatke i proizvode koji su napravljeni na osnovu slika) ili u ekvivalentnim mjerilima (uobičajeno za karte ili proizvode bazirane na kartama), rezolucija se obično izražava kao cijela brojka koju izražava imenilac rezolucije, a rezolucijska udaljenost izražava se kao brojčana vrijednost povezana sa jedinicom dužine.
7.1. specifikacija navođenje pravila interoperabilnosti koja su sprovedena ili druge specifikacije sa kojom je određeni izvor kompatibilan.
Izvor može biti su skladu sa više sprovedenih pravila interoperabilnosti ili drugim specifikacijama.
Navedeno uključuje naslov i referentni datum (datum objavljivanja, datum poslednje izmjene ili nastanka) sprovedenog pravila interoperabilnosti ili drugom specifikacijom.
7.2. stepen usklađenosti izvora sa pravilima interoprabilnosti ili drugom specifikacijom, a polje vrijednosti ovog elementa metapodataka određeno je u Prilogu 2 tačka 5.
8.1. uslove za pristup i korišćenje kojim se određuju uslovi za pristup i korišćenje skupova prostornih podataka i servisa, i visinu naknade za pristup i korišćenje, a polje vrijednosti ovog elementa metapodataka je slobodan tekst.
Ako za pristup i upotrebu izvora nema uslova, upotrebljava se unos "ne primjenjuju se uslovi". Ako su uslovi nepoznati, upotrebljava se unos "uslovi nisu poznati". Ovaj element takođe pruža informacije o svim naknadama koje su potrebne za pristup i upotrebu izvora, ako je primjenjivo, ili se odnose na URL gdje su raspoložive informacije o naknadama.
8.2. ograničenja javnog pristupa kada je ograničen javni pristup skupovima i servisima prostornih podataka, ovaj element metapodataka pruža informacije o ograničenjima i razlozima istih. Ako ne postoje ograničenja javnog pristupa, taj element metapodataka to i pokazuje, a polje vrijednosti ovog elementa metapodataka je slobodan tekst.
9.1. odgovorna strana sa opisom za uspostavljanje, upravljanje, održavanje i distribuciju izvora.
Taj opis uključuje:
- naziv javne institucije kao slobodan tekst; i - adresu elektronske pošte za kontakt kao niz znakova.
9.2. uloga odgovorne strane, a polje vrijednosti ovog elementa metapodataka određeno je u Prilogu 2 tačka 6.
10.1. podaci za kontakt metapodataka sa opisom javne institucije koja je odgovorna za stvaranje i održavanje metapodataka.
Taj opis uključuje:
- naziv javne institucije kao slobodan tekst, - adresu elektronske pošte za kontakt kao niz znakova.
10.2. datum metapodataka koji određuje kada je zapis metapodataka nastao ili bio obnovljen, a taj datum se izražava u skladu sa standardom ISO 8601.
10.3. jezik metapodatka na kojem su izraženi elementi metapodataka, a polje vrijednosti ovog elementa metapodataka ograničeno je na crnogorski jezik u skladu sa normom MEST ISO 639-2.
PRILOG 2
ELEMENTI METAPODATAKA
Metapodaci koji opisuju izvor sadrže, elemente metapodataka ili grupe elemenata metapodataka navedene u Tabeli 1, a vezano za zbirke skupova prostornih podataka, elemente metapodataka ili grupe elemenata metapodataka navedene u Tabeli 2.
Elementi metapodataka ili grupe elemenata metapodataka u skladu su sa očekivanom višestrukosti povezanim uslovima predstavljenim u Tabelama 1 i 2.
U slučaju da nema uslova povezanih sa nekim određenim elementom metapodatka taj je element obavezan.
Tabele sadrže sljedeće podatke:
-Prva kolona poziva se na Prilog 2 koji definše element metapodatka ili grupu elemenata
metapodataka;
- Druga kolona sadrži naziv elementa metapodatka ili grupu elemenata metapodatka;
-Treća kolona određuje raznovrsnost elementa metapodatka. Izražavanje višestrukosti
jednako je zapisu za raznovrstnost na objedinjenom jeziku za modelovanje (UML) u kojem:
- 1 znači da postoji samo jedan primjerak ovog elementa metapodataka u nizu rezultata;
- 1..* znači da postoji najmanje jedan primjerak ovog elementa u nizu rezultata;
-0..1 znači da je prisutnost elementa metapodatka u nizu rezultata uslovna, ali se može
pojaviti samo jednom;
-0..* znači da je prisutnost elementa metapodatka u nizu rezultata uslovna ali da se
element metapodatka može pojaviti jednom ili više puta;
- kada je višestrukost 0..1 ili 0..*, uslov određuje kada je element metapodataka obavezan; i -ako se brojnost elemenata ne odnosi na sve vrste izvora, četvrta kolona sadrži uslovnu
izjavu. Svi su elementi obavezni u drugim okolnostima.
Tabela 1.
Metapodaci za zbirke prostornih podataka i skupovi zbirki prostornih podataka
Upućiva
nje
Element metapodatka Višestruk
ost
Uslov
1.1
Naziv izvora
1 1.2
Rezime izvora
1 1.3
Vrsta izvora
1 1.4
Adresa izvora
0..*
Obavezan ako je URL dostupan za dobijanje
više informacija o izvoru i/ili servisama
vezanim za pristup 1.5
Jedinstveni identifikator
izvora
1..*
1.7
Jezik izvora
0..*
Obavezan ako izvor sadrži tekstualne
informacije.
2.1
Kategorija oblasti
1..* 3
Ključna riječ
1..* 4.1
Geografski granični okvir 1..* 5
Vremenska referenca
1..* 6.1
Porijeklo
1 6.2
Prostorna rezolucija
0..*
Obavezna za skupove podataka i zbirke
skupova podataka ako se može odrediti
ekvivalentni razmjer ili rezolucijska
udaljenost.
7
Usklađenost
1..* 8.1
Uslovi za pristup i
korišćenje
1..*
8.2
Ograničenja javnog
pristupa
1..*
9
Odgovorna strana
1..* 10.1
Podaci za kontakt
metapodataka
1..*
10.2
Datum metapodataka
1 10.3
Jezik metapodataka
1
Tabela 2
Metapodaci za servise prostornih podataka
Upućiva
nje
Element metapodataka Višestruko
st
Uslov
1.1.
Naziv izvora
1 1.2.
Rezime izvora
1 1.3.
Vrsta izvora
1 1.4.
Adresa izvora
0..*
Obavezna ako je dostupna povezanost sa
servisom.
1.6.
Povezani izvor
0..*
Obavezan ako je dostupna veza sa skupom
podataka na kojoj funkcioniše servis.
2.2.
Vrste servisa povezane sa
prostornim podacima
1
3.
Ključna riječ
1..* 4.1.
Geografski granični okvir 0…*
Obavezan je za servise sa izričitim
geografskim opsegom.
5.
Vremenska referenca
1..* 6.2.
Prostorna rezolucija
0..*
Obavezna je ako postoje ograničenja u okviru
prostorne rezolucije za ovaj servis.
7.
Usklađenost
1..* 8.1.
Uslovi za pristup i
korišćenje
1..*
8.2.
Ograničenja javnog
pristupa
1..*
9.
Odgovorna strana
1..* 10.1.
Podaci za kontakt
metapodatka
1..*
10.2.
Datum metapodatka
1 10.3.
Jezik metapodatka
1
POLJA VRIJEDNOSTI Kada je to određeno u opisima elemenata metapodataka u Prilogu 1, polja vrijednosti opisana u tačkama 1 do 6 koriste višestrukosti koje su navedene u Tabelama 1 i 2 ovog priloga.
Obzirom na određeno polje vrijednosti, svaka je vrijednost određena sa:
 numeričkom oznakom,
 tekstualnim nazivom na crnogorskom jeziku,
 jezički neutralnim nazivom za kompjutere (vrijednost izražena između zagrada),
 izbornim opisom ili definicijom.
1. VRSTA IZVORA 1.1. Zbirka skupova prostornih podataka (series) 1.2. Skup prostornih podataka (dataset) 1.3. Servis prostornih podataka (service).
2. KATEGORIJE OBLASTI U SKLADU SA STANDARDOM EN ISO 19115 2.1. Poljoprivreda (farming) Uzgoj životinja i/ili biljaka.
Ova kategorija odnosi se na oblast prostornih podataka: objekti poljoprivrede i akvakulture. Objekti i mašine za poljoprivredu i akvakulturu.
2.2. Biota (biota) Flora i/ili fauna u prirodnoj sredini.
Ova kategorija odnosi se na oblasti prostornih podataka: bio-geografske regione, staništa i biotope i geografske razmještaje biljnih i životinjskih vrsta.
2.3. Granice (boundaries) Pravni status i opisi područja.
Ova kategorija odnosi se na oblasti prostornih podataka: administrativne jedinice i statističke jedinice.
2.4. Klimatologija/meteorologija/atmosfera (climatology/Meteorology/Atmosphere) Procesi i pojave u atmosferi.
Ova se kategorija odnosi se na oblasti prostornih podataka: atmosferski uslovi i meteorološko-geografske karakteristike.
2.5. Ekonimija (economy) Ekonomske djelatnosti, uslovi i zapošljavanje.
Ova kategorija odnosi se na oblasti prostornih podataka: izvori energije i mineralne sirovine. 2.6. Nadmorska visina (elevation) Visina iznad nivoa mora ili dubina ispod nivoa mora.
Ova kategorija odnosi se na oblast prostornih podataka: digitalni modeli visine za kopno i vodenu površinu.
2.7. Životna sredina (environment) Izvori, zaštita i očuvanje životne sredine.
Ova kategorija odnosi se na oblast prostornih podataka: područja koja su proglašena zonama zaštite ili kojima se upravlja u skladu sa posebnim propisima.
2.8. Geološke informacije (geoscientific/Information) Informacije koje se odnose o nauci o Zemlji.
Ova kategorija odnosi se na oblast prostornih podataka: zemljište, geologija i područja sa rizikom od prirodnih katastrofa.
2.9. Zdravlje (health) Zdravlje, zdravstveni usluge, socijalna ekologija i sigurnost.
Ova kategorija odnosi se na oblast prostornih podataka: zdravlje ljudi i bezbjednost.
2.10. Slikovni prikazi/Osnovne karte/Zemljišni pokrivač (imagery/BaseMaps/EarthCover) Osnovne karte.
Ova kategorija odnosi se na oblast prostornih podataka: fotografski podaci zemljine površine, dobijeni putem satelitskih ili snimanja iz vazduha (ortofoto) i zemljišni pokrivač.
2.11. Obavještajna služba/Vojska (intelligence/Military) Vojne baze, zgrade, aktivnosti.
Ova kategorija se ne odnosi na određenu oblast prostornih podataka.
2.12. Kopnene vode (inland/Waters) Obilježja kopnenih voda, sistemi za odvodnjavanje i njihova obilježja.
Ova kategorija odnosi se na oblast prostornih podataka: hidrografija.
2.13. Položaj (location) Lokacijske informacije i servisi.
Ova kategorija odnosi se na oblast prostornih podataka: geografski nazivi i adresa lokacija nepokretnosti.
2.14. Okeani (oceans) Obilježja i karakteristike slanih voda (osim voda u unutrašnjosti).
Ova kategorija odnosi se na oblast prostornih podataka: okeanografsko-geografske karakteristike i morska područja.
2.15. Planiranje/katastar (planning/Cadastre) Informacije koje se koriste za prikladne radnje za upotrebu zemljišta u budućnosti.
Ova kategorija odnosi se na oblast prostornih podataka: katastarske parcele; namjenu površina i zaštićena područja u skladu sa zakonom i zaštićena nepokretna kulturna dobra. 2.16. Društvo (society) Obilježja društva i kulture.
Ova kategorija odnosi se na oblast prostornih podataka: razmještaj stanovništva - demografija.
2.17. Zgrade (structure) Objekti koje je napravio čovjek.
Ova kategorija odnosi se na oblasti prostornih podataka: lokacije objekata, proizvodna i industrijska postrojenja i lokacije za monitoring životne sredine.
2.18. Prevozna sredstva (transportation) Sredstva i pomoć za prevoz ljudi i/ili robe.
Ova kategorija odnosi se na oblast prostornih podataka: saobraćajne mreže koje obuhvataju saobraćajne, željezničke, vazdušne i vodene saobraćajne mreže, elektronske komunikacione mreže i prateću infrastrukturu.
2.19. Komunalne servisi/Komunikacije (utilities/Communication) Energetski, vodovodni i otpadni sistemi i komunikacijska infrastruktura i servisi.
Ova kategorija odnosi se na oblast prostornih podataka: komunalni i drugi servisi od javnog interesa.
3. VRSTE SERVISA PROSTORNIH PODATAKA 3.1. Servisi traženja (discovery) Servisi koje omogućavaju traženje skupova prostornih podataka i servisa prostornih podataka na osnovu sadržaja odgovarajućeg metapodatka kao i prikazivanje sadržaja metapodatka. 3.2. Servisi pregleda (view) Servisi koji omogućavaju, barem, prikazivanje, navigaciju, povećavanje i smanjivanje, panoramski pregled ili prekrivanje vidljivih grupa prostornih podataka kao i prikazivanje informacije iz legende i sve vezane sadržaje metapodatka.
3.3. Servisi prenosa (download) Servisi koji omogućavaju umnožavanje i prenos skupova prostornih podataka ili djelova takvih skupova kada je moguć neposredni pristup podacima.
3.4. Servisi preoblikovanja (transformation) Servisi koji omogućavaju da se zbirke prostornih podataka preoblikuju s namjerom postizanja interoperabilnosti.
3.5. Servisi pozivanja prostornih podataka (invoke) Servisi koji omogućavaju definisanje ulaznih i izlaznih podataka koje očekuje servis vezan za prostor i tok rada ili lanac servisa koji kombinuje raznovrsne servise. Takođe omogućava određivanje interfejsa spoljne mrežne servisa toka rada ili lanca servisa.
3.6. Drugi servisi (other) 4. KLASIFIKACIJA SERVISA PROSTORNIH PODATAKA Ključne riječi temelje se na taksonomiji geografskih servisa iz standarda EN ISO 19119. Ova taksonomija podijeljena je u kategorije, podkategorije koje određuju vrijednosti domena klasifikacije servisa prostornih podataka.
100 Geografski servisi ljudskih interakcija (humanInteractionService) Ova kategorija uključuje sledeće podkategorije:
101 Pregledač kataloga (humanCatalogueViewer)
Servis za korisnika koji mu omogućava interakciju sa katalogom kako bi pronašao, listao i
upravljao metapodacima o geografskim podacima ili geografskim servisima.
102 Geografski pregledač (humanGeographicViewer)
Servis za korisnika koji mu omogućava uvid u jednu ili više zbirki oznaka ili slojeva.
103 Geografski pregledač aritmetičkih tabela (humanGeographicSpreadsheetViewer)
Servis za korisnika koji mu omogućava interakciju sa raznovrsnim servisima
informaconih tehnologija kao i da zatraži proračune slične aritmetičkim računskim
tabelama, ali proširene geografskim podacima.
104 Urednik servisa (humanServiceEditor)
Servis za korisnika koji mu omogućava kontrolu geografskih procesnih servisa.
105 Urednik lančane definicije (humanChainDefinitionEditor)
Omogućava korisniku interakciju sa servisom lančanog određivanja.
106 Proces menadžer (humanWorkflowEnactmentManager)
Omogućava korisniku interakciju sa servisom odredbi toka rada.
107 Urednik geografskih obilježja (humanGeographicFeatureEditor)
Geografski pregledač koji korisniku omogućava interakciju sa podacima o obilježjima.
108 Urednik geografskih simbola (humanGeographicSymbolEditor)
Servis za korisnika koji mu omogućava odabir i upravljanje katalogom simbola.
109 Urednik generalizacije obilježja (humanFeatureGeneralizationEditor)
Servis za korisnika koji mu omogućava mijenjanje kartografske karakteristike oznake ili
arhiva oznaka tako da pojednostavi njihovu vizuelizaciju ali održava njihove značajne
elemente - prostorni ekvivalent pojednostavljenja.
110 Preglednik geografskih struktura podataka(humanGeographicDataStructureViewer)
Servis za korisnika koji mu omogućava pristup djelovima skupa podataka kako bi dobio
uvid u njegovu unutrašnju strukturu.
200 Servis upravljanja geografskim modelom/informacijom (infoManagementService) Ova kategorija sastoji se od sljedećih potkategorija:
201 Servis pristupa obilježja (infoFeatureAccessService)
Servis koji korisniku omogućava pristup i upravljanje memorijom obilježja.
202 Servis pristupa karti (infoMapAccessService)
Servis koji korisniku omogućava pristup geografskim grafikama, tj. slikama geografskih
podataka.
203 Servis pristupa slojevima (infoCoverageAccessService)
Servis koji korisniku omogućava pristup i upravljanje memorijom slojeva.
204 Servis opisa senzora (infoSensorDescriptionService)
Servis koji korisniku omogućava opis senzora za niz podataka, uključujući lokaciju i
orijentaciju senzora kao i geometričke, dinamičke i radiometričke karakteristike senzora
za namjenu geoprocesuiranja.
205 Servis pristupa proizvodu (infoProductAccessService)
Servis koji korisniku omogućava pristup i upravljanje memorijom geografskih proizvoda. 206 Servis vrste obilježja (infoFeatureTypeService)
Servis koji korisniku omogućava pristup i upravljanje arhivom definicija vrsta obilježja.
207 Servis kataloga (infoCatalogueService)
Servis koji korisniku omogućava traženje i upravljanje servisama arhiviranja
metapodataka.
208 Servis registra (infoRegistryService)
Servis koji korisniku omogućava pristup skladištu metapodataka o tipovima.
209 Servis geografskog leksikona (infoGazetteerService)
Servis koji korisniku omogućava pristup zbirci primjera jednog ili više razreda stvarnih
fenomena koji sadrže neke informacije vezane za položaj.
210 Servis upravljanja narudžbama (infoOrderHandlingService)
Servis koja korisniku omogućava naručivanje proizvoda od ponuđača.
211 Servis trajnih narudžbi (infoStandingOrderService)
Servis upravljanja narudžbama koja omogućava korisniku da zatraži da proizvod na
geografskom području bude raspoređen čim postane dostupan.
300 Servis upravljanja geografskim tokom rada zadatka (taskManagementService) Ova kategorija uključuje sledeće podkategorije:
301 Servis lančanog određivanja (chainDefinitionService)
Servis lančanog određivanja i mogućnost da se izvede servisom odredbi toka rada.
302 Servis odredbi toka rada (workflowEnactmentService)
Servis odredbi toka rada objašnjava lanac i nadzire ubrzavanje servisa i aktivnosti
dijeljenja.
303 Servis naručivanja (subscriptionService)
Servis koji omogućava korisniku da se registruje i dobije obaveštenje o događajima.
400 Servis geografske obrade - prostorne (spatialProcessingService) Ova kategorija uključuje sledeće podkategorije:
401 Servis preračuna koordinata (spatialCoordinateConversionService)
Servis za promjenu koordinata iz jednog sistema koordinata u drugi koji je povezan sa
istim podatkom.
402 Servis mijenjanja koordinate (spatialCoordinateTransformationService)
Servis za promjenu koordinata iz koordinatnog referentnog sistema koji se temelji na
jednom podatku u koordinatni referentni sistem koji se temelji na drugom podatku.
403 Servis promjene pokrivenosti/vektora (spatialCoverageVectorConversionService)
Servis za promjenu prostornog prikaza iz šeme prekrivanja/pokrivenosti u šemu vektora
ili obratno.
404 Servis promjene koordinata prikaza (spatialImageCoordinateConversionService)
Preračun koordinata ili servisa preračuna koordinata za promjenu sistema odnosa
koordinata za neki prikaz.
405 Servis ispravljanja (spatialRectificationService)
Servis za pretvaranje slike u okomito paralelnu projekciju i konstantnu ljestvicu
406 Servis orto-ispravljanja (spatialOrthorectificationService)
Servis ispravljanja koja odstranjuje nagib i pomjeranja slike zbog nagiba terena.
407 Servis namještanja senzorskog geometrijskog modela (spatial Sensor Geometry Model
Adjustment Service)
Servis koji namješta senzorske geometrijske modele kako bi se poboljšalo slaganje slike sa
drugim slikama i/ili poznatim položajima terena.
408 Servis pretvaranja fotografskog geometrijskog modela (spatial Image Geometry Model
Conversion Service)
Servis koji pretvara senzorske geometrijske modele u različit, ali ravnopravan senzorski
geometrijski model.
409 Servis klasifikovanja (spatialSubsettingService)
Servis koji izvlači podatke iz unosa u stalno prostorno područje ili pomoću geografskog
položaja ili mrežnih koordinata.
410 Servis analize uzorka (spatialSamplingService)
Servis koji izvlači podatke iz unosa koristeći plan stalne analize uzorka ili pomoću
geografskih položaja ili mrežnih koordinata.
411 Servis promjene pokrivača (spatialTilingChangeService)
Servis koji mijenja pokrivenost geografskih podataka.
412 Servis mjerenja dimenzija (spatialDimensionMeasurementService)
Servis računanja dimenzija objekata prikazanih kao slika ili kao drugi metapodatak.
413 Servis manipulacije obilježja (spatialFeatureManipulationService)
Upisuje jedno obilježje drugoj slici ili drugom skupu podataka ili skupu koordinata
ispravljajući relativne promjene prevoda, rotacione razlike, razlike razmjera i razlike
perspektive. Provjerava jesu li sva obilježja u skupu podataka topološki dosljedna u
skladu sa topološkim pravilima i prepoznaje i/ili ispravlja uočene nedosljednosti.
414 Servis spajanja obilježja (spatialFeatureMatchingService)
Servis koja određuje koja obilježja i dijelovi obilježja predstavljaju istu jedinicu stvarnog
svijeta iz raznovrsnih izvora podatka, na primjer, povezivanje ivica i ograničena spajanja u
jedno.
415 Servis generalizovanja obilježja (spatialFeatureGeneralizationService)
Servis koja smanjuje prostornu varijaciju obilježja kako bi povećala efikasnost komunikacije
pomoću suprotstavljanja neželjenih učinaka smanjenja podataka.
416 Servis određivanja smjera (spatialRouteDeterminationService)
Servis kojom se određuje optimalni put između dvije određene tačke na temelju unešenih
parametara i svojstava koja se nalaze u katalogu obilježja.
417 Servis pozicioniranja (spatialPositioningService)
Servis koji pruža uređaj za geolokaciju kako bi se upotrijebila, dobila i jednosmisleno
interpretirala informacija o položaju kako bi se utvrdilo da li rezultati zadovoljavaju
zahtjeve upotrebe.
418 Servis analize blizine (spatialProximityAnalysisService)
Uz dati položaj ili geografsko obilježje, pronalazi sve objekte sa datim skupom atributa
koji su smješteni unutar udaljenosti položaja ili obilježja koja je odredio korisnik.
500 Servis geografske obrade - tematske (thematicProcessingService) Ova kategorija sastoji se od sledećih podkategorija:
501 Servis izračuna geo-parametra (thematicGoparameterCalculationService)
Servis koja izvodi kvantitativne rezultate, orijentisane na aplikaciju, koji nisu dostupni iz
samih sirovih podataka.
502 Servis tematske klasifikacije (thematicClassificationService)
Servis za klasifikovanje regija geografskih podataka koji se temelje na tematskim
atributima.
503 Servis generalizacije obilježja (thematicFeatureGeneralizationService)
Servis koji generalizuje vrste obilježja u zbirku obilježja kako bi povećala efikasnost
komunikacije suprotstavljanju neželjenih posljedica smanjenja podataka.
504 Servis pod-određivanja (thematicSubsettingService)
Servis koji izvlači podatke iz unosa koji se temelje na vrijednostima parametra.
505 Servis prostornog brojanja (thematicSpatialCountingService)
Servis koja broji geografska obilježja.
506 Servis pronalaženja promjene (thematicChangeDetectionService)
Servis za pronalaženje razlika između dvije zbirke podataka koje predstavljaju ista
geografska područja u različitim vremenima.
507 Servis izvlačenja geografskih informacija (thematic Geographic Information Extraction
Service)
Servis koji podržava izvlačenje obilježja i informacija o terenu iz primljenih i skeniranih
slika.
508 Servis obrade slika (thematicImageProcessingService)
Servis za promjenu vrijednosti tematskih atributa slike koristeći matematičku funkciju.
509 Servis generisanja smanjena rezolucije (thematicReducedResolutionGenerationService)
Servis koja smanjuje rezoluciju slike.
510 Servis manipulacije slikama (thematicImageManipulationService)
Servis za manipulisanje vrijednostima podataka u slikama: mijenjanje boje i vrijednosti
kontrasta: primjenjivanje različitih filtera, manipulisanje rezolucijom slike, oduzimanje
zvuka, segmentacija, sistemsko-radiometriske ispravke, atmosfersko oslabljivanje,
promjene u osvjetljavanju prikaza i tako dalje.
511 Servis razumijevanja slike (thematicImageUnderstandingService)
Servis koji pruža određivanje razlike automatizovane slike, razlikovanje zabilježene slike,
analiza i prikaz značenja razlike i razlikovanje na temelju područja i modela.
512 Servis sinteze slike (thematicImageSynthesisService)
Servis za stvaranje ili pretvaranje slika korišćenjem kompjuterski utemeljenih
vremenskih modela, izmjenom perspektive i manipulacijom obilježja slike za poboljšanje
vidljivosti, rezolucije oštrine i/ili smanjenja učinka zatamnjenja ili magle.
513 Manipulacija talasnih dužina snimka (thematicMultibandImageManipulationService)
Servis koji mijenja snimak promjenom talasnih dužina snimka 514 Servis određivanja objekta (thematicObjectDetectionService)
Servis za određivanje objekta iz stvarnog svijeta na slici.
515 Servis geoanalize (thematicGeoparsingService)
Servis za skeniranje tekstualnih dokumenata za odnose utemeljene na lokaciji, poput
naziva mjesta, adresa, poštanskih brojeva i tako dalje, u pripremi za prelazak na uslugu
geoanalize.
516 Servis geokodiranje (thematicGeocodingService)
Servis za povećanje tekstualnih referenci koje su zasnovane na lokaciji sa geografskim
koordinatama (ili nekom drugom prostornom referencom).
600 Servis geografske obrade - vremenske (temporalProcessingService) Ova kategorija sadrži sljedeće podkategorije:
601 Servis proračuna sistema vremenskih referenci
(temporalReferenceSystemTransformationService)
Servis za promjenu vrijednosti vremenskih primjera iz jednog vremenski referentnog
sistema u drugi vremenski referentni sistem.
602 Servis pod-klasifikovanja (temporalSubsettingService)
Servis koji izvlači podatke iz unosa u stalnom vremenskom intervalu zasnovanim na
vrijednosti intervala.
603 Servis analize na osnovu uzorka(temporalSamplingService)
Servis koji izvlači podatke iz unosa korišćenjem dosljedne šeme analize na osnovu uzorka
zasnovane na vrijednostima vremenskih intervala.
604 Servis analize vremenske aproksimacije (temporalProximityAnalysisService)
Sa datim vremenskim intervalom ili događajem, pronalazi sve objekte sa datim atributima
koji su smješteni unutar intervala kojeg određuje korisnik iz intervala ili događaja.
700 Servis geografske obrade metapodatka (metadataProcessingService) Ova kategorija sadrži sljedeće podkategorije:
701 Servis statističkog proračuna metapoda (metadataStatisticalCalculationService)
Servis za izračunavanje statistike skupa podataka.
702 Servis geografskog obilježavanja (metadataGeographicAnnotationService)
Servis za dodavanje dodatnih informacija slici ili obilježja u zbirci obilježja.
800 Servis geografske komunikacije (comService) Ova kategorija sadrži sledeće podkategorije:
801 Servis kodiranja (comEncodingService)
Servis koji pruža sprovođenje kodiranog pravila i pruža sisoblasti za kodiranje i
dekodiranje funkcionalnosti.
802 Servis prenosa (comTransferService)
Servis koji omogućava sprovođenje jednog ili više protokola prenosa koji omogućavaju
prenos podataka između podjeljenih sistema informacija putem povezanih ili
nepovezanih komunikacijskih medija.
803 Geografski servis smanjivanja (comGeographicCompressionService)
Servis koji pretvara prostorne djelove skupa obilježja u komprimovani oblik.
804 Geografski servis konverzije formata (comGeographicFormatConversionService)
Servis koji pretvara iz jednog geografskog formata podataka u drugi.
805 Servis slanja poruka (comMessagingService)
Servis koji omogućava da nekoliko korisnika istovremeno gledaju, komentarišu i traže
izmjene zbirke obilježja.
806 Odvojena datoteka i upravljanje (comRemoteFileAndExecutableManagement)
Servis koji omogućava pristup sekundarnim memorijama geografskih obilježja kako bi bili
lokalno dostupni korisniku.
5. STEPEN USKLAĐENOSTI 5.1. Usklađeno (conformant) Izvor je potpuno usklađen sa navedenim specifikacijama.
5.2. Nije usklađeno (notConformant) Izvor nije usklađen sa navedenim specifikacijama.
5.3. Nije ocijenjeno (notEvaluated) Usklađenost nije ocijenjena.
6. ULOGA JAVNE INSTITUCIJE 6.1. Davalac izvora (resourceProvider) Javna institucija koja obezbjeđuje izvor podataka.
6.2. Čuvar (custodian) Javna institucija koja preuzima odgovornost za podatke i osigurava održavanje i upravljanje izvorom podataka.
6.3. Vlasnik (owner) Javna institucija koja je vlasnik izvora podataka.
6.4. Korisnik (user) Korisnik izvora podataka.
6.5. Distributer (distributor) Javna institucija koja vrši distribuciju izvora podataka.
6.6. Začetnik (originator) Javna institucija koja je stvorila izvor podataka.
6.7. Kontak (pointOfContact) Javna institucija koja se može kontaktirati kako bi se saznalo više o izvoru podataka ili njegovom preuzimanju.
6.8. Glavni istraživač (principalInvestigator) Ključna javna institucija odgovorna za sakupljanje informacija i sprovođenje istraživanja. 6.9. Prerađivač (processor) Javna institucija koja je obradila podatke na taj način da je izvor izmijenjen.
6.10. Izdavač (publisher) Strana koja je objavila izvor.
6.11. Autor (author) Javna institucijatucija koja je autor izvora.
