PRILOG 1
SMJERNICE O ELEKTRONSKOJ KOMUNIKACIONOJ INFRASTRUKTURI,
POVEZANOJ OPREMI I ELEMENTIMA MREŽE
Sadržaj:
1.
Uvod ................................................................................................................................. 23
2.
Sadržaj Smjernica ............................................................................................................. 24
2.1.
Definicije ....................................................................................................................... 24
2.2.
Izvori podataka i period prikupljanja podataka ....................................................... 25
2.3.
Geografska prostorna rezolucija podataka ................................................................ 26
2.4.
Format podataka .......................................................................................................... 27
2.5.
Elementi elektronske komunikacione infrastrukture, povezane opreme ............... 28
2.6.
Elementi mreže ............................................................................................................. 28
2.7.
Kategorizacija prikupljenih podataka u Geoportalu Agencije ................................. 29
2.8.
Specifikacija planova ................................................................................................... 32
2.9.
Objavljivanje, pitanja povjerljivosti i agregacije podataka kako bi se pružile
informacije trećim stranama .................................................................................................. 33
3.
Obaveze korisnika ........................................................................................................... 34
ANEKSI ................................................................................................................................... 35
1.
Aneks - Evaluacija jedinica prostorne rezolucije .......................................................... 35
2.
Aneks - Struktura i format atributnih podataka .......................................................... 35
2.1.
Struktura i format atributnih podataka o elektronskoj komunikacionoj
infrastrukturi, povezanoj opremi ...................................................................................... 35
2.2.
Struktura i format atributnih podataka o elementima mreže ............................... 42
2.3.
Struktura i format relacija izmedju features klasa ................................................. 50
3.
Aneks - Format i tip podataka ........................................................................................ 53
3.1.
Vektorski model ....................................................................................................... 53
3.2.
Rasterski model ........................................................................................................ 54
3.3.
Tabelarni podaci ....................................................................................................... 54
4.
Aneks - Projektovani koordinatni sistem ...................................................................... 54 1. Uvod
Sistem za mapiranje elektronske komunikacione infrastrukture, povezane opreme i elemenata mreže (u daljem tekstu: Geoportal Agencije) se zasniva na podacima koje operatori dostavljaju Agenciji, shodno Zakonu o elektronskim komunikacijama i Pravilniku o sadržaju, načinu dostavljanja i objavljivanja podataka o vrsti, raspoloživosti i geografskoj lokaciji postojeće i planirane elektronske komunikacione infrastrukture i povezane opreme i elemenata mreže.
Smjernice o elektronskoj komunikacionoj infrastrukturi, povezanoj opremi i elementima mreže (u daljem tekstu: Smjernice) propisuju format, sadržaj i način dostavljanja podataka u Geoportal, kao i obaveze operatora u vezi sa unosom i ažuriranjem podataka. Ove Smjernice su sastavni dio Pravilnika o sadržaju, načinu dostavljanja i objavljivanja podataka o vrsti, raspoloživosti i geografskoj lokaciji postojeće i planirane elektronske komunikacione infrastrukture i povezane opreme i elemenata mreže.
Cilj Smjernica je da se osigura standardizovan i ažuran Geoportal koji će služiti za:
-
Precizno mapiranje elektronske komunikacione infrastrukture, povezane opreme i
elemenata mreže kao i praćenje njenog razvoja,
-
Efikasno planiranje razvoja elektronskih komunikacionih mreža,
-
Podršku operatorima, investitorima i institucijama u donošenju strateških odluka,
-
Integraciju sa drugim relevantnim državnim servisima.
2. Sadržaj Smjernica
U ovoj tački opisani su elementi Smjernica o elektronskoj komunikacionoj infrastrukturi, povezanoj opremi i elementima mreže koji treba da obezbijede geografsko mapiranje podataka o postojećoj i planiranoj elektronskoj komunikacionoj infrastrukturi, povezanoj opremi i elementima mreže, a posebno sljedeće:
-
Izvori podataka i period prikupljanja podataka;
-
Geografska prostorna rezolucija podataka;
-
Elementi elektronske komunikacione infrastrukture, povezane opreme;
-
Elementi mreže;
-
Podaci i karakterizacija GIS sistema;
-
Specifikacija planova;
-
Objavljivanje, pitanja povjerljivosti i agregacije podataka kako bi se pružile
informacije trećim stranama.
2.1.
Definicije
Pojedini pojmovi iz ovih Smjernica imaju sledeće značenje:
Geografski informacioni sistem (GIS): sistem hardvera, softvera i procedura za jednostavnije
upravljanja,
manipulaciju,
analizu,
modeliranje
i
prikazivanje georeferenciranih podataka za rešavanje kompleksnih problema u pogledu planiranja i upravljanja resursima;
Prostorna rezolucija: izražava veličinu najmanjeg objekta u skupu prostornih podataka koji može biti opisan. Odnosi se na količinu detalja koja se može razaznati. Takođe je poznata kao granularnost;
Trasa telekomunikacione kablovske kanalizacije: projektovani ili već izgrađen pravac i geodetski pozicionirana linija telekomunikacione kablovske kanalizacije unutar koridora telekomunikacione kablovske kanalizacije;
Telekomunikaciona
kablovska
kanalizacija:
vrsta
elektronske
komunikacione infrastrukture koji se sastoji od mreže podzemnih cijevi od pogodnog materijala, telekomunikacionih kablovskih okana i telekomunikacionih kablovskih galerija, koja služi za postavljanje i zaštitu telekomunikacionih kablova;
Telekomunikaciona cijev: cijev izrađena od polivinil hlorida, polietilena, betona ili gvožđa i drugih materijala koja služi za postavljanje i zaštitu telekomunikacionih kablova;
Telekomunikacioni kabl: elemenat mreže koji predstavlja fizički medijum dizajniran za prenos podataka, signala ili informacija u telekomunikacionim sistemima. Sastoji se od provodnika i/ili talasovoda (kao što su bakarne žice ili optička vlakna) koji su zaštićeni izolacionim slojevima, a često i dodatnim omotačem kako bi se osigurala zaštita od spoljnih
uticaja
poput
vlage,
elektromagnetnih
smetnji
ili
fizičkih
oštećenja. Telekomunikacioni kablovi se koriste za povezivanje uređaja i mreža, omogućavajući prenos glasovnih, video ili podatkovnih signala;
Telekomunikaciono kablovsko okno: podzemna prostorija višestruke namjene koje se postavljaju na mjestima nastavljanja, ukrštanja i promjene smjerova telekomunikacione kablovske kanalizacije, kao i ispred pristupnih čvorova i drugih objekata u kojima je smještena oprema elektronskih komunikacionih mreža;
Telekomunikacioni završetak: elemenat mreže koji predstavlja tačku na kojoj se krajnjem korisniku omogućava pristup javnoj elektronskoj komunikacionoj mreži;
Telekomunikacioni
i
drugi
stubovi:
su
elementi
elektronske
komunikacione infrastrukture ili fizičke infrastrukture i služe kao nosači nadzemnih telekomunikacionih kablova;
Antenski stub: građevinska konstrukcija, obično izrađena od metala ili betona, koji služi za montažu antena i drugih uređaja za bežičnu komunikaciju;
Zgrade/objekti za smještaj telekomunikacione opreme: predstavljaju objekte u kojima se nalazi telekomunikaciona oprema i sa njom pripadajuća oprema;
Pristupni čvor: je elemenat mreže koji predstavlja aktivnu opremu na koju se povezuje oprema krajnjeg korisnika (CPE), ponekad nazvana prva tačka koncentracije. Iako se pristupni čvorovi razlikuju u zavisnosti od postojećih mrežnih arhitektura, oni uvijek formiraju "granicu" između segmenta distribucije ("backhaul") i segmenta pristupa ("lokalna petlja", "poslednja milja"). Primjeri pristupnih čvorova su: DSLAM/MSAN za DSL, CMTS za DOCSIS ili OLT za FTTH.
2.2.
Izvori podataka i period prikupljanja podataka
Operatori elektronskih komunikacija, kao vlasnici postojeće elektronske komunikacione infrastrukture, povezane opreme i elemenata mreže, obavezni su da redovno dostavljaju i ažuriraju podatke u skladu sa članom 26 Zakona o elektronskim komunikacijama i sljedećim smjernicama:
-
Rok ažuriranja: Najkasnije 30 dana nakon promjene stanja na terenu;
-
Validacija podataka: Prije unosa, podaci prolaze kroz proces provjere kako bi se
osigurala tačnost i usklađenost sa propisanim standardima. Ukoliko validacija
podataka prođe uspješno podaci se mogu unijeti/izmjeniti/obrisati, u suprotnom
podatke je potrebno ispraviti u skladu sa izvještajem koje operatori dobiju iz
sistema. Alat za validaciju podataka je dostupan i prilikom pojedinačnog i prilikom
grupnog unosa podataka;
-
Dostavljanje podataka: Putem Geoportala Agencije pojedinačno ili grupno. Detaljni
proces unosa/izmjene/brisanje podataka je naveden u Uputstvu za korišćenje
Geoportala.
Operatori elektronskih komunikacija, kao investitori planirane elektronske komunikacione infrastrukture, povezane opreme i elemenata mreže, obavezni su da redovno dostavljaju podatke u skladu sa članom 26 Zakona o elektronskim komunikacijama i sljedećim smjernicama:
-
Rok ažuriranja: Najkasnije 6 mjeseci prije početka izgradnje elektronske
komunikacione infrastrukture, povezane opreme i elemenata mreže;
-
Validacija podataka: Prije unosa, podaci prolaze kroz proces provjere kako bi se
osigurala tačnost i usklađenost sa propisanim standardima. Ukoliko validacija
podataka prođe uspješno podaci se mogu unijeti/izmjeniti/obrisati. Alat za
validaciju podataka je dostupan i prilikom pojedinačnog i prilikom grupnog unosa
podataka;
-
Dostavljanje podataka: Putem Geoportala Agencije pojedinačno ili grupno. Detaljni
proces unosa/izmjene/brisanje podataka je naveden u Uputstvu za korišćenje
Geoportala.
Napomena: Neblagovremeno ažuriranje navedenih podataka shodno članu 218 tačka 17 i 18 Zakona o elektronskim komunikacijama podliježe novčanoj kazni.
Agencija će obezbijediti ostale relevantne podatke koji će poslužiti za adekvatno mapiranje elektronske komunikacione infrastrukture i povezane opreme i elemente mreže. Navedeni podaci će se obezbijediti od relevantnih institucija (koje se bave poslovima katastra, sakupljanjem statističkih podataka i dr.), a odnose se na sljedeće:
-
Bazu podataka o adresama, granice opština, granice naselja, katastarske parcele,
objekte sa brojem jedinica;
-
Osnovnu kartografiju (satelitske i ortofoto snimke Crne Gore);
-
Distribucija stanovništva i domaćinstava na teritoriji države, opštine, naselja;
-
Javne objekte, kao što su škole, bolnice, saobraćajna čvorišta, javne institucije.
Treba napomenuti da Agencija može po zahtjevu Državnih i lokalnih institucija ustupiti podatke o elektronskoj komunikacionoj infrastrukturi, povezanoj opremi i elementima mreže u vidu WMS ili WFS servisa.
2.3. Geografska prostorna rezolucija podataka
Za prikupljanje i prikaz podataka moguće je koristiti nekoliko prostornih rezolucija na nivou administrativnih granica, na nivou mreže (grida) i na nivou tačke ili adrese, kako je prikazano i na sljedećoj slici.
Za prikupljanje podataka o elektronskoj komunikacionoj infrastrukturi, povezanoj opremi i elementima mreže operatori dostavljaju podatke na nivou tačke koristeći standardizirani koordinatni sistem WGS84 (World Geodetic System 1984), koji je globalno priznat kao standard za geografske podatke i omogućava precizno georeferenciranje podataka.
Pored toga, Agencija je na osnovu analize i obrade podataka izvršila procjenu pokrivenosti širokopojasnog pristupa koji je prikazan na nivou mreže (grida).
Geografska prostorna rezolucija podataka o procjeni dostupnosti širokopojasnog pristupa prikazuje se u skladu s vrstom pristupa i to:
-
Fiksni širokopojasni pristup - podaci su prikazani u mreži dimenzija 100m x 100m.
Ova rezolucija omogućava prihvatljivu procjenu dostupnosti fiksne mrežne
infrastrukture uz održavanje ravnoteže između detaljnosti i obrade podataka.
Agencija će u budućnosti, u skladu sa dostupnim podacima, unapređivati
preciznost prostorne rezolucije za fiksni širokopojasni pristup, sa ciljem da je
dovede do nivoa geokodirane adrese;
-
Mobilni širokopojasni pristup - podaci su prikazani u mreži (grid) dimenzija 50m x
50m. Ova rezolucija osigurava veći nivo detalja, s obzirom na dinamičnu prirodu
mobilne mreže i različite faktore koji utiču na pokrivenost i kvalitet signala.
2.4. Format podataka
GIS podaci mogu se podijeliti u dvije kategorije:
-
georeferencirane podatke, koji mogu biti u vektorskom i rasterskom formatu i
-
atributne podatke koje su predstavljeni u tabelarnom formatu.
Podaci o elektronskoj komunikacionoj infrastrukturi, povezanoj opremi i elementima mreže se dostavljaju u vektorskom formatu i to kao ESRI SHP datoteke (Shapefile) sa definisanim koordinatnim sistemom "WGS 1984" ili "EPSG:4326 (EPSG- European Petroleum Survey Group)", dok se alfanumerički podaci dostavljaju kao DBF (.dbf) fajlovi. Šabloni shapefile-ova za unos/izmjenu/brisanje navedenih podataka moguće je preuzeti sa početne stranice Geoportala.
Pored podatka u vektorskom i tabelarnom formatu, Agencija preko Geoportala prikuplja i podatke u rasterskom formatu i to najčešće u vidu servisa WMS (Web Map Service), WFS (Web Feature Service) i TIFF formatu. Putem Geoportala Agencija u rasterskom formatu u vidu WMS ili WFS servisa dobija podatke o podlogama tj. mapama Crne Gore, ortofoto snimcima.
Podaci o elektronskoj komunikacionoj infrastrukturi, povezanoj opremi i elementima mreže mogu se izvoziti iz Geoportala Agencije u različitim koordinatnim sistemima i vektorskim formatima poput: SHP, dbf, XLSX, PDF, KML, KMZ, DWG, GeoJSON.
Detaljna razrada formata podataka koje Agencija prikuplja data je u Aneksu 3.
2.5. Elementi elektronske komunikacione infrastrukture, povezane opreme
Elementi elektronske komunikacione infrastrukture i povezane opreme, za koje se dostavljaju podaci u skladu sa ovim Smjernicama, su:
-
Telekomunikaciona kablovska kanalizacija koja predstavlja vrstu elektronske
komunikacione infrastrukture, a koja obuhvata podatke o infrastrukturi i to:
telekomunikacionim cijevima i telekomunikacioni oknima za svaku pojedinačnu
trasu;
-
Antenski stubovi koji predstavljaju vrstu elektronske komunikacione infrastrukture
i obuhvataju podatke o antenskom stubu i povezanoj opremi za svaki pojedinačni
stub;
-
Telekomunikacioni
i
drugi
stubovi
koji
predstavljaju
vrstu
elektronske
komunikacione infrastrukture, a koji obuhvataju podatke o stubovima i nadzemnim
(vazdušnim) telekomunikacionim kablovima za svaku pojedinačnu trasu;
-
Zgrade i drugi građevinski objekti koji predstavljaju vrstu elektronske
komunikacione infrastrukture i obuhvataju podatke o zgradama i drugim
građevinskim objektima i povezanoj opremi koja se nalazi u svakoj pojedinačnoj
zgradi i drugim objektima.
Detaljna razrada elemenata elektronske komunikacione infrastrukture i povezane opreme dat je kroz tabelarni prikaz u Aneksu 2.1. Struktura i format atributnih podataka o elektronskoj komunikacionoj infrastrukturi, povezanoj opremi.
2.6. Elementi mreže
Elementi elektronske komunikacione mreže, za koje se dostavljaju podaci u skladu sa ovim Smjernicama, su:
-
Telekomunikacioni kablovi,
-
Telekomunikacioni završeci i
-
Pristupni čvorovi.
Detaljna razrada elemenata mreže dat je kroz tabelarni prikaz u Aneksu 2.2. Struktura i format atributnih podataka o elementima mreže.
2.7. Kategorizacija prikupljenih podataka u Geoportalu Agencije
Geoportal predstavlja Geografski informacioni sistem Agencije koji sadrži podatke postojećoj i planiranoj elektronskoj komunikacionoj infrastrukturi, povezanoj opremi i elemenata mreže.
Funkcije Geoportala Agencije uključuju: unos podataka, prikaz podataka, upravljanje podacima, pretraga podataka, upit u izvještaje i analizu podataka. Detaljan opis funkcionalnosti Geoportala Agencije, kao i pristup istih, biće dat u Uputstvu za korišćenje Geoportala Agencije.
U ovom poglavlju data je informacija o kategorizaciji podataka koji se prikupljaju preko Geoportala Agencije.
Atributni podaci o povezanoj opremi isporučuju se u tabelarnom formatu (.dbf) i oni su povezani (u relaciji) sa georeferenciranim podacima.
Georeferencirani podaci o elektronskoj komunikacionoj infrastrukturi, povezanoj opremi i elementima mreže su na mapi prikazani u vidu lejera. Lejeri na mapi mogu biti predstavljeni u 3 oblika kao tačka, linija ili multilinije i poligon ili multipoligoni.
Lejeri na mapi mogu da sadrže tačke, linije ili oblasti (poligon ili multipoligon) koje predstavljaju određenu klasu ili tip entiteta iz realnog svijeta kao što su ulice, poštanski brojevi i tako dalje. Sloj sadrži kako vizuelni prikaz svakog elementa, tako i vezu elementa sa njegovom atributnom bazom podataka. Lejeri koji će se koristiti u skladu sa ovim Smjernicama su predstavljeni u sljedećoj tabeli:
Tip lejera
Primjeri Lejeri koje
Agencija može da ima
Detaljni sadržaj lejera
Referentni lejeri
Administrativne
oblasti
(poligoni)
Ruralne i urbane oblasti
(Poligoni ili raster)
Lokacije
od
javnog
značaja (npr. Univerziteti,
škole, bolnice, itd. - tačke
ili poligoni)
Saobraćajne trase (linije ili
poligoni)
Popisne oblasti sa socio-
demografskim podacima
(poligoni)
Osnovne mape
Slojevi neobrađenih podataka
Telekomunikaciona
kablovska kanalizacija
Telekomunikaciona
trasa
(linija)
Telekomunikaciona cijev (linija)
Telekomunikaciono
okno
(tačka)
Antenski stubovi
Antenski stup (tačka)
Oprema na antenskom stubu
Telekomunikacioni i
drugi stubovi
Nadzemna trasa (linija)
Telekomunikacioni ili drugi
stub (tačka)
Zgrade/objekti
Zgrada (poligon)
Oprema u zgradi
Iznajmljeni dio u zgradi
Elementi mreže
Telekomunikacioni kabl (linija)
Telekomunikacioni završetak
(tačka)
Nadzemni telekomunikacioni
kabl (linija)
Nadzemni telekomunikacioni
završetak (tačka)
Pristupni čvor (tačka) Slojevi koji su rezultat analiza
Procjena pokrivenosti oblasti
po operatoru/tehnologiji/brzini
Agregirani rezultati pokrivanja
za veće gridove
Drugo u skladu sa odlukom
Agencije
Telekomunikaciona kablovska kanalizacija sadrži podatke o:
-
Telekomunikacionoj trasi;
-
Telekomunikacionim cijevima i galerijama:
o Galerija (podzemna prostorija u obliku hodnika koja služi za smještaj velikog
broja telekomunikacionih kablova);
o Cijevi velikog prečnika (cijev izrađena od polivinil hlorida, polietilena ili
betona spoljnog prečnika od 60 do 110 mm);
o Cijevi malog prečnika (cijev izrađena od polietilena visoke gustine,
spoljašnjeg prečnika od 20 do 50 mm, sa unutrašnjim zidom koji osigurava nizak
koeficijent trenja)
o Mikrocijevi (cijev spoljašnjeg prečnika od 3 do 16 mm, s unutrašnjim zidom
koji osigurava nizak koeficijent trenja).
-
Telekomunikacionim kablovima:
o Koaksijalni;
o Optički;
o Bakarni.
-
Telekomunikacionim oknima:
o Betonska monolitna;
o Betonska montažna od betonskih blokova;
o Betonska zidana (AB);
o Plastična monolitna;
o Plastična montažna.
-
Telekomunikacionim završecima:
o Završetak od upredenog bakarnog kabla;
o Završetak koaksijalnog kabla;
o Završetak optičkog i
o Drugo.
Antenski stubovi po tipu mogu biti:
o Betonski;
o Cijevasti;
o Čelično rešetkasti;
o Pauk;
o Nosači antena.
Napomena: Antenski stubovi sadrže atributne podatke o povezanoj opremi koji su u tabelarnom obliku a koji su u relaciji sa svakim pojedinačnim antenskim stubom.
Telekomunikacioni i drugi stubovi sadrže podatke o:
-
Trasama vazdušnih telekomunikacionih kablova.
-
Stubovima
na
kojima
se
nalaze
telekomunikacioni
kablovi
i
druga
telekomunikaciona oprema:
o Betonski;
o Čelični;
o Drveni.
A po namjeni mogu biti:
o Dalekovodni stubovi;
o Niskonaponski stubovi;
o Stubovi javne rasvjete;
o Drugi.
-
Vazdušnim telekomunikacionim kablovima:
o Koaksijalni;
o Optički;
o Bakarni.
-
Telekomunikacionim završecima:
o Završetak od upredenog bakarnog kabla;
o Završetak koaksijalnog kabla;
o Završetak optičkog i
o Drugo.
Zgrade i drugi građevinski objekti po tipu mogu pripadati objektima:
o Objekat čvrste gradnje;
o Kontejner;
o Vanjski kabinet;
o Unutrašnji kabinet i
o Ostalo
Napomena: Zgrade i drugi građevinski objekti u kojima se nalazi telekomunikaciona oprema sadrži atributne podatke o povezanoj opremi i iznajmljenom prostoru koji su u tabelarnom obliku, a koji su u relaciji sa ovom elektronskom komunikacionom infrastrukturom.
Format i strukturu shp file-ova preko kojih je moguće odraditi unos/izmjenu/brisanje podataka o elektronskoj komunikacionoj infrastrukturi, povezanoj opremi i elementima mreže moguće je preuzeti sa web adrese na kojoj se nalazi Geoportal Agencije.
2.8. Specifikacija planova
Podatke o planovima izgradnje/postavljanje elektronske komunikacione infrastrukture, povezane opreme i elemenata mreže operatori dostavljaju na način što će:
 na mapi označiti oblast u kojoj se planira izgradnja/postavljanje elektronske
