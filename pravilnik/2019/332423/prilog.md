PRILOG 1
SADRŽAJ INFRASTRUKTURE PROSTORNIH PODATAKA PREMA OBLASTIMA
1.1
Koordinatni referentni sistemi
Koordinatni referentni sistem je sistem za nedvosmisleno referenciranje prostornih informacija u prostoru u obliku koordinata (x,y,z) i/ili širine, dužine i visine, a koji se temelje na horizontalnom i vertikalnom geodetskom datumu;
Oblast predstavlja strukturu za prostorno referenciranje objekata pomoću koordinata. Ovom oblašću povezuju se odgovarajući standardi informacionih tehnologija i podaci, gdje god je to moguće, i osigurava okvir za razvoj aplikacija specifičnih za oblast, upotrebom geografskih podataka.
Prostorno koordinisanje odnosi se na odabrane tačke zemljine površine, npr. geodetske tačke, permanentne stanice sa satelitskim mjerenjima, repere ili mareografe.
Opseg, upotreba, primjeri:
Upotreba Globalnog navigacionog satelitskog sistema - Global Navigation Satellite System (GNSS) za precizno mapiranje zahtjeva posebne servise koje osiguravaju različite informacije i korekcije od referentnih GNSS stanica (stepen tačnosti 1 m do 1 cm).
MEST ISO 19111 može se koristiti kao osnova za implementaciju koordinatnog referentnog sistema u infrastrukturi za prostorne podatke.
Pravila za koordinatne referentne sisteme uzimaju u obzir da su referentni sistemi realizovani u realnom vremenu, npr. GNSS servisi osiguravaju korekciju u realnom vremenu.
Evropski referentni visinski sistem - European Vertical Reference System (EVRS) je visinski sistem povezan sa gravitacijom. Gravitaciono povezane visine koriste se kako bi opisale različite promjene vezane za životnu sredinu, npr. sve pojave vezane za nivo vode. Evropski kopneni referentni sistem 89 - European Terrestrial Reference System 89 (ETRS89) i EVRS mogu se implementirati u sistemu prostornih podataka u skladu sa MEST ISO 19111 uz restrikcije koje se odnose na kinematičke aspekte.
Koordinate se mogu transformisati u ETRS89 sistem sa decimetarskom prema metarskoj preciznosti.
Primjer operacija sa koordinatama u opsegu MEST ISO 19111 realizovan je kroz "Informacioni i servisni sistem za Evropski koordinatni referentni sistem, koji osigurava matematičke parametre za promjenu koordinata iz nacionalnog referentnog sistema u ETRS89.
Većina mrežnih servisa identifikuje referentne koordinatne sisteme upotrebom kodova Evropske grupe za istraživanje nafte - European Petroleum Survey Group (EPSG).
Važni tipovi objekata i atributi:
Važni objekti koji slijede izdvojeni su iz MEST ISO 19111 za:
a) Referentni koordinatni sistem:
•
Identifikator referentnog koordinatnog sistema;
•
Identifikator datuma;
•
Tip datuma;
•
Sidrena tačka datuma;
•
Datum realizacije epohe;
•
Datum valjanosti područja;
•
Identifikator elipsoida; i
•
Spljoštenost elipsoida.
b) Operacije koordinata:
•
Koordinatni identifikator;
•
Validno područje operacije koordinata;
•
Identifikator izvora referentnog koordinatnog sistema;
•
Identifikator cilja referentnog koordinatnog sistema;
•
Naziv metode operacije koordinata;
•
Formula metode operacije koordinata; i
•
Vrijednost parametra operacije koordinata.
Veze i preklapanje sa drugim oblastima - Referentni koordinatni sistemi su preduslov za uspješnu realizaciju svih oblasti prostornih podataka.
1.2
Geografski sistemi mreža
Geografski sistem mreža je usklađena mreža višestruke rezolucije sa zajedničkim ishodištem i standardizovanim položajem i veličinom mrežnih polja.
Mreža za predstavljanje tematskih informacija je sistem regularnih i georeferenciranih polja specifičnog oblika i veličine kao i pridruženog svojstva.
Geografske mreže su definisane i harmonizovane pan-evropske mreže standardizovanog položaja i veličine mrežnih polja (npr. 10x10 m, 100x100 m, 1x1 km, 16x16 km).
Mreža predložena kao pan-evropski standard odnosi se na ETRS89 Lambertov azimutni koordinatni referentni sistem jednakih površina sa centrom projekcije u tački N 52o, E 10o.
Obim, upotreba, primjeri:
Višestepeni evropski informacioni sistem zemljišta - Multiscale European Soil Information System (MEUSIS) razvijen je u okviru aktivnosti evropskog kabineta za zemljište i uključuje nacionalne premjere zemljišta i naučne institucije.
Sistem je baziran na geografskoj bazi podataka zemljišta - Soil Geographical Database of Europe (SGDBE) u razmjeri 1: 1 000 000. Referentna mreža MEUSIS-a bazirana je na mreži predloženoj od strane infrastrukture prostornih podataka.
Program saradnje za praćenje i procjenu prekograničnog prenosa zagađujućih materija u vazduhu na velikim udaljenostima u Evropi - Co-operative Programme for Monitoring and Evaluation of the Long-range Transmission of Air Pollutants in Europe (EMEP) je naučno baziran program u okviru Konvencije o prekograničnom zagađenju vazduha na velikim udaljenostima. Popis zagađenja vazduha baziran je na modelima koji koriste mrežni sistem dvije rezolucije: 50 km x 50 km i 150 km x 150 km, koji je baziran na polarnoj stereografskoj projekciji sa stvarnom površinom na širini N 60o i paralelom y-osi na W 32o. EMEP 50 sastoji se od matrice 132 x 111 tačaka, dok EMEP 150 domena uključuje 44 x 37 tačaka.
Atlas flore Evrope - Atlas Florae Europaeae (AFE) je projekat za mapiranje distribucije vaskularnih biljaka u Evropi, koji je pokrenut 1965. godine kao zajednički napor evropskih botaničara.
Hronološki podaci upisani su u kartu sa kvadratima 50 x 50 km, baziranoj na Univerzalnoj transverznoj Merkartorovoj - Universal Transverse Mercator (UTM) projekciji i vojnom mrežnom referentnom sistemu - Military Grid Reference System (MGRS). Vojni mrežni referentni sistem je ekstenzija UTM sistema. UTM broj zone i slovo zone koriste se da bi se identifikovala površina 6 stepeni u smjeru istok - zapad i 8 stepeni u smjeru sjever - jug.
Broj i indetifikator UTM zone prati 100 km kvadrat identifikatora, istočno - zapadni sistem koristi skup abecednih znakova za 100 km mrežu kvadrata. Počevši od 180-tog stepena meridijana znakovi A do Z (izuzevši I i O) koriste se za svakih 18 stepeni prije nego počnu ispočetka. Sjeverno od ekvatora koriste se znakovi od A do V (izuzevši I i O) za 100 km mrežu kvadrata, ponavljajući se svakih 2000 km. Sjeverni identifikatori normalno počinju na ekvatoru s "A" za neparne brojeve UTM istočne zone.
Sistem za praćenje rasta biljaka - Crop Growth Monitoring System (CGMS) mreža razvila se u okviru Praćenja poljoprivrede daljinskim istraživanjem -Monitoring Agriculture with Remote Sensing (MARS), odnosno prikupljanju meteoroloških podataka i podataka daljinskih istraživanja. Podaci su se transformisali i modelovali u parametre usjeva. Mreža je bazirana na Lambertovoj azimutnoj ekvivalentnoj projekciji sa ishodom projekcije u N 48o E 9o i sastoji se od 5625 ćelija, dimenzije 50 km x 50 km svaka.
Podaci statističke tačke i tačke razmjera konvertovani u mrežne elemente mogu biti neka druga površina upotrebe sistema geografske mreže. Postoji veliki broj praktične implementacije same konverzije, međutim ne postoji nacionalni standard u tom okviru.
Atmosferska i okeanografska brojna predviđanja ili klimatski modeli imaju 4-dimenzionalnu mrežu koja se mijenja relativno često (često na godišnjoj osnovi) kako se model (i super računaljka na kojoj se pokreće) razvija. Podaci tih modela razmjenjuju se pod Svjetskom meteorološkom organizacijom - World Meteorological Organization (WMO), specifikacijama podataka koji uključuju definiciju razmjene mreže u okviru metapodataka koji prate podatke. Definicija i registracija tih mreža isključena je iz nadležnosti ove klauzule iz razloga što su vrlo promjenjive i mogu biti specifične za implementaciju podataka. WMO odobrava opštu svrhu, malo orijentisan format razmjene podataka, određen FM 92-VII Ext. GRIB - Binarna koordinatna mreža - Gridded Binary (GRIB). Efikasan je za prenos velike količine mrežnih podataka prema automatizovanim centrima preko telekomunikacionih linija velikih brzina upotrebom modernih protokola. GRIB može jednako dobro služiti kao format za čuvanje podataka, generišući jednaku efikasnost relativno prema čuvanju podataka i uređajima za pronalaženje.
Nacionalni mrežni sistemi moraju se takođe uzeti u obzir jer se koristi velika količina podataka koja je georeferencirana. Ponekad su nacionalni mrežni sistemi bazirani na distribuciji listova nacionalnih topografskih karata. Mogućnost usklađivanja nacionalnog mrežnog sistema treba uzeti u obzir, međutim, čini se da je to dugoročan zadatak.
Važni tipovi objekata i atributi: Tipovi objekata i atributi zavise od oblasti podataka prikupljenih i održavanih u okviru mrežnog referentnog sistema. Najvažniji prostorni identifikatori za oblast 1.2 su kod mrežne ćelije, koji je opisan u dijelu iznad.
Sledeći objekti i atributi mogu biti relevantni:
Mrežna ćelija (površina, linija tačka)

Identifikator sistema mrežne ćelije;

Ime sistema mrežne ćelije;

Identifikator mrežne ćelije; i

Vrijednost mrežne ćelije.
Veze i preklapanja sa drugim oblastima: Glavni linkovi i preklapanja su tamo gdje su mreže korišćene za lokaciju registracije/mjerna mjesta, za agregaciju podataka za različite oblasti i za prikaz. Preklapanja s ostalim oblastima su:

Ortofoto snimci;

Prostorne statističke jedinice;

Zemljište;

Zdravlje ljudi i bezbijednost;

Rasprostranjenost stanovništva - demografija;

Atmosferski uslovi;

Meteorološko - geografske karakteristike;

Okeanografsko - geografske karakteristike; i

geografski razmještaji biljnih i iživotinjskih vrsta.
1.3
Geografski nazivi
Geografski nazivi su nazivi područja, regiona, mjesta, velikih gradova, predgrađa, gradova ili naselja ili bilo kojeg geografskog ili topografskog obilježja od javnog ili istorijskog značaja.
Geografski nazivi ili nazivi mjesta opisuju obilježja na Zemlji - položaja ili pezajžne objekte na kopnu i na moru. Često se termin topografski nazivi koristi kao naglasak na prostornoj zavisnosti i relacijama prema susjednim topografskim objektima.
Geografski nazivi za specifične objekte pejzaža mogu biti različiti na različitim jezicima. Višejezični aspekti trebali bi biti pokriveni u skupu podataka. U nekim skupovima podataka njihova primarna svrha je odrediti geografski položaj, a u drugima mogu biti atributi, zapravo sekundarne važnosti. Geografski nazivi trebali bi, u oba slučaja, biti dostupni i u službenom obliku (oblicima) i jeziku (jezicima) zemlje, uključujući manjinski jezik (jezike).
Obim, upotreba, primjeri: Skupovi podataka geografskih naziva obično su izrađeni od strane kartografskih agencija i lokalnih vlasti. Podaci geografskih naziva sa pan-evropskim pokrivačem postoje u Geografskom informacionom sistemu Komisije - Geographic Information System of the Commission (GISCO). (Infrastruktura prostornih podataka IMS, 2003).
Baza podataka geografskih naziva je prilagođena generalizovanju u verzijama/mjerilima, koja treba da osigura veze između edonima (oblik naziva koji se koristi u govornom jeziku na lokaciji geografskog objekta) i njegovog eksonima (oblici naziva korišćeni na različitim stranim jezicima).
Baza podataka geografskih naziva može se koristiti za:

Pretraživanje i pregled;

Lokaciju na svim slojevima;

Kao osnovni sloj na karti;

Efektivne operacije na lokalnoj nivou (npr. transport i hitne radnje); i

Dokumentovanje oblika geografskih naziva u manjinskim jezicima. (Infrastruktura
prostornih podataka IMS, 2003), (UNGEGN, 2002).
Registar geografskih naziva je geografski imenik. Prema definiciji MEST ISO 19112 registar geografskih naziva osigurava glavni zapis svih instanci lokacija za određeni tip ili tipove lokacije. Registri geografskih naziva nisu samo indeksi "geografskih naziva", nego mogu biti i zapisi bilo koje vrste tipa ili tipova objekata. Podaci o poziciji mogu uključivati koordinatnu referencu, ali mogu biti čisto opisni. (Infrastruktura prostornih podataka ETC, 2002).
Važni objektni tipovi i atributi:
Geografski nazivi:

Jezik;

Status (službeni, eksonim, edonim itd.);

Važnost (indicirana mjerilom karte);

Klasifikacija (tip objekta); i

Prostorna referenca; direktna u smislu koordinata i/ili indirektna u smislu veze sa
prostornim skupom podataka.
Veze i preklapanja s ostalim oblastima:

Adrese, iz razloga što je geografski naziv bitan element adrese.
Servis geografskih naziva je indirektan prostorni referentni sistem. Kao takav njegova važnost slična je referentnom koordinatnom sistemu. Geografski nazivi su atributi mnogim objektima koji se pojavljuju u ostalim oblastima, a posebno u Upravnim jedinicama, Hidrografiji i Visinama.
1.4
Administrativne jedinice
Administrativne jedinice su administrativne jedinice lokalne, regionalne ili državne uprave, koje razdjeljuju područja na kojima države članice imaju i/ili primjenjuju jurisdikcijska prava i koje su razdvojene upravnim granicama.
Službene administrativne jedinice su dostupne prema upravnim nivoima koje se koriste u državama.
Svaka
nacionalna
teritorija
podijeljena
je
prema
upravnim
jedinicama. Administrativne jedinice podijeljene su administrativnim granicama. Definicija je predstavljena tako da ne uključuje Administrativne jedinice kao što su popisni krugovi, poštanske regije i ostale specifične regije. Administrativne jedinice i administrativne granice stvaraju dijelove prostora.
Obim, upotreba, primjeri:
Podaci upravnih jedinica upotrebljavaju se za:

Poslovanje i upravljanje;

Pokazivanje nadležnih tijela;

Referenciranje podataka i statistike;

Osnove za proizvodnju statističke karte koja prikazuje ekonomske fenomene,
demografiju itd.;

Kao referenca za ispravljanje lokacije objekata; i

Za izrezivanje (cookie cutting) baza podataka. (Infrastruktura prostornih podataka IMS,
2003).
Upravna podjela stvara indirektni prostorno referentni sistem. Referenca na prostornu jedinicu osigurava prostornu dimenziju prema podatku, bez upotrebe koordinata (Infrastruktura prostornih podataka IMS, 2003).
Administrativne granice su ključ horizontalne operabilnosti između proizvoda čuvara nacionalnih podataka. Susjedi bi se trebale složiti oko međunarodnih granica i moguće rezolucije na mjestima gdje dijele geometriju (Infrastruktura prostornih podataka RDM, 2002).
Referentni datum upravnih jedinica treba uzeti u obzir u svrhu povezivanja na statističke informacije, kao na primjer broj stanovnika.
Primjer upotrebe: Evropska granična mapa - EuroBoundary Map (EBM), pan-Evropski skup podataka administrativnih granica proizveden i distribuiran od strane EuroGeographicsa od 1995. EBM osigurava informacije o geometriji i hijerarhijskoj strukturi administrativnih jedinica u Evropi, zajedno sa vezom na odgovarajuće kodove Nomenklature statističkih teritorijalnih jedinica - Nomenclature of Territorial Units for Statistics (NUTS). Putem NUTS kodova korisnik može povezati NUTS bazirane statističke informacije s prostornim podacima od EBM-a. Ovo služi u mnogim područjima primjene kao što su:

Analize tržišta;

Upravljanje imovinom;

Georeferenciranje demografskih analiza;

Tematsko planiranje;

Referenciranje prekograničnih statističkih podataka; i

Georeferenciranje demografskih analiza.
Projekt DIAMONT, kojim upravlja Evropska akademija u Italiji, koristi EuroBoundaryMap kao referentnu informaciju pri savjetovanju Alpine Konvencije o stvaranju Alpine informacionog sistema (SOIA) i odabiru prikladnih indikatora i relevantnih podataka za održivi regionalni razvoj. Još jedan primjer je Evropska agencija za životnu sredinu koja mapira NUTS bazirane informacije o nivou organske proizvodnje na administrativnoj podjeli Evrope.
Važni objektni tipovi i atributi:
Upravna jedinica:

Naziv: službeni naziv administrativne jedinice na službenom jeziku (cima);

Državni upravni nivo (prvi nivo, drugi nivo, …);

Državni kod: službeni kod administrativne jedinice korišćen od strane Državnog zavoda
za statistiku;

Veze sa statističkim kodovima kao što su NUTS i Lokalne administrativne jedinice -Local
Administrative Units (LAU); i

Kod države prema MEST ISO 3166 definiciji.
Administrativna granica:

Nivo administrativne granice (međunarodna, prvi, drugi nivo, …); i

Status (npr. definitivno, u sporu, isključiva ekonomska zona, teritorijalno more) .
NUTS i LAU nomenklature koriste se na ukupnom evropskom nivou u kontekstu Infrastrukture prostornih podataka se mogu smatrati od veće koristi i na nižim nivoima. Nomenklatura teritorijalnih jedinica za statistiku (NUTS) uspostavljena je od strane evropskog zavoda za statistiku (EUROSTAT) kako bi osigurala jednu jedinstvenu podjelu teritorijalnih jedinica za stvaranje regionalnih statistika za Evropsku Uniju. NUTS isključuje specifične teritorijalne jedinice i lokacijske jedinice u korist regionalnih jedinica opšte prirode. Na detaljnijem nivou postoje četvrti i opštine. Zovu se Lokalne administrativne jedinice (LAU, Local Administrative Unit) i nisu subjekti NUTS regulacije. Na vrhu hijerarhije su individualne zemlje članice Evropske unije, ispod su NUTS nivoi 1 do 3 pa LAU nivo 1 i 2. NUTS područja nužno se ne poklapaju sa državnim upravnim jedinicama.
Veze i preklapanja s ostalim oblastima:
Glavna preklapanja su:

Hidrografija: obalna linija ima bitnu ulogu u mnogim aplikacijama koje razdvajaju kopno
od vodene površine. Obalna linija trebalo bi da se integriše u podatke administrativnih
jedinica. Administrativne granice se mogu podudarati sa vodenim tokovima ili obalom;

Geografski nazivi: nazivi upravnih jedinica;

Katastarske parcele: Upravna jedinica poklapa se sa većinom ali ne u svim slučajevima
katastarskih granica ili zemljišnim knjigama;

Prostorne jedinice za statistiku; i

Područja upravljanja/zaštićena područja/uređena područja i jedinice za izvještavanje:
upravni organi često su organizovani prema upravnim jedinicama.
1.5
Adrese lokacija nepokretnosti
Lokacija objekata koja se zasniva na identifikatorima adrese, a to su najčešće naziv ulice, kućni broj i poštanski broj.
NAPOMENA: Osim naziva ulice, kućnog i poštanskog broja, sve ostale komponente predstavljaju geografke nazive (grada, sela, opštine, naselja, predgrađa, administrativne jedinice).
Adresa je identifikacija i sažet pojam koji izražava fiksni položaj i put pristupa do kuće, poslovne ili druge zgrade (objekta) ili zemljišne parcele (vlasništva). Potpuna adresna identifikacija je hijerarhija koja se sastoji od komponenti kao što su geografski nazivi, sa većim brojem detalja, npr. grad, ime ulice, adresni broj (ili broj zgrade) pored poštanskog broja. Adrese mogu poslužiti u nekoliko svrha: funkcija lokacije (npr. za posjetu ili dostavu pošte), funkcija identifikacije (u kontekstu registracije zgrade), funkcija jurisdikcije (koji organ vlasti je odgovoran za objekat povezan sa adresom) i funkcija sortiranja i naručivanja.
Pod nekretninom se može indetifikovati nekoliko različitih tipova objekata: zemljišne parcele, zgrade (uključujući stanove), a nekada takođe drugačiji tipovi kao npr. vodovi. Za zgrade (sa stanovima) u većini slučajeva postoji povezanost s adresom. U ruralnim područjima postoje zgrade bez potpune poštanske adrese, npr. samo ime grada i ulice bez kućnog broja. Isto tako i u urbanim područjima: npr. zgrade vodova. Napomena: registracija adresa trenutno nije usklađena u Evropi. Ostali objekti koji nisu zgrade, a koji mogu imati adresu uključuju sportske terene, (službenu) lokaciju pokretne kućice (prikolice ili prikolice za stanovanje) ili lokaciju broda - kuće (mjesto sidrišta).
Opseg, upotreba, primjeri: Danas se, adrese i informacije o adresama naširoko koriste u brojne svrhe unutra poslovnog, javno administracionog i građanskog svakodnevnog života. U velikom broju aplikacija, informacije o adresi upotrebljavaju se kao zajednička administrativna referenca, geografski identifikator i mehanizam za povezivanje. Kao slični referentni sistemi (npr. naziv mjesta, katastar), podaci o adresi ispunjavaju zahtjev da budu referentni podaci. Informacije o adresama mogu se, zato što se često smatraju u poštanskom kontekstu, ne smatrati pravim geoinformacijama na prvi pogled. Kako je najvažnija komponenta adrese fizička lokacija, ona je geoinformacija. Adrese se koriste za povezivanje s ostalim različitim izvorima administrativnih informacija koje mogu biti povezane s lokacijom putem adresa.
"Prostorno referenciranje geografskim identifikatorima" opisuje metode koje specifikuju prostorne reference putem drugih geografskih objekata (kao što su ceste). Ovaj standard opisuje kako izgraditi hijerarhijski registar geografskih naziva sa mogućnošću kreiranja jedinstvenog geografskog identifikatora, upotrebom veze roditelj-dijete. Adrese se često prikazuju u rječnicima geografskih naziva (npr. svi gradovi u regiji, svi nazivi ulica u gradu, svi kućni brojevi duž ulice). Takođe, jasno je da su često u jednoj zemlji različite organizacije odgovorne za različite aspekte adresa (npr. država za službene nazive gradova, službenih cesta i kućnih brojeva, poštanski servisi za poštanski broj), što konstantno ažuriranje adresa čini netrivijalnim zadatkom.
Iako svi nacionalni ili lokalni adresni sistemi dijele jednaki koncept i opšta svojstva, postoji razlika u formalnom i neformalnom standardu, pravilima, šemama i modelima podataka u Evropi. Razlika takođe postoji u proširenju adresnog sistema npr. u ruralnom području. Isto tako, način na koji su brojevi kuća dodjeljeni, može se u potpunosti razlikovati (i usklađivanje je dobrodošlo). Brojne alternative su sljedeće:
- Kućni brojevi su u sekvencama njihovih lokacija u ulice (desno/lijevo imaju neparne/parne
brojeve, a najniži brojevi su prema centru grada). Kad podvučemo crtu, dolazimo do toga da
to i nije predinamično: dodavanje jedne nove zgrade ili novog ulaza zahtijeva dodavanje
slova nakon brojevi ili slične trikove kao što su brojevi koji nisu u upotrebi. U nekim
zemljama slova nakon brojki čuvaju značajne informacije, dok je u ostalim zemljama to
način da se kreira jedinstvena oznaka.
- Brojevi kuća su u sekvencama, što je lako za realizaciju, a sigurno se osiguravaju jedinstveni
brojevi. Međutim, korisnicima ovog sistema vjerovatno će biti teško pronaći pravu lokaciju.
- Kućni brojevi su izvedeni iz udaljenosti od početka ceste (ulice); na primjer u urbanim
područjima svakih 10 metara ide broj, a u ruralnim svakih 100 metara ide kućni broj (čak
iako ne postoji kuća). Promjenom iz urbanog u ruralno dodaje se jedan broj.
- Ne upotrebljavaju se kućni brojevi već direktno (2D i 3D) geografske koordinate.
Katastri i zemljišne knjige ne sadrže u svim slučajevima i registar adresa (povezan s koordinatama). U većini slučajeva jedinice lokalne samouprave su odgovorne za uspostavljanje naziva ulica i kućnih brojeva, državna pošta za poštanske brojeve. Održavanje nije jedinstveno. Ulazna vrata ili centralne koordinate uglavnom su dostupne u referentnom koordinatnom sistemu koji se upotrebljava širom zemlje.
Važni tipovi objekata i atributi: Glavni tipovi objekata su adrese sa vezama prema drugim objektima kao što su katastarske parcele, (stanovi) zgrade i ostali nepokretni registrovani objekti (kao što su vodovi). Relevantni u kontekstu ove oblasti (oblasti) su, kao prvo, identifikatori nekretnina (eventualno bazirani na hijerarhiji upravnih jedinica), sljedeći su atributi koji povezuju to sa adresom i/ili referentnom koordinatom objekta i eventualno naslednikom/prethodnikom (npr. promijenjeno ime ulice ili kućni broj).
Važni atributi adresa su: poštanski kod, geografska koordinata referentne tačke adrese, grad, ulica, kućni broj (i aneksi) i tekstualni opis. U nekim područjima vodeni putevi mogu igrati ulogu ulice. U međunarodnom kontekstu, relevantna je i specifikacija države (MEST ISO 3166-1). Na ostalim nivoima mogu se spomenuti država, opština, itd.
Uloga popisa odobrenih predmeta često je važan dio standarda: odobreni službeni nazivi gradova (na više jezika), ulica, poštanskih brojeva itd.
Adrese ne bi trebalo smatrati samo kao identifikatore parcela, zgrada ili nekih drugih objekata. Adresa kao takva, je stavka (funkcija, objekat) koja ima atribut lokacije, tipa geometrije (tačka ili površina). Objekat (klasa objekta) "adresa" može biti povezana sa ostalim objektima npr. parcelom, zgradom, naseljem, autobuskom stanicom, odlagalištem limenki ili poštanskim sandučićem. Svi primjeri fenomena stvarnog svijeta koje možda želimo pronaći putem adrese.
Veze i preklapanja sa ostalim oblastima:
Postoje snažne veze sa:

Geografskim nazivima;

Zgradama;

Katastarskim parcelama;

Prometnim mrežama (za ime ulice i broj ceste); i

