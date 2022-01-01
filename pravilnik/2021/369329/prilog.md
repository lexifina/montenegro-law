PRILOG 1
TEHNIČKI ZAHTJEVI EKO DIZAJNA ZA SERVERE I MREŽNE UREĐAJE ZA SKLADIŠTENJE PODATAKA
Definicije koje se koriste imaju sljedeća značenja:
1)
server sa najviše dvije procesorske utičnice je server koji ima najviše dva interfejsa za ugradnju procesora. Za servere sa više čvorova
ovaj se izraz odnosi na server čiji svaki čvor ima najviše dvije procesorske utičnice;
2)
ulazno-izlazni uređaj (I/O uređaj) je uređaj koji omogućava ulaz i izlaz podataka između servera ili proizvoda za skladištenje
podataka i drugih uređaja. I/O jedinica može biti sastavni dio matične ploče servera ili može biti spojena na matičnu ploču preko slota
za proširivanje (npr. PCI ili PCIe);
3)
matična ploča je glavna štampana ploča servera i obuhvata priključke za spajanje dodatnih ploča i, obično, sljedeće komponente:
procesor, memoriju, BIOS i slotove za proširivanje;
4)
procesor je logičko kolo koje odgovara na i obrađuje osnovne naredbe koje pokreću server i predstavlja centralnu procesorsku jedinicu
(CPU) servera koja se ugrađuje na matičnu ploču servera priključenjem u odgovarajuću utičnicu ili direktnim lemljenjem. CPU može
uključivati jedno ili više procesorskih jezgara;
5)
memorija je dio servera izvan procesora u kojem se čuvaju informacije za neposrednu upotrebu od strane procesora, a čiji se kapacitet
izražava u gigabajtima (GB);
6)
kartica za proširenje predstavlja unutrašnju komponentu spojenu linijskim priključkom na zajednički/standardni interfejs, kao što je
PCIe i omogućava dodatnu funkcionalnost;
7)
grafička kartica je kartica za proširenje koja ima najmanje jednu grafičku procesorsku jedinicu sa lokalnim interfejsom kontrole
memorije i lokalnom namjenskom grafičkom memorijom;
8)
DDR kanal sa baferom predstavlja kanal ili memorijski port koji spaja memorijski kontroler sa definisanim brojem memorijskih
uređaja u serveru. Tipičan server može imati više memorijskih kontrolera, a oni mogu podržavati jedan ili više DDR kanala sa baferom.
Svaki pojedinačni DDR kanal sa baferom podataka opslužuje samo dio ukupnog memorijskog prostora servera koji se može adresirati. 9)
blejd server (blade server) je server projektovan za korišćenje u blejd šasiji. Blejd server je uređaj koji funkcioniše kao samostalan
server i ima bar jedan procesor i sistemsku memoriju, ali je u radu zavisan od zajedničkih resursa koje pruža blejd šasija (npr. jedinica
za napajanje, hlađenje). Ako u tehničkoj dokumentaciji proizvoda nije navedeno da služi za povećavanje mogućnosti samostalnog
servera, procesor ili memorijski modul se ne smatraju se blejd serverom;
10) blejd šasija je kućište sa zajedničkim resursima za rad servera, sistema za skladištenje i drugih uređaja u blejd formatu. Zajednički
resursi koje pruža blejd šasija mogu obuhvatati jedinice za napajanje, skladištenje podataka i hardver za distribuciju napajanja
jednosmjernom strujom, regulaciju temperature, upravljanje sistemom i mrežne usluge;
11) server visokih performans (HPC server) je server koji je projektovan i optimizovan za izvođenje visoko paralelnih aplikacija, visoko
zahtjevnih računarskih operacija ili aplikacija vještačke inteligencije za duboko učenje. HPC serveri moraju ispunjavati sljedeće
kriterijume:
a)
sastoje se od višestrukih računarskih čvorova, grupisanih radi povećanja računarskih performansi;
b)
sadrže međuprocesorkse veze velike brzine među čvorovima;
12) porodica servera je specifikacija koja definiše skup servera koji dijele istu kombinaciju šasije i matične ploče, a koja može imati više
hardverskih i softverskih konfiguracija. Sve konfiguracije unutar porodice servera moraju imati sljedeće zajedničke karakteristike:
a)
pripadaju istom modelu ili istoj vrsti mašine;
b)
imaju isti format (tj. samostojeći, ormarski ili blejd) ili dijele isti mehanički i električni dizajn sa manjim razlikama koje
omogućuju ugradnju različitih formata;
c)
imaju procesore iz jedne određene serije procesora ili imaju procesore koji se ugrađuju u isti tip utičnica;
d)
imaju zajedničke jedinice za napajanje;
e)
imaju isti broj dostupnih procesorskih utičnica i isti broj popunjenih dostupnih procesorskih utičnica;
13) jedinica za napajanje (PSU) je uređaj koji pretvara naizmjeničnu ili jednosmjernu ulaznu energiju (struju) u jednosmjernu izlaznu
energiju za potrebe napajanja servera ili proizvoda za skladištenje podataka. Jedinica za napajanje servera ili proizvoda za skladištenje
podataka mora biti samostalna i fizički odvojiva od matične ploče, a sa sistemom se spaja odvojivom ili čvrstom električnom vezom;
14) faktor snage je odnos između stvarno potrošene snage u Vatima i prividne, preuzete snage u Voltamperima;
15) jednoizlazna jedinica za napajanje je jedinica za napajanje projektovana tako da većinu nazivne izlazne snage predaje na jedan
primarni jednosmjerni izlaz radi napajanja servera ili proizvoda za skladištenje podataka. Jednoizlazne jedinice za napajanje mogu imati
izlaze u stanju pripravnosti koji su aktivni uvijek kad su spojeni na izvor ulazne snage. Ukupna nazivna izlazna snaga svih dodatnih
izlaza jedinice za napajanje koji nijesu primarni izlazi ili izlazi u stanju pripravnosti ne smije biti veća od 20 W. Jedinice za napajanje sa
višestrukim izlazima na istom naponskom nivou kao primarni izlaz smatraju se jednoizlaznim jedinicama za napajanje osim ako:
a)
druge izlaze generišu zasebni pretvarači ili ako imaju zasebne faze ispravljanja izlaza; ili
b)
drugi izlazi imaju nezavisna ograničenja jačine struje;
16) višeizlazna jedinica za napajanje je jedinica za napajanje projektovana tako da većinu nazivne izlazne snage predaje na više od jednog
primarnog jednosmjernog izlaza radi napajanja servera ili proizvoda za skladištenje podataka. Višeizlazne jedinice za napajanje mogu
imati jedan ili više izlaza u stanju pripravnosti koji ostaju aktivni kad su spojeni na izvor ulazne struje. Ukupna nazivna izlazna snaga
svih dodatnih izlaza jedinice za napajanje koji nijesu primarni izlazi ili izlazi u stanju pripravnosti mora biti manja od 20 W;
17) server sa jednosmjernim napajanjem je server koji je isključivo projektovan za rad sa izvorom jednosmjerne struje;
18) proizvod za skladištenje podataka sa jednosmjernim napajanjem je proizvod za skladištenje podataka koji je isključivo projektovan
za rad sa izvorom jednosmjerne struje;
19) stanje pripravnosti je radno stanje u kojem su operativni sistem i drugi softver učitani, a server je sposoban izvršavati radne
transakcije, ali sistem nije zatražio ni uvrstio na listu čekanja nijednu radnu transakciju (tj. server je operativan, ali ne obavlja nikakav
koristan rad).
20) snaga u stanju pripravnosti (Pidle) je snaga, izražena u vatima, potrebna u stanju pripravnosti;
21) konfiguracija niskih performansi porodice servera predstavlja kombinaciju dva uređaja za skladištenje podataka, procesora sa
najnižim rezultatom množenja broja jezgara i frekvencije (u GHz) i kapaciteta memorije (u GB) koji je najmanje jednak rezultatu
množenja broja memorijskih kanala i dvostrukog linijskog memorijskog modula (DIMM) najmanjeg kapaciteta (u GB) ponuđenog za
server, a koja odgovara modelu proizvoda sa najnižim performansama unutar te porodice servera. Svi memorijski kanali moraju biti
popunjeni dvostrukim linijskim memorijskim modulima istog tipa i kapaciteta;
22) konfiguracija visokih performansi porodice servera predstavlja kombinaciju dva uređaja za skladištenje podataka, procesora sa
najvećim rezultatom množenja broja jezgara i frekvencije (u GHz) i kapaciteta memorije (u GB) koji nije manji od trostrukog rezultata
množenja broja CPU, broja jezgara i broja hardverskih niti, a koja odgovara modelu proizvoda sa najvišim performansama unutar te
porodice proizvoda. Svi memorijski kanali moraju biti popunjeni dvostrukim linijskim memorijskim modulima (DIMM) istog tipa i
kapaciteta;
23) hardverska nit predstavlja hardverski resurs u CPU za realizaciju serije (niza) softverskih naredbi (CPU jezgro može imati resurse za
istovremenu realizaciju više od jedne niti);
24) efikasnost u aktivnom stanju (Effserver) je numerička vrijednost efikasnosti servera izmjerena i izračunata u skladu sa Prilogom 2; 25) aktivno stanje je radno stanje u kojem server pruža odgovor na prethodne ili aktuelne spoljašnje zahtjeve (npr. naredbe primljene
putem mreže). Aktivno stanje obuhvata i aktivnu obradu i pretragu podataka iz memorije, iz keš memorije ili sa internog/eksternog
uređaja za skladištenje podataka, tokom čekanja daljih naredbi putem mreže;
26) performanse servera predstavljaju broj transakcija koje server izvrši u jedinici vremena tokom standardizovanog ispitivanja diskretnih
komponenti sistema (npr. procesora, memorije, sistema za skladištenje) i podsistema (npr. RAM, CPU);
27) maksimalna snaga (Pmax) je najveća snaga u Vatima zabilježena u jedanaest radnih procesa u skladu sa standardom;
28) performanse centralne procesorske jedinice (PerfCPU) predstavljaju broj transakcija koje server izvrši u jedinici vremena tokom
standardizovanog ispitivanja podsistema CPU;
29) pomoćni procesni akcelerator -APA (Auxiliary Processing Accelerator) predstavlja specijalizovani procesor i prateći podsistem koji
povećavaju računarski kapacitet, kao što su uređaji za grafičku obradu ili programabilni logički sklopovi (Field Programmable Gate
Arrays). APA ne može funkcionisati u serveru bez CPU. APA može biti ugrađen u server kao dodatna grafička kartica ili kartica za
proširenje, instalirana u opštenamjenski slot za proširenje ili integrisana u komponentu servera, kao što je matična ploča;
30) prošireni APA je APA na dodatnoj kartici ugrađenoj u slot za proširenje. Kartica proširenog APA može sadržati jedan APA ili više
njih i/ili zasebne, namjenskih odvojive prekidače;
31) integrisani APA je APA koji je integrisan na matičnu ploču ili u paket CPU-a;
32) vrsta proizvoda predstavlja dizajn servera ili proizvoda za skladištenje podataka, uključujući šasiju (ormar, stub ili blejd), broj utičnica
i, ako je riječ o serveru, informaciju da li se radi o serveru sa povećanom otpornošću, blejd serveru, serveru sa više čvorova, HPC
serveru, serveru sa integrisanim APA, serveru sa jednosmjernim napajanjem ili serveru koji ne pripada ni jednoj od navedenih
kategorija;
33) rasklapanje predstavlja postupak kojim se predmet (proizvod) rastavlja tako da se poslije može ponovo sklopiti i pustiti u rad;
34) integrisani softver (firmware) je softver sistema, hardvera, komponente ili perifernog uređaja koji dolazi sa proizvodom i daje
osnovne naredbe kako bi hardver funkcionisao, a uključuje i sva primjenjiva programska i hardverska ažuriranja;
35) sigurno brisanje podataka znači stvarno brisanje svih tragova postojećih podataka sa uređaja za skladištenje podataka, pri čemu se
preko njih zapisuju novi podaci tako da pristup izvornim podacima, ili njihovim dijelovima, postaje nemoguć.
1.
Zahtjevi eko dizajna za servere i mrežne uređaje za skladištenje podataka 1.1
Zahtjevi u pogledu efikasnosti jedinice za napajanje i faktora snage 1.1.1
U Fazi 1 za servere i mrežne uređaje za skladištenje podataka, osim servera sa jednosmjernim napajanjem i uređaja za skladištenje
podataka sa jednosmjernim napajanjem, efikasnost jedinice za napajanje na 10 %, 20 %, 50 % i 100 % nazivnog opterećenja i
faktor snage na 50 % nazivnog opterećenja ne smiju biti niži od vrijednosti datih u Tabeli 1.
Tabela 1: Minimalni zahtjevi u pogledu efikasnosti jedinice za napajanje i faktora snage
Faza 1
Minimalna efikasnost jedinice za napajanje
Minimalni faktor
snage % nazivnog opterećenja
10 %
20 %
50 %
100 %
50 % Višeizlazna jedinica
-
88 %
92 %
88 %
0,90 Jednoizlazna jedinica
-
90 %
94 %
91 %
0,95
1.1.2
U Fazi 2 za servere i mrežne uređaje za skladištenje podataka, osim servera sa jednosmjernim napajanjem i uređaja za skladištenje
podataka sa jednosmjernim napajanjem, efikasnost jedinice za napajanje na 10 %, 20 %, 50 % i 100 % nazivnog opterećenja i
faktor snage na 50 % nazivnog opterećenja ne smiju biti niži od vrijednosti datih u Tabeli 2.
Tabela 2: Minimalni zahtjevi u pogledu efikasnosti jedinice za napajanje i faktora snage
Faza 2
Minimalna efikasnost jedinice za napajanje
Minimalni faktor
snage % nazivnog opterećenja
10 %
20 %
50 %
100 %
50 % Višeizlazna jedinica
-
90 %
94 %
91 %
0,95 Jednoizlazna jedinica
90 %
94 %
96 %
91 %
0,95
1.2
Zahtjevi u pogledu efikasnosti upotrebe materijala 1.2.1
U Fazi 1 proizvođač obezbjeđuje da tehnike spajanja, pričvršćivanja ili zaptivanja ne onemogućuju da se sljedeće komponente,
ukoliko su prisutne, rasklope za potrebe popravke ili ponovne upotrebe:
1.
jedinice za skladištenje podataka;
2.
memorija;
3.
procesor (CPU);
4.
matična ploča;
5.
kartica za proširenje/grafička kartica;
6.
jedinica za napajanje;
7.
šasija;
8.
baterija.
1.2.2
U fazi 1 funkcionalnost za sigurno brisanje podataka mora biti dostupna za brisanje podataka na svim jedinicama za skladištenje
podataka koje proizvod ima.
1.2.3
U Fazi 1 najnovija dostupna verzije integrisanog softvera (firmware) mora biti dostupna od dvije godine nakon stavljanja na tržište
prvog proizvoda određenog modela proizvoda do najmanje osam godina od stavljanja na tržište posljednjeg proizvoda tog modela
proizvoda i to besplatno ili po troškovima koji su utvrđeni na transparentan način i nijesu diskriminatorni.
Takođe, najnovije dostupno sigurnosno ažuriranje integrisanog softvera (firmware) mora biti dostupno od trenutka stavljanja na
tržište modela proizvoda do najmanje osam godina od stavljanja na tržište posljednjeg proizvoda tog modela proizvoda i to
besplatno.
2.
Zahtjevi eko dizajna za servere sa najviše dvije procesorske utičnice 2.1. Snaga u stanju pripravnosti U Fazi 1 snaga servera stanju pripravnosti (Pidle), osim servera sa povećanom otpornošću, HPC servera i servera sa integrisanim APA, ne smije biti veća od vrijednosti izračunate na osnovu sljedeće formule:
pri čemu je:
-
Pbase osnovna dopuštena snaga u stanju pripravnosti data u Tabeli 3, a
-
ΣPadd_i zbir dopuštenih snaga u stanju pripravnosti za moguće dodatne komponente kako je određeno u Tabeli 4.
Za blejd servere Pidle se dobija dijeljenjem ukupne izmjerene snage sa brojem blejd servera ugrađenih u blejd šasiju koji se ispituje.
Za servere sa više čvorova broj utičnica računa se po čvoru, a Pidle se izračunava dijeljenjem ukupne izmjerene snage sa brojem čvorova ugrađenih u kućište koje se ispituje.
Tabela 3: Osnovna dopuštena snaga u stanju pripravnosti
Vrsta proizvoda
Osnovna dopuštena snaga u
stanju pripravnosti, Pbase (W) serveri sa 1 procesorskom utičnicom (osim blejd servera i servera sa više čvorova)
25 serveri sa 2 procesorske utičnice (osim blejd servera i servera sa više čvorova)
38 Blejd serveri ili serveri sa više čvorova
40
Tabela 4: Dodatna dopuštena snaga u stanju pripravnosti za dodatne komponente
Karakteristike sistema
Primjenjuje se na
Dodatna dopuštena snaga
u stanju pripravnosti Performanse CPU-a
sve servere
1 utičnica: 10 × PerfCPU W
2 utičnice: 7 × PerfCPU W Dodatna jedinica za napajanje
jedinice za napajanje ugrađene izričito
radi redundantnosti napajanja
10 W po jedinici za napajanje
HDD ili SSD
ugrađene HDD-ove ili SSD-ove
5,0 W po HDD-u ili SSD-u Dodatna memorija
ugrađenu memoriju preko 4 GB
0,18 W po GB Dodatni DDR kanal sa baferom
ugrađene DDR kanale sa baferom
većim od 8 kanala
4,0 W po DDR kanalu sa baferom
Dodatne I/O jedinice
ugrađene uređaje sa više od dva
Ethernet priključka ≥ 1 Gbit
< 1 Gb/s: nije dopuštena dodatna snaga
= 1 Gb/s: 2,0 W po aktivnom priključku
> 1 Gb/s i < 10 Gb/s: 4,0 W po aktivnom
priključku
> 10 Gb/s i < 25 Gb/s: 15,0 W po aktivnom
priključku
> 25 Gb/s i < 50 Gb/s: 20,0 W po aktivnom
priključku
≥ 50 Gb/s 26,0 W po aktivnom priključku
2.2. Efikasnost u aktivnom stanju U Fazi 1 efikasnost servera u stanju pripravnosti (Effserver), osim servera sa povećanom otpornošću, HPC servera i servera sa integrisanim APA, ne smije biti manja od vrijednosti iz Tabele 5.
Tabela 5: Zahtjevi za efikasnost u aktivnom stanju
Vrsta proizvoda
Najmanja efikasnost u aktivnom stanju Serveri sa 1 procesorskom utičnicom
9,0 Serveri sa 2 procesorske utičnice
9,5 Blejd serveri ili serveri sa više čvorova
8,0
3. Zahtjevi za informacijama koje obezbjeđuju proizvođači 3.1.
U Fazi 1, osim za servere izrađene po narudžbi, sljedeće informacije o serverima moraju se objaviti u uputstvima za tehničare i krajnje
korisnike (u slučaju da se uputstva dostavljaju uz proizvod), kao i na internet stranicama proizvođača/dobavljača sa slobodnim
pristupom, od trenutka stavljanja na tržište modela proizvoda do najmanje osam godina nakon stavljanja na tržište posljednjeg
proizvoda tog modela proizvoda:
a)
vrsta proizvoda;
b)
ime proizvođača, registrovani trgovački naziv i registrovana trgovačka kontakt adresa;
c)
broj modela proizvoda i, ako je primjenjivo, brojevi modela konfiguracije niskih performansi i konfiguracije visokih
performansi;
d)
godina proizvodnje;
e)
efikasnost jedinice za napajanje na 10% (ako je primjenjivo), 20%, 50% i 100% nazivne izlazne snage, osim za servere sa
jednosmjernim napajanjem, izražena u % i zaokružena na prvu decimalu;
f)
faktor snage na 50 % nazivnog opterećenja, osim za servere sa jednosmjernim napajanjem, zaokružen na treću decimalu;
g)
nazivna izlazna snaga jedinice za napajanje (u vatima), zaokružena na najbliži cijeli broj. Ako je model proizvoda dio porodice
servera, za sve jedinice za napajanje koje se nude za tu porodicu servera moraju se navesti informacije iz podtč. e) i f) ove tačke;
h)
snaga u stanju pripravnosti, izražena u Vatima i zaokružena na prvu decimalu;
i)
popis svih komponenti za koje je dopuštena dodatna snaga u stanju pripravnosti, ako ih ima (dodatne jedinice za napajanje,
dodatni HDD-ovi ili SSD-ovi, dodatna memorija, dodatni DDR kanali sa baferom, dodatne I/O jedinice);
j)
maksimalna snaga, izražena u Vatima i zaokružena na prvu decimalu;
k)
deklarisana klasa radnih uslova, u skladu sa Tabelom 6;
l)
snaga u stanju pripravnosti (u Vatima) na gornjoj graničnoj temperaturi deklarisane klase radnih uslova;
m) efikasnost i performanse servera u aktivnom stanju;
n)
informacije o funkcionalnosti sigurnog brisanja podataka iz tačke 1.2.2. ovog priloga, uključujući uputstvo o tome kako se
koristi, koje tehnike su primijenjene i koji standardi sigurnog brisanja podataka su podržani;
o)
za blejd servere popis preporučenih kombinacija sa kompatibilnim šasijama;
p)
ako je model proizvoda dio porodice servera, popis svih konfiguracija tog modela koje taj model predstavlja.
Ako je model proizvoda dio porodice servera, informacije o proizvodu koje se zahtijevaju u tački 3.1. potč. e) do m) daju se za
konfiguraciju niskih performansi i konfiguraciju visokih performansi porodice servera.
3.2.
U Fazi 1, osim za uređaje za skladištenje podataka izrađene po narudžbi, sljedeće informacije o mrežnim uređajima za skladištenje
podataka moraju se objaviti u uputstvima za tehničare i krajnje korisnike (u slučaju da se uputstva dostavljaju uz proizvod), kao i na
internet stranicama proizvođača/dobavljača sa slobodnim pristupom, od trenutka stavljanja na tržište modela proizvoda do najmanje
osam godina nakon stavljanja na tržište posljednjeg proizvoda tog modela proizvoda:
a)
vrsta proizvoda;
b)
ime proizvođača, registrovani trgovački naziv i registrovana trgovačka kontakt adresa;
c)
broj modela proizvoda;
d)
godina proizvodnje;
e)
efikasnost jedinice za napajanje na 10% (ako je primjenjivo), 20%, 50% i 100% nazivne izlazne snage, osim za uređaje za
skladištenje podataka sa jednosmjernim napajanjem, izražena u % i zaokružena na prvu decimalu;
f)
faktor snage na 50 % nazivnog opterećenja, osim za uređaje za skladištenje podataka sa jednosmjernim napajanjem, zaokružen
na treću decimalu;
g)
deklarisana klasa radnih uslova, u skladu sa Tabelom 6 uz sljedeći navod: "Ovaj proizvod je ispitan kako bi se potvrdilo da će
raditi unutar graničnih vrijednosti (na primjer graničnih vrijednosti temperature i vlažnosti) deklarisane klase radnih uslova.";
h)
informacije o alatima za brisanje podataka iz tačke 1.2.2. ovog priloga, uključujući uputstva o tome kako se upotrebljavaju,
uključujući uputstvo o tome kako se koristi, koje tehnike su primijenjene i koji standardi sigurnog brisanja podataka su podržani; 3.3.
U Fazi 1, od trenutka stavljanja na tržište modela proizvoda do najmanje osam godina nakon stavljanja na tržište posljednjeg
proizvoda tog modela proizvoda, proizvođači/dobavljači besplatno stavljaju na raspolaganje sljedeće informacije o serverima i
mrežnim uređajima za skladištenje podataka trećim stranama koje se bave održavanjem, popravkom, ponovnom upotrebom,
recikliranjem i nadogradnjom servera (uključujući posrednike, servisere rezervnih dijelova, dobavljače rezervnih dijelova, izvođače
recikliranja i treće strane koje izvode održavanje), a koje su se registrova na za to namijenjenoj internet stranici:
a)
okvirna masa izražena u rasponu (manje od 5 g, od 5 g do 25 g, više od 25 g) sljedećih ključnih sirovina na bazi sadržaja u
komponentama:
i.
kobalta u baterijama;
ii.
neodimijuma u HDD-ovima;
b)
uputstvo za rasklapanja proizvoda iz tačke 1.2.1 ovog priloga, uključujući za svaku potrebnu operaciju i komponentu:
i.
vrstu operacije;
ii.
vrstu i broj tehnike pričvršćivanja sa ciljem rastavljanja;
iii.
potrebne alate.
U slučaju da je model proizvoda dio porodice servera, informacije o proizvodu koje se zahtijevaju u tački 3.3. podtč. a) i b) daju se ili
za model proizvoda ili, alternativno, za konfiguracije niskih performansi i konfiguracije visokih performansi iz porodice servera.
3.4.
U Fazi 1, za potrebe ocjenjivanja usaglašenosti u skladu sa članom 5 ovog pravilnika, u tehničkoj dokumentaciji navode se sljedeće
informacije o serverima i mrežnim uređajima za skladištenje podataka:
a)
informacije navedene u tč 3.1. i 3.3 za servere;
b)
informacije navedene u tč. 3.2. i 3.3 za uređaje za skladištenje podataka.
Tabela 6: Klase radnih uslova
Temperatura suvog termometra
°C
Raspon rel. vlažnosti, nekondenzirajuće
Klasa radnih uslova
Dopušteni
raspon
Preporučeni
raspon
Dopušteni raspon
Preporučeni
raspon
Max.
tačka
rose (°C)
Najveća
stopa
promjene
(°C/h) A1
15 - 32
18 - 27
od tačke rose (R) od -12
°C
(R)
i
relativne
vlažnosti (RV) od 8%
do
17 °C R i 80% RV
od -9 °C R do
15 °C R i 60 % RV
17
5/20
A2
10 - 35
18 - 27
od -12 °C R i 8 % RV
do
21 °C R i 80 % RV
isto kao u A1
21
5/20 A3
5 - 40
18 - 27
od -12 °C R i 8 % RV
do
24 °C R i 85 % RV
isto kao u A1
5/20
A4
5 - 45
18 - 27
od -12 °C R i 8 % RV
do
24 °C R i 90 % RV
isto kao u A1
24
5/20
PRILOG 2
MJERENJA I PRORAČUNI
1.
U svrhu ocjenjivanja usaglašenosti i provjere usaglašenosti sa propisanim zahtjevima iz ovog pravilnika, sprovode se mjerenja i
proračuni primjenom harmonizovanih standarda ili primjenom pouzdanih, tačnih i ponovljivih mjernih postupaka koje uzimaju u obzir
opšte priznate najnovije mjerne metode i kojima se postižu rezultati koji imaju visok nivo pouzdanosti.
2.
Serveri se ispituju ili u konfiguraciji pojedinačnog modela proizvoda ili, kad je riječ o serverima koji su dio porodice servera, u
konfiguraciji niskih performansi i konfiguraciji visokih performansi deklarisanoj za potrebe tačke 3.1. podtačke p) Priloga 1, koja
obuhvata hardversku konfiguraciju i postavke sistema, osim ako nije drugačije određeno.
Prilikom ispitivanja svake konfiguracije koje se nude unutar porodice servera moraju sadržati jednak broj popunjenih procesorskih
utičnica. Porodica servera može se definisati za server sa djelimično popunjenim procesorskim utičnicama (na primjer server sa dvije
procesorske utičnice kojem je samo jedna procesorska utičnica popunjena) sve dok se konfiguracije ispituju kao zasebna porodica
servera i ispunjavaju iste zahtjeve za broj popunjenih procesorskih utičnica u toj zasebnoj porodici servera.
U slučaju servera sa proširenim APA, za potrebe mjerenja snage u stanju pripravnosti, efikasnosti u aktivnom stanju i performansi
servera u aktivnom stanju, jedinica se ispituje bez proširenog APA. Ako prošireni APA posjeduje zasebne PCIe prekidače za
komunikaciju APA i CPU, za potrebe ispitivanja svih konfiguracija u aktivnom stanju i stanju pripravnosti uklanjaju se sve zasebne
PCIe kartice ili adapteri.
U slučaju servera sa više čvorova, jedinici koja se ispituje, potrošnja energije se mjeri po čvoru u potpuno napunjenoj konfiguraciji
šasije. Svi serveri sa više čvorova u šasiji sa više čvorova moraju imati istu konfiguraciju (moraju biti homogeni).
U slučaju blejd servera, jedinici koja se ispituje, potrošnja energije se mjeri u napola popunjenoj konfiguraciji šasije, a kako slijedi:
1)
konfiguracija pojedinačnih blejd servera,
a)
svi pojedinačni blejd serveri ugrađeni u šasiju moraju biti identični i imati istu konfiguraciju;
2)
napola popunjena šasija,
a)
izračunava se koliko je blejd servera potrebno da se popuni pola odjeljaka za blejd servera jednostruke širine u blejd šasiji;
b)
u slučaju blejd servera sa više područja napajanja, bira se broj područja napajanja koji je najbliži popunjavanju polovine blejd
šasije. Ako postoje dvije mogućnosti koje su jednako blizu polovini popunjenosti polovine šasije, ispitivanje se sprovodi sa
područjem ili kombinacijom područja koja koristi veći broj blejd servera;
c)
treba bi se pridržavati svih preporuka iz korisničkog uputstva ili preporuka proizvođača za djelimično popunjavanje šasije,
među kojima može biti prekid veze sa određenim napajanjima i ventilatorima za nepopunjena područja napajanja;
d)
ako preporuke iz korisničkog uputstva nijesu dostupne ili ako su nepotpune, primjenjuju se sljedeće smjernice:
i.
potpuno popuniti područja napajanja;
ii.
ako je moguće, prekinuti veze sa napajanjima i ventilatorima za nepopunjena područja napajanja;
iii.
sve prazne odjeljke zatvorite "praznim" pločama ili sličnim preprekama u cilju sprječavanja protoka vazduha tokom
ispitivanja.
3.
Podaci za proračun efikasnosti u aktivnom stanju (Effserver) i potrošnje u stanju pripravnosti (Pidle) mjere se tokom istog ispitivanja u
skladu sa relevantnim standardima, pri čemu se snaga u stanju pripravnosti mjeri ili prije ili nakon sprovođenja dijela ispitivanja u
kojem se mjeri efikasnost u aktivnom stanju.
Efikasnost u aktivnom stanju (Effserver) serverima izračunava se na sljedeći način:
pri čemu su WCPU , WMemory i WStorage ponderi koji se primjenjuju na radne procese za procesor, memoriju odnosno skladištenje kako
slijedi:
-
WCPU je ponder za radne procese za CPU i iznosi 0,65;
-
WMemory je ponder za radne procese za memoriju i iznosi 0,30;
-
WStorage je ponder za radne procese za skladištenje i iznosi 0,05;
a pojedinačne efikasnosti se računaju kao:
pri čemu je:
-
i = 1 za radni proces Compress;
-
i = 2 za radni proces LU;
-
i = 3 za radni proces SOR;
-
i = 4 za radni proces Crypto;
-
i = 5 za radni proces Sort;
-
i = 6 za radni proces SHA256;
-
i = 7 za radni proces Hybrid SSJ;
pri čemu je:
-
i = 1 za radni proces Flood3;
-
i = 2 za radni proces Capacity3;
pri čemu je:
-
i = 1 za radni proces Sequential;
-
i = 2 za radni proces Random;
-
i
pri čemu je:
-
Perfi geometrijska sredina mjerenja performansi u normalizovanom intervalu,
-
Pwri geometrijska sredina izmjerenih vrijednosti snage u intervalu.
Da bi se za server dobilo jedinstven pokazatelj energetske efikasnosti, vrijednosti efikasnosti u intervalu za sve različite radne procese
objedinjuju se sljedećim postupkom:
a)
objedinjavanjem vrijednosti efikasnosti u intervalu za pojedinačne radne procese koristeći geometrijsku sredinu kako bi se dobile
vrijednosti efikasnosti radnog procesa za pojedinačni radni proces;
b)
objedinjavanjem rezultata efikasnosti radnog procesa koristeći funkciju geometrijske sredine po vrsti radnog opterećenja (CPU,
memorija, skladištenje) kako bi se dobila vrijednost po vrsti radnog opterećenja;
c)
kombinovanjem tri vrste radnog opterećenja služeći se ponderisanom geometrijskom sredinom kako bi se dobila jedinstvena
vrijednost za ukupnu efikasnost servera.
PRILOG 3
POSTUPAK PROVJERE USAGLAŠENOSTI SA TEHNIČKIM ZAHTJEVIMA EKO DIZAJNA
Dopuštena odstupanja pri provjeri utvrđena u ovom prilogu odnose se samo na provjeru izmjerenih parametara i proizvođač/dobavljač ih ne smije upotrebljavati kao dopušteno odstupanje za određivanje vrijednosti u tehničkoj dokumentaciji ili za tumačenje tih vrijednosti u svrhu postizanja usaglašenosti odnosno za izvještavanje o većoj efikasnosti na bilo koji način.
Ako je proizvod projektovan tako da može detektovati kad je podvrgnut ispitivanju (npr. prepoznavanjem ispitnih uslova ili ciklusa) i automatski reaguje promjenom svog rada tokom ispitivanja kako bi postigao povoljnije vrijednosti za bilo koji od parametara utvrđenih u ovom pravilniku ili koje je proizvođač/dobavljač deklarisao u tehničkoj dokumentaciji ili bilo kojoj dokumentaciji priloženoj uz proizvod, proizvod se ne smatra usaglašenim.
Prilikom provjere usaglašenosti sa tehničkim zahtjevima eko dizajna sprovodi se sljedeći postupak:
1.
Provjerava se jedna jedinica modela ili, ako proizvođač izvještava o porodici servera, konfiguracija modela. Ako se provjerava
konfiguracija niskih performansi ili konfiguracija visokih performansi, deklarisane vrijednosti predstavljaju vrijednosti odgovarajuće
konfiguracije. Ako se provjerava nasumično odabrana ili tražena konfiguracija modela, deklarisane vrijednosti predstavljaju vrijednosti
konfiguracije visokih performansi;
2.
smatra se da je model ili konfiguracija modela u skladu sa propisanim zahtjevima:
a)
ako vrijednosti navedene u tehničkoj dokumentaciji (deklarisane vrijednosti) i, gdje je primjenljivo, vrijednosti upotrijebljene za
proračun tih vrijednosti nijesu povoljnije za proizvođača ili od rezultata odgovarajućih mjerenja;
b)
ako deklarisane vrijednosti ispunjavaju sve zahtjeve utvrđene u ovom pravilniku, a sve potrebne informacije o proizvodu koje je
objavio proizvođač ili dobavljač ne sadrže vrijednosti koje su povoljnije za proizvođača ili dobavljača od deklarisanih vrijednosti;
c)
ako su za jedinicu modela ili, alternativno, ako je proizvođač deklarisao da server predstavlja porodica servera, za konfiguraciju
modela niskih performansi ili konfiguraciju modela visokih performansi porodice servera, utvrđene vrijednosti (vrijednosti
relevantnih parametara izmjerene u ispitivanju i vrijednosti izračunate na osnovu tih mjerenja) u skladu sa odgovarajućim
dopuštenim odstupanjima za provjeru iz Tabele 7;
3.
ako rezultati iz tačke 2 podtačka a) ili (b) nijesu postignuti, smatra se da model i sve konfiguracije modela koje su obuhvaćene istim
informacijama o proizvodu (u skladu sa tačkom 3.1 podtačkom p) Priloga 1) nijesu u skladu sa ovim Pravilnikom;
4.
ako rezultat iz tačke 2 podtačke c) nije postignut:
a)
za modele ili konfiguracije modela porodice servera koji se proizvode u manje od pet primjeraka godišnje smatra se da model i sve
konfiguracije modela koje su obuhvaćene istim informacijama o proizvodu (u skladu sa tačkom 3.1 podtačkom p) Priloga 1) nijesu
u skladu sa ovim pravilnikom;
b)
za modele koji se proizvode u više od pet primjeraka godišnje za ispitivanje se biraju tri dodatne jedinice istog modela ili,
alternativno, ako je proizvođač deklarisao da server predstavlja porodicu servera, jedinica konfiguracije modela niskih performansi
i jedinica konfiguracije visokih performansi;
5.
smatra se da je model ili konfiguracija modela u skladu sa primjenjivim zahtjevima ako je, za tri odabrane jedinice, aritmetička sredina
utvrđenih vrijednosti u skladu sa odgovarajućim dopuštenim odstupanjima za provjeru iz Tabele 7;
6.
ako rezultati iz tačke 4 podtačke b) nijesu postignuti, smatra se da model i sve konfiguracije modela koje su obuhvaćene istim
informacijama o proizvodu (u skladu sa tačkom 3.1 podtačkom p) Priloga 1) nijesu u skladu sa ovim pravilnikom.
U cilju provjere usaglašenosti primjenjuju se metode mjerenja i proračuna utvrđene u Prilogu 2.
Prilikom provjere usaglašenosti primjenjuju se isključivo dopuštena odstupanja za provjeru utvrđena u Tabeli 7.
Tabela 7: Dopuštena odstupanja za provjeru
Parametri
Dopuštena odstupanja za provjeru Efikasnost jedinice za napajanje (%)
Utvrđena vrijednost ne smije biti više od 2 % manja od deklarisane
vrijednosti.
Faktor snage
Utvrđena vrijednost ne smije biti više od 10 % manja od deklarisane
vrijednosti.
Snaga u stanju pripravnosti, Pidle i najveća snaga (W)
Utvrđena vrijednost ne smije biti više od 10 % veća od deklarisane
vrijednosti.
Efikasnost i performanse u aktivnom stanju
Utvrđena vrijednost ne smije biti više od 10 % manja od deklarisane
vrijednosti.