komunikacione infrastrukture, povezane opreme i elemenata mreže i
 pridružiti prethodno označenoj oblasti PDF obavještenje o početku izgradnje,
lokaciji
izgradnje
i
tehničkim
karakteristikama
planirane
elektronske
komunikacione mreže, elektronske komunikacione infrastrukture i povezane
opreme ili njihovih elemenata.
2.9. Objavljivanje, pitanja povjerljivosti i agregacije podataka kako bi se pružile
informacije trećim stranama
Imajući u vidu da je Geoportal Agencije - sistem koji omogućava pristup od strane više korisnika, Agencija je predvidjela sledeće nivoe pristupa:
1. Operatori (Operatori elektronskih komunikacija),
2. Planeri (Obrađivači prostorno planskih dokumenata, izvođači radova...),
3. Državne institucije (Ministarstva, Uprave...),
4. Lokalne samouprave (Opštine, Lokalne institucije...)
5. Javni pristup (investitori i sva zainteresovana lica).
Geoportal Agencije, u zavisnosti od nivoa pristupa, korisnicima nudi uvid u atributne detalje elektronske komunikacione infrastrukture, povezane opreme i elemenata mreže kao i pristup određenim funkcionalnostima sistema.
Javni pristup je korisnički pristup Geoportalu Agencije koji jedino ne podliježe prethodnoj registraciji i ovi korisnici imaju uvid u prostorne podatke, tj. geografski raspored postojeće infrastrukture i pristup osnovnim funkcijama portala. Takođe, ovi korisnici mogu pristupiti mapi pokrivenosti fiksnim i mobilnim širokopojasnim pristupom interneta i pristupiti podacima o pokrivenosti domaćinstava fiksnim širokopojasnim pristupom interneta.
Operator Za korisnike koji pripadaju grupi operatora, prilikom kreiranja korisničkog naloga, potrebno je odabrati i kojem operatoru pripadaju. Oni imaju sva prava koja su dodijeljena za javni pristup, kao i mogućnost unosa/ažuriranja/uklanjanja objekata EKI, kao i pratećih podataka (oprema, iznajmljivanje, veze), kako pojedinačno tako i masovno iz pripremljenih fajlova. Upravljanje objektima EKI je omogućeno isključivo za infrastrukturu koja je u vlasništvu konkretnog operatora, dok je opremu moguće dodavati/mijenjati/uklanjati i na objektima drugih operatora. Ova grupa ima mogućnost filtriranja i preuzimanja podataka u različitim GIS formatima.
Planeri Korisnici koji pripadaju ovoj grupi imaju pristup svim funkcionalnostima koje su odobrene za javni pristup, malo širi skup alfanumeričkih podataka nad kojima mogu vršiti uvid, kao i mogućnost uvoza granice zahvata plana, na osnovu koje mogu vršiti izvoz podataka iz sistema, u okviru unijete granice, u shp formatu.
Državne institucije Korisnici koji pripadaju ovoj grupi imaju sva prava kao korisnici iz grupe "Planeri" sa izuzetkom preuzimanja podataka iz zahvata plana.
Lokalne samouprave Korisnici iz ove grupe imaju uvid u podatke kao i državne institucije uz mogućnost unosa planiranih saobraćajnica, odnosno saobraćajnica na kojima je planirana rekonstrukcija.
Pristup funkcionalnostima Geoportala Agencije biće navedene u Uputstvu za korišćenje Geoportala.
3. Obaveze korisnika
Svi korisnici Geoportala dužni su se pridržavati određenih obaveza koji proističu iz ovih Smjernica.
Operatori vlasnici elektronske komunikacione infrastrukture, povezane opreme i elemenata mreže treba da:
-
Redovno ažuriraju svoje podatke što će dovesti do povećavaju njihove tačnost,
-
Dostavljaju podatke u propisanim šablonima Shapefile datoteka,
-
Prijave Administratoru sistema ukoliko primjete neku grešku na sistemu,
-
Iniciraju obuku u slučaju potrebe i
-
Poštuju rokove za dostavljanje i ažuriranje podataka.
Državne i lokalne institucije treba da:
-
Obezbijede dostupnost potrebnih podataka,
-
Obezbjede stalnu saradnja sa Agencijom u vezi sa integracijom i razmjenom
informacija i podataka.
Svi korisnici treba da koriste podatke isključivo u svrhu za koje su namijenjeni i da iste ne zloupotrebljavaju.
Operatori su dužni da sa predmetnim podacima postupaju u skladu sa zakonima kojim se uređuje zaštita podataka. Radi zaštite povjerljivosti podataka, operatori su dužni da jasno naznače koji se podaci smatraju povjerljivim.
ANEKSI
1. Aneks - Evaluacija jedinica prostorne rezolucije
TAČKE - Podaci se dostavljaju kao tačke koje predstavljaju adrese.
Prednosti:
- Veoma precizan opis realnog stanja
Nedostaci:
- Moraju se ispuniti visoki zahtjevi za
sigurnost podataka
- Veliki napori za mapiranje
- Moguća nespremnost mrežnih
operatora / internet provajdera za
dostavljanje podataka zbog čuvanja
poslovne tajne MREŽE (GRIDOVI) - Podaci o širokopojasnim uslugama često se prikazuju na nivou mreže.
Prednosti:
- Dovoljan nivo povjerljivosti podataka za operatore vlasnike elektronske komunikacione infrastrukture, povezane opreme i elemenata mreže.
- Relativno precizni podaci sa malom marginom greške.
Nedostaci:
- Potreban je određeni napor za
pravljenje odgovarajuće analize kako
bi podaci bili prikazani u mrežnom
nivou.
AGREGACIJA Podaci se takođe mogu prikupljati tako što će se omogućiti veza sa drugim GIS sistemima i na taj način pribaviti podaci o granicama opština, granice naselja i sl.
Prednosti:
Potencijalno vrlo mali napor za isporučioce/dobavljače podataka, u zavisnosti od izabranog nivoa agregacije.
Nedostaci:
- Mala mogućnosti za dalju analizu
podataka, u zavisnosti od izabranog
nivoa agregacije
- Nema mogućnosti za otkrivanje
preklapajućih poligona i samim tim
moguća je greška u isporučenim
podacima.
2. Aneks - Struktura i format atributnih podataka
2.1. Struktura i format atributnih podataka o elektronskoj komunikacionoj
infrastrukturi, povezanoj opremi Potrebno je voditi računa o identifikatorima (id) koji su definisani u svakoj tabeli (klasi), a koji moraju biti jedinstveni kod jednog operatora i ne smiju se mijenjati, jer se na osnovu njih vrši ažuriranje (Izmjena) i brisanje podataka.
Podaci o elektronskoj komunikacionoj infrastrukturi, povezanoj opremi i elementima mreže u shp datotekama trebaju biti usklađeni sa nazivima Tabela (Klasama). Takođe, naziv, formati i atributne vrijednosti polja moraju biti uslkađeni prema slijedećim tabelama:
Klasa: TKK_TRASA.SHP Naziv polja Tip
polja
Obavezno Opis polja
trasa
Text
NE
Naziv trase telekomunikacione kablovske kanalizacije
(Oblasti ili Naselje ili Ulica ili druga slična
odrednica)
duzina
Double
DA
Duži na trase (m)
(Dužinu trase treba istaći u metrima)
id_trasa
Text
DA
Identifikator trase
(Ovo polje podrazumjeva upis jedinstvene oznake za
trasu)
id_operat1
Text
DA
Identifikator operatora
(Operator vlasnik trase
telekomunikacione kablovske kanalizacije)
id_operat2
Text
DA
Identifikator operatora
(Operator vlasnik trase
telekomunikacione kablovske kanalizacije)
id_operat3
Text
DA
Identifikator operatora
(Operator vlasnik trase
telekomunikacione kablovske kanalizacije)
Klasa: TKK_CIJEV.SHP Naziv polja Tip
polja
Obavezno Opis polja
cijev_tip
Text
DA
d_tip_cijevi
(Galerija, Mikrocijevi, Cijevi malog prečnika (PE 20-
50mm), cijevi velikog prečnika (PVC 60-110mm))
cijev_status
Text
DA
Status cijevi
(iznajmljen/neiskorišćen/sadrži
druge cijevi/koristi vlasnik) korisnik
Text
DA
Iznajmljeni kapacitet - operator korisnik
(operator koji koristi cijev na trasi
telekomunikacione kablovske kanalizacije)
cijev_parent Text
DA
Pripadnost drugoj cjevi
(ukoliko se cijev nalazi u drugoj cijevi većeg presjeka
treba u ovom polju upisati ID_cev većeg presjeka
kojoj pripada manja cijev a koja će biti veza sa
poljem id_cijevi)
R_cijevi
Double
DA
Prečnik cijevi (mm)
(Prečnik cijevi u milimetrima)
id_cijev
Text
DA
Identifikator cijevi
(jedinstveni identifikacioni broj cijevi)
id_operat1
Text
DA
Identifikator operatora vlasnika cijevi
(Operator vlasnik trase telekomunikacione kablovske
kanalizacije)
id_operat2
Text
DA
Identifikator operatora vlasnika cijevi
(Operator vlasnik trase telekomunikacione kablovske
kanalizacije)
id_operat3
Text
DA
Identifikator operatora vlasnika cijevi
(Operator vlasnik trase telekomunikacione kablovske
kanalizacije)
prohodnost
Text
DA
Prohodnost cijevi
(neispitano (default), prohodno,
neprohodno)
Klasa: TKK_OKNA.SHP Naziv polja Tip
polja
Obavezno Opis polja
tip_okn
Text
DA
Tip kablovskog okna na trasi
(Tipovi kablovskih okana: Betonska monolitna,
Betonska montažna od betonskih blokova, Betonska
zidana (AB), Plastična monolitna, Plastična
montažna)
ozn_okn
Text
DA
Naziv/oznaka kablovskog okna na trasi
(Naziv ili Oznaka kablovskog okna)
sirina_okn
Text
DA
Širina okna (m)
(širina okna u metrima)
duzina_okn
Text
DA
Dužina okna (m)
(dužina okna u metrima)
sema_okn
Text
DA
Razvojna šema okna
(Razvojna šema okna će se dostavljati u skladu sa
uputstvom o korišćenju Geoportala)
id_okn
Text
DA
Identifikator okna
(jedinstvena identifikacioni broj okna)
id_operat1
Text
DA
Identifikator operatora vlasnika
(Operator vlasnik trase telekomunikacione kablovske
kanalizacije)
id_operat2
Text
DA
Identifikator operatora vlasnika
(Operator vlasnik trase telekomunikacione kablovske
kanalizacije)
id_operat3
Text
DA
Identifikator operatora vlasnika
(Operator vlasnik trase telekomunikacione kablovske
kanalizacije)
Klasa: VV_TRASA.SHP Naziv polja Tip
polja
Obavezno Opis polja
trasa
Text
NE
Naziv trase vazdušnih vodova
(Oblasti ili Naselje ili Ulica ili druga slična
odrednica)
duzina
Double
DA
Dužina trase (m)
(Dužinu trase treba istaći u metrima)
id_vv_tras
Text
DA
Identifikator trase
(Ovo polje podrazumjeva upis jedinstvene oznake za
trasu, koja se ne smije mijenjati tokom kasnije
izmjene podataka o ovom entitetu u bazi)
id_operat1
Text
DA
Identifikator operatora
(Operator vlasnik trase)
id_operat2
Text
DA
Identifikator operatora
(Operator vlasnik trase)
id_operat3
Text
DA
Identifikator operatora
(Operator vlasnik trase)
Klasa: VV_STUB.SHP Naziv polja Tip
polja
Obavezno Opis polja
tip
Text
DA
Tip stuba na trasi
(ovo polje sadrži domene)
namjena
Text
DA
Upisati namjenu stuba
(ovo polje sadrži domene)
visina
Text
DA
Visina stuba
(Visina stuba upisujemo u metrima)
tip_nosaca
Text
DA
Tip nosača kabla
(Tip nosača telekomunikacionih kablova na
stubovima)
id_vv_stub
Text
DA
Identifikator stuba
(jedinstveni identifikacioni broj stuba)
id_operat1
Text
DA
Identifikator operatora vlasnika
(Operator vlasnik trase)
id_operat2
Text
DA
Identifikator operatora vlasnika
(Operator vlasnik trase)
id_operat3
Text
DA
Identifikator operatora vlasnika
(Operator vlasnik trase)
Klasa: AS_TACKA.SHP Naziv polja Tip
polja
Obavezno Opis polja
naziv_as
Text
DA
Naziv antenskog stuba
(Naziv antenskog stuba)
naziv_lok
Text
DA
Naziv lokacije antenskog stuba
(Naziv lokacije)
nad_visina
Double
DA
Nadmorska visina (m)
(Nadmorska visina osnove antenskog stuba u
metrima)
tip
Text
DA
Tip antenskog stuba
(Tipovi antenskog stuba: Betonski, cjevasti, pauk,
nosači antena)
dim_osnove Text
DA
Dimenzije osnove antenskog stuba
(Ovo polje definiše dimenziju osnove antenskog stuba
u metrima kvadratnim ukoliko se radi o čelično
rešetkastom stubu ili prečnik ukoliko se radi o
cjevastom stubu)
vis_stuba
Double
DA
Visina antenskog stuba (m)
(Visina antenskog stuba u metrima)
visina_obj
Double
DA
Visina objekta na kome se nalazi
antenski stub (m)
(Visina objekta na kome se nalazi stub u metrima)
foto_sever
Text
DA
Crtež ili fotografija stuba (sjever)
(Fotografija/slika stuba se unosi u skladu sa
uputstvom o korišćenju Geoportala)
foto_istok
Text
DA
Crtež ili fotografija stuba (istok)
(Fotografija/slika stuba se unosi u skladu sa
uputstvom o korišćenju Geoportala)
foto_jug
Text
DA
Crtež ili fotografija stuba (jug)
(Fotografija/slika stuba se unosi u skladu sa
uputstvom o korišćenju Geoportala)
foto_zapad
Text
DA
Crtež ili fotografija stuba (zapad)
(Fotografija/slika stuba se unosi u skladu sa
uputstvom o korišćenju Geoportala)
id_as
Text
DA
Identifikator tačke
(jedinstveni identifikacioni broj antenskog stuba)
id_operat1
Text
DA
Identifikator operatora vlasnika stuba
(Operator vlasnik antenskog stuba)
id_operat2
Text
DA
Identifikator operatora vlasnika stuba
(Operator vlasnik antenskog stuba)
id_operat3
Text
DA
Identifikator operatora vlasnika stuba
(Operator vlasnik antenskog stuba)
Klasa: ZGRADA.SHP Naziv polja Tip
polja
Obavezno Opis polja
naziv_lok
Text
DA
Naziv lokacije
(Naziv lokacije)
naziv_zgr
Text
DA
Naziv zgrade
(Naziv zgrade odnosno građevinskog objekta)
tip_zgr
Text
DA
Tip zgrade odnosno građevinskog objekta
(Tip zgrade/ objekta: Objekat čvrste gradnje,
kontejner i vanjski kabinet) uk_povrs
Text
DA
Ukupna površina objekta (m2)
(Ukupna površina objekta/zgrade data po
površinama prostorija koje ga sačinjavaju metri
kvadratni)
tlocrt
Text
DA
Tlocrt zgrade
(Tlocrt zgrade se dostavlja u skladu sa uputstvom o
korišćenju Geoportala)
uk_snaga
Text
DA
Ukupna instalisana snaga elektroenergetskog
napajanja
objekta (W)
(Ukupna instalisana snaga elektroenergetskog
napajanja u objektu treba biti izražena u vatima)
re_snaga
Text
DA
Ukupna instalisana snaga rezervnog
elektroenergetskog napajanja objekta (W)
(Ukupna instalisana snaga rezervnog
elektroenergetskog napajanja u objektu treba biti
izražena u vatima)
uk_potro
Text
DA
Ukupna potrošnja instalisane opreme (W)
(Ukupna potrošnja instalisane
opreme u objektu treba biti izražena u vatima)
uk_izna
Text
DA
Ukupni iznajmljeni prostor (m2)
(Ukupni iznajmljeni prostor treba dati u kvadratnim
metrima)
id_zgr
Text
DA
Identifikator zgrade
(Jedinstveni broj objekta/zgrade)
id_operat1
Text
DA
Identifikator operatora vlasnika zgrade
(Operator vlasnik objekta/zgrade)
id_operat2
Text
DA
Identifikator operatora vlasnika zgrade
(Operator vlasnik objekta/zgrade)
id_operat3
Text
DA
Identifikator operatora vlasnika zgrade
(Operator vlasnik objekta/zgrade)
Klasa: ZGRADA_IZN.DBF Naziv polja Tip
polja
Obavezno Opis polja povrsina
Text
DA
Iznajmljeni prostor m2
(Iznajmljeni prostor u objektu u kvadratnim metrima)
id_zgr
Text
DA
Identifikator zgrade
(Jedinstveni broj objekta/zgrade, veza sa klasom
ZGRADA.SHP)
id_korisn
Text
DA
Identifikator operatora korisnika iznajmljenog
prostora
(Operator koji iznajmljuje prostor za smještanje
opreme)
id_prost
Text
DA
Identifikator prostora
(Jedinstveni broj prostora)
id_operat1
Text
DA
Identifikator operatora koji unosi podatke
(Operator vlasnik objekta/zgrade)
id_operat2
Text
DA
Identifikator operatora koji unosi podatke
(Operator vlasnik objekta/zgrade)
id_operat3
Text
DA
Identifikator operatora koji unosi podatke
(Operator vlasnik objekta/zgrade)
2.2. Struktura i format atributnih podataka o elementima mreže
Potrebno je voditi računa o identifikatorima (id) koji su definisani u svakoj tabeli (klasi), a koji moraju biti jedinstveni kod jednog operatora i ne smiju se mijenjati, jer se na osnovu njih vrši ažuriranje (Izmjena) i brisanje podataka.
Podaci o elementima mreže u shp datotekama trebaju biti usklađeni sa nazivima Tabela (Klasama).
Takođe, naziv i format polja mora biti usklađeni prema slijedećim tabelama:
Klasa: TKK_KABL.SHP Naziv polja Tip
polja
Obavezno Opis polja
oznaka
Text
DA
Oznaka kabla
(Fabrička oznaka sa kapacitetom)
kapacitet
Text
DA
Kapacitet kabla
(Treba navesti kapacitet kabla)
tip
Text
DA
Tip kabla
(Koaksijalni, optički i bakarni
kabal...)
precnik
Text
DA
Prečnik kabla (mm)
(Poprečni presjek kabla u milimetrima)
polaganje
Text
DA
Godina polaganja
(Godina polaganja kabla)
status
Text
DA
Aktivan/neaktivan
(Status kabla da li je aktivan ili neaktivan)
id_kbl
Text
DA
Identifikator kabla
(jedinstvena identifikacioni broj kabla)
postavljen
Text
DA
Način postavljanja
(Način postavljanja kabla: u cijevi, kroz kablovsku
kanalizaciju, ukopan direktno u zemlju)
id_cev
Text
DA
Identifikator cijevi
(popunjava se samo ukoliko je kabl u cijevi, veza sa
klasom TKK_CIJEV.SHP )
idvlasnik1
Text
DA
Identifikator operatora- vlasnik kabla
(Naziv operatora koji je vlasnik kabla)
br_vlakana1 Integer
DA
Broj vlakana ili parica u vlasništvu vlasnika1
idvlasnik2
Text
DA
Identifikator operatora- vlasnik kabla
(Naziv operatora koji je vlasnik kabla)
br_vlakana2 Integer
DA
Broj vlakana ili parica u vlasništvu vlasnika2 idvlasnik3
Text
DA
Identifikator operatora- vlasnik kabla
(Naziv operatora koji je vlasnik kabla)
br_vlakana3 Integer
DA
Broj vlakana ili parica u vlasništvu vlasnika3
Idvlasnik4
Text
DA
Identifikator operatora- vlasnik kabla
(Naziv operatora koji je vlasnik kabla)
br_vlakana4 Integer
DA
Broj vlakana ili parica u vlasništvu vlasnika3
Klasa: TKK_ZAVRSETAK.SHP Naziv polja
Tip
polja
Obavez
no
Opis polja
mesto_o pis
Text
DA
Podaci o završetku kabla u objektu
(Mjesto i opis)
tip_zavrs e
Text
DA
Podaci o završetku kabla u objektu - Tip završetka
(Završetak od upredenog bakarnog kabla, Završetak
koaksijalnog kabla, Završetak optičkog i Drugo)
id_zav
Text
DA
Identifikator tačke
(Jedinstveni identifikacioni broj završetka)
id_operat 1
Text
DA
Identifikator operatora vlasnika
(Operator vlasnik telekomunikacionog završetka)
id_operat 2
Text
DA
Identifikator operatora vlasnika
(Operator vlasnik telekomunikacionog završetka)
id_operat 3
Text
DA
Identifikator operatora vlasnika
(Operator vlasnik telekomunikacionog završetka)
adresa
Text
NE
Adresa i broj lokacije završetka
(Ulica i broj završetka)
kapacitet
Long
Intege
r
DA
Kapacitet završetka kabla u objektu
(kablovska glava, orman, razdjelnik, ODF, GTO, ZOK i sl)
iskorisce n
Long
Intege
r
DA
Broj izvedenih priključaka
(kablovska glava, orman, razdjelnik, ODF, GTO, ZOK i sl)
tehnologi ja
Text
DA
Tehnologija za pružanje usluge
-
DSL/ADSL preko bakarnih parica
-
VDSL preko bakarnih parica
-
VECT - VDSL vektoring preko bakarnih parica
-
DOCSIS 1.0 ili 2.0 preko koaksijalnog kabla
-
DOCSIS 3.0 ili 3.1 0 preko koaksijalnog kabla
-
FTTH/FTTB preko optičkih vlakana
-
FWA u licenciranim rf opsezima - FWA
-
FWA u nelicenciranim rf opsezima - WIFI
-
Drugo Dostupn a_ brzina
Text
DA
Sistem automatski dodjeljuje brzine na osnovu tehnologije
Klasa: VV_KABL.SHP Naziv polja
Tip
polja
Obavez
no
Opis polja
oznaka
Text
DA
Oznaka kabla
(Fabrička oznaka sa kapacitetom)
tip
Text
DA
Tip kabla
(Koaksijalni, optički i bakarni kabl...)
precnik
Text
DA
Prečnik kabla
(Poprečni presjek kabla
u milimetrima)
polaganj e
Text
DA
Godina postavljanja (Godina polaganja kabla)
status
Text
DA
Aktivan/neaktivan
(Status kabla da li je aktivan ili neaktivan)
id_vv_k bl
Text
DA
Identifikator kabla
(jedinstveni identifikacioni broj kabla) idvlasni k1
Text
DA
Identifikator operatora- vlasnik kabla
(Naziv operatora koji je vlasnik kabla) br_vlaka na1
Intege
r
DA
Broj vlakana u vlasništvu vlasnika1
idvlasni k2
Text
DA
Identifikator operatora- vlasnik kabla
(Naziv operatora koji je vlasnik kabla) br_vlaka na2
Intege
r
DA
Broj vlakana u vlasništvu vlasnika2
idvlasni k3
Text
DA
Identifikator operatora- vlasnik kabla
(Naziv operatora koji je
vlasnik kabla) br_vlaka na3
Intege
r
DA
Broj vlakana u vlasništvu vlasnika3
Idvlasni k4
Text
DA
Identifikator operatora- vlasnik kabla
(Naziv operatora koji je vlasnik kabla) br_vlaka na4
Intege
r
DA
Broj vlakana u vlasništvu vlasnika3
id_opera to
Text
DA
Identifikator operatora koji unosi podatke
(Operator vlasnik trase)
Id_vv_tr asa
Text
DA
Identifikator trase . Upisati id_trase kojoj pripada kabl
(Ovo polje podrazumjeva upis jedinstvene oznake za
trasu, koja se ne smije mijenjati tokom kasnije izmjene
podataka o ovom entitetu u bazi)
Klasa: VV_ZAVRSETAK.SHP
Naziv polja
Tip
polja
Obavezno Opis polja
mjesto_opis
Text
DA
Podaci o završetku kabla u objektu - Mjesto i opis
(Mjesto i opis)
tip_zavrse
Text
DA
Podaci o završetku kabla u objektu - Tip završetka
kapacitet
Double
DA
Kapacitet završetka kabla na stubu
(kablovska glava, orman, razdjelnik, ODF,
GTO, ZOK i sl)
Iskorišćen
Double
DA
Broj izvedenih priključaka
id_vv_zav
Text
DA
Identifikator tačke
(Jedinstveni identifikacioni broj
završetka)
id_operat1
Text
DA
Identifikator operatora vlasnika
(Operator vlasnik nadzemnog telekomunikacionog
završetka)
id_operat2
Text
DA
Identifikator operatora vlasnika
(Operator vlasnik nadzemnog telekomunikacionog
završetka)
id_operat3
Text
DA
Identifikator operatora vlasnika
(Operator vlasnik nadzemnog telekomunikacionog
završetka) adresa
Text
NE
Adresa i broj lokacije završetka
(Ulica i broj završetka)
tehnologija
Text
DA
Tehnologija za pružanje usluge
-
DSL/ADSL preko bakarnih parica
-
VDSL preko bakarnih parica
-
VECT - VDSL vektoring preko bakarnih parica
-
DOCSIS 1.0 ili 2.0 preko koaksijalnog kabla
-
DOCSIS 3.0 ili 3.1 0 preko koaksijalnog kabla
-
FTTH/FTTB preko optičkih vlakana
-
FWA u licenciranim rf opsezima - FWA
-
FWA u nelicenciranim rf opsezima - WIFI
-
Drugo
brzina
Text
DA
Sistem automatski dodjeljuje brzine na
osnovu tehnologije
Klasa: PRISTUPNI ČVOR.SHP
Naziv polja
Tip
polja
Obavezno Opis polja
mjesto_opis
Text
DA
Podaci o pristupnom čvoru - Mjesto i opis
(Mjesto i opis)
tip_pristupnog čvora
Text
DA
Podaci o pristupnom čvoru -
(Tip pristupnog čvora)
kapacitet
Double
DA
Kapacitet pristupnog čvora
(Instalirani kapacitet)
Iskorišćen
Double
DA
Broj izvedenih priključaka
(Iskorišćeni kapacitet) Uplink
Text
DA
Kapacitet uplinka (Gb/s)
id_pristupnog čvora
Text
DA
Identifikator tačke
(Jedinstveni identifikacioni broj Pristupnog
čvora)
id_operat1
Text
DA
Identifikator operatora vlasnika
(Operator vlasnik pristupnog čvora)
id_operat2
Text
DA
Identifikator operatora vlasnika
(Operator vlasnik pristupnog čvora)
id_operat3
Text
DA
Identifikator operatora vlasnika
(Operator vlasnik pristupnog čvora)
adresa
Text
DA
Adresa lokacije pristupnog čvora
(Adresa pristupnog čvora) tehnologija
Text
DA
Tehnologija za pružanje usluge
-
DSL/ADSL preko bakarnih parica
-
VDSL preko bakarnih parica
-
VECT - VDSL vektoring preko bakarnih
parica
-
DOCSIS 1.0 ili 2.0 preko koaksijalnog kabla
-
DOCSIS 3.0 ili 3.1 0 preko koaksijalnog kabla
-
FTTH/FTTB preko optičkih vlakana
-
FWA u licenciranim rf opsezima - FWA
-
FWA u nelicenciranim rf opsezima - WIFI
-
Drugo
id_zgr
Text
DA
Identifikator zgrade
(Jedinstveni broj objekta/zgrade, veza sa klasom
ZGRADA.SHP)
id_zav
Text
DA
Identifikator tačke
(Jedinstveni identifikacioni broj završetka, veza
sa klasom TKK_ZAVRSETAK.SHP)
id_vv_zav
Text
DA
Identifikator tačke
(Jedinstveni identifikacioni broj
Završetka, klasom VV_ZAVRSETAK.SHP) Klasa: AS_OPREMA.DBF
Naziv polja
Tip
polja
Obavezno Opis polja
tip
Text
DA
Tip opreme
(Tip opreme koja je na stubu)
namjena
Text
DA
Namjena opreme
(Namjena opreme)
namjena_det Text
DA
Namjena detalji
(Namjena opreme npr. pokrivanje područja 2G, 3G, 4G
i 5G signalom, rr veza lokacije1- lokacija2, Radio, TV
i sl.)
status
Text
DA
Aktivna/neaktivna
(Status opreme da li je aktivna ili neaktivna)
id_vlasnik
Text
DA
Identifikator vlasnika opreme
(Operator vlasnik opreme na antenskom stubu)
vlasnikdet
Text
DA
Vlasnik opreme detalji
(Upisuje se naziv TV, radio stanice ili funkcionalnog
sistema)
id_as
Text
DA
Identifikator antenskog stuba
(Jedinstveni broj antenskog stuba, veza sa klasom
AS_TACKA.SHP)
id_oprem
Text
DA
Identifikator opreme
(Jedinstveni broj opreme na stubu)
id_operat1
Text
DA
Identifikator operatora koji unosi podatke
(Operator vlasnik antenskog stuba)
id_operat2
Text
DA
Identifikator operatora koji unosi podatke
(Operator vlasnik antenskog stuba)
id_operat3
Text
DA
Identifikator operatora koji unosi podatke
(Operator vlasnik antenskog stuba) Klasa: ZGRADA_OPR.DBF
Naziv polja
Tip
polja Obavezno Opis polja
tip
Text
DA
Tip opreme
(Tip opreme koja je u objektu/zgradi)
namjena
Text
DA
Namjena opreme
(Namjena opreme koja pripada određenom domenu npr:
Mobilna mreža, fiksna mreža. Internet, distribucija
AVM signala, napajanje, klimatizacija )
namjena_det Text
DA
Namjena detalji
(Namjena detalji: baterijsko napajanje, agregat, bazna
stanica, MSAN, ADSL, serveri, prenosna oprema,
komutaciona oprema...)
status
Text
DA
Aktivna/neaktivna
(Status opreme da li je aktivna ili neaktivna)
id_zgr
Text
DA
Identifikator zgrade
(Jedinstveni broj objekta/zgrade, veza sa klasom
ZGRADA.SHP)
id_vlasnik
Text
DA
Vlasnik opreme
(Na osnovu predefinisanih domena korisnik upisuje
broj pod kojim se operator vodi)
vlasnikdet
Text
DA
Vlasnik opreme detalji
(Upisuje se naziv TV, radio
stanice ili funkcionalnog sistema)
id_oprem
Text
DA
Identifikator opreme
(Jedinstveni broj opreme u objektu/zgradi)
id_operat1
Text
DA
Identifikator operatora koji unosi podatke
(Operator vlasnik objekta/zgrade)
id_operat2
Text
DA
Identifikator operatora koji unosi podatke
(Operator vlasnik objekta/zgrade)
id_operat3
Text
DA
Identifikator operatora koji unosi podatke
(Operator vlasnik objekta/zgrade)
2.3. Struktura i format relacija između "features" klasa
Tabele koje se popunjavaju za relaciju više na više (M to N) su:
Tabela: tkktrasa_to_tkkcijev_MN.DBF
Naziv polja
Tip
polja Obavezno Opis polja
id_trasa
Text
DA
Identifikator trase
(Jedinstveni broj trase)
id_cijev
Text
DA
Identifikator cijevi
(Jedinstveni broj cijevi)
Tabela: tkktrasa_to_tkkkabl_MN.DBF
Naziv polja
Tip
polja
Obavez
no
Opis polja
id_trasa
Text
DA
Identifikator cijevi
(Jedinstveni broj cijevi)
id_kabl
Text
DA
Identifikator kabla
(Jedinstveni broj kabla)
Tabela: tkkcijev_to_tkkkabl_MN.DBF
Naziv polja
Tip
polja Obavezno Opis polja
id_cev
Text
DA
Identifikator cijevi
(Jedinstveni broj cijevi)
id_kabl
Text
DA
Identifikator kabla
(Jedinstveni broj kabla)
Tabela: tkkkabl_to_tkkokna_MN.DBF
Naziv polja
Tip
polja Obavezno Opis polja
id_kabl
Text
DA
Identifikator kabla
(Jedinstveni broj kabla)
id_okn
Text
DA
Identifikator okna
(Jedinstveni broj okna)
Tabela: tkkkabl_to_tkkzavr_MN.DBF
Naziv polja
Tip
polja Obavezno Opis polja
id_kabl
Text
DA
Identifikator kabla
(Jedinstveni broj kabla)
id_zav
Text
DA
Identifikator završetka
(Jedinstveni broj završetka)
Tabela: vvtrasa_to_vvkabl_MN.DBF
Naziv polja
Tip
polja Obavezno Opis polja
id_vv_kabl
Text
DA
Identifikator kabla
(Jedinstveni broj kabla)
id_vv_trasa
Text
DA
Identifikator trasa
(Jedinstveni broj trasa)
Tabela: vvkabl_to_vvstub_MN.DBF
Naziv polja
Tip
polja Obavezno Opis polja
id_vv_kabl
Text
DA
Identifikator kabla
(Jedinstveni broj kabla)
id_vv_okn
Text
DA
Identifikator okna
(Jedinstveni broj okna)
Tabela: vvkabl_to_vvzavr_MN.DBF
Naziv polja
Tip
polja Obavezno Opis polja
id_vv_kabl
Text
DA
Identifikator kabla
(Jedinstveni broj kabla)
id_vv_zav
Text
DA
Identifikator završetka
(Jedinstveni broj završetka) 3. Aneks - Format i tip podataka
Podaci u GIS-u mogu se podijeliti u dvije kategorije: georeferencirani podaci, koji su predstavljeni u vektorskim i rasterskim oblicima (npr. ortofoto snimci), i atributne podaci, koji su prikazani u tabelarnom formatu.
Prednosti i nedostaci vektorskih i rasterskih prikaza su:
-
Tačnost unosa i tačnost prikaza podataka značajno su veći u vektorskom obliku;
-
Skladištenje rasterskih entiteta zahtijeva više prostora;
-
Rukovanje sa vektorskim podacima u GIS aplikacijama je mnogo brže (snimanje,
učitavanje, prikazivanje, uređivanje, kopiranje, brisanje);
-
Slobodna i bogata simbologija vektorskih entiteta (praktično neograničena primjena
boja, ispuna, nijansi itd.);
-
Geometrijska fleksibilnost vektorskih entiteta (npr. laka izmjena);
-
Mogućnost izvođenja složenih izračuna (npr. površina);
-
Vektorski podaci su nezavisni od rezolucije i može se koristiti u shemama koje
zahtijevaju glatke zakrivljene linije;
-
Vektorske podatke je lako konvertovati u rasterske podatke;
-
Neki procesi ne mogu koristiti rasterske podatke;
-
Teže je štampati rasterske slike koristeći ograničen spektar boja;
-
Vektorske slike su veoma složene, a implementacija ovih formata na različitim
uređajima je, shodno tome, problematična. Konverzija iz jednog formata u drugi
takođe je teška;
-
Kreiranje novih vektorskih entiteta ili modifikacija / ažuriranje postojećih entiteta
može se lako izvršiti.
3.1. Vektorski model Vektorski modeli se sastoje od tačaka, linija (lukova) i poligona (površina). Svaka od ovih jedinica je jednostavno sastavljena kao niz jedne ili više koordinatnih tačaka. Na primjer, linija je zbirka povezanih tačaka, a poligon je zbirka povezanih linija.
Najpopularniji formati vektorskih podataka u GIS-u su:
-
Shapefile format je popularan geospacijalni vektorski format za GIS softver za
čuvanje lokacije, oblika i atributa geografskih karakteristika. Razvio ga je i reguliše
ESRI kao (uglavnom) otvorenu specifikaciju za interoperabilnost podataka između
ESRI i drugih GIS softverskih proizvoda. Za grupni unos podataka o elektronskoj
komunikacionoj infrastrukturi koristi se shp file format a šablon istog je moguće
preuzeti sa Geoportala Agencije.
-
GeoJSON je jednostavan format, zasnovan na Java Script Object Notation (‘JSON’),
koji koriste mnogi open source GIS paketi. GeoJSON funkcije uključuju tačke,
linijske nizove, poligone i višedjelne kolekcije ovih tipova.
-
Keyhole Markup Language (KML) je format datoteke koji se koristi za prikaz
geografskih podataka u pretraživačima Zemlje poput Google Earth-a.
3.2. Rasterski model Rasterski model podataka sastoji se od redova i kolona jednake veličine piksela povezanih radi formiranja ravne površine. Rasteri su digitalne vazdušne fotografije, satelitski snimci, digitalne slike ili skenirane mape.
3.3. Tabelarni podaci Tabelarni podaci su jednostavno informacije prikazane u obliku tabele sa redovima i kolonama.
Za transformaciju bilo kog tipa modela datoteka u model podataka potreban za bilo koju GIS aplikaciju, neophodno je imati prostorni ETL (extract, transform, load) alat ili jednostavno uvezati ove podatke sa vektorskim podacima kako bi isti bili mapirani.
4. Aneks - Projektovani koordinatni sistem Projektovani koordinatni sistem pruža mehanizme za projektovanje mapa Zemljine sferne na dvodimenzionalnu ravan (x, y).
Najčešće korišćeni projektovani koordinatni sistemi uključuju:
-
Universal Transverse Mercator (UTM) je sistem koordinata koji predstavlja
horizontalni položaj na globusu i dijeli Zemlju na šezdeset zona.
-
Lambertova azimutalna ekvivalentna projekcija je specifična projekcija sa sfere na
ploču koja tačno predstavlja površinu u svim regijama sfere.
-
Evropski Terestrički Referentni Sistem 1989 (ETRS89) je standardni koordinatni
sistem za Evropu, koji podržava EuroGeographics i Evropska unija.
Koordinatni sistem je referentni sistem koji se koristi za predstavljanje lokacija geografskih karakteristika i posmatranja, kao što su GPS lokacije.
Najnoviji geografski koordinatni sistem je World Geodetic System 84 (WGS 1984 ili EPSG:4326), koji uključuje standardni koordinatni sistem, referentni elipsoid i visinske podatke. Geoportal Agencije koristi EPSG:4326 koordinantni sistem kako bi na mapi prikazao elemente elektronske komunikacione infrastrukture, povezane opreme i elemenata mreže.
Dostupni su brojni besplatni softverski alati koji mogu transformisati bilo koji koordinatni sistem u WGS84 sistem.