Upravnim jedinicama.
Mnoge zemlje imaju registre zgrada. Jedna zgrada može se sastojati od više jedinica (a ponekad su grupisane na specifičan način, ulazima). Ti registri, takođe, često uključuju zgrade sa građevinskim dozvolama. Adrese su vezane za (stanove) zgrade, izuzevši poštansku sandučad. Ne postoji relacija 1:1 između adresa i parcela (ili zgrada). Mnoge adrese mogu biti povezane sa nulom (poštanski sanduci), jednom ili više parcela (zgrada sa stanovima). Adrese ne pokrivaju sve jedinice vlasništva u zemlji, posebno na selu. Za zemljišne parcele bez zgrada vjerovatno neće postojati kompletna poštanska adresa, nego samo indikacija naziva ulice, a za objekte nekretnina kao što su vodovi vjerovatno će to biti još teže. Adrese stoga ne mogu biti prikladne za jedinstvenu katastarsku identifikaciju. Operacija u kojoj se dobijaju koordinate povezane sa adresom zove se geokodiranje. Za stanove to mogu biti čak 3D koordinate (ili 2D koordinate, sa indikacijom nivoa). Zgrada (ili parcela) može imati više od jedne adrese (npr. zgrada je locirana na uglu ulice).
1.6
Katastarske parcele
Katastarska parcela je dio područja katastarske opštine, odnosno katastarskog područja na moru, određen brojem parcele i njenim granicama.
Katastarska površina je zasebna površina zemljišta ili detaljnije volumen prostora sa homogenim pravima nad nekretninom i jedinstvenim vlasništvom.
Napomena: Pod jedinstvenim vlasništvom smatra se da vlasništvo pripada jednom ili nekoliko vlasnika za cijelu katastarsku parcelu. Pod homogenim pravima nad nekretninom misli se da se prava vlasništva, zakupa i založnog prava odnose na cijelu parcelu. Ovo se ne odnosi na specifična prava kao pravo služenja koja mogu imati uticaj samo na dio parcele.
Katastar je definisan kao registar pod nadležnošću države. Pristup katastarskim informacijama definisan je propisima koji štite lične informacije. Osnovna jedinica katastra je katastarska parcela. Iste mogu biti grupisane u katastarske opštine. Katastarska parcela ima svoj jedinstveni identifikator nekretnine (broj katastarske parcele). Prostorni opis katastarske parcele i ostalih katastarskih objekata dat je uz odgovarajući stepen tačnosti. Opisni podaci mogu uključiti prirodu, veličinu, vrijednost i zakonska prava ili ograničenja povezane sa svakim odvojenim zemljišnim objektom iznad ili ispod površine. Katastarske parcele bi trebalo da prekrivaju teritoriju cijele države i ne bi trebalo biti preklapanja ili rupa (u stvarnosti). Izuzetak od ovog pravila može biti državno zemljište (ili javno) koje nije registrovano u katastru (iako ovo nije preporučeno u praksi).
Opseg, upotreba i primjeri: Raspon katastarskih informacija ograničen je na geografsku stranu katastarskog informacijskog sistema (zemljišna administracija) i ne pokriva administrativnu ili zakonsku stranu sa objektima kao što su prava i osobe. Međutim, parcela ima snažnu vezu sa tim objektima pošto je definicija bazirana na tome.
Svaka zemlja (zemlje mogu biti u federacijama) u Evropi ima katastarski ili zemljišno informacioni sistem koji je operativan, često kao odgovornost državnih organizacija ili odgovornost više lokalne vlasti. Zbog različitih pravnih sistema i različite nacionalne tradicije, postoji bogata različitost katastarskih sistema. Kako je ova interoperabilnost limitirana (u kontekstu Evropskog zemljišnog informacionog sistema -European Land Information Service (EULIS) i rezultati su visoki troškovi razvoja i održavanja sistema, nevladine (međunarodne) organizacije, kao što je Međunarodna federacija geodeta-International Federation of Surveyors (FIG), razvile su osnovni model katastarskog domena - core cadastral domain model (CCDM). CCDM je podnesen i prihvaćen od strane MEST ISO TC211 odboru kao novi radni prijedlog, ali mu je ime promijenjeno u Model domena zemljišne administracije- Land Administration Domain Model (LADM) kao rezultat komentara tokom ovog procesa.
Sistem katastarskih i zemljišnih informacija formira važan dio sistema zemljišne administracije zemalja. Katastarske aktivnosti povezane su sa integrisanom kreacijom i ažuriranjem alfanumeričkih i grafičkih informacija parcele tokom životnog ciklusa parcele. Katastarske organizacije u svakoj zemlji članici su te javne organizacije koje imaju specifičnih zakonska ovlašćenja u kreiranju i ažuriranju alfanumeričkih i grafičkih georeferenciranih informacija zemljišne parcele ili njenih koordinata na državnom nivou (PSS, 2003).
Nalazimo različite situacije u katastrima Evropske unije. Katastri su oduvijek institucije koje su u skladu sa evropskim javnim modelom, iako sa velikim rasponom mogućih varijacija. Ukratko, može se istaknuti da, dok je u nekim zemljama dizajniran katastarski model povezan sa gruntovnicom sa funkcijom povećanja sigurnosti na tržištu nekretnina, ostale zemlje stavile su veću pažnju probleme sa porezom i podsticanje poljoprivrednih i globalnih razvojnih aktivnosti. Katastarske organizacije osiguravaju podatke građanima za mnoge svrhe, javnu administraciju i za različite sektore društva. One mogu imati različite ciljeve, svrhe i administrativnu pripadnost te upravljačke modele od jedne do druge zemlje.
Važni tipovi objekata i atributi:
Glavni geografski tipovi objekata su parcele, granice i tačke (razmjer). Glavni administrativno zakonski tipovi objekata su prava (zabrane, odgovornosti) i lica (fizička i pravna), koje dalje neće biti objašnjavane (van opsega ove oblasti). Važni atributi su geometrija (tačka, linija zavisno o objektu, a može biti granični okvir za laganiji pristup), izvor podataka (referentni terenski dokumenti, terenska skica i datoteke totalne stanice ili Globalni satelitski navigacioni sistem - Global Navigation Satellite System (GNSS) instrumenti ili na primjer id fotogrametrijskog projekta), kvaliteta (tačnost), zakonske površine (uključene u službena zakonska dokumenta, uopšteno ta površina nije jednaka površini izračunatoj iz prostornih katastarskih ivičnih tačaka na granicama) i ponekad takođe vrijednosti i upotrijebljeni kodovi. Zakonska površina možda neće moći uvijek biti dostupna. Prava imaju sljedeći atributi: tip prava (zemljišno, zavisno), udio u pravu, vremenska specifikacija prava (može biti limitirana), reference prema zakonskim izvorima, dokumenta i veze sa hipotekom koja može biti na pravu (ili bolje RRR= Right, Restriction, Responsibility, PZO=Prava, Zabrane, Odgovornosti).
Katastarske parcele moraju imati jedinstveni identifikator nekretnine na koji je "prikačen" zakonski status. Taj identifikator može biti baziran na hijerarhiji administrativnih površina (provincija/okruga/kantona/…, /opštine/…., sekcije/poligona/…) i ponekad na "majci" parceli (podbroj parcele…./…./…. 37 misli se na primjer .../..../..../37/1 i ..../..../..../37/2). Na evropskom nivou, nacionalni identifikatori trebali bi dobiti kod države kao prefiks kako bi se učinili jedinstvenima u Evropi. Alternativno može postojati eksplicitna veza između prethodnika i nasljednika. Katastarske informacije trebale bi se održavati u kontinuitetu kako bi se reflektovala aktuelna zakonska situacija. Naravno, u stvarnosti i u pružanju informacija moglo bi biti blagog kašnjenja. Zbog pravne važnosti, arhivska komponenta se trenutno održava u nekim zemljama, ali to bi moglo biti potrebno u mnogim zemljama.
Osim vlasništva, katastarske parcele ili da budemo uopšteniji nepokretne nekretnine, mogu se povezati sa ostalim tipovima stvarnih prava (plodouživanje, površina, dugoročni zakup,…), odgovornosti i zabrana. Linija gdje se nepovezanost u specifičnim zakonskim situacijama pojavljuje je katastarska granica. Čvorne tačke granice mogu se označiti na terenu (ili ne). U mnogim slučajevima dostupne su terenske skice i opažanja. Opažanja (postojeće koordinate, uglovi i udaljenosti) upotrebljavaju se kako bi se odredile koordinate; te koordinate prilagođene su katastarskoj karti. Trenutna praksa je izraziti koordinate na katastarskoj karti u državnom koordinatnom sistemu. U budućnosti bi se to moglo promijeniti u evropski terestički referentni sistem (ETRS89), zbog 1. sve više i više GNSS (Geografski informacioni sistem -Geographic Information System -GPS, Globalni navigacioni satelitski sistem -Global Navigation Satellite System- GLONASS i Evropsli globalni navigacioni satelitski sistem -Europe's Global Navigation Satellite System -Galileo) mjerenja biće korišćeno u prikupljanju podataka i 2. ovo će omogućiti bolju konzistentnost podataka blizu međudržavnih granica u Evropi.
Granica ima i nekoliko vlastitih atributa. Terenske skice (ili mjerni planovi) mogu se upotrijebiti kod rekonstrukcije granice. Iz tehničkog ugla gledanja skup povezanih granica ponekad je spremljen kao zatvoreni poligon sa rizikom od pojave rupa i preklapanja između parcela (problem kvaliteta u bazi podataka, ne u stvarnosti). Ovo takođe ukazuje da bi se svaka granica trebalo sačuvati barem dva puta (na lijevoj i desnoj parceli), što je preklapanje.
Dalje, granice takođe imaju svoje vlastite atribute, koji se moraju pričvrstiti na specifičnu instancu (što bi značilo tri reprezentacije). Kako bi se to izbjeglo često se upotrebljava predstavljanje parcele bazirano na topološkoj strukturi. Uglavnom granice nemaju smisleni (bazirano na administrativnoj hijerarhiji) identifikator, ali mogu biti povezane sa terenskim skicama (koje imaju neki smisleni potpuni identifikator, poznat u spoljnom svijetu).
Prostor postaje sve više i više oskudan, kako ljudi kreiraju konstrukcije iznad i ispod jedni drugih. U mnogim evropskim zemljama zakonsko rješenje za to je kreativnost. Jedna mogućnost za registrovanje rezultirajuće nekretnine je korištenje 3D volumenske katastarske parcele (bazirane na 3D planovima mjerenja ili terenskim skicama).
Sljedeći temeljni atributi katastarskih parcela identifikovani su od strane zajedničke radne grupe Stalnog komiteta za katastar-Permanent Commeetee on Cadastre PCC i Eurografike - EuroGeographicsa (WG-CPI, 2006, napomena da ovi osnovni atributi moraju postojati u digitalnom obliku):

Jedinstveni identifikator;

Površina;

Granice;

Georeferenciranost (u državnom koordinatnom sistemu); i

Porijeklo i istorija parcele.
Sljedeći dodatni sadržaj katastarskih parcela identifikovan je od strane zajedničke radne grupe PCC-a i EuroGeographicsa (WG-CPI, 2006). To ne znači sa su ove oblasti nužno dio odgovornosti katastarske administracije. Neke oblasti uspostavljaju veze sa drugim oblastima infrastrukture prostornih podataka (npr. Adresama i Zgradama) i opet neke oblasti su sigurno van infrastrukture prostornih podataka (vlasnik, korisnik, u tim slučajevima uključene su samo reference, ali ne i sam sadržaj):

Vlasnik;

Korisnik;

Prava i zabrane;

Lokalizacija;

Administrativne granice (granice administrativnih jedinica);

Zgrade ili dijelovi zgrada i sve vrste građevina;

Službene zone (administrativne zabrane);

Iskoristivost zemljišta: način na koji se zemlja koristi, uključujući prirodu vegetacije po
njenoj površini. Radna grupa za upravljanje zemljištem, koja radi pod pokroviteljstvom
UN-ECE Komiteta za ljudska naselja -Working Party on Land Administration, operating
under the auspices of the UN-ECE Committee on Human Settlements (WPLA);

Prekrivenost tla (vegetacija, usijevi, šuma);

Vrijednost/stepen produktivnosti;

Adresa/e; i

Opis.
Potrebno je napomenuti da model katastarskih parcela može biti generalizovan i tada primijenjen na ostale tematske podatke i komponente skupova podataka (npr. zaštićena područja). Odnosno, sličan uzorak modela može se ponovno pojaviti u okviru modela za različite oblasti-oblasti podataka; npr. uzorak "prostorni objekt - veza (prava/zabrane/odgovornosti) - osoba" ili uzorak "objekat mjerenja (opažanje i razmjera) - rezultira prostornim objektom (interpretacija)". Preporučuje se da se neke od ovih oblast i komponenti uzmu u obzir na višem nivou pri identifikaciji tih sličnosti u ranoj fazi i da se pobrine da su rezultirajući modeli usklađeni, odnosno bazirani na istom uzorku modela. Međuvladin odbor Australije i Novog Zelanda o premjeru i mapiranju harmonizovanih modela podataka daje primjer ovog pristupa i ima takođe niz sličnosti sa osnovnim modelom katastarskog domena - core cadastral domain model - CCDM pristupom.
Još jedan relevantno opažanje od strane CCDM rada je to da je preporučeno koristiti modularni pristup po dobroj praksi jedinstvenog jezika za modelovanje - Unified Modeling Language UML modeliranja (dijeljenje modela u pakete). Takav pristup je posebno koristan za infrastrukturu prostornih podataka zato što dopušta da odgovornosti za upravljanje različitim komponentama modela budu pridružene najprikladnijoj grupi. Jednostavnost svakog paketa je izričit cilj dizajna, kako paket postaje složeniji teže je dati skladne podatke.
Veze i preklapanja sa ostalim oblastima: Granica može samo biti granica parcele i/ili granica administrativne jedinice (opština, pokrajina, država; to je važna relacija sa oblašću 4.
Parcele i granice imaju veze sa Zgradama - ponekad korišćene kao lokalna referenca za granice, ali takođe i u orijentacione svrhe.
Parcele i granice imaju veze sa Saobraćajnim mrežama - istu orijentacionu svrhu, ali ulice, željeznice, vodeni putevi takođe su odvojene parcele pošto su često u vlasništvu države.
Čvrsta veza postoji između Katastarskih parcela i Adresa.
Veze postoje između Katastarskih parcela, Korišćenja zemljišta i Zemljišnog pokrivača.
1.7
Saobraćajne mreže koje obuhvataju saobraćajne, željezničke, vazdušne i vodene
saobraćajne mreže, elektronske komunikacione mreže i prateću infrastrukturu
Mreže uličnog, željezničkog, vazdušnog i vodenog prevoza te pripadajuća infrastruktura. Uključuje veze između različitih mreža.
Saobraćajna komponenta trebalo bi da obuhvati integrisanu saobraćajnu mrežu i sa njom povezane objekte, koja je neprekidna u okviru državne granice. U skladu sa članom 10.2 Infrastrukture prostornih podataka, nacionalne saobraćajne mreže mogu takođe biti neprekidne na Evropskom nivou, npr. spojene na državnim granicama. Saobraćajni podaci uključuju topografske objekte povezane sa uličnim, željezničkim, vodenim i vazdušnim saobraćajem. Važno je da su uspostavljeni objekti koji sačinjavaju mrežu, gdje je to prikladno, i da budu uspostavljene veze između različitih mreža, npr. višestruka čvorišta, posebno na lokalnom nivou kako bi se zadovoljili zahtjevi za pametnim saobraćajnim sistemima kao što su lokacijski bazirani sistemi i telematika. Saobraćajna mreža trebalo bi reflektovati tok saobraćaja kako bi se aktivirali navigacijski sistemi.
Ruta je jedna vrsta apstraktnih ili nevidljivih objekata koje opisuju prostorne servisi ponuđene u saobraćajnom sistemu. Autobuske linije, trajektne linije, biciklističke rute mogu biti primjeri informacija o linijama. Obično su veze ili segmenti saobraćajnog sistema spojeni zajedno stvarajući rutu, ali mogu egzistirati i kao odvojeni podaci o objektima. Trebalo bi razjasniti ako su takvi podaci uključeni u ovu oblast ili nisu, kako se kroz podatke Infrastrukture prostornih podataka i mrežne servise mogu podržati takve informacije o ruti.
Opseg, upotreba i primjeri:

Sistemi usmjeravanja, upravljanje saobraćajem;

Procjene životne sredine;

Sigurnost;

Upravljanje katastrofama i hitnim situacijama;

Socijalno i ekonomsko planiranje itd.;

Planiranje saobraćaja;

Planiranje iskoristivosti zemljišta; i

Upravljanje rizicima (Infrastruktura prostornih podataka IMS, 2003).
Važni tipovi objekata i atributi:
Za uličnu mrežu
Putna veza:

Vrsta puta (put za motorna vozila, dvosmjerna, jednosmjerna, obilazak….);

Funkcionalne klase puta (važne za saobraćaj);

Broj puta;

Ime puta;

Stanje (iskorišćena, u izgradnji, funkcionalna); i

Površina puta (asfaltirana, neasfaltirana).
Most, tunel
Tačkasti objekat puta:

Vrsta tačke (čvorište, obilazak);

Broj tačke; i

Ime tačke.
Za vodenu mrežu:

Plovni kanali (morski), plovne vode (na kopnu - rijeke/kanali);

Trajektna linija; i

Luka.
Za željezničku mrežu
Veza sa željeznicom:

Tip željeznice (brza, tramvaj,…);

Stanje objekta (iskorišćena, u izgradnji, funkcionalna);

Klasifikacija željezničkog kolosijeka; i

Energija (električna ili ne).
Most, tunel
Željeznička stanica:

Ime;

Stanje objekta; i

Funkcija (putnička, teretna, oboje).
Za vazdušni saobraćaj
Aerodrom:

Ime;

ICAO identifikator (Međunarodna organizacija za civilno vazduhoplovstvo -
International Civil Aviation Organization -ICAO), IATA identifikator (Međunarodna
asocijacija za vazdušni transport - International Air Transport Association -IATA).
Heliodrom:

Ime.
U pogledu plovidbenih servisa moglo bi biti korisno zadržati navigacijske atribute na putnoj mreži (smjer toka, zabrane pristupa, sezonske zabrane, ograničenja brzine,…).
Veze i preklapanja sa ostalim oblastima:
Glavna preklapanja su:

Hidrografija kao vodena mreža dio je i hidrografije i saobraćaja;

Adrese: putna veza može nositi korisne informacije o adresama; i

Korišćenje zemljišta, kao put su kategorija u podacima korišćenja zemljišta i planiranim
podacima iskoristivosti zemljišta.
1.8
Hidrografija Hidrografski elementi, uključujući morska područja i sva druga vodena tijela i sa njima povezane pojedinosti, uključujući riječne bazene i pod-bazene. Prema potrebi, u skladu sa odredbama koje su utvrđene u propisima kojima je uređena oblast voda na području politike voda i u obliku mreža.
Oblast "Hidrografija" pokriva mrežu rijeka, jezera i morskih područja. "Statički" objekti su u oblasti "Hidrografija", a "dinamički" objekti, kao što su nivo vode, nalaze se u povezanim oblastima u grupi III.
Oblast takođe uključuje riječne slivove. Riječni slivovi, prema definiciji u propisima kojima je uređena oblast voda podrazumijeva površinu kopna od kojeg sva površinska oticanja teku kroz dijelove potoka, rijeka i eventualno jezera u more na jednom ušću, razvodu ili delti. Podsliv označava površinu zemlje iz koje sva površinska oticanja teku kroz niz potoka, rijeka i eventualno jezera u određenu tačku u vodenom toku, uglavnom ušću jezera ili rijeke.
Podzemne vode su takođe važan dio hidrološkog ciklusa voda, ali opisuju se u oblasti Geologija.
Opseg, upotreba i primjeri:
Hidrografski podaci upotrebljavaju se u: (Infrastruktura prostornih podataka IMS, 2003)

Vodenoj navigaciji/saobraćajnim rutama;

ekološkom turizmu;

Procjeni i nadzoru u procjeni vodenih resursa;

Procjeni uzoraka taka čestica i zagađivača, nadzor zagađenja;

Procjeni prečišćavanja otpadnih voda;

Procjeni migracija vrsta i biodiverziteta, hidrološkim elementima budućih staništa;

Upravljanju unutrašnjim ribolovom

Opasnim deponijama

Upravljanju, planiranju iskoristivosti zemljišta

Upravljanju i planiranju rekreacije

Transportnim rutama

Snadbijevanje vodom.
Vodeni slivovi upotrebljavaju se u procjeni protoka vode i poplavama, protoku zagađivača, praćenju erozije. Slivovi se upotrebljavaju za kreiranje propisa o vodama, upravljanje riječnim slivovima okruga, ali nemaju potpunu podudarnost sa granicama.
Politika Savjeta:

u propisima kojima je uređena oblast voda, uspostavljanje okvira za akcije zajednice u
polju politike voda; i

Upravljanje rizicima od poplava; prevencija poplava, zaštita i ublažavanje.
Propis kojima je uređena oblast voda i uspostavlja okvir za akcije zajednice na polju politike voda i uključena je u zakonske okvire. Zahtijeva da unutrašnje i priobalne vode unutra definisanih okruga riječnih slivova dostignu status 'dobar' do 2015. i definišu kako bi se to trebalo postići kroz uspostavljanje ciljeva zaštite životne sredine i ekoloških ciljeva.
Propisima kojima je uređena oblast voda zahtijeva baratanje prostornim podacima, zajedno sa pripremama Planova upravljanja riječnim slivovima i za izvještavanje Komisije. U prvom slučaju, GIS tehnike će biti neophodne kod izvođenja različitih nivoa informacija (o karakteristikama riječnih slivova i vodenih tijela, o hemijskim i ekološkim statusima vodenih tijela - plovnih objekata), dok će u drugom slučaju GIS biti alat za pripremu i dostavu GIS slojeva koji su potrebni za izvještavanje.
Važni tipovi objekata i atributi:
Vodeni tok:

Ime;

Hidrološki kod (u propisima kojima je uređena oblast voda);

Hidrološka postojanost (trajna, povremena);

Kategorija hidrografskog porijekla (prirodno, vještačko);

Tip (potok, kanal, akvadukt, jarak, estuarij,…, virtualni);

Pozicija/tlo; i

Plovnost.
Jezero, bara:

Ime (ako postoji);

Hidrološki kod (u propisima kojima je uređena oblast voda);

Hidrološka postojanost (trajna, povremena); i

Kategorija hidrografskog porijekla(prirodno, neprirodno).
Ostali objekti na vodenoj mreži kao što su slap, brana, ustava, nasip.
Izolovane vodene infrastrukture, kao što su fontane, crpne stanice.
Riječni sliv:

Ime;

Hidrološki kod (u propisima kojima je uređena oblast voda); i

Hidrološki nivo ("administrativna važnost").
Morska područja:

Kategorija (prelazne vode, obalne vode);

Ime (ako postoji); i

Hidrološki kod (u propisima kojima je uređena oblast voda).
Veze u preklapanja sa ostalim oblastima:
Glavne veze s ostalim oblastima:

Saobraćajne mreže - navigacija na vodi (Aneks I)

Geografski nazivi- nazivi plovnih objekata;

Visine - geometrijska konzistentnost i obalna linija;

Pokrivenost zemljišta - močvare, plovni objekti (Aneks II);

Geologija - za vodonosnike;

Komunalne i javne servisi - za snadbijevanje vodom;

Sistemi za nadzor životne sredine;

Proizvodna i industrijska postrojenja - objekti za eksploataciju vode;

Sistemi za poljoprivredu i akvakulturu - posebno za sisteme za navodnjavanje;

Područja upravljanja/zaštićena područja/uređena područja i jedinice za izvještavanje jer
su neke od tih zona povezane s hidrografijom;

Područja prirodnih opasnosti - na primjer opasnost od poplave;

Morske regije - o granici između kopna i mora; i

Okeanografsko-geografske karakteristike obilježja.
Geolozi podzemnu vodu obično tretiraju kao geološki resurs. Podzemna voda u vodonosnicima uglavnom zavisi o geološkoj strukturi površine (tip stijene). Stoga je to integralni, neodvojiv dio Geologije. Vodonosnik je spomenut u infrastrukturi prostornih podataka, međutim, kao dio hidrološkog ciklusa, snažno je povezan sa oblašću Hidrografije. Trenutna definicija Hidrografije preuzeće podzemne vode pod "sve ostale vode povezane sa hidrografskim elementima".
1.9
Zaštićena područja u skladu sa zakonom i zaštićena nepokretna kulturna dobra
Područje koje je određeno ili kojim se upravlja u okviru međunarodnog prava, prava Zajednice i prava države članice, kako bi se postigli posebni ciljevi zaštite.
Područja sa određenim ciljevima zaštite definisana po sektoru. Mnoge od kategorija odnose se na očuvanje prirode, ali mogu se odnositi i na druge ciljeve, npr. resursi riba ili šuma, ili područja objekata kulturne baštine. Zaštita prirode može biti povezana sa određenim predjelima, staništima ili vrstama. Zaštićena područja mogu biti locirana i u kopnenim i u vodenim ili morskim okruženjima. Zaštićena područja razlikuju se od klasifikacija prirodnih i kulturnih izvora i objekata utemeljenih na životnoj sredini, pošto su lokacije, granice i površina zaštićenih područja zasnovane na formalnim, zakonskim ili administrativnim sporazumima/odlukama.
Opseg, primjeri korišćenja:
Oblast se odnosi na politiku iz zajednice i UN-a:

Propis kojima se reguliše oblast zaštite staništa;

Propis kojima se reguliše oblast zaštite ptica;

Svjetska baština;

Ramsarska konvencija;

Barselonska konvencija;

Helsinška konvencija;

OSPAR Konvencija; i

UN Geopark.
Područja propisa o staništima. Područja su određena pod oblašću zaštite prirode, zaštita staništa, a većina ih je registrovana kao poligon. Pokrivenost: sve zemlje EU. Takođe, oblast koja se odnosi na vode traženo je propisima kojima je uređena oblast voda: "površine određene za zaštitu staništa ili vrsta gdje je održavanje ili poboljšavanje statusa voda važan faktor u njihovoj zaštiti, uključujući relevantna mjesta određena pod oblašću prirode, zaštita staništa.
Područja zaštite prirode koja se odnosi na zaštitu prica. Područja određena pod ovom oblašću a većina ih je registrovana kao poligon. Pokrivenost: sve zemlje EU. Takođe propisima kojima je uređena oblast voda traženo je da površine određene za zaštitu staništa ili vrsta gdje je održavanje ili poboljšanje statusa voda važan faktor u njihovoj zaštiti, uključujući mjesta određena pod oblašću prirode koja se odnosi na zaštitu prica.
Staništa i područja s pticama uglavnom su upravljana i prijavljena pod programom Natura 2000.
Ostala međunarodno određena područja. Međunarodno određena područja mogu se naći u evropskim i državnim bazama podataka, kao što su lokacije za Ramsar, Svjetsku baštinu i područja biosfere. Podaci mogu uključivati sljedeće oznake: biogenetske rezerve, evropsku diplomu rezervata biosfere, mjesta svjetske baštine, mjesta ramsarske konvencije, mjesta barselonske konvencije, mjesta helsinške konvencije, mjesta OSPAR konvencije - Konvencija o zaštiti morske životne sredine sjeveroistočnog Atlantika - The Convention for the Protection of the Marine Environment of the North-East Atlantic (OSPAR).
Nacionalno određena područja Zajednička baza podataka o proglašenim područjima - Common Database on Designated areas (CDDA). Evropske zalihe nacionalno određenih područja (CDDA) sadrže informacije o zaštićenim područjima i o nacionalnim zakonskim instrumentima, koji direktno ili indirektno kreiraju zaštićena područja. Inventar počinje pod Koordinacija informacija o životnoj sredini - Coordination of Information on the Environment (CORINE) programom. Održava ju je za Evropsku agenciji za životnu sredinu -European Environment Agency EEA Evropskom tematskom centru European Topic Centre - o biodiverzitetu i ažurira se godišnje kroz Evropska mreža za informisanje i posmatranje životne sredine -European Environment Information and Observation Network (EIONET).
Zaštićeno kulturološko naslijeđe - kopno i more. Definicija infrastrukture prostornih podataka po oblastima zaštićenih područja ne isključuje vještačke objekte ili ostale vrste područja kulturnog nasljeđa. Iz tog razloga površine ili objekti sa formalnim statusom zaštite treba da budu definisani. Skupovi podataka postoje sa kategorijama područja kulturnog nasljeđa na kopnu i moru. Treba biti svjestan da objekti i površine sa formalnom zaštitom mogu biti samo mali dio cijelog skupa područja kulturonog nasljeđa, stare kuće, antičke stare kuće/građevine, olupine brodova ili drugi kulturni objekti. Kada govorimo o konzervatorskim i upravljačkim potrebama površine, skupovi podataka koji predstavljaju vrijednosti kulturne i prirodne zaštite biće relevantni.
Zaštićeno geološko nasljeđe - kopno i more - Zaštićena područja sa geološkim, hidrološkim, geomorfološkim ili rudarskim interesima sa prepoznatim naučnim i obrazovnim interesima.
Važni objektni tipovi i atributi:
Zaštićeno područje, površina, tačka linija:

Sistem klasifikacije;

Kategorija;

Id;

Ime površine/mjesta;

Opis;

Pozivanje na pravni osnov/ugovor;

Datum uspostavljanja zaštićenog područja;

Datum modifikacije zaštićenog područja; i

Cilj zaštite.
Veze i preklapanje s ostalim oblastima:
Objekti, administrativno definisani granicama, mogu slijediti granice objekta u prirodi (šuma) ili vještačke sredine (putevi), granicu nekretnine, administrativnu granicu različitih vrsta, obalnu liniju, rijeke te se stoga povezati i preklopiti s mnogim oblastima.

Administrativne jedinice;

Katastarske parcele;

Hidrografija - npr. rijeke, jezera, slapovi mogu biti klasifikovani kao prirodna baština ili
park prirode;

Visine - naročito obalna linija;

Zemljišni pokrivač;

Geologija;

Korišćenje zemljišta (zaštita se često vidi kao neka vrsta korišćenja zemljišta);

Područja upravljanja/zaštićena područja/uređena područja i jedinice za izvještavanje;

Biogeografske regioni;

Staništa i biotopi; i

Izvori minerala.
1.10 Digitalni model visina za kopno i vodenu površinu Digitalni modeli visina za površinu kopna, leda i okeana. Uključuju nadmorske visine, batimetriju i obalne linije.
Ova oblast uključuje:

Nadmorsku visinu, uopšteno predstavljenu kao:
o podaci reljefa, topografija površine terena, nazvana digitalni model reljefa koji
opisuje trodimenzionalni oblik Zemljine površine,
o površinski podaci, nazvani digitalni model visina, uključujući trodimenzionalan
oblik svakog objekta smještenog na zemlji (zgrade, mostovi, drveće…).

Batimetriju, npr. rešetkasti model dna.
Visina će biti određena obzirom na zajednički vertikalni koordinatni referentni sistem. Trenutno je važeći Evropski vertikalni referentni sistem 2000 (EVRS), ali EVRS 2007 u fazi razvijanja i može se uzeti u obzir.
Opseg, primjeri korišćenja:

Modeliranje nagiba i lavina, opasnost od poplave, rizik od erozije, tok vode i zagađivači,
širenje zagađenja vazduhom, požari, buka i biodiverzitet;

Aplikacije za životnu sredinu;

Snabdijevanje vodom;

Energetski sektor;

Agrikultura i šumarstvo;

Sigurnost na moru;

Lokacije područja vrijednog biodiverziteta u plićacima;

Lokacije morskih izvora i vrijednih područja za uzgoj ribe;

Razumijevanje uzoraka toka i hemijskog sastava u vodi;

Procjena položaja cjevovoda u moru; i

Proizvodnja ortofota.
Važni tipovi objekata i atributi:
Osnovni podaci:
Digitalni elevacijski model -Digital Elevation Model - DEM i/ili Digitalni model terena Digital Terrain Model DTM kao pravilna mreža, različitih rezolucija, za kopno i morsko dno.
TIN (Truoglasta nepravilna mreža).
Dodatni podaci:
Slojnice i izobate:
 Visine.
Prijelomnice:
 Kategorija (brijeg, uzdužni profil, ostalo).
Kote
 Visine;
 Kategorija (vrh, prijevoj,…);
 Ime.
Sounding

Visine.
Linija plime i osjeke.
Veze i preklapanja sa ostalim oblastima::
Glavne relacije sa ostalim oblastima su:

Administrativne granice: neke granice mogu se definisati kao grebeni;

Geografski nazivi: nazivi uzvišenja, npr. planinski vrhovi;

Hidrografija: postoji preklapanje za neke objekte (obalna linija) i konzistentna pravila
između dvije oblasti, na primjer: rijeka mora teći u uzdužni profil, jezero ili more moraju
imati istu visinu za sve površinske tačke i plovne objekte; i

Zgrade, za 3D modele gradskih područja.
1.11 Zemljišni pokrivač
Fizički ili biološki pokrivač Zemljine površine, uključujući vještačke površine, poljoprivredna područja, šume, (polu-) prirodna područja, močvare, plovne objekte.
Zemljišni pokrivač je fizički ili biološki opis zemljine površine. Na taj način se razlikuje od podataka o korišćenju zemljišta (grupa III, oblast broj 4), a koji su posvećeni opisu korišćenja Zemljine površine.
Informacije o pokrivaču trebaju biti homogene i uporedive među različitim lokacijama u Evropi, zasnovane na infrastrukturama za informacije pokrivača zemljišta koje su uspostavile zemlje članice (ako postoje) te dostupne i održive na najprihvatljivijem nivou.
Generalni direktorat Evropske komisije za životnu sredinu (Directorate-General for the Environment, DG ENV), pored drugih generalnih direktorata Evropske komisije (Directorate- General, DG), zajedno sa 37 zemalja učesnika finansira i primjenjuju evropske višegodišnje baze podataka pokrivača zemljišta, u okviru servisa u upravljanju zemljištem Global Monitoring for Environment and Security (GMES) i kao rezultat korisničkih zahtjeva na državnim i evropskim nivoima.
Opseg, primjeri korišćenja:
Politike iz Evropske unije i UN-a:

Međunarodna okvirna konvencija o klimatskim promjenama (Kyoto protokol);

Konvencija o dalekometnom međugraničnom zagađenju vazduha;

Fond novog evropskog regionalnog razvoja;

Propisa o vodama;

Tematska strategija o zaštiti zemljišta;

Konvencija o biološkom diverzitetu; i

Ozelenjavanje EU zajedničkom agrikulturnom politikom.
Primjeri korišćenja okvirnom politikom:

Regionalno planiranje/ESDP (Planiranje evropskog prostornog razvoja - European
spatial Development planning), ESPON (European spatial planning observation netvork
-Evropska mreža za praćenje prostornog planiranja), Strukturni fondovi: procjena
uticaja politike na perspektive regionalnog razvoja;

Sprovođenje zajedničke poljoprivredne politike: ruralnog razvoja (manje razvijena
područja), zahtjevi upravljanja zakonitostima (ekološki propisi: npr. o nitratima,
staništima, vodama), premjer agro-okruženja;

Politika zaštite životne sredine/propisom kojim je uređena oblast zaštite staništa:
sprovođenje Konvencije o biodiverzitetu, staništima i zaštićenim područjima;

Politika zaštite životne sredine/propisima kojima je uređena oblast voda: integrisana
analiza basena;

Politika zaštite životne sredine/propisima o kvalitetu vazduha, indstrijskom zagađenju i
kontroli rizika, zaštiti klime): procjena emisija u vazduhu i mjerenja kvaliteta vazduha;

Saobraćajna politika/zajednička saobraćajna politika,: strateška procjena uticaja na
životnu sredinu (SEA) za transevropske saobraćajne mreže, saobraćaja i mehanizama za
izvještavanje o životnoj sredini.
Primjeri Evropsko/međunarodnih klasifikacionih šema:

CORINE (Koordinacija informacija o životnoj sredini); i

LCCS (Klasifikacioni sistem pokrivača).
Važni tipovi objekata i atributi:
Primjer (baziran na CORINE-u, samo u ilustracijsku svrhu):

Vještačka površine:

Urbana industrija;

Industrijske, komercijalne i saobraćajne jedinice;

Rudnici, deponije i građevinska područja; i

Vještačka, nepoljoprivredna vegetativna područja.

Poljoprivredna područja:

Oranice;

Trajni usijevi;

Pašnjaci; i

Heterogene poljoprivredne površine.

Šume

Polu-prirodna područja:

Makija i/ili slične biljne vegetacije, i

Otvoreni prostori sa malo ili bez vegetacije.

Močvare:

Kopnene močvare; i

Pomorske močvare.

Vodena tijela:

Kopnene vode; i

Morske vode.
Važni atributi: Površina, opseg, tip pokrivača.
Linkovi i preklapanja sa ostalim oblastima:
Postoji snažna veza sa ortofoto snimcima kao glavnim izvorom za informacije o pokrivaču. Pokrivač je povezan sa korišćenjem zemljišta.
Međutim, snažne veze postoje i sa ostalim oblastima infrastrukture prostornih podataka oblastima koje se mogu smatrati elementima pokrivača kao što su:
-
Saobraćajne mreže;
-
Hidrografija;
-
Zgrade;
-
Proizvodna i industrijska postrojenja;
-
Sistemi za poljoprivredu i akvakulturu; i
-
Okeanografsko-geografske karakteristike.
1.12 Fotografski podaci zemljišnog pokrivača, dobijeni putem satelita ili snimanja iz
vazduha (ortofoto)
Geo-referencirani i/ili orto-retifikovani slikovni podaci Zemljine površine, dobijeni pomoću satelitskih ili vazdušnih senzora.
Ortofoto snimak je rasterska slika koja je geometrijski ispravljena (ortorektifikaovana) kako bi se uklonilo iskrivljenje prouzrokovano optikom kamere, pomakom kamere i razlikama u visini. Izvor je ili satelitski ili vazdušni senzor. Podaci su ortorektificirani ortoretifikovani kako bi se postigla tačnost srazmjerna datoj tačnosti topografske karte.
Opseg, primjeri upotrebe:
Vazdušnim ili satelitskim snimcima mogu se uzeti u obzir za:

ekstrakciju, mapiranje i ažuriranje specifičnih komponenti na Zemljinoj površini (npr.
Saobraćajna mreža, Hidrografija, Pokrivač, Geologija);

proizvodnju tematskih informacija (npr. Korišćenje zemljišta, Proizvodna i industrijska
postrojenja, Poljoprivredni i akvakulturni objekti);

osiguravanje sinoptičkog pogleda na datu teritoriju; i

prikaz kao kulisa drugim podacima (Infrastruktura prostornih podataka RDM, 2002).
Ostale aplikacije uključuju:

lokalizaciju ostalih tematskih podataka;

lokalizaciju opažanja slikovnih podataka zemlje kao takvih;

brzo georeferenciranje i isporuku nedavno stečenih snimaka (posvećeno prirodnim ili
industrijskim opasnostima) koji će biti lokalizovani sa drugim tematskim podacima
(geologija, zemljište, stare karte itd.); i

kontinuirano ažuriranje brzo razvijajućih nivoa referentnih podataka.
Različiti podaci već postoje ili su planirani u bliskoj budućnosti za pan-Evropu, npr. vazdušne fotografije, SPOT, IRS P6 podaci (za IMAGE2006) i Landsat 7 ETM+ (za IMAGE2000).
Na nacionalnom, evropskom i globalnom nivou učinjeni su napori kako bi se implementirale efikasne metode za opažanje Zemlje. "Global Monitoring for Environment and Security" (nekada GMES danas Copernicus) predstavlja zajednički napor u okupljanju provajdera podataka i informacija na jednom mjestu zajedno sa korisnicima, kako bi mogli bolje razumjeti jedni druge i informacije o životnoj sredini i sigurnosti učiniti dostupne kroz poboljšane ili nove servisi. Na Svjetskom skupu o opažanju Zemlje u Washingtonu, jul 2003., osnovana je Grupa o Zemljinom posmatranju (GEO), sa ciljem rješavanja zahtjeva za informacijama o životnoj sredini na globalnom nivou. Ovaj posao završen je u Briselu u februaru 2005. prihvatanjem 10-godišnjeg akcionog plana integrisanog Globalnog sistema za posmatranja Zemlje (GEOSS).
Važni tipovi objekata i atributi:
Uglavnom su ortofoto snimci predstavljeni diskretnim rektificiranim mrežnim pokrivačem. Pokrivač sadrži skup vrijednosti, npr. radiometrijske karakteristike.
Preklapanje i veze sa ostalim oblastima:

Visinama, iz razloga što se DEM zahtjeva za ortorektifikaciju; i

Ortofoto snimci su povezani sa mnogim oblastima u INFRASTRUKTURA PROSTORNIH
PODATAKA -u, pošto informacije mogu biti izvučene iz ortofota uz pomoć
kompjutorske analize ili vizualne interpretacije.
1.13 Geologija Geologija je opisana u skladu sa sastavom i strukturom. Uključuje stjenovito tlo, podzemne vode i geomorfologiju.
Geološke informacije daju osnovna znanja o fizičkom i hemijskom sastavu i porijeklu podzemlja, posebno kod svojstava stijena i sedimenata (starosti, petrografiji, porijeklu i tektonskim elementima…) te njihovoj strukturi.
Opseg, primjeri upotrebe:
Geološke informacije, na obali i na moru, osnova su za lociranje distribucije prirodnih izvora kao što su rude, podzemne vode, nafta, industrijski minerali, agregatni materijali i građevinski kamen. Oni mogu, doduše indirektno, upozoriti na opasnost od prirodnih katastrofa, klimatskih promjena ili snabdjeti informacijama o prikladnim mjestima za popunjavanje zemljišta, izgradnju kuća ili naprednim aspektima turizma. Oni time osiguravaju osnovu za planiranje i zaštitu životne sredine i podržavaju javno-političke odluke.
Tako su geološki podaci osnova za razumijevanje zemlje i njenih procesa.
Stoga se geološki podaci upotrebljavaju u:

Detektovanju geo-katastrofa;

Lociranju prirodnih mineralnih izvora (nafta, gas, plinski hidrati, ugljen, rude npr.
željezo, bakar, aluminijum, pijesak, šljunak, krečnjak itd.);

Lociranju podzemnih izvora za snadbijevanje pitkom vodom;

Pomoći kod prikazivanja pokazatelja klimatskih promjena;

Pomoći u zaštiti kopnenih voda;

Osiguravanju sigurnosti pri izgradnji zgrada i infrastrukture;

Osiguravanju sigurnog odlaganja otpada;

Osiguranju sigurne konstrukcije zgrada i infrastruktura;

Donošenju javnih odluka;

Osiguranju presudnih informacija za planiranje životne sredine;

Dodatnu vrijednost informacijama u turizmu; i

Osiguranju presudnih informacija za interpretaciju geofizičkih i geohemijskih podataka.
Važni tipovi objekata i atributi:

Starost (od…do…., kao godine geoloških formacija predstavljaju vremenske raspone prije
nego apsolutno vrijeme i nazivi perioda)

Tip stijene:

Sedimentne stijene;

Magmatske stijene;

Metamorfne stijene;

Antropogeni depoziti;

Regolit (nekonsolidovane površinske formacije, prelomljene/trošne stijene);

Genetski aspekti;

Tektonski aspekti;

Regionalni nazivi; i

Metamorfizam.
Hidrogeološki parametri individualnih formacija stijena:

Tip vodonosnika:

Porozni vodonosnici;

Raspucani vodonosnici;

Kraški vodonosnici;

Kvalitativni parametri podzemnih voda;

Kvantitativni parametri podzemnih voda;

Dinamički parametri (stopa punjenja/pražnjenja, stopa i smjer toka podzemne vode);

Osjetljivost vodonosnika;

Dubina stijene; i

Geomorfološki objekti (uključujući stopu sedimentacije/erozije u obalnim područjima).
Preklapanja i veze sa ostalim oblastima:
Glavne veze sa ostalim oblastima:

Tlo;

Korišćenje zemljišta;

Hidrografija;

Zaštićena područja;

Područja upravljanja/područja koja su zaštićena zonama zaštite/uređena područja i
jedinice za izvještavanje;

Područja prirodnih opasnosti;

Okeanografsko-geografske karakteristike;

Biogeografske regioni;

Staništa i biotopi;

Izvori energije;

Izvori minerala;

Sistemi za nadzor životne sredine; i

Morske regije.
Podzemna voda u vodonosnicima kontrolisana je fizičkim svojstvima i strukturom vodonosnika i njegovih susjednih stijena. Podzemna voda je prema geolozima često tretirana kao geološki izvor i stoga je to integralni dio Geologije.
1.14 Statističke jedinice
Jedinice za širenje i korišćenje statističkih informacija.
Oblast Prostorne jedinice za statistiku gledamo kao jednu od nekoliko tematskih grupa upravnih jedinica, ali ona može uključivati i ostale jedinice površina (npr. rešetke ili slivnike) ili tačke, u statistikama koje su bazirane na tačkama (npr. statistike na nivou adrese). Poglavlja Strategije o implementaciji (Infrastruktura prostornih podataka IMS, 2003.) opisuju sljedeće podgrupe upravnih jedinica:
-
Službene administrativne jedinice;
-
Vladine zone upravljanja;
-
Blokove, popise stanovništva i statističke krugove;
-
Civilne sigurnosne jedinice;
-
Jedinice za izvještavanje i upravljanje životnom sredinom
-
Poštanske kodove/regije.
Jedinice za širenje statističkih informacija mogu se posmatrati kao prostorne jedinice; površine, linije ili tačkasti objekti koji se koriste kod izvještavanja o podacima, u geografskim analizama i u distribucijskim sistemima za ekološke i socio-ekonomske podatke. "Korišćenje" se može interpretirati kao nešto drugačije od "širenja", budući da su riječi povezane veznikom "ili". Korišćenje može predstavljati bilo kakvu upotrebu u punom krugu uspostavljanja, spajanja, procjene i prikaza "statističkih informacija". Statističke informacije mogu se definisati kao "bilo koji numerički prikaz fenomena".
Opseg, primjeri upotrebe:
Korisnici statistika izražavaju povećanu potrebu za usklađivanjem kako bi imali uporedive podatke širom Evropske unije. Kako bi to funkcioniralo, unutrašnje tržište zahtijeva statističke standarde koji su primjenjivi za kolekciju, prenos i publikovanje statistika države i Zajednice tako da svi operatori u jedinstvenom tržištu mogu biti snadbjeveni sa uporedivim statističkim podacima. U tom kontekstu, klasifikacija je važan alat za prikupljanje, sastavljanje i širenje uporedive statistike. Regionalna statistika je kamen temeljac Evropskog statističkog sistema. Dugi niz godina evropske regionalne statistike prikupljale su se, sastavljale i širile na osnovu zajedničkih regionalnih klasifikacija zvanih "Nomenklatura teritorijalnih jedinica za statistiku" (NUTS). Jasna pravila za taj klasifikacioni sistem određena su pravnim okvirima. NUTS klasifikacija služi kao usklađeni sistem za aplikacije na evropskom i regionalnom nivou, dok istovremeno ne sprečava postojanje drugih pod podjela i klasifikacija.
Nomenklatura teritorijalnih jedinica za statistiku (NUTS) ustanovljena je od strane Evropske kancelarije za statistiku (EUROSTAT) kako bi se osigurala jedna jedinstvena podjela teritorijalnih jedinica za stvaranje regionalnih statistika Evropske Unije. NUTS isključuje određene teritorijalne jedinice i lokalne jedinice u korist regionalnih jedinica opšte prirode. Na detaljnijem nivou, postoje okruzi i opštine. Oni se zovu Lokalne administrativne jedinice (LAU) i nisu subjekti NUTS uredbe. Na vrhu hijerarhije su individualne zemlje članice EU, ispod toga su NUTS nivoi 1 do 3 pa LAU nivoi 1 i 2. NUTS regije nužno se ne moraju poklapati sa administrativnim jedinicama.
Trenutni fokus na sisteme e-Vlade u svim sektorima i uopšteno brzih promjena u smjeru uključivanja prostorne dimenzije u aktivnostima upravljanja i planiranja značiće da tačke, površine i granice različitih vrsta regiona postaju važne, kao da postoji interes u skoro svakom sektoru za spajanjem informacija.
Prostorne jedinice za statistiku mogu se upotrijebiti kod prikupljanja podataka (uglavnom prostornih podataka krupnijeg mjerila) kao i za spajanje ili prikazivanje podataka (u različitim mjerilima za različite svrhe, na primjer: na različitim statističkim NUTS nivoima). Isto tako administrativne jedinice, Prostorne jedinice za statistiku, mogu se koristiti za georeferenciranje podataka iz različitih statističkih polja, kao što su demografija i socijalna statistika, ekonomija, okolina i prirodni izvori.
Važni objektni tipovi i atributi:
Definicija precizira vrstu objekata koji su relevantni za demografiju: definicija uključuje izraz "nagomilani" (engl. aggregated). Vjerovatno se informacije u ovoj oblasti ne odnose na informacije na nivou adresa, ali nagomilavanje predstavljeno kao tačkasto bazirana pozicija može biti relevantno, npr. proizvodne aktivnosti u gradovima. Ispod su dati primjeri objekata. Najpotrebniji atribut je jedinstveni ID, koji se može upotrijebiti za povezivanje atributnih informacija. Nikakve tematske informacije ne bi trebale biti dio podataka u oblasti "Prostorne jedinice za statistiku".
Upravna jedinica, npr. od LAU2 nivoa

Id Popisne četvrti

Id Male površine oslobođene regionalizacijske statistike

Id Naselja - mala naselja, sela, blokovi, opštine, gradovi, manji gradovi

Id
Takođe se mogu dati podaci o stanovništvu na drugim regionalnim spajanjima, npr. na nivou vodenog sliva, što je učinjeno u procjenama koje su dio propisa o vodama (WFD).
Veze i preklapanje sa drugim oblastima:
Skupovi podataka koji se rješavaju u ovoj oblasti mogu biti pokriveni i u drugim oblastima ili kao geometrija/objekti koji se preklapaju ili kao tražena geometrija za tematsku prezentaciju. Prostorne jedinice za statistiku mogu se koristiti kao osnova za spajanje i prezentaciju tematskih karata za skoro svaku oblast ili sektorski specifičnu problematiku. Najvažnije veze date ovdje imaju vezu uglavnom na geometriju statističkih jedinica.

Administrativne jedinice; usko povezane sa ovom oblašću, kako su obje vrsta šireg
paketa administrativno definisanih granica i regiona. Prostorne jedinice za statistiku
mogu se sastojati od ili poklapati se sa administrativnim jedinicama. Prema NUTS
odredbi, preklapanje sa administrativnim jedinicama je namjerno sa svrhom
razlikovanja zona gdje koherentne snažne odluke omogućavaju razradu politike.

Razmještaj stanovništva - demografija; oblast uključuje slične geografske objekte kao i
oblast "Prostorne jedinice za statistiku", međutim oblast demografije takođe uključuje
mnoštvo tematskih informacija o atributima, što nedostaje u oblasti "Prostorne jedinice
za statistiku". Može se reći da se oblast demografije za neku vrstu informacija i spajanja
pozajmljuje/odnosi se na vrste objekata iz oblasti "Prostorne jedinice za statistiku" i
"Administrativne jedinice".

Područja koja su proglašena zonama zaštite ili kojima se upravlja u skladu sa posebnim
propisima /uređena područja i jedinice za izvještavanje. To mogu biti specifični sektori i
određene zone upravljanja. Uključuju glavne zajedničke operativne prostorne jedinice
kao što su vatrogasci, policija, hitna pomoć, obalna straža itd., vrlo visokih vrijednosti i u
sektorima vlastitih operacija i - hitnih operacija između sektora, npr. u prilikama
prirodnih i tehnoloških opasnosti, nesrećama u kojima se utiče na zdravlje, privredu ili
ekologiju. Takvi sektori/zone upravljanja uobičano se koriste kao osnova za spajanje
ekonomskih, proizvodnih ili servisnih informacija, takođe se može raditi o zdravstvenim
informacijama ili ostalim socioekonomskim informacijama. Uglavnom se ne koriste za
biološke informacije. Oblast se može preklapati sa "Prostornim jedinicama za statistiku",
a granicu između njih potrebno je razjasniti. Vjerovatno sistem statističkih jedinica treba
samo da uključi jedinice/sisteme napravljene za višenamjensku upotrebu/da nisu
specifično sektorski sistem statističkih jedinica.

Geografskie mreže: U većini slučajeva sistem geografskih mreža i mrežne ćelije
funkcionišu kao statističke jedinice, kako statističke informacije se skupljaju/prikazuju
ćeliju po ćeliju, međutim kako je to definisano u odvojenim oblastima, ne bi trebalo biti
uključeno u oblast "Prostorne jedinice za statistiku".

Ljudsko zdravlje i sigurnost, oblast "Prostorne jedinice za statistiku" može biti osnovna
komponenta za spajanje i prikaz informacija povezanih sa zdravljem.
1.15 Lokacija objekata
Geografski položaj zgrada.
Zgrada je pokriveni objekt, korisna za zaštitu ljudi, životinja, stvari ili proizvodnju ekonomskih dobara. Zgrada se odnosi na bilo kakvu strukturu trajno izgrađenu ili podignutu na njenom mjestu. Informacije o lokaciji zgrada mogu se isporučiti kao tačka ili u trenutno osnovnom obliku zgrade.
Uglavnom su zgrade dio katastra. Na lokalnom nivou zgrade su dostupne u okviru krupnijeg mjerila katastarskih planova ili skupova katastarskih podataka i geometrijski su predstavljene kao površine.
Većina zgrada može se identifikovati (geokodirati) putem adrese (zasebne oblasti u infrastrukturi prostornih podataka).
Opseg, primjeri upotrebe:

Lokalno planiranje i upravljanje;

Hitne operacije i operacije spašavanja;

Agencije nekretnina;

Građevinski sektor;

Oporezivanje;

Životna sredina (nivo buke, zaštita kulturne baštine…); i

Popis stanovništva, statistike.
Važni tipovi objekata i atributi:
Tip objekta "Zgrada" može biti opisan sa sljedećim atributima:

Stanje objekta (ruševina, u izgradnji, u funkciji);

Funkcija: industrijska, trgovinska, poljoprivredna, stambena,…;

Visina i/ili broj spratova; i

Veličina.
i za specifične zgrade:

Priroda (škola, muzej, crkva, bolnica,…); i

Ime.
Veze i preklapanja sa ostalim oblastima:
Snažna veza postoji sa:

Adresama; i

Katastarskim parcelama.
Zgrade su povezane sa oblastima:

Zemljišni pokrivač;

Korišćenje zemljišta;

Komunalne i druge servisi od javnog interesa;

Proizvodna i industrijska postrojenja; i

Objekti poljoprivrede i akvakulture.
1.16 Zemljište
Tla i pod tla obilježena su prema dubini, teksturi, strukturi i sadržaju parcela i organskih materijala, kamenitosti, eroziji i tamo gdje je prikladno srednjem nagibu i očekivanom kapacitetu pohranjivanja vode.
Predložen okvir propisa kojima se reguliše oblast tla (COM 2006., 232 konačna verzija), koji teži uspostavljanju okvira za zaštitu tla, navodi da je tlo "gornji sloj Zemljine kore smješten između stijene i površine, isključujući podzemne vode kako je definisano u propisima kojima je uređena oblast voda.
U saopštenju Komisije koje se tiče tematske strategije za zaštitu zemljišta (COM 2006., 231 konačna verzija), spomenuto je da je "zemljište opšte definisano kao gornji sloj Zemljine kore, formiranih mineralnih čestica, organskih materija, vode, vazduha i živih organizama. To je okruženje između zemlje, vazduha i vode i domaćin većini biosfere".
Kako je formiranje zemljišta izrazito spor proces, zemljište se može smatrati prvenstveno kao neobnovljivi izvor. Zemljište nam daje hranu, biomasu i sirove materijale. Služi kao platforma ljudskim aktivnostima i predjelu, kao arhiv baštine te igra bitnu ulogu kao stanište i banka gena. Zemljište skladišti, filtrira i transformiše mnoge materija, uključujući vodu, minerale i ugljenik. U principu, to je najveće skladište ugljenika na svijetu. Te funkcije moraju se zaštititi zbog svoje socioekonomske i ekološke važnosti.
Zemljište je izrazito kompleksan i varijabilan medij. Preko 320 glavnih tipova zemljišta identifikovano je u Evropi i u okviru svakog postoje velike varijacije u fizičkim, hemijskim i biološkim svojstvima. Struktura zemljišta igra glavnu ulogu u određivanju sposobnosti izvođenja svojih funkcija. Bilo kakva šteta u strukturi zemljišta takođe uništava ostale medije životne sredine i ekosistem.
Zemljište je subjekat niza procesa razgradnje ili oštećenja. To uključuje erozije, smanjenje organske materije, lokalno i difuzno oštećenje, zaptivanje, sabijanje, pad u biodiverzitetu, salinitet, poplave i klizišta. Kombinacija nekih nabrojanih oštećenja može u završnici voditi u sušu ili sub-sušne klimatske uslove koji vode prema pretvaranju zemljišta u pustinju.
Tipično, zemljište je karakterisano na osnovu opisa profila tla, analizirano uzimanjem uzoraka iz genetskih horizonata ili dubinskih klasa i klasificirano prema nacionalnoj ili internacionalnoj nomenklaturi. Karte zemljišta sadrže granice tipičnih kombinacija faktora razvoja zemljišta ciljnog mjerila kartiranja. Ne postoje međunarodno definisane šeme spajanja između različitih mjerila karata.
Prikupljanje informacija o zemljišto može se široko klasifikovati u tri kategorije:
a)
Mapiranje zemljišta, omogućava identifikaciju površine zemlje u svrhu upravljanja;
b)
Zalihe zemljišta, osiguravaju jednokratnu procjenu stanja zemljišta i/ili svojstva u
jednom trenutku u vremenu te promatranje zemljišta, osiguravajući niz procjena
pokazujući kako se uslovi zemljišta i/ili svojstva mijenjaju tokom vremena; i
c)
Tematsko mapiranje zemljišta.
(a)
Karte zemljišta Uopšteni cilj mapiranja zemljišta je osigurati prostoran prikaz i opis zemljišta kontinenata, zemalja, regija, farma ili bilo koje površine zemlje koja je od interesa. Uključuje identifikovanje različitih tipova zemljišta koji postoje, prikupljanje podataka o njihovoj prirodi, svojstvima i potencijalnoj iskoristivosti te zapisivanje tih informacija na kartama, geografske informacijske sisteme i njihove izvedene medije.
(b) Zalihe zemljišta i posmatranje zemljišta Zalihe zemljišta (uglavnom zasnovane na "profilima zemljišta") osiguravaju informacije o uslovima zemljišta. Mogu se uvesti u karte zemljišta kao atributi podataka (semantički) opisujući svojstva zemljišta. Praćenje zemljišta u mrežnim sistemima širom države, Evrope ili u režimu slojevitog uzorkovanja, dizajnirano je da osigura informacije o tome kako se zemljišta mijenjaju vremenom (vidi takođe oblast "Sistemi za nadzor životne sredine"). Geohemijski promjer takođe prikuplja informacije o zemljištu i specifično je usmjerena osiguravanju informacija o vrijednostima prirodne pozadine i o nametnutom antropičkom zagađenju.
(c)
Tematski podaci/karte rizika u zaštiti zemljšta i izvještavanju o životnoj sredini
Opšta primjena GIS tehnologije i kreacija baza podataka georeferenciranih informacija o zemljištu dopustila je određeni broj novih tipova procjena proizvodeći više politički relevantnih informacija nego osnovne karte zemljišta. Na primjer, pristupi modeliranja upotrebom postojećih zaliha zemljišta dopuštaju izvođenje informacija kao što su rizici od erozije, sadržaj organskih materija, difuzna kontaminacija zemljišta, sabijanje, salinitet, itd.
Opseg, primjeri upotrebe:
Karte zemljišta: karte zemljišta su spremne za regionalnu i nacionalnu procjenu životne sredine i izvještavanje u pregledu razmjera, uključujući razmjer 1:5 000 000 (Evropa), 1:1 000 000 (Evropa, zemlje) i 1:250 000 (zemlje, regije). Na temelju rada sprovedenog od strane kancelarije Evropske mreže zemljišta (ESBN), dogovoreno je da klasifikacija zemljišta bude Svjetska referentna baza za potencijal zemljišta (World Reference Base for Soil Resources - WRB) (FAO 2006.). Sva tri razmjera upotrebljavaju se u kontekstu Evropskog informacijskog sistema za zemljište (EUSIS). Kancelarija Evropske mreže zemljišta razvila je priručnike kako bi se poboljšalo usklađeno mapiranje zemljišta u preglednim razmjera (Finke i dr. 2001.; Lambert i dr. 2001.)
Za razliku od pregleda razmjera, temeljni podaci o zemljištu/karte zemljišta su dostupne u cijeloj Evropi (zemlje, regije) u različitim krupnijim razmjerama (razmjer > 1:50 000) i upotrebljavaju različite klasifikacijske sisteme, referentne datume za mapiranje i legende karata. One su rezultat opsežnih nacionalnih i regionalnih promjera zemljišta izvedenih u proteklih 50 godina, uglavnom za poljoprivredne svrhe. Kako bi se olakšala uporedivost podataka, potrebne su metode usklađivanja i one se odnose na nacionalne nomenklature prema WRB (FAO 2006.a, b).
Praćenje zemljišta: Postoji tek nekoliko primjera potpuno operativnog sistema za praćenje zemjišta u Evropi na nacionalnom i regionalnom nivou. Mnogi od tih nacionalnih sistema izvode samo jedno opažanje u vremenu i stoga se ne mogu smatrati potpuno operativnim sistemima. Van-Camp i dr. (2004.) zaključuju da minimalni skup zajedničkih parametara koji će se pratiti postojećim sistemima za praćenje zemljišta na nacionalnom nivou još uvijek treba odabrati. Isto vrijedi i za standardizovane metode i procedure. Više informacija može se primiti u pregledu postojećih sistema za praćenje zemljišta od strane Huberta i dr. (2001.), ažurirane, ali ne objavljene od EEA/ETC-TE (2003.).
Za Evropu kao cjelinu, osnovana su dva glavna popisa aktivnosti: (1) Geohemijski Atlas Evrope osigurava informacije o regionalnom uzorku i vrijednostima pozadine za 60 elemenata u gornjem zemljištu (Salminem i dr. 2006.). (2) Praćenje uslova šumskog zemljišta, sprovedeno od Međunarodni kooperativni program za procjenu i monitoring egekata zagađenja vazduha na šume - International Cooperative Programmee on Assessment and Monitoring of Air Pollution Effects on Forest ICP šumske mreže (16 x 16 km mreža; 1990-1995).
Tematski podaci: kako bi se olakšala primjena podataka zemljišta (tj. procijenili teško mjerljivi integrativni parametri i procijenila osjetljivost zemljišta na pritiske), Kancelarija evropske mreže zemljišta (ESBN) razvio je skup pedotransfer pravila, dostupnih kao zasebna metoda kompilacije koja dolazi sa 1:1 000 000 Evropskom bazom zemljišta (Van Rast i dr. 1995.; ESBN 1998.). Na nacionalnom nivou, takva pravila i funkcije takođe postoje, najopsežnija kompilacija nađena je u Ad-hoc-AG Boden (2000.).
Važni tipovi objekata i atributi:
Temeljna šema za podatke o zemljištu oslanja se na profile zemljišta ili nadogradnju zemljišta. Zavisno od odgovarajuće nomenklature zemljišta, opisane su makro morfološke karakteristike profila zemljišta ili jezgre zemljišta. Uzorci se uzimaju za genetske horizonte ili dubinske klase i analiziraju na hemijska, biološka i fizička svojstva zemljišta. Koristeći te informacije, zemljište se klasifikuje, kako bi se uporedila i opisala različita mjesta. Tip podataka u bazi podataka zemljišta dosta varira između karata zemljišta i rezolucija i između projekata. Kao primjer, u Geografskoj bazi podataka zemljišta za Evropu 1:1 000 000, informacije o zemljištu osigurane su za tipološke jedinice zemljišta Soil Typological Units (STU). Na toj geografskoj zastupljenosti, tehnički nije izvodivo zacrtavanje svake tipološke jedinice zemljišta. Zato su tipološke jedinice zemljišta grupsane u mapirane jedinice zemljišta Soil Mapping Units (SMU kako bi stvorile veze sa zemljištem. Kriteriumji za grupisanje zemljišta i SMU razgraničenje uzimaju u obzir funkcionisanje pedoloških sistema u okviru predjela. STU karakterišu različiti tipovi zemljišta koji su identifikovani i opisani atributima (varijablama) specificirajući prirodu i svojstva zemljišta, na primjer teksturu, režim vlažnosti, kamenitost itd.
Koncept mapiranja u razmjeru 1:250 000 (opisan u Priručniku procedura, Finke i dr. 2001.) je različit po svojoj prirodi i razlikuje tijela zemljišta i pejzaže. Tijelo zemljišta predstavlja djelić zemljišta sa neprecizno poznatim geografskim granicama. Opisuje trodimenzionalni entitet u kontinuuma tla upotrebom Svjetska referentna baza za zemljišnje resurse -World Reference Base for Soil Resources WRB klasifikacije tla (FAO 1998.), roditeljski materijal, dubinu do prepreke za korijenje i dominantnu teksturu zemljišta. Slično kao STU, tijelo zemljišta sadrži relevantne atribute koji opisuju zemljište. Pejzaž je nacrtan u razmjeri 1:250 000 i grupiše tijela zemljišta.
Evropska karta regiona zemljišta u razmjeri 1:5 000 000 predstavlja regionalno ograničen dio zemljišnog pokrivača karakterisan klimatskim tipom i roditeljskim materijalom (Finke i dr. 2001.).
Primjer za tipove objekata i atribute na Evropskoj karti zemljišta:
Baza podataka geografskog zemljišta za Evropu 1:250 000
Tijelo zemljišta
pejzaž
- atributi zemljištaa za genetske horizonte
jednog ili više profila zemljišta koji
karakterišu tijelo zemljišta
- dominantno zemljište
- glavni oblik zemljišta
- regionalni nagib
- intenzitet reljefa
- indeks vlažnosti
- dominantno korišćenje zemljišta itd.
Baza podataka geografskog zemljišta za Evropu 1:1 000 000
Jedinica mapiranja
zemljišta (SMU) i
tipološka jedinica tla
(STU)
- dominantno zemljište
- ko-dominantno zemljište
- ograničenja za poljoprivrednu proizvodnju
- kod zemljišta
- prisutnost nepropusnog sloja
- dominantni roditeljski materijal
- prepreke za korijenje
- klasa nagiba
- promjene teksture
- klase teksture
- korišćenje zemljišta
- prisutnost, tip postojećeg sistema za
upravljanje vodama
- režim klase vode u zemljištu
- visina iznad površine mora itd.
Osim toga, svaka jedinica mapiranja može se opisati temeljeno na uobičajenim svojstvima zemljišta primljenim od opisanih i /ili analiziranih profila zemljišta za dominantne i/ili povezane tipove zemljišta.
Perspektiva za prikupljanje i usklađivanje podataka zemljišta na Evropskom nivou: MREŽNI pristup
Evropska baza podataka zemljišta (ESDB), prekrivajući EU-25 razvijena je zajednički sa Evropskim partnerima i tu se jedino nalaze usklađene sačuvane digitalne informacije o zemljištu za Evropu. To je rezultat kompleksnog i dugotrajnog poduhvata, zbog velike heterogenosti zemljišta u zemljama. U svjetlu ažuriranja takve baze podataka i prikupljanja podataka, pojednostavljenje je potrebno kroz bolje prilagođeni tehnički okvir. Jedna ideja je da se sprovede prijavljivanje podataka zemljišta na osnovu hijerarhijskog sistema mreže (ili rastera) sa zajedničkom tačkom ishoda i standardizovanom lokacijom i veličinom ćelije mreže. Ovaj sistem predstavlja pogodan okvir za izgradnju Evropskog sistema podataka zemljišta i olakšava interoperabilnost kroz zajednički referentni koordinatni sistem, jedinstveni mrežni kodni sistem, skup detaljnih i standardizovanih metapodataka i otvoreni razmjenski format. To predstavlja osnov za Evropski informacioni sistem zemljišta (MEUSIS) u više razmjera, sistem kojim podaci tla proizvedeni u određenoj razmjeri mogu lako biti integrisani ili upoređeni sa podacima zemljišta proizvedenim u drugoj razmjeri, osiguravajući da su pravila za prikaz podataka jednaka u svim promjerima. Kako bi se to postiglo, biće razvijen i primijenjen zajednički standard za prikupljanje usklađenih informacija o zemljištu. Valja naglasiti da će, u cilju pružanja podataka o zemljištu u mrežnom formatu, zemlje koje osiguravaju podatke trebati procesiurati svoje originalne podatke o zemljištu, koji se drže u tradicionalno vektorsko temeljenim bazama podataka o zemljištu, kako bi pristajali mreži. Konačni rezultat razvoja MEUSISA biti će postojanje usklađenog informativnog sistema zemljišta za Evropu koji će racionalizovati bolji protok informacija od proizvođača podataka u lokalnom i regionalnom promjeru prema korisnicima podataka u krupnijem promjeru (nacionalni, evropski i globalni razmjer).
Preklapanje i veze sa ostalim oblastima:

Područja koja su proglašena zonama zaštite ili kojima se upravlja u skladu sa posebnim
propisima; /zaštićena područja/uređena područja i jedinice za izvještavanje; staništa i
biotopi; rasprostranjenost vrsta: uslovi zemljišta mogu biti indirektan kriterijum
razgraničenja (vlažna zemljišta u kombinaciji sa specifičnim tipom vegetacije; uslovi
zemljišta koji utiču na davno korišćenje zemljišta itd.);

Visine: važan faktor kod formacije zemljišta;

Zemljišni pokrivač; korišćenje zemljišta, objekti poljoprivrede i akvakulture: antropogeni
faktori koji utiču na uslove zemljišta;

Geologija: roditeljski materijal je glavni faktor formiranja zemljišta; obzirom na hidro
geologiju, fizičke karakteristike zemljišta, kontrolu vode koja se cijedi i otiče;

Sistemi za nadzor životne sredine: sistem za praćenje zemljišta;

Područja prirodnih opasnosti: relevantna u politici zaštite zemljišta (klizišta, poplave);
mogu prouzrokovati popriličan gubitak zemljišta; uslovi zemljišta (npr. sadržaj ilovače)
utiče na osjetljivost i ozbiljnost degradacijskog procesa;

Atmosferski uslovi; meteorološko geografski objekti: važni faktori mjesta; kontrolišu
procese u zemljištu; i

Biogeografske regije: uslovi formiranja regionalne slojevitosti; upotreba u mapiranju
zemljišta i aplikacijama sa informacijama o zemljištu.
1.17 Namjena površina Područje opisano u skladu sa njegovom sadašnjom i buduće planiranom funkcionalnom veličinom ili socioekonomskom svrhom (npr. stambenom, industrijskom, poslovnom, poljoprivrednom, šumarskom, rekreacijskom).
Regulativa zemljišta je uopšteno alat za prostorno planiranje na regionalnom i lokalnom nivou. Korišćenje zemljišta može se okarakterisati kao obično mapiranje postojećih funkcija odnosno kao objektivna slika korišćenja i funkcije područja, ali takođe može biti planski, karakterišući način na koji se zemlja može koristiti u sadašnjosti i budućnosti.
Postoje dvije glavne definicije korišćenja zemljišta, funkcionalna i sekvencijalna (Duhamel, 1998.). Prva od njih definše korišćenje zemljišta kao opis zemljišta u smislu njegove socioekonomske svrhe (poljoprivredne, stambene, šumarske itd.). Druga opisuje korišćenje zemljišta kao seriju operacija na zemljištu, koje sprovode ljudi sa namjerom da dobiju proizvode i/ili benefite kroz korišćenje zemljišnih resursa.
Planovi korišćenja zemljišta/regulacije korisnika zemljišta
Planovi korišćenja zemljišta regulišu trenutno i buduće korišćenje površina. Planovi korišćenja zemljišta uobičajeno imaju značajnu tekstualnu regulaciju za svaku površinu/kategoriju zemljišta ili specifičnu površinu. Planovi korišćenja zemljišta su različitih pojedinosti; opštinski planovi korišćenja zemljišta, detaljni planovi regulacije za blokove ili manja područja u urbanim područjima.

Korišćenje zemljišta može se posmatrati kao podjela na visokom nivou, npr. razlika
između privatne i državne zemlje, npr. u promjeru 1:1 milion;

Planovi korišćenja zemljišta, uobičajno rađeni na regionalnom nivou kao neka vrsta
glavnih planova, npr. prekrivanje cijele površine opštine u promjeru 1:50 000; i

Planovi registracije zemljišta na detaljnijem nižem nivou mogu prekrivati naseljene
površine ili površine specifičnog ekonomskog ili socijalnog interesa. Planovi mogu
usmjeriti nivo upotrebljivosti, postotak prekrivenosti zgradama u okviru površine,
regulaciju visina ili funkcionalnu regulaciju i proizvedene karte mogu biti u detaljnijoj
razmjeri, npr. 1: 5 000.
To je vrlo raznolika situacija koja se tiče regulacije zemljišta/planova korišćenja zemljišta pošto se ovi prostorni podaci uobičajno temelje na nacionalnim ili regionalnim zakonima ili drugim vrstama pravila. Dokumenta/karte često se vide kao pravna dokumenta i kategorije ostaju decenijama kao prava koja diriguju upotrebu zemljišta i imovine. Kategorije korišćenja zemljišta slijede takve regulative. Nadalje, operativni planovi mogu za neke površine biti stari i temeljeni na starim zakonima i nomenklatura se može promijeniti tokom vremena. Operativni planovi korišćenja mogu biti stariji od 100 godina i više. Takođe predloženi planovi ili oni koji su u procesu ili su predmet javne/sektorske rasprave mogu biti relevantni za širenje infrastrukture.
Zajednička strategija za pokretanje planova korišćenja zemljišta u GIS-u sprovodi se kroz proizvodnju rasterskih verzija planova za korišćenje zemljišta. To se prema nekima čini kao vrlo dobra strategija, pošto rasterizacijom radimo "kopiju" vizuelnog sadržaja, čime blokiramo sadržaj i tačnost promjena i zablude oko interpretacije pravnih dokumenata karata. Neke organizacije imaju strategiju najprije da izvrše snadbijevanje rasterskim verzijama postojećih planova i sa dugoročnim planom uspostavljanja vektorskih verzija.
Funkcionalno korišćenje zemljišta - prema socioekonomskoj svrsi
Funkcionalne površine u okviru urbanih ili ruralnih površina mogu biti mapirane kroz terenski rad, informacije iz registra ili kroz modeliranje upotrebom socioekonomskih ulaznih podataka u GIS-u.
Predložena klasifikacija fenomena korišćenja zemljišta zasniva se na ISIC Rev. 3 (Međunarodna standardna klasifikacija svih ekonomskih aktivnosti - International Standard Industrial Classification) klasifikaciji napisanoj od strane Ujedinjenih nacija (odobreno od Statističke komisije 1989.) i predloženo za upotrebu širom svijeta. Ova klasifikacija integrisana je u smislu da osigurava potpuno usklađivanje sa ostalim glavnim granama ekonomske klasifikacije: klasifikacijom proizvoda ICIP (Central Product Classification - Centralna klasifikacija proizvoda) koje su osnova za statistiku vanjske trgovine, statistiku proizvodnje i potrošnje, statistiku energije itd. ISIC Rev. 3 važno je naglasiti, je potpuno kompatibilan sa EU NACE Rev. 1 (Nome- nclature des Activités de la Communauté Européenne - Klasifikacija djelatnosti u Evropskoj zajednici) sistemom za prva dva nivoa. (Sistem je zamijenjen 1.01.2008., vidjeti reference).
ISIC sistem se sastoji od četiri nivoa komponenata: 17 sekcija, 60 odjeljena, 159 grupa i 292 klase. 7 dijelova prvog nivoa karakterišu glavne ekonomske aktivnosti. Te kategorije su:
SEKCIJA A
Poljoprivreda, lov i šumarstvo SEKCIJA B
Ribolov SEKCIJA C
Rudarstvo i vađenje kamena SEKCIJA D
Proizvodnja SEKCIJA E
Struja, gas i snadbijevanje vodom SEKCIJA F
Građevina SEKCIJA G
Trgovina na veliko i malo, popravak motornih vozila, motora i ličnih i kućnih
dobara SEKCIJA H
Hoteli i restorani SEKCIJA I
Prevoz, skladištenje i veze SEKCIJA J
Finansijsko posredovanje SEKCIJA K
Nekretnine, iznajmljivanje i poslovne aktivnosti SEKCIJA L
Javna administracija i odbrana, obavezno socijalno osiguranje
SEKCIJA M
Obrazovanje SEKCIJA N
Zdravstvena zaštita i socijalna zaštita SEKCIJA O
Ostale društvene, socijalne i lične uslužne djelatnosti SEKCIJA P
Privatna domaćinstva sa zaposlenim osobljem SEKCIJA Q
Van teritorijalne organizacije i tijela
Opseg, primjeri upotrebe:
Mnoge upravljačke i planske aktivnosti na lokalnom nivou zahtijevaju detaljne podatke. Važna je ispravna lokacija, geografska pozicija. Stepen tačnosti koji je potreban za položaj nekog objekta varira, potreba (i želja za proizvodnjom) tačnih podataka veća je u urbanim ili izgrađenim područjima i manja u ruralnim i prirodnim/polu-prirodnim okruženjima. Slično, interes u čestom ažuriranju opada sa stepenom udaljenosti od centralnog područja. Detaljno planiranje područja pokriva kopnena i morska područja.
Korišćenje zemljišta je važno za procjenu uticaja i praćenje sprovođenja politika i pravnih instrumenata za održivo upravljanje životnom sredinom, kao što je Natura2000.
Politike: 6akcionog plana za životnu sredinu (6EAP), smjernica za procjenu uticaja na životnu sredinu (EIA). Nekoliko politika i strategija daje istaknutu prednost regionalnom pristupu sa integrisanim upravljanjem zemljištem, kao što je Integrisano upravljanje obalnom zonom, komu- nikacija o planiranju i životnoj sredini, propisa o voda i komunikacija o prevencijama rizika.
Procjena uticaja na životnu sredinu (EIA) za projekte i strateška procjena uticaja na životnu sredinu (SEA) za politike, planove i programe, osiguravaju identifikaciju i procjenu značajnih uticaja na životnu sredinu koje se uzimaju u obzir prilikom donošenja odluka, na koje javnost može uticati.
Važni tipovi objekata i atributi:
Vrste funkcija zavise od vrste korišćenja zemljišta i planu korišćenja zemljišta. Prikaz plana korišćenja zemljišta može biti strukturiran kao slojeviti skup podataka.

Granice plana/regulacije;

Površina kategorije korišćenja zemljišta;

Površina kategorije regulacije zemljišta;

Površina kategorije ograničenja zemljišta; i

Elementi u planu (granice ceste, granice zgrada, granice šumskog/poljoprivrednog
zemljišta itd.)
Važni atributi:

Kategorija korišćenja zemljišta;

Kategorija regulacije korišćenja zemljišta;

Kategorija ograničenja korišćenja zemljišta;

Prisutna/postojeća ili predložena/planirana/budućnost;

Pravna referenca;

Datum stupanja na snagu; i

Veza sa tekstom propisa za svaku površinu.
Veze i preklapanja sa ostalim oblastima:

Katastarske parcele;

Hidrografija;

Saobraćajne mreže;

Zaštićena područja;

Zemljišni pokrivač;

Zgrade;

Zdravlje ljudi i bezbijednost;

Komunalne i druge servisi od javnog interesa;

Proizvodna i industrijska postrojenja;

Objekti poljoprivrede i akvakulture;

Razmještaj stanovništva - demografija;

područja koja su proglašena zonama zaštite ili kojima se upravlja u skladu sa posebnim
propisima; /uređena područja i jedinice za izvještavanje;

Područja sa rizikom od prirodnih katastrofa;

Staništa i biotope;

Izvori energije; i

Mineralne sirovine.
1.18 Zdravlje ljudi i bezbjednost
Geografski razmještaj patoloških pojava koje preovladavaju (alergije, tumori, bolesti disajnih puteva itd.), informacije koje pokazuju učinak na zdravlje (biomarkeri, smanjenje plodnosti, epidemije), ili dobrobiti ljudi (umor, stres, itd.) koji su direktno (zagađenje vazduha, hemikalije, prorijeđenost ozonskog omotača, buka itd.) ili indirektno (hrana, genetski izmijenjeni organizmi, itd.) povezani sa kvalitetom životne sredine.
Opisni pristup ljudskom zdravlju i sigurnosti fokusiraće se na:

Opisno geografsku distribuciju bolesti, dobrobiti ljudi ili ostalih zdravstvenih ili
sigurnosnih kvaliteta koji prikazuju geografske obrasce, mogu takođe uključivati opise
vjerovatnoće;

Uzroke i elemente koji utiču na zdravlje;

Dobrobit ljudi, uključujući kvalitet ljudskog okruženja;

Pitanja sigurnosti, ponašanja povezana sa zdravljem; i

Zdravstvene servisi.
Da bi ilustrovali vrste geografskih informacija koje mogu biti uključene u oblasti infrastrukture prostornih podataka, prikazaće se neki primjeri o medicinskim statistikama i medicinskoj geografiji :
Generalna statistika o zdravlju - promjene tokom vremena

Smrtnost - broj umrlih u relaciji s ukupnom populacijom tokom vremena;

Očekivani životni vijek - prosječan broj godina koji novorođena djeca mogu očekivati
da će živjeti ako se smrt kasnije pojavi u skladu sa smrtnošću svake starosne grupe
populacije u okviru ovog perioda. Očekivani životni vijek može se takođe procijeniti kao
očekivano preostalo vrijeme života u bilo kojoj određenoj dobi;

Oboljevanje - učestalost bolesti u relaciji sa ukupnom populacijom tokom datog perioda
vremena.
Obolijevanje može biti opisano mnogim različitim indikatorima:
o Učestalost: broj novih slučajeva u relaciji sa ukupnom populacijom tokom datog
vremenskog perioda;
o Kumulativna učestalost: ukupan broj novih slučajeva u dužem vremenskom
periodu, npr. nekoliko godina, u relaciji sa ukupnom populacijom;
o Prevalencija: ukupan broj slučajeva registrovanih u okviru populacije u datom
vremenu u relaciji sa ukupnom populacijom; i
o Stopa, specifična stopa za dob, starosno prilagođena stopa.
Relevantni materijali o geografskim uzorcima zdravlja jesu poređenje glavnih izvora smrti ili bolesti u različitim tačkama u vremenu. Ovo može, na primjer, ilustrovati epidemiološku tranziciju sa padom smrtnosti odočajdi i i infektivnih bolesti te povećanje degenerativnih bolesti.
Incidentni podaci o specifičnim bolestima ili drugim zdravstvenim pitanjima Pregled incidenata može se podijeliti prema polu, godinama, regiji ili ruralno-urbanoj podpodjeli i podaci mogu dati mogućnost određivanja trendova tokom vremena. Primjeri koji se mogu geografski tretirati:

Vrsta zaraze ili bolesti: koronarne bolesti srca, moždani udar, smrtnost odojčadi,
smrtnost povezana sa rakom, pregled oboljena, kardiovaskularne bolesti, mišićno-
koštane bolesti, psihički problemi, ozlijede, polno prenosive bolesti, zarazne bolesti;

Učestalost raka: Rak obuhvata različite tipove sa različitim geografskim uzorcima.
Incidentni podaci iz materijala javnih registara o starosno specifičnim trendovima,
varijacije pola u geografskom kontekstu, stopa incidenta i stopa preživljavanja: rak
jezika, usta, grla, stomaka, debelog crijeva, rektuma, pluća, prostate, bubrega, bešike,
maligni melanom, rak limfe.
Uzroci slabog ili dobrog zdravlja - faktori rizika - izlaganje Oblast može takođe uključiti fokus na uzrok slabog ili dobrog zdravlja. Za svrhu infrastrukture prostornih podataka potrebno je definisati zdravlje u kontekstu životne sredine, gledati zdravlje kao rezultat interakcije između tri faktora, čovjeka kao biološkog organizma, staništa i ponašanja - sposobnosti ljudskog organizma da podnese hemijske, fizičke biološke, psihološke ili socijalne stresove.

Prvo, to može osigurati dokaze o uzrocima bolesti. Iako su primjeri geografskih studija
koji vode prema osnovnim novim znanjima o uzrocima bolesti rijetki, geografski uzroci
bolesti mogu generisati hipoteze o uzrocima koji se mogu slijediti upotrebom ostalih
pristupa ili se sugestije iz ostalih istraživačkih pristupa mogu testirati geografski;

Drugo, takve informacije mogu biti korisne u planiranju strategija promocije zdravlja; i

Treće, znanje o geografskim varijacijama u različitim aspektima zdravlja mogu biti
korisne u planiranju zdravstvene zaštite.
Elementi geografske raspodjele tokom izlaganja mogu pomoći razumijevanju veza između izlaganja i zdravlja ili bolesti. Analiza uzroka treba da uključi sljedeća dva koncepta: Faktor rizika: faktor koji je poznat pri povećanju rizika od bolesti ili ostalih problema i Izloženost: rizik da će biti izložen faktoru rizika:

Izloženost hemijskim agensima u životnoj sredini, vazduhu, vodi, hrani i zemljištu, je
uzrok brojnih negativnih uticaja na ljude od raka do uticaja na novorođenčad. Npr.
geohemijski geografski podaci mogu se upotrijebiti u analizama izloženosti;

Među izloženostima za koje je dokazano da su kancerogene spomenuće se slijedeće;
radioaktivna i ultraljubičasta radijacija, neke hemikalije, stimulansi kao što su alkohol i
nikotin, hrana i neki profesionalni čimbenici;

Dvije grupe opasnih hemikalija - teški metali i dugotrajne organske zagađujuće
supstance (POP) trenutno dobijaju posebnu pažnju. Nadalje pažnju treba dati CMR
(kancerogenim, mutagenskim i reprotoksičnim hemikalijama), PBT (postojane, bio
akumulativne, otrovne hemikalije) i vPvB (vrlo postojane i vrlo bio akumulativne
materije), koje su materije od posebne pažnje prema Regulativa o registraciji evaluaciji,
autorizaciji i ggraničavanju supstanci i smješa (REACH-u). Izloženost teškim metalima
povezana je sa razvojem retardacije, različitim rakovima i oštećenjima bubrega.
Izloženost zlatu i olovu takođe je povezana sa razvojem autoimunih bolesti. Rastući
dokaz da POP mogu imati ozbiljne posljedice na ljudsko zdravlje.

Izloženost genetički modifikovani organizmi (GMO) u životnoj sredini, vazduhu, vodi,
hrani i zemljištu trenuto zahtjeva posebnu pažnju pošto može potencijalno
prouzrokovati negativne efekte na ljudsko zdravlje i životnu sredinu.
Ljudska dobrobit Ljudska dobrobit može biti povezana sa životnom sredinom, stresom, npr. bukom, teškim saobraćajnim zagađenjem, takođe se može reflektovati na statistici ili stopama negativnog blagostanja, npr. psihijatrijskim problemima, bolestima čiji je uzrok povezanost sa alkoholom, socijalni problemi ili smrt, zdravstveni problemi ili smrtnost u saobraćaju, povrede ili smrt kroz ostale nezgode, samoubojstvo uopšteno ili samoubistvo vatrenim oružjem kao poseban slučaj.
Sigurnost Sigurnost može sadržati pitanja kao što su lična ljudska iskustva ili percepcija njihove sigurnosne situacije, povezanost sa stopama dugog niza pokazatelja npr. stopom kriminala ili može biti karta Vjerovatnoćui za npr. zločine.
Servisi zdravstvene zaštite Zdravstvene servisi mogu se interpretirati kao dio oblasti zdravlja, kako je njihovo pojavljivanje i kvalitet usko povezano sa zdravljem i dobrobiti. Problemi mogu uticati na javne zdravstvene servisi u geografskom kontekstu - distribuciji npr. bolnica i sličnih institucija, medicinskih laboratorija ili institucija za rehabilitaciju. Daju se detalji o stopi distribucije i parametrima kvaliteta doktora, sestara, psihoterapeuta ili drugih praktičara. To može takođe uključiti servisi u obliku ambulantnih usluga, ambulantnih područja i ostalih vrsta hitnih upravljačkih sistema, gdje je dokazano da upotreba GIS-a poboljšava izvođenje. Briga ljudi za vlastito zdravlje i zdravlje svoje porodice i njihovih srodnika je još jedna važna usluga koja obično nije registrovana.
Opseg, primjeri upotrebe:

Važni aspekti o zdravlju u 6EAP, koje slijedi koristi zdravstvena komunikacija. Visoka
zabrinutost za građane; (Infrastruktura prostornih podataka IMS, 2003.)

Zdravstveno planiranje i upravljanje;

Praćenje plodova mora i cvjetanje mora koje bi moglo naštetiti ljudskom zdravlju;

Istraživanje o uzrocima smrti i bolesti: Tokom medicinske geografije i geografske
epidemiologije različiti zdravstveni problemi mogu se analizirati u geografskom
kontekstu;

Upravljanje hitnim situacijama; i

Sigurnosno upravljanje: tokom protekle decenije kaznenopravna zajednica je počela
ubirati vrijedne analitičke prednosti geografskih informacioninih sistema (GIS). Moćna
tehnologija poboljšava sposobnost istraživača i praktičara kod identifikacije hot spotova,
analize prostornih obrazaca kriminala i kriminalnog ponašanja i kod dijeljenja
nejednakih skupova podataka preko jurisdikcijskih granica.
Važni tipovi objekata i atributi:
Sistemi geografskih mreža, administrativne jedinice i prostorne jedinice za statistiku Podaci o stopama različitosti problema povezanih s vrućinom može biti povezano s geografskim mrežnim sistemom, administrativnim i statističkim jedinicama. Upotreba podrazumijeva povezanost između informacioninih atributa povezanih sa zdravljem i geometrijom na mreži, administrativnim ili statističkim jedinicama. Važno je da ti podaci s različitim regionalnim prijelomom imaju stabilne i poznate identifikatore (ID). Detaljne geografske informacije o ukupnoj populaciji, spolu i godinama krucijalne su u geografskom kartiranju zdravlja. Nema posebnih zdravstvenih atributa koji bi se trebali spomenuti, oblast je toliko velika da to ne bi imalo smisla. Za detalje o minimalnim zahtjevima na objektima i atributima, vidi ove oblasti:
Distribucijsko područje/područje posmatranja/tačka posmatranja Tačka ili područje lokalizacije koje pokazuje bilo koju vrstu posmatranja povezanu sa zdravljem ili sigurnošću, npr. zaraze kao što je malarija, potencijalne ljudske epidemije i rizike kao što je ptičji grip, distribucija ili slučajevi kriminala. Važni atributi kao vrsta slučaja, datum opažanja, izvor opažanja. Postojeći materijali ne dopuštaju više određenih obrisa relevantnih objekata i atributa.
Lokacije instituta za zdravlje Sektorski
specifične
regije
upravljanja,
npr.
zdravstvena
njega/upravljanje regionama/ambulantne regije.
Sektorski specifične regije upravljanja

Sektor;

Podsektor;

Tip aktivnosti upravljanja;

Odgovorna organizacija; i

Godina ovjere.
Faktori rizika koji se koriste u procjeni uzroka mogu se povezati sa serijom objekata i tretiraju se kao i ostale oblasti. Mogu postojati kvalitetne informacije o antropogenoj životnoj sredini, stresu i podacima zagađenja koje nisu pokrivene drugim oblastima, a relevantne su kao ulazni element u analizama koje pokriva oblast Ljudsko zdravlje i sigurnost. Treba procijeniti da li treba to obraditi u ovoj oblasti, kao što su na primjer zone nivoa buke.
Veze i preklapanje sa ostalim oblastima:

Geografski sistemi mreža;

Administrativne jedinice;

Geologija (geo hemija);

Prostorne jedinice za statistiku;

Zemljište;

Komunalne i druge servisi od javnog interesa;

Sistemi za nadzor životne sredine - Lokacije za monitoring životne sredine;

Područja upravljanja/jedinice za izvještavanje;

Atmosferski uslovi; i

Meteorološko-geografske karakteristike.
1.19 Komunalne i druge servisi od javnog interesa
Uključuje komunalne sisteme kao što su kanalizacija, skladištenje otpada, snabdijevanje energijom i vodom, administrativne i socijalne državne servisi kao što su javna administracija, sjedišta civilne zaštite, škole i bolnice.
Jako široka oblast infrastrukture prostornih podataka koja uključuje razne vrste objekata:
Komunalne servisi/mreže: fizička konstrukcija za transport definisanih proizvoda. To može uključivati cjevovode za transport nafte, gasa, vode, kanalizacije ili druge cijevi. Dalekovodi mogu uključivati električne, telefonske kablove, kablovsku televiziju ili ostale mreže. Važni su dalekovodi i na kopnu i na moru (dnu mora). Sve vrste prenosnih sistema imaju čvorove i povezane su sa postrojenjima za proizvodnju i tretiranje raznih vrsta proizvoda. Uprkos snažnoj unutrašnjoj povezanosti, oblasti u infrastrukturi prostornih podataka tretiraju se odvojeno - proizvodna i industrijska postrojenja uglavnom se tretiraju u oblasti Proizvodnja i industrijska postrojenja. Razlikujemo različite vrste prenosnih sistema:

Naftovodi i plinovodi: Glavne cijevi iz naftnih i plinskih polja/područja bušotina i
mjesta gdje se skladišti. Važna proizvodna i industrijska postrojenja takvih izvora
povezana su sa ovakvom mrežom, kao što su nuklearne elektrane, elektrane, trafo
stanice i naftni rezervoari. Geografski informacioni sistem komisije -Geographic
Information System of the Commission (GISCO), autoriteti za energiju/industriju,
kompanije.

Vodovod: Lokacija vodovoda - velika i lokalna mreža. Ovdje su od interesa veliki
vodovodi. Povezani s proizvodnim postrojenjima za vodu za potrošnju/procese. Cijevi za
navodnjavanje tretiraju se odvojeno u sklopu poljoprivrednih postrojenja. Institucije za
vodosnadbijevanje, vodovi/zdravlje.

Kanalizacija: Mreža kanalizacije, povezana sa kanalizacijskim postrojenjima. Ovdje su
od interesa glavne cijevi. Vodovi.

Dalekovodi električne energije: Skup podataka koji pokazuje veće dalekovode za
električnu energiju, na kopnu i moru. Položaj dalekovoda važan je podatak za energetski
sektor kao takav te za urbaniste, građevinare i ribare, u slučaju kablova u moru. Dio
važnih informacija sadržan je u bazama podataka prepreka za nisko letenje. Šire:
Državne institucije za energiju/industrije. Lokalni vlasti, kompanije.

Telefonski/podatkovni/kablovski kablovi: Lokacija telefona/podatka: Sirovi podaci
potrebni u planiranju zemljišta. Važna čvorišta, npr. antene, mogu se vidjeti kao dio
mreže. Smještaj kablova može biti u sukobu s ostalim prirodnim aktivnostima, npr.
ribarstvom. Tehnička tačnost podataka za lokalni nivo kompanija.
Sirove baze podataka cjevovoda i komunalnih usluga postoje na Evropskom nivou, npr. GISCO baza podataka u razmjeri 1: 1 000 000. Podaci u zemlji su nehomogeni. Postoje primjeri nacionalnih portala koji upozoravaju na konstrukciju, distribuciju karata/podataka o lokaciji cjevovoda. Na lokalnom i regionalnom nivou odgovornost vladinih kancelarija ili različitih subjekata/firmi. U nekim zemljama postoje nacionalni portali za informacije o kablovima u građevinskim poslovima.
Postrojenja za obradu i odlaganje otpada:
Važno je identifikovati objekte zaštite životne sredine pomoću jedinstvenih identifikatora. Kategorija komponenti podataka se podudara sa ekonomskom/statističkom kategorijom (NACE/SERIEE). Lokacija prema geografskoj tački, adresi ili u nekim slučajevima kao površina.

Mjesta kontrolisane obrade otpada za bezopasan otpad na kopnu: geografska
lokacija službenih ili uređenih postrojenja za tretiranje i skladištenje otpada. Uključena
kategorija prostorne komponente "postrojenja za zaštitu životne sredine":
o Skladišni prostori na kopnu - deponija;
o Peći za paljenje otpada; i
o Drugi objekti za prečišćavanje.
Informacije o vrsti tretiranja, vrsti materije za tretiranje, kapacitetu, postotku
biorazgradivog otpada, obnovljivoj energiji iz peći i deponija.

Mjesta kontrolisane obrade otpada za opasni otpad na kopnu: geografske lokacije
službenih ili uređenih postrojenja za tretiranje i skladištenje opasnog otpada; uključena
u kategoriju prostorne komponente "postrojenja za zaštitu životne sredine".
Izvještavanje u skladu sa propisma iz oblasti sprečavanja velikih udesa koji uključuje
opasne supstance . Razlika između:
o Termičke obrade;
o Deponija;
o Tretiranja i skladištenja nuklearnog otpada;
o Ostala tretiranja opasnog otpada (npr. hemikalija), i
o Ostala postrojenja za tretiranje.
Informacije o vrsti tretiranja, vrsti tretirane materije, kapacitetu (i potencijalnim
rizicima).

Uređene površine za odlaganje otpada u more: Površine u moru za odlaganje otpada,
npr. brodovi, naftne platforme, industrijski otpad, vojni otpad. Konvencija o zaštiti
morske sredine severo-istočnog Atlantika Uređene površine za odlaganje otpada u more:
Površine u moru za odlaganje otpada, npr. brodovi, naftne platforme, industrijski otpad,
vojni otpad. Konvencija o zaštiti morske sredine severo-istočnog Atlantika - Convention
for the Protection of the Marine Environment of the North-East Atlantic (Oslo-Paris-
Convention) - OSPAR dopušta odlaganje u more. Izvještavanje po ugovornoj strani i
kategoriji mjesta, broj izdatih odobrenja, licencirane tone i ugovorna strana. Važno kod
upravljanja životnom sredinom i upravljanja biološkim izvorima na moru. Podnošenje
podataka za godišnji izvještaj OSPAR-a o odlaganju otpada u more od OSPAR konvencije
za zaštitu morskog okruženja sjeverno istočnog Atlantika. Očekivane vlasti za isporuku
mogu biti morsko upravljanje/morski otpad/vlasti za zaštitu životne sredine, OSPAR.
Uključene u komponentu prostornih podataka "regulaciju površina".
To takođe uključuje nuklearni otpad. Primjer su ruske deponije: službeni izvori navode
ukupno o 0.45 PBg radioaktivne tečnosti koja je odložena u Barencovo more i 0.32 PBg u
Karsko more. Većina krutog radioaktivnog otpada odložena je duž istočne obale Nove
Zemlje i otvorenog Karskog mora. Neki materijali i količine dostupni su na postojećim
stranicama.

Ilegalne ili nekontrolisane deponije otpada - more i kopno. Ilegalne deponije/divlje
deponije na kopnu su česte, ali politike su usmjerene na smanjenje takvih deponija.
Važno je u lokalnom sistemu upravljanja otpadom i kontroli zagađenja locirati takve
ilegalne deponije, kako bi se sprovele ciljane akcije. Nekontrolisane površine na moru
gdje je otpad zabilježen takođe su važne, to mogu biti olupine brodova, industrijski
otpad, vojni otpad, auti. OSPAR dozvoljava odlaganje u moru.

Rudarski otpad: Rudarski otpad je posebna vrsta otpada. Ostaci od rudarstva mogu
sadržati niski sadržaj metala ili minerala koji nije ekonomski izvlačiti, ali ispiranje može
pruzrokovati kontaminaciju tla i vode. Otpaci od rudarskih aktivnosti uglavnom su
locirani blizu mjesta kopanja. U upravljanju i procjeni rudarskog otpada postoje potrebe
za prostornim podacima kao što je lokacija rudnika i otpada, vodotokova, riječne mreže,
vode i mora, tla.

Kanalizacioni mulj: generisanje, mreža kanalizacionih cijevi i objekti otpadnih
voda: Ovdje su tretirani kao grupa:
o Odvod/objekti otpadnih voda, informacija o kapacitetu, vrsta tretmana,
kategorija primatelja
o Kanalizacijska mreža tretira se pod komponentom podataka: vodovi
o Kanalizacioni mulj proširio se na poljoprivredno zemljište - regulirane "zone
dozvola"
o Širenje kanalizacijskog mulja - mapiranje prikladnosti poljoprivredne
površine i odlagališta zemljišta.
Objekti zaštite životne sredine Oblast takođe uključuje specifične vrste objekata: objekti zaštite životne sredine uključuju niz komunalnih ili privatnih kanalizacionih objekata/mjesta tretiranja otpadnih voda, objekata za tretiranje otpadnih voda (npr. peći za spaljivanje otpada, deponije), konstrukcije objekata protiv buke, objekti zaštite od prirodnih nepogoda (potporni zidovi na klizištima, zidovi protiv poplava itd.). Važno je identifikovati objekte zaštite oživotne sredine jedinstvenim identifikatorima. Kategorija komponente podataka podudara se sa ekonomsko/statističkim kategorijama (NACE/SERIEE). Lokacija putem geografske tačke, adrese ili u nekim slučajevima površine.
Primjeri

Tretiranje otpada i mjesta odlaganja - opasan otpad: Planovi tretiranja otpada,
lokacije opasnog otpada. Glavna razlika između opasnog i bezopasnog otpada. Razlika
između termičke obrade, deponije i ostalih obrada za bezopasni otpad. Informacije o
vrsti obrade, vrsti korišćene supstance, kapacitetu (i potencijalnim rizicima). Propisima
kojima je uređena oblast upravljanja otpadom, rudarskim otpadom, propisma iz oblasti
sprečavanja velikih udesa koji uključuje opasne supstance , iz oblasti voda.

Mjesto obrade kanalizacionih/otpadnih voda: Objekti obrade otpadnih voda,
Informacije o kapacitetu, vrsti tretmana, kategoriji primaoca. Kanalizacijska mreža
obrađena je pod komponentom podataka: vodovi. WFD, MS do DG ENV, lokalni autoriteti.
Objekti definisani u propisima za upravljanje otpadnim vodama/ industrijski otpad
mogu biti dio ove uopštene kategorije Mjesta obrade kanalizacionih/otpadnih voda.
Objekti zaštite od prirodnih opasnosti: Bilo koja vrsta ili konstrukcija koja štiti od prirodnih opasnosti, (npr. potporni zidovi na klizištima, zidovi protiv poplave itd.). Hidrografske službe, civilna zaštita, lokalne vlasti.

Konstrukcije protiv buke: Konstrukcije/zidovi ili ostali objekti, za ograničavanje
širenja buke koja dolazi sa ceste, željeznice ili zbog avio saobraćaja, industrijske ili druge
buke. Za industriju su uključene i modifikacije na izvoru. Zaštita na radu je isključena.
6EAP.
Administrativne i socijalne državne servisi kao što je javna administracija, civilna zaštita, mjesta, škole, bolnice. Vrsta mjesta obično je prezentovana na državnim i opštinskim portalima i Sistemima karata kao "podatak od posebnog interesa" i može biti tačkasto bazirana lokacija različitih kategorija opštinskih i državnih usluga i socijalne infrastrukture.

Policijske stanice;

Vatrogasne stanice;

Bolnice;

Zdravstveni centri;

Centri za brigu starijih osoba;

Škole i vrtići;

Sanacija/mjesta isporuke otpada (deponije); i

Državne i kancelarije lokalne samouprave.
Opseg, primjeri upotrebe:
Planiranje korišćenja zemljišta. Planiranje rizika/upravljanje. Predviđeni razvoj Propisma iz oblasti sprečavanja velikih udesa koji uključuje opasne supstance za obradu dalekovoda kao moguće tehnološke opasnosti, Propisma iz oblasti sprečavanja velikih udesa koji uključuje opasne supstance je od glavne važnosti u regulisanju upravljanja rizikom. Pristup podacima vodova-putem linkova toliko potrebnim u procjenama uticaja na životnu sredinu potrebno je izvesti kod planiranja velikih električnih dalekovoda ili cjevovoda. Postojeći i planirani dalekovodi/cjevovodi trebali bi biti dostupni kod planiranja korišćenja zemljišta. Detaljni mrežni podaci su potrebni u izgradnji.
Informacije o objektima zaštite životne sredine koji će se koristiti u procjeni, indikatori razvoja i uopšteno izvještavanje po pitanjima životne sredine. Statistike povezane sa zaštitom objekata mogu biti povezane sa lokacijom. Postoji potreba za takvim informacijama u prostornim analizama antropogenog pritiska na riječne slivove. Na lokalnom nivou važno je u planiranju korišćenja zemljišta, upravljanju vodama, obalnim područjima, prirodnim i tehnološkim rizicima.
Upravljanje otpadom povezano je sa dva problema: prevencijom nastajanja otpada i održivim upravljanjem otpada: ponovno korišćenje i recikliranje, optimizacija konačnog odlaganja i prevoz otpada. 6EAP daje prioritet prevenciji otpada i postizanju razdvajanja korišćenja resursa od ekonomskog rasta kroz značajno poboljšanu efikasnost resursa, demateralizaciju ekonomije i prevenciju otpada. Ostala područja politike povezana su sa politikom otpada, npr. politikama o klimatskim promjenama, vazduhu, urbanom zemljištu i vodi.

Propis iz oblasti sprečavanja velikih udesa uključuje opasne supstance, procjenu uticaja
na životnu sredinu -Environmental Impact Assessment (EIA), Otpad, EAP
Važni tipovi objekata i atributi:
Objekti u mrežama mogu uključiti dalekovode/cjevovode i čvorove koji su zapravo pumpe itd. Glavna proizvodnja i mjesta obrade obrađeni su u oblasti Proizvodni i industrijski objekti.
Cjevovod - nafta, gas, togasa:

Kategorija sadržaja;

Id segmenta;

Kapacitet, maks.;

Prosječan volumen;

Razmjera;

Režim pritiska;

Sistem konstrukcije;

Datum konstrukcije; i

Odgovorna organizacija.
Sistem kanalizacione mreže:

Id segmenta;

Kapacitet, maks.;

Prosječan volumen;

Sistem konstrukcije uključujući npr. materijal korićten za izgradnju mreže (liveno
željezo, cement,…);

Visina;

Datum konstrukcije; i

Odgovorna organizacija.
Sistem mreže vodovoda:

Id segmenta;

Kapacitet, maks.;

Prosječan volumen;

Sistem konstrukcije uključujući npr. materijal korišćen za izgradnju mreže (liveno
željezo, cement,…);

Datum konstrukcije; i

Odgovorna organizacija.
Električni dalekovodi

Id segmenta;

Kapacitet, maks.;

Prosječan volumen;

Sistem konstrukcije;

Datum konstrukcije; i

Odgovorna organizacija.
Prenosna mreža za bilo koju vrstu podataka/signala:

Id segmenta;

Kategorija objekta (objektni tip) npr. antene, bazne stanice, relej antene, kablovi itd.;

Kategorija podataka/signala, npr. radio, podatak, mobilni telefon, TV;

Datum konstrukcije; i

Odgovorna organizacija.
Objekat zaštite životne sredine:

Kategorija objekta (tip objekta);

Tip obrade/servisi;

Opis, kapacitet, konstrukcija itd.;

Ime;

Datum konstrukcije; i

Odgovorna organizacija.
Javne/državne servisi/ objekti (tačka):

Kategorija servisi/objekta;

Ime;

Id;

Informacija; i

Link na web site.
Ako se daju mjerne vrijednosti, može se dodati registracijski atribut, sa informacijama o sub atributima kao što su:

Registracijsko tijelo;

Registracijski režim;

Registracijski parametar;

Vrijednost; i

Registracijski datum, vrijeme.
Preklapanja i veze s ostalim oblastima:
Vodosnadbijevanje i kanalizacija mogu se preklapati sa oblastima:

Hidrografija;

Zgrade;

Korišćenje zemljišta;

Sistemi za nadzor životne sredine (poput postrojenja za obradu/pumpe);

Proizvodna i industrijska postrojenja; i

Izvori energije.
1.20 Lokacije za monitoring životne sredine
Lokacija i rad objekata za praćenje životne sredine uključuju opažanja i mjerenja emisija, stanja segmenata životne sredine i ostalih parametara ekosistema (biodiverzitet, ekoloških uslova vegetacije, itd. ) od strane ili u ime javnih vlasti.
Objekti praćenja stanja životne sredine su objekti za posmatranje i mjerenje emisija, statusa i efekta ekološkog segmenta (vazduha, šume, morske vode) i/ili ostalih aspekata životne sredine (npr. biodiverzitet, ljudsko zdravlje). Koncept praćenja može se povezati sa sistematskom i hijerarhijskom strukturom, uključujući mrežu za praćenje, stanice za praćenje, mjesta za praćenje i pod mjesta. Nadzorno mjesto može trajno biti smješteno na lokaciji ili može biti privremeno, korišćeno samo neko određeno vrijeme. Kontinuirano kretanje objekata za praćenje, npr. na brodovima, može biti vrsta objekta za praćenje. Nadzorna mjesta u obliku lokacija i područja mogu se prijaviti kao georeferencirane tačke, linije i poligoni. U slučajevima gdje su podaci klasifikovani ili povjerljivi, postoji mogućnost spajanja na rešetku. Problematično je to da se definicija oblasti odnosi na vrstu organizacija za snadbijevanje podacima.
Opseg, primjeri upotrebe:
Mnoge različite konvencije, propisi, naučni programi za praćenje i ostali programi direktnog nadzora i protoka informacija o praćenju povezane su sa nadzornim mjestima. Trenutno različite institucije koriste različite modele podataka i definicije. Infrastruktura prostornih podataka uključuje opšti model nadzornih mjesta.
Primjeri:

Meteorološke stanice: uključuju snimanje vremenskih uslova i klimatološke
informacije. Informacije mogu uključivati jednostavne informacije o padavinama,
temperaturi, ali i stanice sa dodatnim informacijama o snježnom pokrivaču, vlazi itd. koje
su važne u mnogim procjenama uticaja na životnu sredinu. Različite organizacije, npr.
ECOMET, mogu osigurati podatke, uglavnom u realnom vremenu, putem gržavnih
meteoroloških i hidroloških servisa. Kategorija "meteorološka stanica" može se takođe
definisati kao tačka lokacije za klimatološke informacije, kao što su uopšteni atributi i
dodatne informacije o max/min mjesečnoj temperaturi/padavinama, sa brzinom,
sunčevim
zračenjem,
atmosferskim
pritiskom,
relativnoj
vlazi,
potencijalnim
isparavanjima, oblačnosti. Primjer je mreža Evropskih klimatoloških stanica, dugoročne
srednje mjesečne i srednje godišnje vrijednosti, cca. Postoji 19 meteoroloških atributa za
4773 stanica, dok uobičajene varijable (padavine, temperatura) postoje za cca 10 000
stanica.

Stanice za praćenje kvaliteta vazduha: Lokacije mjesta stanica za praćenje i stanica za
mjerenje kvaliteta vazduha, opasnih materija (ozon), i ostalih zagađivača.

Stanice za praćenje kvaliteta vode: Propis iz oblasti upravljanja vodama predstavlja
različite vrste mjesta za praćenje:
o Sistem za praćenje površinskih voda;
o Pumpanje pitke vode (istražne stanice, operativne stanice); i
o Stanice za praćenje podzemnih voda (stanica nivoa podzemnih voda, operativna
GW stanica, GW stanica za nadzor).
Stanice mogu biti npr. hidrometrijske (količina vode, protok i nivo stanice), hemijski
kvalitet vode, biološki kvalitet vode.

Bodovi fenološkog posmatranja: mjesta gdje se izvode opažanja fenološke mreže
(Evropska fenološka mreža EPN).

Stanice za praćenje morske sredine: Morsko bazirani objekti za praćenje i mjerenja
okeana i parametara morskog dna i zagađenja (npr. teški metali, naftne mrlje). Mogu biti
povezani sa nacionalnim i međunarodnim konvencijama i sporazumima, npr. OSPAR
konvencija. HELCOM obaveza izvještavanja, može služiti kao primjer. Reguliše: nadzorna
mjesta u Baltičkom moru i zahtijeva registraciju i izvještavanje o eutrofikaciji, zagađenju
metalima, zagađenju otrovnim materijamaa, kvaliteta vode i zagađenje vode. Različite
frekvencije.

Stanice za praćenje zemljišta: Praćenje trendova u hemijskim stanjima zemljišta.

Stanice za praćenje jačine magnetnog polja.

Mjesta za kupanje: Usklađenost sa propisima o kvalitetu vode za kupanje: Zone obalne i
svježe vode: Iznešeni su podaci o kvalitetu vode za kupanje (obalne i zone svježe vode)
prema propisima o kvalitetu vode za kupanje. Parametri za koje je izračunata usklađe-
nost uključuju: ukupne koliforme, fekalne koliforme, mineralna ulja, površinsko aktivne
materije i fenole. Informacija se podnosi Komisiji od strane zemalja i postaje dostupna,
kao izvještaj zemlje, na internet stranici DG Environment. Izvor: DG Environment.

Ostala praćenja povezana sa vodom definisana u: propisima za ribarske vode i
propisima koji se odnose na zagađenje vode ispuštanjem određenih opasnih materija.

GMO praćenje mjesta i površina: propisima koji se odnose na genetički modifikovane
organizme, Aneks VII
(http://ec.europa.eu/environment/biotechnology/pdf/dec2002_811.pdf) propisuje da se praćenje i izvještavanje o namjernom uvođenju GMO-a sprovodi u životnoj sredini.
Primjeri elemenata koji bi se posmatrali su:
a) Efekti na ne ciljanim organizmima (uključujući razvoj otpornosti kod divljih
srodnika) ili štetočinskim organizmima, promjene u rasponu domaćina ili u
raširenosti štetočinskih organizama i virusa, razvoj novih virusa;
b) raspršenost, uspostavljanje i otpornost u ne ciljanim sredinama ili ekosistemima;
c) ukrštanje sa seksualno kompatibilnim rođacima u prirodnoj populaciji;
d) nenamjerne promjene u osnovnom ponašanju organizama, na primjer, promjene
u reprodukciji; i
e) promjene u biodiverzitetu (npr. u broju ili kompoziciji vrsta).
Dizajn praćenja (mjesta i površine) mora biti naznačen. Uključuje poljoprivredna polja
gdje se žitarica komercijalno uzgajala kao i okolna staništa.
Važni tipovi objekata i atributi:
Oblast je široka i različite zajednice mogu imati različite modele za definisanje objekata za praćenje. Primjer mogućeg uopštenitog sadržaja dat je ispod. Oblast se može podijeliti u podteme, dozvoljavajući različitim poljima definisanje glavnog skupa karakteristika. Mogu se raditi ekstenzije definisanim modelima podataka, tipovima objekata ili atributima u definisanim intervalima vremena.
Monitoring /nadzorno mjesto:

Registracijsko tijelo;

Registracijski režim;

Metodologija razmjere;

Parametri registracije;

Parametar jedinica;

Vrijednost parametara; i

Datum registracije, vrijeme.
Veze i preklapanja sa ostalim oblastima:
Objekti sredine mogu biti zgrade ili mogu biti locirani na postojećim objektima, industriji itd. Oblast se može preklapati s Infrastruktura prostornih podataka po oblastima kao što su:

Hidrografija;

Područja koja su proglašena zonama zaštite ili kojima se upravlja u skladu sa posebnim
propisima;

FotografskI podaci zemljine površine, dobijeni putem satelitskih ili snimanja iz vazduha
(ortofoto);

Geologija;

Lokacije objekata;

Zemljište;

Zdravlje ljudi i bezbjednost;

Proizvodna i industrijska postrojenja;

Objekti poljoprivrede i akvakulture;

Komunalne i druge servisi od javnog interesa;

Područja sa rizikom od prirodnih katastrofa;

Atmosferski uslovi;

Meteorološko-geografske karakteristike;

Okeanografsko-geografske karakteristike; i

Morska područja.
1.21 Proizvodna i industrijska postrojenja
Industrijska proizvodna mjesta, uključujući instalacije pokrivene propisom koji se tiče integrisanog sprečavanja i kontrole zagađenja i objekata za pumpanje vode, rudarstvo i objekata za skladištenje.
Lokacija industrijske proizvodnje, rudnika, deponija i energetskih objekata. Što se tiče industrije to može biti hemijska, ugljenvodonična (nafta-gas), rudnici ili bilo koja druga industrija. Upotreba PRTR kategorija kao uobičajenih nomenklatura za takve objekte relevantna je jer obuhvata širok skup relevantnih industrijskih aktivnosti. Kategorizacija se može mapirati na ostale međunarodne kategorizacijske sisteme kao NACE, SERIEE ili ISIC.
Definicija takođe spominje i pumpanje vode, rudarstvo i objekte za spremanje (pohranu). Poslednja mogu biti spremišta za različite vrste proizvoda potrebnih kao ulaz u industrijsko/proizvodnim procesima ili mogu biti viđena kao spremišta za stvarne proizvode i takođe formirani otpad iz proizvodnih procesa. Oblast "Proizvodna i industrijska postrojenja" mora se gledati kao jedna od nekoliko tematskih grupa "postrojenja" kao što su:

Komunalne i javne servise;

Sistemi za nadzor životne sredine; i

Objekti poljoprivrede i akvakulture.
IMS dokumenti (Infrastruktura prostornih podataka IMS, 2003.) sadrže različite podgrupe vodova i objekata sa grupama dalekovoda i cjevovoda, sistemima zaštite životne sredine, proizvodnim objektima, industrijom, poljoprivrednim objektima, trgovinom i uslužnim djelatnostima. Prva i zadnja oblast u IMS-u nisu spomenute kao odvojene oblasti u radnoj verziji teksta, niti u sistemima nadzora životne sredine. Upoznati smo sa dvije nove oblasti "Komunalne i javne servisi" i "Sistemi za nadzor životne sredine".
Definicija uključuje referencu na IPPC propise. Propisima kojima je uređena oblast industrijskog zagađenja, sprečavanje i kontrola zagađivanja životne sredine - IPPC opisuje Evropski registar zračenja (EPER), kao i Protokol o registrima i ispuštanju zagađujućih supstanci PRTR uspostavlja integrisano ispuštanje zagađivača i registar prenosa (PRTR).
Vrste proizvodnih/industrijskih postrojenja:
Industrijska mjesta: Aglomeracija i individualna lokalizacija glavne industrije, uključujući hemijsku, rafinerije ugljenvodonik rafineriju, drvnu, ribarsku itd. Id na kompaniju/mjesto. Propisi iz oblasti sprečavanja velikih udesa koji uključuje opasne supstance.
Lokacija nuklearnih postrojenja: Koristiće se kao referentna tačka za otpuštanje iz nuklearnih postrojenja. Izvještavanje o svakoj proizvodnoj jedinici: Podnošenje podataka za godišnji izvještaj o ispuštanjima voda iz nuklearnog postrojenja iz OSPAR konvencije za zaštitu morske sredine sjeverno-istočnog Atlantskog okeana. Ovo je zakonska obaveza sledećih zemalja: Belgije, Danske, Francuske, Njemačke, Norveške, Portugala, Španije, Švedske, Švajcarske, Holandije i Ujedinjenog Kraljevstva. Nije nužno izvještavanje o geografskoj lokaciji, ali ime jedinice/adresa ili ostali id-evi mogli bi povezati informacije sa geografskom lokacijom. OSPAR/HELCOM
Vađenje energetskih sirovina i mjesto proizvodnje: Lokalizacija mjesta proizvodnje energije za proizvodnju toplote, struje i gasa. Mjesta mogu uključivati područja ekstrakcije, npr. za naftne i plinske platforme, hidroelektrane, nuklearne elektrane. Mjesta takođe uključuju distribuciju postrojenja za energiju, mjesta za skladištenje, ali ne i mrežu (vidjeti sastavne podatke vodova).
Rudnici: Individualna lokalizacija rudnika ili generalizovanih rudarskih površina, uključujući mjesta za skladištenje, deponije, sedimentacijske brane itd.
Opseg, primjeri uporabe:
Potrebne u modeliranju i procjeni pritisaka na životnu sredinu, u prostornom planiranju i upravljanju rizicima i opasnostima. Potrebno na svim geografskim nivoima, od Evropskog do lokalnog. Potrebno za informiranje javnosti. Grubo zastupanje u Evropskom skupu podataka za neke objekte u GISCO-u. Takođe u geografskoj bazi podataka u EPER-u, sa preglednikom karata i detaljima o proizvodnom mjestu, vidjeti www.eper.eu.int Evropske politike: 6EAP, IPPC, EPER, OSPAR/HELCOM, Propisma iz oblasti sprečavanja velikih udesa koji uključuje opasne supstance.
Važni objektni tipovi i atributi:
Postrojenja su opisana u nekoliko oblasti infrastrukture prostornih podataka. Modeli podataka i atributi trebalo bi, koliko je to moguće, usklađeni između samih oblasti.
Objekt u ovoj oblasti je lokacijska tačka proizvodnog/industrijskog postrojenja. Međutim, mnogi od proizvodnih postrojenja prekrivaju velika područja, tako da površinske objekte takođe treba uzeti u obzir, i razmatra se u detaljnom mapiranju/referenciranju zgrada ili delineaciji ostalih objekata. U Infrastrukturi prostornih podataka Startegijskoj implementacionoj grupi - Infra- strukture prostornih podataka - Implementation Strategy Group (IMS) dokumentima dalekovodi i cjevovodi su uključeni kao vrsta "vodova i objekata". Dalekovodi različitih vrsta mogli bi se prikazivati kao povezani objekti sa "stvarnim" proizvodnim/industrijskim postrojenjima.
Proizvodna/industrijska postrojenja:

Id;

Ime;

Klasifikacioni sistem;

Klasifikacija aktivnosti/proizvodnja, NACE kod;

Volumen proizvodnje, po komponenti i vremenu;

Vlasnik/odgovoran;

Dozvoljeni volumen zračenja; i

itd.
Postrojenje za pohranu:

Id;

Ime;

Klasifikacioni sistem;

Klasa/tip;

Komponenta, ime, volumen; i

Vlasnik/odgovorna organizacija.
Deponije:

Id;

Ime;

Klasifikacioni sistem;

Klasa/tip;

Komponenta, ime, volumen; i

Vlasnik/odgovorna organizacija.
Antene/uređaji i oprema za podatke/signale:

Id;

Ime;

Klasa/tip:kategorija objekta (objektni tip) npr. antene, bazne stanice, relej antene;

Kategorija podataka/signal, npr. radio, podaci, mobilni, tv;

Datum izgradnje; i

Odgovorna organizacija.
Veze i preklapanje sa ostalim oblastima:
Skupovi podataka rješavani u ovoj oblasti mogu se preklapati sa ostalim oblastima i granice između oblast trebaju se identifikovati. Posebna pažnja prema oblastima:

Korištenje zemljišta;

Sistemi za poljoprivredu i akvakulturu-usko povezano;

Komunalne i javne servisi koje uključuju postrojenja za vodove kao što su kanalizacija,
upravljanje otpadom, snadbijevanje el energijom i vodom; i

Sistemi za nadzor životne sredine. Veza, kada je sistem za nadzor lociran na proizvodnoj
lokaciji.
Veze i na:

Zgrade;

Adrese;

Izvore energije; i

Izvore minerala.
1.22 Objekt poljoprivrede i akvakulture
Oprema za poljoprivredu i proizvodni objekti (uključujući sisteme navodnjavanja, staklenike i štale).
Poljoprivredni objekti: Poljoprivredni objekti su konstrukcije koje se koriste u poljoprivrednoj proizvodnji. Poljoprivreda je definisana tako da uključuje orezivanje godišnjih ili trajnih usjeva i držanje/uzgoj životinja. Šumarstvo u cjelini vjerovatno nije uključeno, ali intenzivne šumske plantaže na bivšim poljima mogu se uključiti. Objekti će se klasifikovati prema NACE1.1 korišćenom u službenim statistikama, u trenucima kada je ona relevantna. ISIC sistem za klasifikaciju industrijskih područja takođe može biti relevantan. Primjeri poljoprivredno proizvodnih objekata su sistemi navodnjavanja, staklenici, štale, skladišta, cjevovodi. Definicija objekta trebalo bi se razjasniti, npr. ako su objekti kao sistemi zidova za prevenciju erozije, sistemi kanala korišćenih za navodnjavanje, sistemi terasa korišćeni za proizvodnju voća, građevine van oblasti "objekta".
Akvakulturni objekti: Objekti za proizvodnju i obradu riba, školjki, algi i ostalih vrsta akvakulture. Akvakultura uključuje samo trajne i polu trajne sisteme za uzgoj organizama i ne uključuje lokacije za lov životinja ili biljaka u njihovom prirodnom okruženju. Akvakulturni objekti mogu egzistirati i u morskim i u kopnenim vodama te terestičkim proizvodnim sistemima.
Opseg, primjeri upotrebe:
Važno je u lokalnom planiranju korišćenja zemljišta i upravljanju poljoprivredom i vodama, takođe od javnog interesa, procjeni uticaja na životnu sredinu, kao ulaz za identifikovanje izvora/objekata pod prijetnjom u kriznom upravljanju. Osim toga, važno je znanje kod prostornog praćenja širenja ljudskih ili biljnih/životinjskih zaraza.
Važni tipovi objekata i atributi:
Agrikulturni objekti proizvodnje/obrade i akvakulturni objekti proizvodnje/obrade mogu imati tačnu lokaciju mjesta (tačka, površina). Objekti mogu biti prostorno izraženi kao tačke, ali tamo gdje je proizvodno područje veliko, pokrivač površine može biti relevantan, npr. površine staklenika ili mjesta proizvodnje školjki na moru.
Dokumentacija o lokaciji objekta može postojati kao koordinata ili indirektno preko adrese nekretnine ili zgrade. Upotreba GIS-a ili mrežnih usluga može združiti tematske baze podataka i baze podataka koje nude mogućnosti za indirektno referenciranje.
Poljoprivredni objekti:

Klasifikacioni sistem;

Vrsta objekta;

Uloga objekta u proizvodnom sistemu;

Vrsta proizvodnje;

Količina proizvodnje

Vrsta zračenja, različite materije;

Količina zračenja, različite materije; i

Sistem kontrole zaraze.
Akvakulturni objekti:

Klasifikacioni sistem;

Vrsta objekta;

Uloga objekta u proizvodnom sistemu;

Vrsta proizvodnje;

Količina proizvodnje;

Vrsta zračenja, različite materije; i

Količina zračenja, različite materijei.
Veze i preklapanja s ostalim oblastima:
Veze/preklapanja sa oblastima:

Zgrade;

Adrese;

Hidrografija (sistemi za navodnjavanje);

Zemljišni pokrivač;

Korišćenje zemljišta;

Proizvodna i industrijska postrojenja; i

sistemi za nadzor životne sredine. Veze, kada je objekat za praćenje lociran na
poljoprivrednom ili akvakulturnom objektu.
1.23 Razmještaj stanovništva - demografija
Geografska rasprostranjenost stanovništva, uključujući obilježja stanovništva i razne aktivnosti, razvrstana po mreži, regiji, administrativnoj jedinici ili drugoj analitičkoj jedinici.
Uobičajeno je imati statistike sa geografskim prekidom na državnom i lokalnom nivou. Posljednjih decenija, statističke kancelarije započele su izradu demografskih i socio-ekonomskih statistika u velikim urbanim područjima sa referencom na blokove kuća i obradu podataka GIS- om. U nekim zemljama odabrana metodologija upućuje na agregaciju lokacijski baziranih informacija (adresa/domaćinstava) na mrežu (npr. 1x1 km ili 0.1x0.1 km).
Uključuje široki spektar izvora informacija, kao što su regionalne statistike sa Eurostatom; ostale evropske i državne podatke, regionalne i lokalne podatke. Oblast može biti podijeljena u nekoliko komponenti:

Karakteristike stanovništva; i

Stanovništvo/stepen ljudskih aktivnosti.
Što se tiče informacija o stanovništvu, ono može ili već uključuje ukupan broj stanovnika, godine: populacioni brojevi za svaku klasu godine ili agregirane godišnje klase (0-5, 6-15, 16-20, 21-30, 31-40, 41-50, 51-67, 68-80, preko 81), a može uključiti i pol, smrtnost, životni vijek, migracije. Brojevi se mogu prikazati na godišnjem nivou sa informacijama o promjenama tokom vremena, kao što je rast/redukcija u stanovništvu, npr. zadnje 2 godine, zadnjih 5 godina, zadnjih 10 godina. Takođe, može uključivati detalje o prosječnim noćnim i dnevnim brojkama nekih komponenti. Podoblast stanovništvo, mogla bi uključivati socio-ekonomske informacije o stanovništvu, kao što je broj domaćinstava, stopa zapošljenosti, obrazovanje, dohodak, domaćinstva sa djecom itd.
Oblasti relevantne za lokalne, regionalne i nacionalne statistike takođe uključuju oblasti kao što su izvori eksploatisanja, poljoprivredna proizvodnja i razne ekološke oblasti. Što se tiče "nivoa aktivnosti", predstavljaju vjerovatno uključivanje oblasti koja se tretira odvojeno u infra- strukturi prostornih podataka i to u "ekonomskim statistikama/lokalnim statistikama".
Ekonomske aktivnosti uključujući proizvodnju, potrošnju, dionice, prihode, zapošljavanje: sta- tistika se odnosi na administrativne jedinice, objekte, mreže, adrese, monetarne i fizičke jedinice. Ekonomski podaci o transportu i saobraćaju klasifikovani su u skladu sa službenom klasifi- kacijom ekonomskih aktivnosti Evropske unije (NACE rev. 1.1. NACE) i pokriva cijelu industriju.
Primjeri direktno povezani sa zaštitom životne sredine:

23.30 (dio) Obrada nuklearnog goriva;

37.10 Reciklaža metalnih ostataka i otpadaka;

37.20 Reciklaža nemetalnih ostataka i otpadaka;

41.00 Skupljanje, prečišćavanje i distribucija vode;

51.57 Veleprodaja ostataka i otpada;

90.01 Prikupljanje i obrada otpadnih voda,

90.02 Prikupljanje i obrada ostalog otpada; i

90.03 Sanitacija, sanacija i slične aktivnosti.

U drugim industrijama, aktivnosti zaštite životne sredine i rashodi zahtijevaju dodatne
podatke, kao što je prikazano u Evropskom sistemu prikupljanja ekonomskih informacija
u oblasti životne sredine - European System for the collection of economic information
on the environment (SERIEE) priručniku (CEPA), Eurostat 1994 (verzija 2002.).
Raspodjela stanovništva takođe može značiti geografsku agregaciju zgrada u naseljima, selima, velikim gradovima, gradovima. Podaci se mogu materijalizovati u vidu baze podataka hijera- rhijskih naselja sa pojedinostima o broju stanovnika za geografske objekte ili lokacije centralnih tačaka ili širenje površine/naselja. Raspodjela stanovništva može takođe biti ili funkcionalnih ili fizičkih karakteristika izgrađenog naselja u okviru površine naselja. Jedan primjer cjelokupne funkcionalne podjele na zone jeste distribuiranje na poslovne zone u okviru grada - Central bussines district (CBD). Može se napraviti detaljnija kategorizacija površine npr. vrsta apartmana, stan, zadruga, vlasništvo, kuća/vila, dvojna kuća, terasasta kuća, apartmanski blok. Razdvajanje statistike je metodologija transformisanja podataka više agregacije prema nižoj, bazirana na modelima. EEA evropska baza stanovništva uvodi transformaciju statistike od administrativnih regiona prema malim ćelijama mreže po modelu baziranom na znanju o raspodjeli stanovništva - pokrivaču zemljišta. Brojevi su agregirani u mrežne stanice.
Popisi stanovništva sprovode se u okviru perioda od npr. 10 godina. U međuvremenu, administrativni registri države omogućavaju uredan protok podataka koji se uopšteno koriste za prezentovanje godišnjih statistika.
Opseg, primjeri upotrebe:
Trenutni fokus na sisteme e-Vlade u okviru svih sektora i uopšteno brze promjene prema upravljačkim aktivnostima uključujući prostornu dimenziju i planiranje vjerovatno će podstaći upotrebu socio-ekonomskih podataka sa geografskom referencom. Kako bi se pripremili za povećanu potrebu korisnika očekivano je da će evropski i nacionalni provajderi širiti informacije o relevantnim nivoima agregiranja, sa međunarodno dogovorenim Id-evima i formatima koji omogućavaju povezivanje geometrije i atributa.
Važni tipovi objekata i atributi:
Definicija precizira vrstu objekta relevantnog za demografiju: Definicija uključuje izraz "agregirano".
Ispod su dati primjeri objekata, važnih atributa, međutim, mogu biti različiti i uopšteno se spominju kao socio-ekonomski atributi. Različite varijable mogu biti relevantne za različite stepene agregiranja.
Upravna jedinica, npr. nivo LAU2

Id;

Socio-ekonomski atributi kako je spomenuto gore .
Mreža, npr. 1x1 km, 100x100m

Id;

Socio-ekonomski atributi kako je spomenuto gore .
Popisne četvrti

Id;

Socio-ekonomski atributi kako je spomenuto gore.
Statistike malog naselja "besplatna" regionalizacija

Id ;

Socio-ekonomski atributi kako je spomenuto gore.
Naselje - malo naselje, selo, blok, veliki grad, grad

Id;

Socio-ekonomski atributi kako je spomenuto gore.
Fizička regija/površina u naselju

Kategorija.
Funkcionalna regija/površina u naselju

Kategorija.
Takođe se može navesti broj stanovnika na ostalim regionalnim agregacijama, npr. na nivou vodenih slivova, što je učinjeno u procjenama i dio je rada propisa o vodama.
Veze i preklapanja s ostalim oblastima:
Tematske informacije u obliku prikupljanja atributa/tabela mogu se povezati sa geometrijskim skupovima podataka navedenim u ostalim oblastima, kao što su sistemi geografskih mreža, administrativne jedinice i prostorne jedinice za statistiku (popisne četvrti). Ostale oblasti mogu se više indirektno povezati sa oblašću demografije, pošto se mogu koristiti kao ulazni parametar ili potrebna geometrija u generisanju skupa podataka agregiranog stanovništva, kao i oblasti adrese, zemljišni pokrivač te komunalne i javne servisi.
1.24 Područja koja su proglašena zonama zaštite ili kojima se upravlja u skladu sa
posebnim propisima
Područja upravljanja, uređena ili koja se koriste za izvještavanje na međunarodnom, evropskom, regionalnom i lokalnom nivou. Uključuju deponije, zaštićena područja oko izvora vode za piće, područja osjetljiva na nitrate, uređene vodene puteve na moru ili velike kopnene vode, područja za odlaganje otpada, područja zaštićena od buke, područja sa dozvolom za istraživanje ruda i rudarstva, područja riječnih bazena, odgovarajuće jedinice za izvještavanje i područja za upravljanje obalnim pojasom.
Širok raspon područja upravljanja, kako na evropskoj, tako i na nacionalnom, regionalnom i lokalnom nivou . Oblasti i objektni tipovi dopuštaju sadržaj informacija iz bilo kojeg sektora - npr. životna sredina, transport, zdravlje, obrazovanje, energija, ribarstvo, poljoprivreda.
Sektorsko specifične površine upravljanja sadrže informacije o zonama upravljanja u sektorima, koje nisu pokrivene oblašću "Administrativne jedinice". Ovdje je dato samo par primjera. Oni mogu uključivati: područja upravljanja zdravstvenom zaštitom, područja registrovana za odbranu, školska područja, vatrogasna područja, područja policijske odgovornosti, područja operacija spašavanja, nacionalne i Međunarodne pomorske organizacije - International Maritime Organisation (IMO) prihvaćene šeme separacije saobraćaja -Traffic Separation Schemes (TSS) i rute dubokih voda, vojne poligone za vježbanje, eksplozivna odlagališta itd.
Različiti režimi i propisi mogu biti relevantni, dati su neki primjeri;
Sigurnost na moru - Safety at Sea (SOLAS) širenje podataka i informacija za sigurnu plovidbu - NAVAREA obaveze mogu biti relevantne za proces specifikacije.
Područja riječnih slivova, područje upravljanja vodama, nije posebno definisan podskup vodenog sliva te je stoga važno da se definiše kao odvojeno područje upravljanja. Raspravlja se o pod-jedinicama za izvještavanje u skladu s propisima kojima je uređeno pitanje voda. U procesu specifikacije trebalo bi da se obrati pažnja na razlike u definicijama, prirodnih razgraničenja relevantnih za vodene slivove, razgraničenja na osnovu administrativne odluke koja je u sukobu sa prirodnim granicama, sliva relevantnog za upravljanje riječnim zonama. Područje riječnog sliva, misli se na površinu kopna i mora, sačinjenog od jedne ili više susjednih riječnih bazena zajedno sa svojim povezanim podzemnim i obalnim vodama, kao glavna jedinica za upravljanje riječnim bazenima. Geografska pokrivenost područja riječnog sliva - nazivi glavnih rijeka u okviru područja riječnog sliva zajedno sa preciznim opisom granica područja riječnog sliva. Predviđeni izvori: Ekološke/hidrološke institucije, obavezno izvještavanje. Sprovođenje razgraničenja u zemljama možda neće reflektovati prirodnu definiciju u skladu s propisima kojima je uređeno pitanje voda.
Opseg, primjeri upotrebe:
OSPAR jedinice za izvještavanje na moru: Opšti podaci u mikro mjerilu jedinica upravljanja na moru. Samo par područja regiona u Pan-Evropi. Predviđeni izvor: OSPAR Biogeografske regije: Evropa je podijeljena u 11 širokih biogeografskih zona. Podatak je poligonski skup podataka s glavnim biogeografskim regionima. Razmjer 1:10 miliona.
Važni objektni tipovi i atributi:
Regije upravljanja:

Sektor;

Pod sektor;

Tip upravljanja aktivnosti;

Odgovorna organizacija; i

Godina provjere.
Veze i preklapanje s ostalim oblastima:

Administrativne jedinice;

Saobraćajne mreže;

Hidrografija;

Geologija;

Prostorne jedinice za statistiku;

Korišćenje zemljišta;

Područja prirodnih opasnosti;

Morski regioni;

Biogeografski regioni;

Mineralne sirovine; i

Izvori energije.
1.25 Područja sa rizikom od prirodnih katastrofa
Osjetljiva područja koja su obilježena u skladu sa prirodnim opasnostima (svim atmosferskim, hidrološkim, seizmološkim, vulkanskim pojavama i požarima, koji zbog svojeg položaja, težine i učestalosti imaju potencijal da ozbiljno utiču na društvo), npr. poplave, odroni zemlje i slijeganje tla, snježne lavine, šumski požari, potresi, vulkanske erupcije.
"Područja prirodnih opasnosti" su područja gdje se površine prirodnih opasnosti presijecaju sa visoko naseljenim područjima i/ili područjima od posebne ekološke/kulturne/ekonomske vrijednosti. Rizik u tom kontekstu definisan je kao: rizik=opasnost x mogućnost pojavljivanja x osjetljivost izloženog stanovništva i ekološke, kulturne i ekonomske imovine u razmatranoj zoni.
Prirodne opasnosti su prirodni procesi ili fenomeni koji se pojavljuju u biosferi i koje mogu predstavljati štetan događaj. Prirodne opasnosti mogu se klasifikovati prema porijeklu: geološke, hidrometeorološke ili biološke. Opasni događaji mogu varirati u magnitudi ili intenzitetu, učestalosti, trajanju, mjerenoj površini, brzini nastanka, prostornoj disperziji i vremenskom razmaku. Međunarodna definicija o opasnosti relevantna je kod definisanja oblasti. Međunarodno dogovorena terminologija o opasnostima trebalo bi se usvojiti u ovom dokumentu Međunarodna strategija Ujedninjenih nacija za smanjenje katastrofa - United Nations International Strategy for Disaster Reduction (UNISDR): Opasnost je definisana kao potencijalno štetan fizički događaj, fenomen ili ljudska aktivnost koja može uzrokovati gubitak života ili ozljedu, štetu nad imovinom, društveni ili ekonomski poremećaj ili uništavanje životne sredine. Opasnosti mogu uključivati latentne uslove koji bi predstavljali buduće prijetnje i imali bi različite izvore: prirodni (geološki, hidrometeorološki i biološki) ili inducirani ljudskim procesima (uništavanje životne sredine i tehnološke opasnosti). Opasnost može biti jedna, sekvencijalna ili kombinovana u svom izvoru i efektu. Svaku opasnost karakteriše lokacija, intenzitet, učestalost i vjerovatnoću.
Geološke opasnosti su prirodni procesi ili fenomeni koji mogu uzrokovati gubitak života ili ozljedu, štetu nad imovinom, društveni ili ekonomski poremećaj ili uništavanje životne sredine. Geološka opasnost uključuje unutrašnje procese Zemlje ili procese tektonskog porijekla, kao što su potresi, geološka aktivnost na rasjedima, cunami, vulkanske aktivnosti i zračenja kao i spoljašne procese kao što su masovna kretanja, klizišta, odroni, lavine, propadanje površine, ekspanzivno zemljište i pukotine ili slivanje blata. Opasnost može biti jedna, sekvencijalna ili kombinovana u svom izvoru i efektu.
Mnoge opasnosti su nagle po svojoj prirodi. Međutim, nekoliko kategorija prirodnih opasnosti sa glavnim uticajem na civilnu sigurnost i na ekološke/kulturne i ekonomske aspekte nisu nagli. Oni mogu biti trajna pojava koja prolazi neprimijećeno (npr. isticanje gasa radona, deficit ili višak elemenata u tlu i vodama), ili spori fenomeni (spora kretanja tla). Tehnološke opasnosti uobičajno su nagli krah neke građevine ili proces koji uzrokuje značajna oštećenja. Prirodne opasnosti imaju potencijal da podstaknu tehnološke opasnosti. Uglavnom kontinuirani procesi kao zagađenja/zračenja nisu klasifikovani kao opasnost. Međutim, ponovljena zračenja mogu se zvati opasnostima, npr. velika hemijska zračenja, radijacija ili naftne mrlje. Kontinuirano zagađenje i ostali problemi životne sredine mogu imati negativan učinak takođe na veličinu i učestalost nekih vrsta prirodnih opasnosti.
Znanje o "Površinama prirodnih opasnosti" važno je kod identifikacije i delineacije zona rizika. Površine prirodnih opasnosti mogu odražavati sve atmosferske, meteorološke, hidrološke, geološke i fenomene šumskih požara koji, zbog svoje lokacije, težine i učestalosti, imaju potencijal i ozbiljni uticaj na društvo, npr. poplave, klizišta i slijeganje, lavine, šumski požari, potresi, vulkanske erupcije, skupljanje i oticanje tla, otpuštanje gasa radona, deficit ili višak elemenata u tlu i vodama. Podaci i servisi su vjerovatno potrebni za oba, procjenu rizika i vanredne situacije. Specijalni servisi za upozorenje mogu biti relevantni.
Ispod su dati primjeri nekih važnih prirodnih nepogoda, sa informacijama o nastanku: Mjesto i učestalost uz neke informacijama o bazama podataka, pokrivenost itd.
Područja sklona poplavama od unutrašnjih voda i jezera Područja poplavljena zbog izuzetnog podizanja podzemnih voda, rijeka i jezera, koja utiču na susjedno kopno ili udaljene površine koje su na istoj visini ili niže od poplavnih voda. Takođe utiču na naseljena i industrijska područja, poljoprivredno zemljište, saobraćajnu mrežu, kanalizacijski sistem, brane itd.
Pojava-Izgled: Ravna obalna područja, područje delti, dno dolina i obala.

Fizičko mapiranje područja podložnih poplavama, linija najviše zabilježenog nivoa,
podjela po zonama sa različitim klasama osjetljivosti. Potrebe podataka: detaljni model
reljefa i mjerenja na terenu;

Područja
sa
određenim
propisima/zabranama
za
različita
korišćenja
zemljišta/korišćenje resursa povezanim sa rizicima od poplava;

Građevine za kontrolu poplava;

Set podataka o zonama ograničenja za korišćenje zemljišta/ zgrade/ aktivnosti nizvodno
od akumulacije u slučaju da akumulacija pukne; i

Kapacitet drenaže zemljišta i površina brtvljenja-zaptivanje tla sa niskim kapacitetom
drenaže.
Područja sklona poplavama za vrijeme proljećnih plima/vanrednih podizanja nivoa mora Područja sklona poplavama zahvaljujući vanrednom porastu nivoa mora i rukavaca, koja utiču na susjedno kopno ili udaljene površine koje su na istoj ili nižoj visini od poplavnih voda. Utiču na domaćinstva i industrijska područja, poljoprivredna zemljišta, saobraćajnu mrežu, sistem kanalizacije, brane itd.
Pojava-Izgled- pojava: Ravna obalna područja, područja niža od nivoa mora. Najčešće luke, područja trgovina itd.
Učestalost: Poplave, kao oluje, su među najučestalijim prirodnim katastrofama u Evropi - sa tendencijom da su najskuplji u pogledu ekonomije i osiguranja.

Fizičko mapiranje područja podložnih poplavama, najviša zabilježena linija, takođe
podjela po zonama sa različitim klasama osjetljivosti. Potrebe podataka: detaljni visinski
model i/ili mjerenja na terenu.
-
Mjerenja radarskim satelitima ili vazdušnom opremom kako bi se izmjerilo nivo
vode;
-
Mjerenja na terenu;

Građevine za kontrolu poplava; i

Područja sa određenim propisima/zabranama za različita korišćenja zemljišta/izvori
korišćenja povezani sa rizicima od poplava.
Zemljotresi Zemljotresi su široko rasprostranjeni u EU i ostalim Evropskim zemljama. Najrazorniji događaji pojavili su se u mediteranskim zemljama, posebno Grčkoj i Italiji, koje su u zoni kolizije između evroazijske i afričke ploče. Kroz posljednje tri decenije nekoliko hiljada ljudi umrlo je i povrijeđeno, nekoliko stotina hiljada su postali beskućnici u događajima koji su potresli Grčku i Italiju. Podaci potrebni za dobijanje uvida i postupanje sa štetom:

Datum i vrijeme događaja; - lokacija epicentra, dubina, sa indeksom pouzdanosti -
magnituda i tip korišćene magnitude - posmatranja (lokalni intenzitet (MSK 1964
standard) sa indeksom pouzdanosti) - učinci -pukotine; i

Potrebni podaci za hitne operacije spašavanja.
Vulkanske erupcije:
Nekoliko aktivnih vulkana postoje u EU i ostalim evropskim zemljama. Aktivnost je niska i prijetnja je minimalna u poređenju sa ostalim prirodnim opasnostima. Neki destruktivni događaji dogodili su se u proteklih par decenija u nekim mediteranskim zemljama kao što je Italija. Akcije su se obično desile na lokalnom nivou.

Teško je opisati važne skupove prostornih podataka povezane s aktivnostima vulkana.
Klizanje blata, klizišta i brza (ispiranje soli) klizišta glinenog tla:

Tla bogata glinom koja se stežu i natiču;

Područja nestabilnog terena, klizišta podijeljena u zone različitih klasa osjetljivosti;

Lokacije bušotina sa daljim informacijama o sadržaju soli itd.;

Pogođeno područje, ako je područje subjekat snažnog padanja i klizanja; i

Područja sa restrikcijama aktivnosti - koje vrste aktivnosti su dopuštene kako bi se
spriječila klizanja i na kojim područjima se ne bi smjelo graditi. Različite zemlje imaju
različit prag npr. što se tiče stepena nagiba na zemlji koja se koristi za gradnju, vrijednost
zavisi od stanju tla (zemlja, glina, stijena).
Područja sklona klizanju planinskih blokova i odronima:
Pojava: Planinska klizanja blokova uglavnom se javljaju u planinskim područjima sa "mladim predjelima" gdje su mraz i vodena erozija aktivni, područja odrona sa strmim nagibima i labavim materijalima. Problemi se pojavljuju tamo gdje korišćenje zemljišta uključuje naselja, infrastrukturu itd.

Fizičko mapiranje područja podložnih odronima zemljanih blokova su podijeljeni u zone
sa različitim klasama osjetljivosti. Bazirane na mapiranju struktura stijena;

Fizičko mapiranje područja podložnih klizanju kamenja su podijeljeni u zone sa
različitim klasama osjetljivosti. Dalje informacije o vrsti materijala. Gruba podjela može
se bazirati na analizama uglova nagiba, dužini nagiba i stabilnosti stijena;

Predviđena pogođena područja koje slijede klizišta zemljanih blokova; same kamene
mase i poplavljena područja koja ih slijede; i

Područja sa određenim propisima/zabranama za različita korištenja zemljišta/izvori
korišćenja povezani sa rizikom od klizanja blokova zemlje i rizikom od odrona.

Građevine za usmjeravanje odrona.
Područja sklona klizanju snijega - lavinama Pojava: U područjima sa značajnim snježnim pokrivačem koji je kombinovan sa strmim padinama. Vjetar će uticati na stvaranje.

Fizičko mapiranje područja podložnih lavinama podijeljeno u zone sa različitim klasama
osjetljivosti;

Područja sa određenim propisima/zabranama za različita korišćenja zemljišta/izvor
korišćenja povezan je sa rizikom od lavina; i

Građevine za usmjeravanje lavina.
Područja sklona šumskim, livadskim i makijskim požarima Područja sklona šumskim, makijskim i livadskim požarima mogu se analizirati upotrebom:

Satelitskih slika;

Vegetacijskog pokrova, kompozicije i sloja; i

Meteoroloških podataka, padavina, temperatura, vjetra.
Područja instalacije sklona štetama od strane oluja/vjetra Pojava: Nejasna slika mora, obalnih dijelova i ravnih dolina, ali takođe i ostalih površina na kontinentu. Osim toga oluje, kao i poplave, su među najuobičajenijim prirodnim katastrofama u Evropi te najskuplje u pogledu ekonomije i osiguranja.

Skupovi podataka. Područja sa snimljenim ekstremnim vjetrom.
Obalna erozija Obalna erozija je važna kategorija prirodnih opasnosti rastuće važnosti u kontekstu klimatskih promjena.
Radijacijska područja Prirodno zračenje iz stijena i nekonsolidovanih grebena smatra se prirodnom zonom rizika zbog moguće visoke koncentracije radijacije u vazduhu zatvorenih prostora.
Opseg, primjeri upotrebe:
Nedavne lokalne i trans nacionalne katastrofe pokazale su Evropskoj Komisiji i zemljama članicama Evropske Unije da su podaci i servisi o prirodnim opasnostima i zonama rizika od najveće važnosti za efektivno upravljanje rizicima. Svake godine evropski građani osjete negativne posljedice prirodnih katastrofa pruzrokovane poplavama, šumskim požarima itd. To je bio jedan od razloga zašto je "Sigurnost građana" odabrana kao glavna oblast budućih EU istraživanja i razvoja aktivnosti u Zajedničkom istraživačkom centru - Joint Reasrch Centre - JRC tokom Petog okvirnog programa. Poboljšana opažanja rizika i opasnosti te koordinacija odgovornosti EU u službi životne sredine Generalnog direktorata (DG) i Istraživanja DG potkrepljuju taj trend. Osim toga evropske politike potkrepljuju različite tematske domene, planirane ili već na mjestu direktno povezane sa problemima prirodnih opasnosti npr. domena poljoprivrede i šumarstva - Generalnog direktorata za poljoprivredu, domena prostornog planiranja - Generalnog direktorata zs regionalna politiku. Što se tiče tehnoloških opasnosti, propis iz oblasti sprečavanja velikih udesa koji uključuje opasne supstance je od glavne važnosti u regulisanju upravljanjima rizicima.
Cilj je umanjiti rizike čineći društvo otpornijim na opasnosti ili umanjujući opasnosti ili regulišući korišćenje zemljišta i proizvodne aktivnosti podložne opasnostima. Neka područja su sklonija prirodnim opasnostima nego druga. Važno je identifikovti ta područja i izgraditi regulacije za dugoročno upravljanje zemljom i proizvodnjom. Karte, prostorne baze podataka i online prostorne servisi aktivno se koriste za izvršavanje takvog upravljanja. Analize rizika osnove su za rad na planiranju i životu sa prirodnim i tehnološkim opasnostima. Sva područja mogu na neki način biti pogođena prirodnim opasnostima i područja određenih vrsta ljudskih aktivnosti mogu biti pogođena tehnološkom opasnošću.
Različite vrste korisnika za rukovanje opasnostima mogu se podijeliti u četiri grupe:

Izvještavanje, razvoj trendova i ukupne politike, obično na nacionalnoj i međunarodnom
nivou;

Procjena prirodnih i tehnoloških rizika - mapiranje područja sklonih udarima opasnosti;

Faza planiranja osiguravanja javnog reda i mira - dugoročne regulacije i upravljanja
zemljom i aktivnostima;

Odgovor na katastrofu i hitne operacije.
U svrhu obavljanja ovih aktivnosti potrebna je određena vrsta podataka i usluga. To je jako bitno u dobro organizovanom sistemu snadbijevanja. Različite vrste podataka i usluga sa kojima se koristi i barata u takvim akcijama mogu biti:

Satelitske slike i fotografije iz vazduha i ortofoto snimci;

Vektorski skupovi podataka sa poligonima i linijama;

Jednostavne tabele sa informacijama o tački;

Adresni informacioni sistem kojim se barata u GIS bazama podataka;

Mrežni servisi različitih vrsta ponuđeni specifičnim zajednicama korisnika ili javnosti, od
strane organizacija kao što su meteorološki ili hidrološki uslovi.
Četiri različita oblika korišćenja identifikovana su ispod, uključujući i okosnice njihovih potreba za prostornim podacima. Bazirano na podacima, različite vrste usluga se mogu razviti i upotrijebiti.

Izvještavnja, pokazatelji, trendovi, cjelokupna politika razvoja: potreba za
prostornim podacima za ove svrhe je ograničena. Obično treba jedna izvještajna jedinica
kao što su zemlje, NUTS regija ili slivno područje. Tu će biti nekih korišćenja
generalizovanih verzija skupova podataka koji će se koristiti pod drugim kategorijama
korišćenja. Ukupni trendovi u učestalosti prirodnih nepogoda su neki od fenomena
povezani sa stanjem životne sredine - posebno klimatska stanja i zemljišni pokrivač.
Potrebni su podaci za analizu veza i zavisnosti.

Analiza osjetljivosti, mapiranje i predviđanje: Potrebni su skupovi podataka koji
opisuju i analiziraju prirodne fenomene koji uzrokuju opasnosti, uobičajeno su to
detaljni podaci visoke tačnosti kao što su mjerne stanice, detaljna tematska mapiranja
dobijena terenskim radom (npr. specifični aspekti tla i pokrivača), interpretacija
vazdušnih snimaka ili daljinska istraživanja, analize detaljnih visinskih modela, podaci
vodenog toka povezani sa riječnom mrežom i mrežom jezera, meteorološki i klimatski
podaci,mapiranja seizmičkih aktivnosti itd. Rad na tome prihvatile su se lokalne vlasti,
državne kartografske agencije, državne agencije koje se bave tom problematikom ili
međunarodne organizacije.

Prevencija planiranja fizičke i sektorske katastrofe: Stvaranje zajednica koje su
otporne na katastrofe dugoročnim fizičkim i sektorskim planiranjem, uglavnom je
sprovedeno na lokalnom i regionalnom nivou. Mapirnje koje je izvedeno od strane
tematske agencija, kako je opisano korišćeno je i transformisano u pojednostavljene
skupove podataka i dokumenata planiranja prikazujući područja visokog rizika i zone
zabrane na ili oko područja visokog rizika. Razgraničenjem zona zabrane potrebni su
populacijski podaci, planovi korišćenja zemljišta itd.

Hitne operacije/odgovor na katastrofu: Za hitne operacije, prirodne i tehnološke
opasnosti potrebene su više-manje iste vrste podataka. Kako bi se upravljanje u hitnim
situacijama ubrzalo i učinilo tačnijim, potrebno je redukovati efekte, podatke koji su
potrebni u nekoliko dijelova operacije:
o Praćenje; neprekidne ili situacije u realnom vremenu, daju informacije o
trendovima,
smjeru
itd.
Upotrebom
GNSS-a
povezanim
sa
detaljnim
topografskim kartografskim podacima,
o Pregled i identifikacija kvaliteta na kopnu i moru; osoba, vlasništva, proizvodnih
aktivnosti, infrastrukture i ekoloških kvaliteta koje mogu biti pogođene nekom
opasnošću/katastrofom. Postoji potreba o poznavanju informacija o stanovništvu
na
najnižem
mogućem
nivou,
informacije
o
nekretnini
omogućavaju
identifikovanje vlasnika individualnih nekretnina, registar adresa je za
informativne i identifikacijske svrhe, mapiranje površina/koje su pogođene
infrastrukturom, kao što su putevi, željeznica, telekomunikacijske linije, voda,
plinovod, naftne instalacije na moru, skladišni prostori za opasne materije, izvori
kao što su važna tijela podzemnih voda, ostale tačke ekstrakcije vode ili nekog
drugog izvora, korišćenje zemljišta, lokacije visokih vrijednosti za područje
životne sredine(biodiverzitet, rekreacija, mjesta kulturnog nasljeđa itd.)
o Lokacije izvora potrebne za izvođenje operacija; infrastruktura, kapacitet puteva
i željeznica, tačke snabdijevanja vodom, odlagališta hitne opreme (čamci
ekstraktori naftnih mrlja, vozila itd.) lokacija i kapacitet bolnica, informacije da bi
se vidjele informacije o vozilima na lokaciji, raspodjela sredstava, uvođenje
osoblja. Ovdje su takođe uključene administrativne granice za odgovorna
područja različitih tijela uključenih u operaciju.
Veze i preklapanja s ostalim oblastima:
Široko polje prirodnih rizika može se povezati i preklopiti sa ostalim oblastima, uglavnom onim koje se tiču fizičkog okruženja; Korišćenje zemljišta (planovi korišćenja zemljišta mogu uticati na zone rizika), Visine, Hidrografija, Zemljišni pokrivač, Geologija, sistemi za nadzor životne sredine, Okeanografsko-geografske karakteristike.
1.26 Atmosferski uslovi
Fizički uslovi u atmosferi. Uključuju prostorne podatke bazirane na mjerenjima, modelima ili na kombinaciji istih, a uključuje mjerne lokacije.
Starije verzije definicije oblasti pronađene su u infrastrukturi prostornih podataka IMS i dokumentima opsega radova:

Prostorni podatak reflektuje fizičke uslove vazduha i atmosfere, ili kao izolinije, mreže ili
druge prostorne forme. Ovo može biti bazirano na mjerenjima ili modelima. Ovo takođe
može uključiti i mjerene lokacije. (Infrastruktura prostornih podataka IMS, 2003.)

Fizički uslovi u atmosferi, predstavljeni kao linije, mreže ili tačke. Uključuju skupove
prostornih podataka bazirane na mjerenjima, modelima ili na kombinaciji istih i
uključuje mjerene lokacije. (Infrastruktura prostornih podataka Opseg radova, 2004.)
Da bi se raspon prostornih tipova podataka relevantan za ovu oblast smjestio u kontekst, smatramo da je tipičan "ciklus prognoze" nacionalnog meteorološkog servisa (NMS). On će: (a) prikupiti meteorološka opažanja u (recimo) 6-to satnom intervalu, (b) "prilagoditi" ih numeričkom modelu kako bi se dala procjena trenutnog atmosferskog stanja, (c) upotrijebiti te analize kao inicijalni uslov za model prognoze za par dana unaprijed. Četiri široke vrste podataka uključene su u različitim fazama ciklusa:
1. Opažanje: oko 11000 površinskih stanica globalno čini Globalni sistem opažanja,
izvještavajući o atmosferskim parametrima kao što su vrijeme, oblačnost,
temperatura, vlaga, vjetar, vidljivost, pritisak. Podskup ovih stanica čine
"klimatska opažanja" koja uključuju dnevni temperaturni minimum i maksimum,
sunčane sate, količinu kiše itd. Osim toga, oko 1000 "visinskih" stanica radi
opažanja pritiska, vjetra, temperature i vlažnosti radio sondama (slobodni uspon
balona). Volonterski posmatrački brodovi i bove izvode opažanja na moru
uključujući temperaturu morske površine, visinu i period talasa. Nekoliko stotina
hiljada izvještaja po danu o pritisku, vjetrovima i temperaturi načinjeno je iz
vazdušnih opažanja.
2. Sinoptičke analize: Mrežni vjetar, temperatura, vlaga, geopotencijalna visina,
padavine, itd. Takođe, elementi "osjetljivog vremena" (fronte, oblaci, olujne
aktivnosti itd.) će biti analizirani.
3. Prognoze: Brojni proizvodi prognoza proizvedeni su operativno. Konvencio-
nalna vremenska prognoza sadrži elemente slične sinoptičkim analizama.
4. Klimatološki podaci: Dugoročne vremenske serije podataka (ili opažanja ili
analiza) mogu se analizirati statistički kako bi se kreirala klimatologija (npr.
dekadski prosjeci 20-tog vijeka, sezonski/mjesečni minimum ili maksimum, itd.).
Postoji značajno preklapanje i nejasnoće između oblast "Atmosferski uslovi" i "Meteorološko- geografska obilježja" - npr. vremenski uslovi ("Meteorološko-geografska obilježja") uključujući padavine, temperature, vjetar itd., koje su precizne komponente stanja u atmosferi ("Atmosferski uslovi"). Date su brojne sugestije od strane učesnika kako bi se riješile ove nejasnoće. One uključuju:

Spajanje oblasti (bilo bi razumno razmisliti o spajanju oblasti tokom razvoja
specifikacija podataka);

Razlikovanje "podataka sa terena" (Atmosferski uslovi) od "tačkasto baziranih podataka"
(Meteorološko-geografska obilježja);

Razlikovanje "vremenskih serija i podataka u skoro realnom vremenu (Atmosferski
uslovi) od "mrežnih klimatskih podataka" (Meteorološko-geografska obilježja); i

Razlikovanje "klimatskih podataka" (Atmosferski uslovi) od "opažanja i prognoze"
(Meteorološko-geografske karakteristike).
Za razjašnjavanje nejasnoća između oblast , smatramo da pristup na više nivoa prema podacima zahtjeva procjenu primjene u Infrastrukturi prostornih podataka kroz "Dokumente o ekološkim tematskim potrebama korisnika" (2002). Podaci na lokalnom ili regionalnom nivou često su potrebni za upravljanje i implementaciju politike, dok su podaci niže rezolucije ("sitnije mjerilo") često traženi za izvještavanje i razvoj politike/evaluaciju. Poslednji sadrže preglede i integrisane proizvode podataka.
Opseg "Atmosferskih uslova" tematskih podataka trebao bi biti ograničen na (6-to satne) sinoptičke analize i prognoze (tipični mrežni model polja), klimatološke podatke i ostale integrisane i/ili pregled podataka.
U nekim područjima ostale su dvosmislenosti. Na primjer, nejasno je da li definicija treba uključiti informacije o kvalitetu vazduha (npr. čestice u vazduhu, atmosferska hemija). Isto tako, dok se morska opažanja prikupe kao potpora meteorološkoj prognozi, ona uključuju parametre povezane sa okeanografskim/morskim oblastima. Određeni fizički parametri atmosferskih graničnih nivoa mogu biti povezani ili sa atmosferskim ili okeanografskim oblastima. Te dvosmislenosti upućuju se na TWG i biće obaviješteni takođe upotrebom primjera korišćenja (use cases) i zahtjevima korisnika.
WMO upravlja posebnom mrežom (Globalni telekomunikacijski sistem) radi distribuiranja opažanja i podataka. Razmjena podataka vođena je od strane WMO Rezolucije 40, koja osigurava besplatno neograničenu razmjenu opažanih podataka "bitnih" za aktivnosti oko prognoza. "Dodatni" nominovani podaci i proizvodi mogu se osigurati uz naknadu, dok svi podaci moraju biti isporučeni besplatno (isključujući troškove reprodukcije i dostave) za istraživanje i edukaciju. ECOMET katalog (http://www.meteo.oma.be/ECOMET/Categories of data and products.htm) pruža "one-stop shop" indeks za oba: "bitne" i naplative podatke i proizvode koji se nude od strane evropskog NMS-a. Sličan katalog dostupan je od strane Evropskog centra za sredneročnu vremensku prognozu (ECMWF) (http://www.ecmwf.int/products/catalogue/).
Opseg, primjeri upotrebe:
Koristi se u ekološkoj i sigurnosnoj procjeni, procjeni klimatskih promjena itd. (Infrastruktura prostornih podataka IMS, 2003)

Za ETC "Obnovljivi izvori energije" komponentu podataka, procjena solarne energije
zahtijeva nacionalne, regionalne i lokalne popise o uslovima solarne energije (klimatski
podaci); energija vjetra zahtijeva klimatološka mjerenja vjetrovitosti.

Evaluacija "prirodnih i tehnoloških zona rizika" (ETC) bazirana je na dijelovima
klimatskih podataka (npr. kiša, snijeg, vjetar)

Informacije o vjetru/klimatske informacije potrebne su kod procjene erozije tla (ETC)

Informacije o vjetru neophodne su kod mapiranja uznapredovale zone buke (ETC).
Važni tipova objekata i atributi:
4-dimenzionalni (prostor+vrijeme) mrežni podaci pokrivača, jako veliki skupovi podataka; stanično bazirani ili analizirani zapisi o klimatologiji.
Veze i preklapanja s ostalim oblastima:
Preklapanje postoji s oblastima:

Meteorološko-geografska obilježja;

Okeanografsko-geografske karakteristike i Morske regioni (posebno za fizičke parametre
povezane sa razinom granica ili atmosferskom/okeanskom sredinom); i

Sistemi za nadzor životne sredine (meteorološke stanice i stanice za mjerenje kvaliteta
vazduha).
1.27 Meteorološko-geografske karakteristike
Vremenski uslovi i njihova mjerenja; padavine, temperatura, isparavanja, brzina i smjer vjetra.
Starije definicije oblasti pronađene su u Infrastruktura prostornih podataka IMS i dokumentima obuhvata radova:

Vremenski uslovi i njihova mjerenja; padavine, temperatura, isparavanja, brzina i smjer
vjetra (Infrastruktura prostornih podataka, 2003.)

Vremenski uslovi i njihova mjerenja; padavine, temperatura, isparavanje, brzina i smjer
vjetra (Infrastruktura prostornih podataka Obuhvat, 2004.)
Da bi se raspon prostornih tipova podataka relevantan za ovu oblast smjestio u kontekst, smatramo da je tipičan "ciklus prognoze" Nacionalnog meteorološkog servisa - National meteorological service (NMS). Ovo će: (a) prikupiti meteorološka opažanja u (recimo) 6-to satnom intervalu, (b) "prilagoditi" ih numeričkom modelu kako bi se dala procjena trenutnog atmosferskog stanja, (c) upotreba tih analiza kao inicijalni uslov za model prognoze za par dana unaprijed. Četiri široke vrste podataka uključene su u različitim fazama ciklusa:
1. Opažanje: oko 11000 površinskih stanica globalno čini Globalni sistem opažanja,
izvještavajući o atmosferskim parametrima kao što su vrijeme, oblačnost,
temperatura, vlaga, vjetar, vidljivost, pritisak. Podskup ovih stanica čine
"klimatska opažanja" koja uključuju dnevni temperaturni minimum i maksimum,
sunčane sate, količinu kiše itd. Osim toga, oko 1000 "visinskih" stanica radi
opažanja pritiska, vjetra, temperature i vlažnosti radio sondama (slobodni uspon
balona). Volonterski promatrački brodovi i bove izvode opažanja na moru
uključujući temperaturu morske površine, visinu i period talasa. Nekoliko stotina
hiljada izvještaja po danu o pritisku, vjetrovima i temperaturi načinjeno je iz
vazdušnih opažanja.
2. Sinoptičke analize: Mrežni vjetar, temperatura, vlaga, geopotencijalna visina,
padavine, itd. Takođe, elementi "osjetljivog vremena" (fronte, oblaci, olujne
aktivnosti itd.) će biti analizirani
3. Prognoze: Brojni proizvodi prognoza proizvedeni su operativno. Konve-
ncionalna vremenska prognoza sadrži elemente slične sinoptičkim analizama
4. Klimatološki podaci: Dugoročne vremenske serije podataka (ili opažanja ili
analiza) mogu se analizirati statistički kako bi se kreirala klimatologija (npr.
dekadski prosjeci 20-tog vijeka, sezonski/mjesečni minimum ili maksimum, itd. ).
Postoji značajno preklapanje i nejasnoće između oblasti "Atmosferski uslovi" i "Meteorološko- geografska obilježja" - npr. vremenski uslovi ("Meteorološko-geografska obilježja") uključujući padavine, temperature, vjetar, itd. koje su precizne komponente stanja u atmosferi ("Atmosferski uslovi"). Date su brojne sugestije od strane učesnika kako bi se riješile ove nejasnoće. One uključuju:

Spajanje oblasti ( bilo bi razumno razmisliti o spajanju oblast tokom razvoja
specifikacija podataka);

Razlikovanje "podataka sa terena" (Atmosferski uslovi) od "tačkasto baziranih podataka"
(Meteorološko-geografske karakteristike);

Razlikovanje "vremenskih serija i podataka u skoro realnom vremenu" (Atmosferski
uslovi) od "mrežnih klimatskih podataka" (Meteorološko-geografska obilježja); i

Razlikovanje "klimatskih podataka" (Atmosferski uslovi) od "opažanja i prognoze"
(Meteorološko-geografska obilježja).
Za razjašnjavanje nejasnoća između oblast , smatramo da pristup podacima na više nivoa zahtjeva procjenu primijenjenu u Infrastrukturi prostornih podataka kroz "Dokumente o ekološkim tematskim potrebama korisnika" (2002). Podaci na lokalnom ili regionalnom nivou često su potrebni za upravljanje i implementaciju politike, dok su podaci niže rezolucije ("sitnije mjerilo") često traženi za izvještavanje i razvoj politike/evaluaciju. Poslednji sadrže rezime i integrisane informatičke servise.
Opseg "Meteorološko-geografskih karakteristika" tematskih podataka trebao bi da je ograničen na lokalnom nivou visoko rezolucijske podatke (povezane sa vremenom), obična opažanja.

Ovo uključuje sinoptička opažanja sa stanica koje čine WMO RA VI (evropsku) osnovnu
regionalnu sinoptičku mrežu.
WMO upravlja posebnom mrežom (Globalni telekomunikacijski sistem) radi distribuiranja opažanja i informatičkih usluga. Razmjena podataka vođena je od strane WMO Rezolucije 40, koja osigurava besplatno neograničenu razmjenu opažanih podataka "bitnih" za aktivnosti oko prognoza. "Dodatni" nominovani podaci i proizvodi mogu se osigurati uz naknadu, dok svi podaci moraju biti isporučeni besplatno (isključujući troškove reprodukcije i dostave) za istraživanje i edukaciju. Ekonomska interesna grupacija nacionalnih meteoroloških službi - Economic Interest Grouping of the National Meteorological Services ECOMET katalog (http://www.meteo.oma.be/ECOMET/Categories of data and products.htm) pruža "one-stop shop" indeks za oba: "bitne" i naplative podatke i proizvode koji se nude od strane evropskog NMS-a. Sličan katalog dostupan je od strane Evropskog centra za srednji nivo vremenske prognoze (ECMWF) (http://www.ecmwf.int/products/catalogue/).
Opseg, primjeri upotrebe:
Koristi se od strane sektora za životnu sredinu kako bi se predvidjele prirodne opasnosti npr. poplave, suše, šumski požari. Takođe ga koriste ostali sektori, npr. vodosnadbijevanje za procjenu punjenja, za prognoziranje poljoprivredne proizvodnje, za davanje meteorološke prognoze pomorcima itd. (Infrastruktura prostornih podataka IMS, 2003.)

Potreban je raspon meteoroloških opažanja kako bi se podržale "vazdušne i klimatske
promjene u sprovođenju i upravljanju politikom zaštite životne sredine Evropskog
tematskog centra - European Topic Centre (ETC);

Potreban je niz meteoroloških podataka (npr. kiša, snijeg, temperatura, vjetar) za
predviđanje i upravljanje prirodnim opasnostima - poplave, lavine, požari; i za
upravljanje hemijskim i ostalim opasnim događajima Evropskog tematskog centra -
European Topic Centre (ETC).
Važni objektni tipovi i atributi:
Sirovi podaci organizovani po stanicama (lokacija, id).
Moguća visoka prostorna rezolucija sirovih površinskih podataka, od instrumenata daljinskih istraživanja i njihove najbolje rezolucije.
Veze i preklapanja sa ostalim oblastima:
Potencijalno preklapanje sa oblastima:

Atmosferski uslovi;

Okeanografsko-geografska obilježja i Morske regioni (posebno za fizičke parametre
povezane sa slojem granica ili atmosferskim/okeanskim interfejsom); i

Sistemi za nadzor životne sredine (meteorološke stanice i kvaliteta vazduha).
1.28 Okeanografsko-geografske karakteristike
Fizičke karakteristike okeana (struje, salinitet, visina talasa itd.).
Starije definicije oblasti pronađene su u Infrastrukturi prostornih podataka IMS i dokumentima radova:

Mjerljive fizičkie karakteristike okeana npr. salinitet, zasićenost kiseonikom, ostale
hemijske komponente, struje. Prikazivanje npr. kao izolinije, mreže ili ostale prostorne
organizacije. Direktno bazirane na mjerenjima ili kombinovane sa modelima.
(Infrastruktura prostornih podataka IMS, 2003.); i

Fizičke karakteristike okeana (npr. struje, salinitet, itd.) prikazane kao linije, mreže ili
tačke. Uključuju prostorne skupove podataka bazirane na mjerenjima, modelima ili na
kombinaciji istih i uključuju mjerne lokacije (Infrastruktura prostornih podataka
Obuhvat, 2004.).
Obje oblasti "Okeanografsko-geografske karakteristike " i "Morske regioni" se bave fizičkim uslovima morskih vodenih masa. (To je slično preklapanje sa onim koje postoji za oblasti 1.13 "Atmosferski uslovi" i 1.14 "Meteorološko-geografske karakteristike".) Kako bi se riješile nejasnoće, pristupu podacima na više nivoa potrebna je procjena primijenjena u Evropskom tematskom centru - European Topic Centre - ETC-u. Podaci na lokalnom i regionalnom nivou često su potrebni za upravljanje i implementaciju politike, dok podaci niže rezolucije ("sitnije mjerilo") često potrebni za izvještavanje i razvoj politike/evaluaciju. Poslednji uključuje rezime i integrisane informatičke servisi.
Oblast "Okeanografsko-geografske karakteristike" smatra se kao oblast koja se odnosi na visoka mora i velike okeanske fizičke/dinamičke strukture.
Operativna predviđanja okeanskih dinamičkih fizičkih uslova - zajedno sa preduslovima opažanjima - ključni su element ove oblasti (npr. kroz GMES osnovne morske servise), sa Francuskom i Velikom Britanijom koje obje vode operativne sisteme.
Relevantni podaci opažanja uključuju:

Daljinska istraživanja morske površine, temperaturu, dinamičku topografiju (satelitskim
visinomjerima), radar sa sintetičkim otvorom, (za primarne produktivnosti i
sedimentaciju);

Bove - brzina površine, temperatura, atmosferski pritisak;

Brodovi-povoljnih prilika i regularni dobrovoljni posmatrački brodovi osiguravaju
temperaturne profile (bathythermograph); i

Argo bova osiguravaju temperaturne i salitetske profile.
Opseg, primjeri upotrebe:
Koriste se u procjeni životne sredine, sektoru eksploatacije resursa. (Infrastruktura prostornih podataka IMS, 2003.)
Važni objektni tipovi i atributi:
Obični vertikalni profil ili podaci površine okeana.
Polja prognoze su veliki mrežni 4-dimenzionalni (prostor+vrijeme) podaci o prekrivaču.
Veze i preklapanje sa ostalim oblastima:
Potencijalno preklapanje sa oblastima:

Morski regioni;

Meteorološko-geografske karakteristike, Atmosferski uslovi (npr. vrlo slični prostorni
objektni tipovi i takođe fizičke veze kroz sloj granice i uobičajni režimi posmatranja); i

Ortofoto snimci (jer mnogi okeanografski podaci dolaze od satelitskih daljinskih
istraživanja, npr. boja okeana, visina morske površine, temperatura morske površine).
1.29 Morska područja
Fizički uslovi mora i slanih vodenih tijela podijeljena u regione i podregione sa zajedničkim karakteristikama.
Starija verzija definicije oblasti pronađena je u Infrastrukturi prostornih podataka IMS dokumentima:

Mora i slana vodena tijela podijeljena su u regioni i podregioni. Svaki region sa
zajedničkim karakteristikama koje se tiču vodenog toka/cirkulacije, susjednih vodenih
slivova, biohemije ili temperature vode, bazirana na naučnim kriterijumima. Detaljne
informacije postoje na regionalnom nivou. (Infrastruktura prostornih podataka IMS,
2003.).
Oboje i "Okeanografsko-geografske karakteristike" i "Morski regioni" odnose se na fizičke karakteristike morskih vodenih masa. (Ovo je slično preklapanje s onim koji postoji za oblasti 1.13 "Atmosferski uslovi" i 1.14 "Meteorološko-geografska obilježja"). Kako bi se riješile nejasnoće, a pristup podacima na više nivoa zahtjeva procjenu primijenjenu u ETC-u. Podaci na lokalnom ili regionalnom nivou često su potrebni za upravljanje i primjenu politike, dok su podaci
niže
rezolucije
("sitnije
mjerilo")
često
traženi
za
izvještavanje
i
razvoj politike/evaluaciju. Poslednji uključuje rezime i integrisane informacione servisi.
"Morski regioni" smatraju se oblašću koja je usmjerena na lokalnom/regionalnom nivou obalne zone.
Dok se 1.15 "Okeanografsko-geografske karakteristike" fokusiraju na fizičke karakteristike i opštu cirkulaciju priobalnih okeanskih voda, oblast "Morski regioni" bavi se morskim karakteristikama obalne zone - regionima definisanim kao "prelazne vode" i "obalne vode" u propisima kojima je uređena oblast voda:

Prelazne vode: tijela površinskih voda u blizini ušća rijeka koja su slankasta po karakteru
kao rezultat blizine obalnih voda, ali koja su znatno pod utjecajem slatkovodnih voda; i

Obalne vode: Površinske vode na kopnenoj strani linije, svaka tačka koja je na
udaljenosti od jedne nautičke milje prema morskoj strani od najbliže tačke osnovne linije
od koje se mjeri širina teritorijalnih voda, šireći se prema potrebi do spoljne granice
prelaznih voda.
Svjetska meteorološka organizacija takođe ima klasifikaciju morskih regiona koja je geometrijski bazirana, dijeleći okean u Marsden kvadrate.
Biotički i fizički parametri i indikatori važni su kod klasifikacije i razgraničenja morskih područja. Zahtjevi fizičkih podataka za važnim indikatorima definisani u u propisima kojima je uređena oblast voda i Politici integrisanog upravljanja obalnim zonama navedeni su u ETC dokumentima. To uključuje:

Hranjive materije (nitrate, fosfate i azot: udio azota) od strane regionalnog mora i tipa
vodenog tijela;

Koncentraciju opasnih supstanci i zagađivača (uključujući teške metale, dugotrajne
organske zagađivače);

Indikatori produktivnosti (uključujući površinski hlorofil);

Biološka klasifikacija voda;

Vodene mase/nivoi karakteristične rasute temperature i svojstva saliniteta;

Karakteristike polarnih područja (uključujući pakete leda);

Vjetar (klimatološki i meteorološki);

Životni parametri (sediment, životne zajednice/staništa);

Nivo mora;

Hemijske vrste i koncentracije;

Fizičke karakteristike (uključujući temperaturu, salinitet);

Struje (uključujući površinske struje);

Zone plime i osjeke; i

Talase.
Opseg, primjeri upotrebe:
Propisima kojima je uređena oblast voda, klase površinskih slanih vodenih tijela, prelaznih voda, obalnih voda u određenoj mjeri poklapaju se sa morskim područjima, ali imaju granice bazirane na administrativnom/izvještajnom kriterijumu, nije naučno definisano. (Infrastruktura prostornih podataka IMS, 2003.)
Politika integralnog upravljanja obalnom zonom - Integrated Coastal Zone Management (ICZM) je evropska integrisana strategija za upravljanje obalnim zonama. Ključna područja djelovanja za ICZM su procjene uticaja na životnu sredinu, planiranje uz obalu, upravljanje staništima i kontrola zagađenja. Radna grupa na pokazateljima i podacima odredila je skup pokazatelja održivog razvoja obalnih zona, uključujući podizanje nivoa mora i ekstremne vremenske uslove.
Važni objektni tipovi i atributi:

Tačkasta mjerenja fizičko-hemijskih svojstava;

Biološka mjerenja;

Meteorološka i klimatska mjerenja (variranje u vremenu); i

Plimne vremenske serije i struje.
Veze i preklapanje sa ostalim oblastima:
Potencijalno preklapanje sa oblastima:

Okeanografsko-geografske karakteristike; i

Meteorološko-geografske karakteristike, Atmosferski uslovi (npr. vrlo slični prostorni
objektni tipovi i takođe fizičke veze preko sloja granica i režimi zajedničkog
posmatranja).
1.30 Biogeografski regioni
Područja sa relativno homogenim ekološkim uslovima koji imaju zajedničke osobine.
Biogeografski regioni prikazuju razmjere regiona sa uobičajenim karakteristikama, uglavnom bazirani na klimatskim, topografskim i geobotaničkim informacijama. Tako biogeografska područja prikazuju područja sa relativno homogenim ekološkim uslovima. Uključeni u ovu oblast su i podaci vegetacijskih karata. Određivanje strukture i kompozicije vegetacije bazirano je prvenstveno sa polazišta ekosistema i njihove korelacije sa određenim uslovima mjesta, uobičajno bazirano na biljno-sociološkoj klasifikaciji. Vegetacija se može mapirati kao trenutni ili potencijalni zemljišni pokrivač. Klasifikacija potencijalne vegetacije opisuje potencijalnu distribuciju glavnih prirodnih zajednica biljaka.
Mapiranje je bazirano prvenstveno na preostalim predstavnicima prirodnih ili gotovo prirodnih ekosistema koji odgovaraju aktualnim klimatskim i edafskim okolnostima. Nekoliko visoko rangiranih podataka postoje za Pan-evropskom nivou, podaci krupnog mjerila sa rascjepkanim sistemima, rezolucijom i pokrivenošću.
Jednom kad je proizveden, biogeografski podatak i potencijalna vegetacijska karta podataka, potencijalne karte vegetacija su relativno stabilne i smatraju se referentnim kartama podataka. Kartiranje postojeće vegetacije na lokalnom nivou potrebno je obnoviti da bi se prikazale promjene u vegetaciji.

Nomenklatura: Visok nivo i pan-evropski podatak slijede dogovorene nomenklature.
Što se tiče lokalnih i regionalnih podataka, tamo postoji široki izbor nomenklatura, npr. u
vegetacijskom mapiranju;

Raspon u tačnosti: Biogeografski regionalni podaci obično podaci sitnijeg mjerila, npr. u
1:1 000 000 ili sitnije. Vegetacijski podaci obično su detaljniji, na lokalnom nivou podaci
srednje preciznosti, 1: 50 000 ili bolje. Obučno korišćena mjerila su 1:25 000 i 1:10 000.

Pojašnjenje o definiciji, granica prema ostalim oblastima infrastrukture
prostornih podataka: Granica između pokrivača i biogeografskih regiona.
Opseg, primjeri upotrebe:
Podaci se koriste za poređenja i procjene biodiverziteta i očuvanja na međunarodnom, nacionalnom, čak i regionalnom nivou. Podaci u obliku detaljnih podataka koriste se u upravljanju zemljištem i lokalnim planiranjem korišćenja zemljišta. Evropska biogeografska područja upotrebljavaju se za Natura 2000 potvrđivanje nacionalnih predloga, koji se obavljaju za čitavu regiju.
Znanje o širini lokalnih i regionalnih biogeografskih regiona, npr. u obliku vegetacijskih karata, mogu se koristiti kod identifikacije klimatskih, topografskih ili geoloških karakteristika, kao da postoji korelacija između određenih vrsta i takvih faktora. Gledajući geologiju, to je jedan od najvažnijih faktora koji se tiče biodiverziteta ili direktno (mahovina, lišajevi, biljke koje se direktno razvijaju na goloj podlozi, trošene stijene) ili indirektno, putem tla i geološki izvedenih glavnih i elemenata u tragovima koje ono sadrži. Vegetacijski biotopi su poprilično često striktno povezani sa postojećim donjim kiselinama, klasifikovanim ili gvožđe-magnezijumskim stijenama (bazalt, ofioliti na primjer). Postoje čak jako elementarno specifične biljke kao što su Armeria maritima ssp. Halleri koja je jedna od rijetkih biljaka koja se razvija na tlima bogatima cinkom, čineći ih jako korisnim pokazateljem za istraživanje depozita oksidirajućeg cinka u Zapadnoj Evropi. Razmjera poljoprivrednih zajednica je jedinstveni alat geološkog mapiranja. Geobotanika je naučno posebna (vidjeti npr. http://www.cstars.ucdavis.edu/papers/html/ustinetal1998b/). Vegetacija - potencijalna vegetacija:

Klasifikacioni sistem/nomenklatura;

Ime klase;

Kod klase;

Datum zadnje verifikacije; i

Izvor.
Primjeri podataka:

Biogeografsko područje: Evropa je podijeljena u 11 širokih biogeografskih područja.
Podatak je skup poligonskih podataka sa glavnim biogeografskim područjima. Granice bi
se trebale smatrati dvosmislenima pošto su generalizovane tako da se uklapaju sa
političkim granicama. Mjerilo 1:10 000 000;

Potencijalna vegetacija: Određivanje strukture i kompozicije potencijalne prirodne
vegetacije bazirano je prvenstveno na preostalim stajalištima prirodnih ili skoro
prirodnih ekosistema i njihove korelacije sa određenim uslovima na mjestu. Klasifikacija
prirodnih (potencijalnih) vegetacija opisuje potencijalnu distribuciju glavnih zajednica
biljaka koje odgovaraju trenutnim klimatskim i edafskim uslovima. Postoje usklađeni
Pan-Evropski podaci, raspršeni podaci sa šarolikim klasifikacionim sistemima na nižim
nivoima. Prekrivenost: Pan-Evropa: Postojeći skupovi podataka u sitnom obimu;

Ekološka područja: Digitalne karte Evropskih ekoloških područja (DMEER) ocrtavaju i
opisuju ekološki različita područja u Evropi, na osnovu ažuriranih znanja o klimatskim,
topografskim i geobotaničkim evropskim podacima, zajedno sa procjenom velikog broja
stručnjaka iz nekoliko Evropskih institucija povezanih sa prirodom i Svjetski fond za
divlje životnje - World Wildlife Fund - WWF-om. Cilj karte ekoloških područja u Evropi je
pokazati širinu područja sa relativno usklađenim ekološkim uslovima, u okviru kojih su
poređenja i procjene biodiverziteta smislene. Prekrivenost: Pan-Evropska. Postojeći
skupovi podataka u maloj razmjeri;

Oko biogeografskih područja za evropska mora još nije postignut konačni dogovor. Do
danas se diskutovalo o različitim modelima od EEA, ICES i OSPHAR/HELCOM te se još
moraju dodati nakon označavanja.
Važni objektni tipovi i atributi:
Biogeografska/ekološka područja:

Klasifikacioni sistem nomenklatura;

Ime klase;

Kod klase;

Datum zadnje verifikacije; i

Izvor.
Veze i preklapanje sa ostalim oblastima:
Biogeografska područja mogu se povezati sa bio različitim oblastima kao što su infrastruktura prostornih podataka oblasti Rasprostranjenost vrsta i Staništa i biotopi, ali može se takođe povezati sa oblastima Zemljišni pokrivač, Geologija, Tlo, Izvori minerala i Područje upravljanja/zaštićena područja/uređena područja i jedinice za izvještavanje.
1.31 Staništa i biotopi
Geografska područja za koja su svojstveni posebni ekološki uslovi, procesi strukture i funkcije (za održavanje života) koje fizički pomažu organizmima da žive na njima. Uključujući kopnena i vodena područja koja se razlikuju po geografskim, abiotičkim i biotičkim karakteristikama, bilo da su u potpunosti prirodna ili poluprirodna.
Kategorija "Staništa i biotopi" prostornih podataka definisana u Infrastrukturi prostornih podataka jedna je od nekoliko oblasti u široj grupi bioloških organizama i bioloških zajednica - biodiverziteta. Uključuje staništa i biotope kao površine i njihove granice. Zajedničko svim prostornim podacima koji padaju pod ovu kategoriju je karakterizacija distribucije geografskih područja koja su funkcionalne površine živućim organizmima, biotopi koji su prostorni i biotička sredina biotičke zajednice/biocenoza, dok su staništa prostorna sredina posebnih vrsta.
Klimatski, geološki, hemijski i biološki uslovi utiču na raspodjelu vrsta i zajednica, na taj način i raspodjelu i slove staništa i biotopa. Neke vrste imaju striktne specifične zahtjeve prema životnoj sredini, dok drugi prihvataju široki raspon u uslovima životne sredine. Na taj način biotopi i staništa mogu široko varirati između različitih organizama. Neke vrste mijenjaju biotope kroz godinu, promjenama tokom sezone ili zahvaljujući migraciji. Neka staništa/biotopi zavise od upravljanja, npr. sve vrste kultivisanih krajeva. Vremenske serije mapiranja mogu se koristiti kod identifikovanja promjena u biotopima/staništima.
Opis živih površina za bilo koju vrstu biote, uglavnom korišćene kao izraz za opisivanje površina koje koriste zoo-bioti. Staništa obično slijede geo botanička/bio-geografska područja/vegeta- cijske tipove. U grubim terminima klase zemljišnog pokrivača i vegetacijske klase predstavljaju kopnena staništa. Staništa takođe mogu biti opisana na detaljnijem nivou npr. živica, potoci itd. Na moru razlike u temperaturi, slanosti, strujama, dubini, topografiji, geologiji morskog dna mogu stvoriti različita staništa. Podaci staništa i biotopi mogu se izraditi terenskim mapirajem, daljinskim istraživanjima i interpretacijom vazdušnih fotografija ili modeliranjem.
Različita dokumenta koje slijede različite definicije za staništa i biotope. Primjer je konzervacija prirodnih staništa i divlje flore i faune. EUNIS je razvijen kao međunarodna nomenklatura za staništa. Različite zemlje ili zajednice imaju različite klasifikacijske sisteme. Mogu postojati teškoće u mapiranju tačno određenih klasa staništa između nacionalnih nomenklatura te takođe između nacionalnih i evropskih nomenklatura. Da bi se pronašle zajedničke evropske definicije i nomenklature potrebno je uzeti u obzir oba nacionalna sistema i različite definicije korišćene od strane međunarodnih zajednica.
Staništa i biotopi uključuju područja predstavljena prirodnim granicama, klasifikovana su prema svom ekološkom ili fizičkom stanju. Nisu uključena staništa i biotopi koja su označena kao zaštićena područja, ona padaju pod neku drugu kategoriju Infrastrukture prostornih podataka oblasti, uglavnom "Zaštićena područja", pošto ona predstavljaju regulacije administrativnih područja i neekološki utemeljene granice.
Izrazi prirodno ili poluprirodno trebaju pojašnjenje. Vještački predjeli koji su staništa (kultivisani predjeli kao područja gradova, kultivisana zemlja, voćnjaci, pašnjaci itd.) mogu se definisati tako da budu van djelokruga ove oblasti.
Opseg, primjeri upotrebe:
Procjene promjena u predjelu i učincima divljih života i biljnog svijeta. Povezano sa propisom o staništima. Staništa spomenuta su u komponenti podataka "regulacija površine".
Odabir vrijednih staništa određen je prema propisom za staništa i ptice. U morskoj sredini odabir vrijednih staništa takođe se određuje prema OSPAR i HELCOM konvenciji.
Dokumentuje se i koristi za identifikovanje biološke raznovrsnosti u okviru područja ili država, kao zemljopisna zastupljenost, različitost i frekvencija zastupljenosti. Koristi se za planiranje zaštite i upravljanje biodiverzitetom u prirodnom, poluprirodnom i vještačom okruženju. Korisnici su vlade, stručne organizacije za zaštitu životne sredine, ali takođe i praktičari upravljanja zemljom i izvorima, farmeri ili ribari. Veliki je diverzitet različitih klasifikacionih sistema i broja detalja u mapiranju.

Mjerilo: Indikacija uobičajnih razmjera mapiranja: od 1:5 000 do 1:1 000 000

Politika zajednice: 6EAP, propisi o staništima i pticama, CAP

Inicijative: NATURA2000, RAMSAR baza podataka, CORINE biotopi i dr.
Primjeri podataka:
Mjesta biotopa: Područja ekološkog biodiverziteta interesnih područja, snimljena pod Natura programom. Mjesta od specifičnog ekološkog interesa u očuvanju prirode, snimljena bez obzira da li su zaštićena ili nisu.
Atributi: statistike sa lica mjesta, podaci staništa, sisari, ptice, vodozemci, ribe, beskičmenjaci, biljke, status označenog mjesta.
Pokrivenost: EU i Phare zemlje, završeno prikupljanje podataka 1995.
Važni objektni tipovi i atributi:
Biotop (površina):

Klasifikacija/Sistem nomenklature;

Kategorija hijerarhijskog nivoa;

Ime kategorije;

Kod kategorije;

Datum mapiranja: datum verifikacije;

Vrste ili tipične vrste pronađene u biotopu; i

Opis mjesta.
Područje staništa:

Klasifikacija/Sistem nomenklature;

Kategorija hijerarjhiskog nivoa;

Ime kategorije;

Kod kategorije;

Datum mapiranja: datum verifikacije;

Vrste ili grupe vrsta na koje se odnosi stanište; i

Opis mjesta.
Nomenklatura bi trebalo što je više moguće slijediti međunarodne dogovore.
Veze i preklapanja s ostalim oblastima:
Staništa i biotopi mogu se povezati sa biološki različitim oblastima kao što su infrastruktura prostornih podataka, oblasti Biogeografska područja i Rasprostranjenost vrsta, ali se mogu povezati i sa oblastima Zemljišni pokrivač, Korišćenje zemljišta, Geologija, Tlo i Izvori minerala.
1.32 Geografski razmještaj biljnih i životinjskih vrsta
Geografski razmještaj životinjskih i biljnih vrsta, razvrstan po mreži, regiji, jedinici uprave ili drugoj analitičkoj jedinici.
Pan-evropske, nacionalne ili lokalne kartografske inicijative, rezultiraju prostornim podacima za vrste u kopnenoj i morskoj sredini, npr. ptice, insekti, sisari, vodozemci, gmizavci, ribe ili vaskularne biljke.
Pojašnjenje:

Definicija u predlogu infrastrukture prostornih podataka ne uključuje individualna
posmatranja ili ostale tačkasto definisane podatke, nego se fokusira na agregirane verzije
podataka o geografskoj rasprostranjenosti vrsta. Spajanje može biti na bilo kom nivou
rezolucije, npr. u geografskim mrežnim sistemima podijeljena na 100x100 metarsku
mrežu ili 50x50 metarsku mrežu ćelija. Možda bi trebalo da bude prihvaćena i uključena
u infrastrukturu prostornih podataka, tačkasto bazirana posmatranja i generisanje
izolinija između posmatranja. Možda se to može definisati kao opcija kod "ostalih
analitičkih jedinica". Agregacija se takođe može tumačiti, ne samo kao prostorno
bazirana agregacija, nego i kao vremenski bazirana agregacija.

U infrastrukturi prostornih podataka, kao definicija spominju se samo vrste. Ali ranije
verzije infrastrukture prostornih podataka, dokumenata (Infrastruktura prostornih
podataka IMS, 2003.) spominju i vrste i grupisane vrste npr. familija (familia).
Opseg, primjeri upotrebe:
Različite inicijative imaju za cilj da dobiju potpune informacije rasprostranjenosti vrsta ažuriranim podacima u Pan-Evropskom mjerilu, za veliki skup sisara, ptica, sisara i gmizavaca, vaskularnih biljaka, zajedno sa sličnim podacima za odabir ostalih organizama važnih kod indikacije o kvalitetu vazduha, kopnenih voda, morske sredine, tla i staništa.
Skupovi digitalnih podataka mogu se koristiti za očuvanje i statističke analize, kao baza istraživanja u ekologiji i biodiverzitetu, za očuvanje i upravljanje prirodom. U procjeni biodiverziteta važno je imati informacije o rasprostranjenosti vrsta, količini i razvoju kroz vrijeme. Potrebno je za Natura-u 2000. Dokumentovano je u nauci i koristi se kod identifikovanja biotičke raznovrsnosti u okviru biotičkih područja ili zemalja, geografska distribucija, promjene tokom vremena, kombinacija vrsta u zajednici i kovarijansa sa faktorima sredine i ekološkim kvalitetama. Koristi se za planiranje zaštite i upravljanja biorazličitosti u prirodnim i polu prirodnim kao i vještačkoj sredini. Korisnici su i vlade i stručne organizacije za zaštitu životne sredine, ali takođe i praktičari upravljanja i izvorima, farmeri ili ribari. To je od velike važnosti za komercijalno iskorišćavanje ekonomskih prirodnih izvora kao što su životinje i biljke koje žive u prirodnim i poluprirodnim sredinama, npr. ribnjaci ili specifične vrste, u morskim i kopnenim vodama, lov, šumarstvo i žetva morske trave.
Glavni instrumenti za očuvanje prirode su propisi o pticama i staništima. Ovi propisi vode do uspostavljanja Natura 2000 mreže.
Diverzitet različitih klasifikacionih sistema i nivoa detalja u mapiranju.

Taksonomske reference moraju poštovati taksonomsku referencu Globalne baze
podataka o biodiverzitetu - Global Biodiversity Information Facility GBIF. Različiti
propisi treba da se odnose na taj sistem, ali postojeće propisi upućuju na različite
taksonomske sisteme.

Razmjera: Indikacija zajedničkog razmjera kartiranja od 1:5 000 do 1:10 000 000.

Politika zajednice: 6EAP, propisi za staništa i ptice, CAP, Politika ribarstva itd.

Inicijativa: NATURA 2000, OSPAR konvencija, GBIF, Flora Europaea itd.
Primjeri podataka:

Podaci rasprostranjenosti ptičjih vrsta: rasprostranjenost vrsta pomoću mreže.
Sastavljeni su skupovi podataka o 440 različitih uzgojnih ptica u Evropi. Svaka uzgojna
vrsta klasifikovana je prema svom uzgojnom statusu u okviru 50 km mreže. Odbor
Evropskog ornitološkog atlasa. Kartiranje rasprostranjenosti uzgoja onih evropskih
vrsta, dobijeni terenskim radom.
Atributne
informacije:
prisutnost
i
odsutnost
svake
vrste,
mogući/vjerovatni/potvrđeni uzgoj, procjene o broju parova po kvadratu, period
popisa, identitet kvadrata, kompletnost promjera, visina,posmatrači i komentari.
Prekrivenost pokrivačom: Pan-Evropa

Podaci rasprostranjenosti biljnih vrsta: skup podataka koji sadrži informacije o
prisutnosti biljnih vrsta u mrežnim kvadratima širom Evrope.
Atributne informacije: vrste nađene u svakom 50 km-skom kvadratu, pojave u
izvornom obliku, upoznavanje, status nepoznat, vjerovatno izumrle, nesiguran
zapis.
Prekrivenost pokrivačem: Pan-Evropa. Trebalo je 25 godina da se mapira 20%
Evropskih vaskularnih biljaka. Postojali su planovi do 1999. kako ubrzati proces.

Raspodjela vodozemaca i gmizavaca: Raspodjela vrsta po kvadratima od 50 km.
Atributne informacije: kodirano latinsko ime, datum viđenja, lociranje redovne
prisutnosti, prisutnost vrsta
Prekrivenost pokrivačem: Pan-Evropa. Završeno za zapadnu Evropu, nije
završeno za istočnu Evropu.

Fauna Europaea: Baza podataka koja sadrži informacije o prisutnosti
životinjskih vrsta u određenim zemljama u Evropi. Podaci prikupljeni u većini
evropskih zemalja i objavljeni u obliku internetske stranice sa mogućnostima
mapiranja.
Prekrivenost pokrivačem: Pan-Europa.
Važni tipovi objekata i atributi:
Mreža ćelija ili površina:

Klasifikacioni sistem;

Porodica, stručni naziv, narodno ime;

Vrste, stručni naziv, narodno ime;

Provjera datuma prisutnosti u mrežnoj ćeliji/površini;

Razdoblje prisutnosti tokom cijele godine u mrežnoj ćeliji/površini (npr. početnim-
krajnjim datumom, unos mjeseci, sezona);

Funkcija: mjesto koje funkcioniše za vrste (npr. migracijski, uzgojni, lokalitet za odmor ili
parenje);

Status: ugrožena, izumrla, itd. (IUNC kategorija);

Referenca na izvor.
Tačka prosmatranja:

Klasifikacioni sistem;

Porodica, stručni naziv, narodni naziv;

Vrste, stručni naziv, narodni naziv;

Provjera datuma prisutnosti u mrežnoj ćeliji/površini;

Period;

Funkcija;

Status: ugrožena, izumrla, itd. (IUNC kategorija);

Referenca na izvor;

Metoda posmatranja.
Klasifikacija/Nomenklatura:

Evropski informacioni sistem u oblasti prirode -European Nature Information System
(EUNIS) http://eunis.eea.eu.int/;

Glabalna baza podataka o biodiverzitetu - Global Biodiversity Information Facility (GBIF)
- vrste, uopšteno;

Konvencija o međunarodnoj trgovini ugroženim vrstama divlje faune i flore -Convention
on International Trade in Endangered Species of Wild Fauna and Flora (CITES
konvencija)

Organizacija za hranu i poljoprivredu -Food and agriculture organization (FAO) sistem
za klasifikaciju ribljih resursa kao troslovni kod;

Mora se definisati kodni sistem za status. Kodni sistem za različite vrste (grupe)
razlikuju se od jedne do drugih. IUCN klasifikacioni sistem za status može se razmotriti.
Veze i preklapanja s ostalim oblastima:

Sistemi geografskih mreža;

Staništa i biotopi;

Biogeografska područja;

Zaštićena područja: vrste ponekad mogu biti registrovane u okviru određenih lokacija
kao što su zaštićena područja.
1.33 Izvori energije
Izvori energije uključujući ugljenvodonik, hidroenergiju, bioenergiju, solarnu, energiju vjetra itd., gdje je relevantno uključiti informacije o visini i dubini u opsegu izvora.
Pojavljuju se Pan-evropske, nacionalne ili lokalne inicijative o mapiranju, kao rezultat vladinih inicijativa ili privatnih interesa. Postoji glavna razlika između fosilnih goriva i obnovljivih izvora energije. Koncept izvora energije osigurava fokus prema aspektu izvora i širini/distribuciji izvora. Dakle tehničke konstrukcije za apstrakciju, transport i obradu nisu pokrivene ovom oblašću. Međutim, one su u velikoj mjeri pokrivene u ostalim oblastima, kao što su proizvodni i industrijski objekti. Upotreba energije, npr. potrošnja benzina nije pokrivena ovom oblašću. Područja licenci, dozvola ili planiranja povezana sa eksploatacijom izvora energije pokrivena su oblašću "Područja upravljanja/zaštićena područja/uređena područja i jedinice za izvještavanje".
Može biti problematično da se definiše pojam izvora i njegova kvantifikacija. Aspekte izvora ne bi trebalo ograničiti samo na izvore koji se iskorišćavaju već treba uključiti i neiskorišćene izvore.
Izvori fosilnih goriva uključuju:

Nalazišta nafte: polja ugljovodonika, naftne količine;

Nalazišta prirodnog gasa, uključujući čvrste metanske klatrate;

Depoziti uglja, lignita i tresetišta;

Rudna ležišta urana.
Za ove izvore priroda, lokacija i 3D geometrija depozita (geološki izvor), priroda nosača ekonomske energije i veličina rezervi, ključni su atributi u trenutku u vremenu.
Različite vrste izvora obnovljive energije mogu uključivati:

Hidroenergiju: vodeni izvori posebno mapirani prema energetskom potencijalu.
Uobičajno preduzete u MS-u, sprovedene od strane državnog organa ili privrednih
subjekata.

Bio-energetski izvori: šumski izvori, šumski otpad, žitarice ili poljoprivredni ostaci
mogu se koristiti u energetske svrhe, npr. u obliku drvnog ogrijeva ili bio dizela. Izvori ili
zalihe ponekad se procjenjuju mapiranjem.

Energija vjetra: Zalihe energije vjetra države rade se u područjima gdje se vjetar
iskorišćava ili se planira njegovo iskorišćavanje. Procijenjeno mjerenje vjetra zajedno sa
topografskim informacijama. Primjer: http://www.nve.no/vindatlas/.

Geotermalna energija: Zemljin prirodni tok toplote je od velikog interesa kao obnovljiv
i čist izvor energije. Mapiranje izvora dostupno je ili relevantno na lokalnom,
regionalnom ili nacionalnom nivou. Geotermalni energetski sistemi koriste prirodnu
toplotu zemlje po sistemu toplih podzemnih voda iz površinskih depozita za direktno
grijanje ili generisanje električne energije (otvoreni sistemi). Alternativno, plitki
geotermalni tokovi iskorišćeni su pomoću nadzemnih toplotnih pumpi (zatvoreni
sistemi). Zajednički izvori toplote u stijenama ili podzemlju mogu se iskoristiti -
cirkulacija antifriza u crijevima kolektora koji su spušteni u relativno plitke bušotine
stijene ili cirkulacija podzemne vode iz dubokih bušotina u stijenama. Toplotne pumpe
prikladne su za, na primjer ekstrakciju toplote iz vazduha, rijeka, mora i vještačkih
komponenti.

Solarna energija i izvori: U cilju smanjenja potrebe za dodatnim grijanjem, važno je
uzeti u obzir solarne uslove na lokalnom mjestu kod lokalnog planiranja. Potrebne su
nacionalne, regionalne i lokalne zalihe solarne energije u odnosu na potrebe grijanja.
Sistemi za skladištenje sunčeve toplote pronađeni su na nekim lokacijama. Solarni izvori
mogu se takođe koristiti u proizvodnji energije, upotrebom tehnologije solarnih ćelija
(silicijumske ćelije). Toplotne pumpe na bazi vazduha mogu koristiti solarnu energiju
pohranjenu u vazduhu.

Ostali izvori energije kao što su talasi, struje, itd.: Popis različitih vrsta izvora
obnovljive energije je dug.
Kvantifikacija izvora može se spojiti ili detaljno opisati. Detaljne informacije su u velikoj mjeri privatne poslovne informacije. Ovo na primjer uključuje podatke o unutrašnjoj strukturi geoloških struktura u okviru naftnih polja. U kontekstu Infrastrukture prostornih podataka, podaci o kojima je riječ uglavnom će biti agregirani ili pregledani podaci. Međutim, u svrhu javnog planiranja na lokalnom nivou detaljne informacije o nekom obnovljivom izvoru energije mogu biti relevantne.
Geografska zastupljenost izvora (objekata) može biti različita za različita mjerila. U mapiranju i iskorišćavanju izvora koriste se 2D (obične karte) i 3D geografski podaci. Izvori se mogu mapirati na svojim prirodnim granicama. Agregirane ili pregledane informacije mogu se referisati na mrežu ćelija u geografskom sistemu mreža, upravnim jedinicama/površinama, statističkim jedinicama/površinama ili tačkama.
Opseg, primjeri upotrebe:
Izvorni podaci digitalne energije mogu se koristiti u:

upravljanju izvorima i aktivnostima iskorišćavanja;

EU politici razvoja i regionalnoj politici;

strateškim poslovima i planiranju izvora;

korišćenju zemljišta i urbanom planiranju;

procjenama uticaja na životnu sredinu;

i kao ulazni podaci u procjeni stanja životne sredine, npr. modeliranje budućih zračenja,
pritiska i održivosti.
Važni objektni tipovi i atributi:
Neki izvori energije kao što su nafta i hidroenergija mogu se vrlo lako uočiti, dok se drugi izvori, kao što su solarni izvori ili vjetar baziran na tačkastom promjeru modeliraju/interpoliraju u "neprekidne" površine i 3D objekte.
Objekti izvora energije (2D ili 3D):

Tip izvora (nafta, gas, vjetar….);

Ime (mjesto/ime lokacije);

Id; i

Kvantifikacija:
-
Volumen; i
-
Datum kvantifikacije.
Područje vodenog sliva:

Id; i

Prosječno oticanje.
Administrativna/statistička jedinica:

Tip izvora (nafta, gas, vjetar…); i

Kvantifikacija:
-
Količina; i
-
Datum kvantifikacije.
Mrežna ćelija:

Tip izvora (nafta, gas…);

Ime;

Id; i

Kvantifikacija:
-
Volumen; i
-
Datum kvantifikacije.
Veze i preklapanja s ostalim oblastima:

Mreže;

Administrativne jedinice;

Geologija;

Prostorne jedinice za statistiku;

Hidrografija;

Tlo (npr. ugljen, treset);

Korištenje zemljišta;

Područja upravljanja/zaštićena područja/uređena područja i jedinice za izvještavanje;

Okeanografsko-geografske karakteristike; i

Izvori minerala.
1.34 Mineralne sirovine
Mineralne sirovine, uključujući metalne rude, industrijske minerale, itd., uključujući dubinske/visinske informacije o veličini izvora tamo gdje je to potrebno.
Oblast Mineralne sirovine odnosi se na opis prirodnih koncentracija vrlo različitih minerala potencijalnog ili dokazanog ekonomskog interesa. Važni atributi su priroda, geneza, lokacija, raspon/distribucija tih izvora. Ekonomski i tehnički podaci povezani sa lokacijom površina licenciranih za istraživanje ili rudarstvo pa sve do crpljenja depozita, transporta, obrade i odlaganja otpada nisu pokriveni ovom oblašću. Međutim, potrebno je skladištiti materijale blizu rudnika i kamenoloma. Od velike je važnosti znanje o tome kako će uticati na životnu sredinu, npr. curenje iz sulfida, itd. Oni su u velikoj mjeri pokriveni ostalim oblastima, kao što je proizvodnja i industrijske karakteristike. Energetski minerali kao što su ugljenik, uran, nafta i gas isključeni su iz ove oblasti, pošto su pokriveni oblašću "Izvori energije". Licence za istraživanje područja i područja dopuštenih za rudarstvo obuhvaćeni su oblašću "Područja upravljanja/ograničenja/zone propisa i područja izvještavanja".
Podaci mineralnih sirovina odnose se na:

Anomalije: lokacije gdje pozadinska koncentracija potencijalno vrijednih elemenata u
tlu, sedimentu potoka ili stijena na kopnu ili na moru prelaze normalne pozadinske
vrijednosti koje su očekivane, s obzirom na lokalni geološki kontekst. Takve karte na
široko se koriste u mineralnim istraživanjima. Atributi su lokacija, hemijski elementi,
priroda elemenata uzoraka, analitičke vrijednosti.

Pojava: tačke ili površine gdje se koncentracija datih minerala opaža, ali bez dokazanog
ekonomskog potencijala. Atributi su lokacija, priroda minerala, analitički podaci, priroda
stijene domaćina, geometrija/morfologija posmatrane pojave.

Depoziti: područja koja imaju mineralne koncentracije sa ekonomskim potencijalom.
Atributi se opisuju u nastavku.
Mineralne sirovine obuhvataju sve količine mineralnih resursa, otkrivenih i neotkrivenih, koji su sadržani u ili su proizvedeni od nakupina prirodnog porijekla na ili u zemljinoj kori.
Izvorna informacija je dostupna u skladu sa obavezom izvještavanja. Nacionalni zakoni takođe utiču na detalje javno dostupnih podataka. Detaljne podatke ili podatke povezane sa nekim depozitima rijetkih metala sa visoko tehnološkim aplikacijama, može biti teško zadržati uzimajući u obzir da su od ekonomskog/privatnog interesa i na taj način su problematični za distribuiranje.
Sektor mineralnih sirovina podijeljen je u određeni broj segmenata, a razlikuje se po tehnologiji uključenoj u istraživanje i rudarstvo, tržišta i prirodi iskorišćenih materijala:

Metalno rudarstvo (neenergetske metalne rude, uran se odnosi na energetski sektor);

Industrijski minerali;

Konstrukcijski minerali i stijene; npr. prirodni kamen (arhitektonsko građevinski
kamen), pijesak, šljunak i slomljeni agregati stijene;

Ukrasno kamenje; i

Drago i poludrago kamenje.
Ukrasno kamenje je kamenje koje se koristi u ukrasne svrhe van ili unutra konstrukcije (mramor, granit, labradorit, sijenit,…). Drago ili poludrago kamenje koristi se za nakit (preklapanje postoji sa nekim segmentom ukrasnog kamenja pošto se neki poludragi minerali koriste i za nakit i za dekoraciju).
Opseg, primjeri upotrebe:
Upotrebljivost i potencijal geografskih podataka o mineralnim izvorima zavise o mjerilu i deta- ljima dostupnih informacija. Digitalne geografske informacije o mineralnim izvorima koriste se:

Za upravljanje izvorima i eksploatacijske aktivnosti;

Za promociju investicija privatnog sektora;

U planiranju iskoristivosti zemljišta;

U procjenama utjicaja na životnu sredinu;

Kao osnova za izradu lokalnih, regionalnih, nacionalnih i EU politika; i

Kao ulazni podaci u procjeni stanja životne sredine, npr. modeliranje pritiska i održivosti.
Pan-evropsko, nacionalno ili lokalno prikupljanje podataka i inicijative za mapiranje su inicijative koje sprovode organizacije za geološka mjerenja. Rudarske kompanije, uglavnom u vlasništvu privatnog sektora, proizvode uglavnom povjerljive karte visoke rezolucije vrlo ograničenog potencijala ili rudarskih područja.
Važni objektni tipovi i atributi:
Zavisno o segmentu samo su neki od ovih atributa relevantni:

Lokalizacija rude/mineralnog depozita;

Ime depozita;

Priroda
glavnog
sastojka
depozita,
definisana
njegovom
ekonomskom
vrijednosti/potencijalom;

Priroda
sekundarnog
sastojka
depozita,
definisanja
njegovom
ekonomskom/potencijalnom vrijednošću;

Geološka svojstva, mehaničko ponašanje, aspekti kvaliteta;

Tonaža i stepen izvora u zemlji + rezerve u zemlji + dio rezervi koji je već iscrpljen
(rezerve su onaj dio izvora koji je tehnički moguće iscrpiti uz trenutne ekonomske
uslove);

Tonaža glavnog sastojka depozita uključenog u izvor i rezerve;

Prosječna ocjena glavnog sastojka depozita;

Tip rude i ishodište mineralizacije (hidrotermalna, magmatska, sedimentarna,
(aluvijalna, morska, ledena…);

Granulometrija (u slučaju pijeska i šljunka);

Štetni sastojci, zračenja;

Korišćenje pojave;

Godište mineralizacije: najstarija i najmlađa dokumentovana godina;

Godište stijene domaćina: najstarija i najmlađa dokumentovana godina;

Geometrija depozita, uključujući dubinu i proširenje mineralizacije u datim odsječenim
ocjenama;

Priroda povezanih promjena na stijeni domaćinu (ako postoji); i

Status depozita.
Generalizovane ili agregirane informacije o izvorima minerala mogu se naći kao geografski podaci sa mrežom ćelija ili u rezoluciji administrativnih područja.
Veze i preklapanja s ostalim oblastima:

Geologija, izvori minerala;

Korišćenje zemljišta;

Tlo;

Proizvodna i industrijska postrojenja;

Područja upravljanja/zaštićena područja/uređena područja i jedinice za izvještavanje;

Okeanografsko-geografske karakteristike; i

Izvori energije.
