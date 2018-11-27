Prilog 1
TEHNIČKE SPECIFIKACIJE INTEROPERABILNOSTI PODSISTEMA KONTROLE, UPRAVLJANJA I SIGNALIZACIJE
1.
UVOD
1.1.
Područje primjene
Tehničke specifikacije interoperabilnosti podsistema kontrole, upravljanja i signalizacije (u daljem
tekstu: TSI) odnosi se na podsistem kontrole, upravljanja i signalizacije u vozilu i na pružni
podsistem kontrole, upravljanja i signalizacije.
TSI se primjenjuje na pružne podsisteme kontrole, upravljanja i signalizacije željezničke mreže
definisane u odjeljku 1.2 (Geografska oblast primjene) i na podsisteme kontrole, upravljanja i
signalizacije u vozilu za vozila koja se na njoj koriste (ili se namjeravaju koristiti). Ta vozila
pripadaju jednom od sledećih tipova:
1)
dizel ili električni vozovi sa sopstvenim pogonom;
2)
vučne jedinice na dizel ili električni pogon;
3)
putnička kola, ako su opremljena upravljačkom kabinom;
4)
pokretna oprema za izgradnju i održavanje željezničke infrastrukture, ako je opremljena
upravljačkom kabinom i predviđena za korišćenje u vidu transporta na sopstvenim
točkovima.";
1.2.
Geografsko područje primjene
Geografska oblast primjene TSI je mreža cjelokupnog željezničkog sistema, koja obuhavata
transevropske mreže konvencionalnog željezničkog sistema (TEN).
Ova TSI se primjenjuje na mreže širine kolosjeka 1435 mm, 1520 mm, 1524 mm, 1600 mm i 1668 mm. Međutim, ne primjenjuje se na kratkim pograničnim prugama širine kolosjeka 1520 mm, koje
su povezane sa mrežom trećih zemalja.
1.3.
Sadržaj TSI
Ovaj TSI odnosi se na interoperabilnost željeznice, koja:
1. se primjenjuje na podsisteme iz Poglavlja 2 ovog priloga;
2. utvrđuje osnovne zahtjeve za podsisteme kontrole, upravljanja i signalizacije i njihove interfejse
sa ostalim podsistemima - Poglavlje 3 (Osnovni zahtjevi za podsisteme kontrole, upravljanja i
signalizacije);
3. utvrđuje funkcionalne i tehničke specifikacije koje moraju zadovoljiti podsistemi i njihovi
interfejsi sa ostalim podsistemima - Poglavlje 4 (Opis osobina podsistema);
4. određuje činioce interoperabilnosti i interfejse koji moraju biti obuhvaćeni evropskim
specifikacijama, uključujući i evropske standarde, a koji su neophodni za postizanje
interoperabilnosti
u
transevropskom
željezničkom
sistemu
-
Poglavlje
5
(Činioci
interoperabilnosti);
5. za svaki razmatrani slučaj, navodi koji postupci treba da se koriste za ocjenu usaglašenosti ili
pogodnosti za upotrebu činilaca interoperabilnosti i za EZ verifikaciju podsistema - Poglavlje 6
(Ocjena usaglašenosti i/ili pogodnosti za upotrebu i verifikacija podsistema);
6. navodi strategiju za sprovođenje e TSI - Poglavlje 7 (Sprovođenje TSI podsistema kontrole,
upravljanja i signalizacije);
7. navodi stručnu osposobljenost, kao i zdravstvene i bezbjednosne uslove koji se zahtjevaju za
osoblje koje radi na ovim podsistemima, održava ih i sprovodi ovu TSI - Poglavlje 4 (Opis osobina
podsistema).
U Poglavlju 7 (Sprovođenje TSI podsistema kontrole, upravljanja i signalizacije) navode se
odredbe za specifične slučajeve.
TSI u Poglavlju 4 (Opis osobina podsistema) utvrđuje operativna pravila i pravila održavanja koja
se specifično primjenjuju na gore navedeno područje primjene iz stavova 1.1. i 1.2.
2.
DEFINICIJA PODSISTEMA I PODRUČJE PRIMJENE
2.1.
Uvod
Podsistemi kontrole, upravljanja i signalizacije su definisani su propisom o interoperabilnosti
željeznice kao "sva oprema potrebna da se osigura bezbjednost i da se upravlja kretanjem vozova
koji imaju odobrenje za saobraćanje u mreži."
Karakteristike podsistema kontrole, upravljanja i signalizacije su:
1. funkcije od suštinskog značaja za bezbjedno upravljanje željezničkim saobraćajem i za njegovo
odvijanje, uključujući i one koje se traže za rad u otežanim uslovima1 1;
2. interfejsi;
3. nivo performansi koji se zahtjeva da se zadovolje osnovni zahtjevi.
2.2.
Područje primjene
TSI podsistema kontrole, upravljanja i signalizacije navode samo one zahtjeve koji su neophodni za
obezbjeđivanje interoperabilnosti transevropskog željezničkog sistema i usaglašenosti sa osnovnim
zahtjevima.
Podsistemi kontrole, upravljanja i signalizacije obuhvataju sljedeće djelove:
1. zaštitu voza;
2. radio komunikaciju;
3. detekciju voza.
Zaštitni sistem Klase A je ERTMS/ETCS dok je radio sistem Klase A GSM-R.
Za detekciju voza Klase A ova TSI navodi samo zahtjeve za interfejse sa drugim podsistemima.
Sistemi Klase B za transevropsku mrežu željezničkog sistema su ograničeni skup nasljeđenih
sistema kontrole, upravljanja i signalizacije koji su se u transevropskoj željezničkoj mreži koristili
prije 20. aprila 2001. godine.
Sistemi Klase B za druge djelove mreže željezničkog sistema u Evropskoj uniji su ograničeni skup
nasljeđenih sistema kontrole, upravljanja i signalizacije koji su se u toj mreži koristili prije 1. jula
2015. godine.
Spisak sistema Klase B utvrđuje u tehničkom dokumentu Evropske agencije za željeznice.
Zahtjevi za podsistem kontrole, upravljanja i signalizacije u vozilu navedeni su u odnosu na zaštitu
voza i na mobilne radio uređaje Klase A.
1 Rad u otežanim uslovima je način funkcionisanja u situaciji kad dođe do kvara. Ove situacije su uzete obzir prilikom projektovanja podsistema
Zahtjevi za pružni podsistem kontrole, upravljanja i signalizacije navedeni su u odnosu na:
1. radio mrežu Klase A;
2. zaštitu voza Klase A;
3. zahtjeve interfejsa sa sistemima za detekciju voza, kako bi se obezbjedila usklađenost sa voznim
sredstvima.
2.3.
Nivoi primjene (ERTMS/ETCS)
Interfejsi navedeni dati u TSI definišu sredstva za prenošenje podataka ka vozovima i, po potrebi,
od vozova. Specifikacije ERTMS/ETCS iz TSI sadrže nivoe primjene prema kojima se prilikom
izvedbe na pruzi može odabrati sredstvo prenosa koje zadovoljava konkretne potrebe.
TSI definiše zahtjeve za sve nivoe primjene.
Vozu opremljenom zaštitom Klase A u vozilu za određeni nivo primjene mora biti omogućeno da
saobraća na tom nivou i na svakom nižem od njega, kao posljedica toga:
- vozu opremljenom zaštitom Klase A u vozilu nivoa 2 mora biti omogućeno da saobraća na tom
nivou i na prugama nivoa 1,
- voz opremljen zaštitom Klase A u vozilu nivoa 1 ne mora da bude opremljen radiom za prenos
podataka GSM-R, ali mora primjenjivati sve funkcije nivoa 2 kako bi se obezbjedilo da u kasnijoj
fazi uključivanjem radia za prenos podataka GSM-R njegova opremljenost bude adekvatna za nivo
2.
3.
OSNOVNI
ZAHTJEVI
ZA
PODSISTEME
KONTROLE,
UPRAVLjANjA
I
SIGNALIZACIJE
3.1.
Opšte napomene
Da bi se ispunilan interoperabilnost željeznice potrebno je da podsistemi i činioci interoperabilnosti,
uključujući i interfejse, ispunjavaju osnovne zahtjeve.
Osnovni zahtjevi su:
1. bezbjednost;
2. pouzdanost i raspoloživost;
3. zaštita zdravlja;
4. zaštita životne sredine;
5. tehnička usklađenost.
Osnovni zahtjevi za sisteme Klase A opisani su u nastavku.
Zahtjevi za sisteme Klase B su odgovornost nadležne države članice.
3.2.
Specifični aspekti podsistema kontrole, upravljanja i signalizacije:
3.2.1.
Bezbjednost
Za svaki projekat na koji se ova specifikacija primjenjuje preduzimaju se mjere neophodne da bi se
obezbjedilo da nivo rizika od eventualne nezgode u okviru podsistema kontrole, upravljanja i
signalizacije ne bude viši od ciljnog nivoa rizika za tu vrstu usluge. U tu svrhu primjenjuje se
zajednička metoda za procjenu i ocjenu rizika.
Da bi se obezbjedilo da mjere preduzete za postizanje bezbjednosti ne ugroze interoperabilnost,
moraju se ispunjavati zahtjevi osnovnog parametra definisanog u Odjeljku 4.2.1 ovog TSI
(Bezbjednosne karakteristike kontrole, upravljanja i signalizacije od značaja za interoperabilnost).
Za ERTMS/ETCS sistem Klase A bezbjednosni cilj je raspodjeljen između podsistema kontrole,
upravljanja i signalizacije u vozilu i pružnog podsistema kontrole, upravljanja i signalizacije.
Detaljni zahtjevi su navedeni u osnovnom parametru definisanom u Odjeljku 4.2.1. (Bezbjednosne
karakteristike podsistema kontrole, upravljanja i signalizacije od značaja za interoperabilnost). Taj
bezbjednosni zahtjev mora se ispuniti zajedno sa zahtjevima o raspoloživosti, kako je definisano u
Odjeljku 3.2.2 (Pouzdanost i raspoloživost).
3.2.2.
Pouzdanost i raspoloživost
Za sistem Klase A ciljevi pouzdanosti i raspoloživosti raspodjeljeni su između podsistema kontrole,
upravljanja i signalizacije u vozilu i pružnog podsistema. Detaljni zahtjevi su navedeni u osnovnom
parametru definisanom u Odjeljku 4.2.1. (Bezbjednosne karakteristike podsistema kontrole,
upravljanja i signalizacije od značaja za interoperabilnost).
Nivo rizika se nadzire zbog toga što su činioci podsistema podložni starenju i trošenju. Zahtjevi za
održavanje navedeni u Odjeljku 4.5 moraju se ispuniti.
3.2.3.
Zaštita zdravlja
U skladu sa propisima EU i nacionalnim propisima koji su usklađeni sa evropskim
zakonodavstvom, mora se voditi računa o tome da se obezbjedi da korišćeni materijali i
konstrukcija podsistema kontrole, upravljanja i signalizacije ne predstavljaju opasnost po zdravlje
za lica koja im imaju pristup.
3.2.4.
Zaštita životne sredine
U skladu sa propisima kojima se uređuje zaštita životne sredine:
1. ukoliko je oprema za kontrolu, upravljanje i signalizaciju izložena prekomjernoj toploti ili vatri,
ne smiju se prekoračiti granične vrijednosti emisije dimova ili gasova koji su štetni za životnu
sredinu;
2. oprema za kontrolu, upravljanje i signalizaciju ne smije sadržati materije koje mogu, pri
normalnoj upotrebi, prekomjerno zagaditi životnu sredinu;
3. oprema za kontrolu, upravljanje i signalizaciju vrši se u skladu sa posebnim propisima za
kontrolu granične vrijednosti emisije elektromagnetnih smetnji i osjetljivost na njih u granicama
željezničkog područja;
4. oprema za kontrolu, upravljanje i signalizaciju mora biti usaglašena sa važećim propisima o
zaštiti od buke;
5. oprema za kontrolu, upravljanje i signalizaciju ne smije biti uzrok bilo kakvih nedozvoljenih
vibracija koje mogu ugroziti stabilnost infrastrukture (u slučajevima kada se infrastruktura propisno
održava).
3.2.5.
Tehnička usklađenost
Tehnička usklađenost obuhvata funkcije, interfejse i performanse koji se zahtjevaju kako bi se
postigla interoperabilnost.
Zahtjevi tehničke usklađenosti su dalje podjeljeni na sledeće tri kategorije:
1. Prva kategorija utvrđuje opšte konstruktivne zahtjeve interoperabilnosti, t.j. uslove okruženja,
internu elektromagnetnu kompatibilnost (EMC) u željezničkom području i zahtjeve za ugradnju.
Ovi zahtjevi usklađenosti definisani su u ovom poglavlju.
2. Druga kategorija opisuje kako podsistemi kontrole, upravljanja i signalizacije treba da se
primjene u tehničkom smislu i koje funkcije moraju da izvrše da bi se obezbjedila interoperabilnost.
Ova kategorija je definisana u Poglavlju 4 ovog priloga.
3. Treća kategorija opisuje kako podsistemi kontrole, upravljanja i signalizacije treba da se koriste
da bi se postigla interoperabilnost. Ova kategorija je definisana u Poglavlju 4 ovog priloga.
3.2.5.1. Konstruktivna usklađenost
3.2.5.1.1. Fizički uslovi okruženja
Oprema za kontrolu, upravljanje i signalizaciju mora biti u stanju da funkcioniše pod klimatskim i
fizičkim uslovima karakterističnim za konkretno područje u kome je lociran taj dio transevropskog
sistema.
Zahtjevi osnovnog parametra 4.2.16 (Uslovi okruženja) moraju se ispuniti.
3.2.5.1.2. Interna elektromagnetna kompatibilnost željeznice
Oprema za kontrolu, upravljanje i signalizaciju ne smije remetiti funkcionisanje druge opreme za
kontrolu, upravljanje i signalizaciju i drugih podsistema, a takođe ni oni ne smiju remetiti njeno
funkcionisanje.
Osnovni parametar za elektromagnetnu kompatibilnost između opreme podsistema kontrole,
upravljanja i signalizacije u vozilu i opreme pružnog podsistema kontrole, upravljanja i
signalizacije opisan je u Odjeljku 4.2.11 (Elektromagnetna kompatibilnost) ovog TSI.
3.2.5.2. Usklađenost podsistema kontrole, upravljanja i signalizacije
Poglavlje 4 definiše zahtjeve za interoperabilnost podsistema kontrole, upravljanja i signalizacije.
Podsistemi kontrole, upravljanja i signalizacije, ovim TSI se obezbjeđuje tehnička interoperabilost
između transevropskog željezničkog sistema velikih brzina i transevropskog konvencionalnog
sistema, ukoliko oba pripadaju sistemima Klase A.
4.
OPIS OSOBINA PODSISTEMA
4.1.
Uvod
U skladu sa bitnim osnovnim zahtjevima, podsisteme kontrole, upravljanja i signalizacije karakterišu
sledeći osnovni parametri:
1.
bezbjednosne karakteristike kontrole, upravljanja i signalizacije od značaja za interoperabilnost
2.
funkcionalnost sistema ERTMS/ETCS u vozilu
3.
funkcionalnost pružnog sistema ERTMS/ETCS
4.
mobilne komunikacione funkcije za željeznice - GSM-R
5.
interfejsi vazdušnog međuprostora ERTMS/ETCS i GSM-R
6.
interni interfejsi podsistema kontrole, upravljanja i signalizacije u vozilu
7.
interfejsi pružnog podsistema kontrole, upravljanja i signalizacije
8.
upravljanje ključevima
9.
upravljanje ETCS-ID
10. sistemi za detekciju voza
11. elektromagnetna kompatibilnost između podsistema kontrole, upravljanja i signalizacije u
vozilu i pružnog podsistema kontrole, upravljanja i signalizacije
12. ERTMS/ETCS DMI (interfejs mašinovođa - voz)
13. GSM-R DMI (interfejs mašinovođa - voz)
14. interfejs sa bilježenjem podataka u regulatorne svrhe
15. vidljivost pružnih objekata za kontrolu, upravljanje i signalizaciju
16. Uulovi okruženja
Zahtjevi u Odjeljku 4.2 (Funkcionalne i tehničke specifikacije podsistema) ovog Priloga u vezi sa
ispunjavanjem ovih osnovnih parametara primjenjuju se na sistem Klase A.
Zahtjevi za sisteme Klase B i za STM (specifične prenosne module) (koji omogućuju da sistem
Klase A u vozilu funkcioniše na infrastrukturi Klase B) utvrđeni su posebnim propisom.
TSI zasniva se na načelima koja omogućuju pružnom podsistemu da bude usklađen sa
podsistemima kontrole, upravljanja i signalizacije u vozilima koji su u skladu sa TSI radi
postizanja:
1. funkcije, interfejsi i ososbine podsistema kontrole, upravljanja i signalizacije u vozilu su
standardizovani, obezbjeđujući da svaki voz reaguje na predvidljiv način na podatke koje prima od
opreme na pruzi;
2. za pružni podsistem kontrole, upravljanja i signalizacije komunikacije pruga - voz i voz - pruga
su u potpunosti standardizovane u ovoj TSI, na funkcionalnost pružnog podsistema kontrole,
upravljanja i signalizacije TSI se primjenjuje fleksibilno, tako da se može optimalno integrisati u
željeznički system, bez ograničenja kretanja podsistema u vozilu usklađenog sa TSI.
Funkcije podsistema kontrole, upravljanja i signalizacije se klasifikuju po kategorijama koje
označavaju da li su izborne (O - optional) ili obavezne (M - mandatory). Ove kategorije su
definisane u Dio A 4.1a za ERTMS/ETCS i u Dio A 4.1b za GSM-R, a u tim tekstovima se navodi i
kako su funkcije klasifikovane.
U skladu sa Odjeljkom 2.2. (Područje primjene) podsistemi kontrole, upravljanja i signalizacije
obuhvataju tri dijela. Sledeća tabela ukazuje na osnovne parametre koji su od značaja za svaki
podsistem i za svaki dio.
Podsistem
Dio
Osnovni parametri
Podsistem kontrole,
upravljanja i
signalizacije u vozilu
zaštita voza
4.2.1, 4.2.2, 4.2.5, 4.2.6, 4.2.8,
4.2.9, 4.2.12, 4.2.14, 4.2.16
radio komunikacija
4.2.1.2, 4.2.4, 4.2.5, 4.2.6, 4.2.13,
4.2.14,
Pružni podsistem
kontrole, upravljanja i
signalizacije
zaštita voza
4.2.1, 4.2.3, 4.2.5, 4.2.7, 4.2.8,
4.2.9,
radio komunikacija
4.2.1.2, 4.2.4, 4.2.5, 4.2.7, 4.2.16
detekcija voza
4.2.10, 4.2.11, 4.2.16
U pogledu osnovnih zahtjeva utvrđenih u Poglavlju 3, funkcionalne i tehničke specifikacije
podsistema kontrole, upravljanja i signalizacije su:
4.2.
Funkcionalne i tehničke specifikacije podsistema
4.2.1.
Bezbjednosne karakteristike podsistema kontrole, upravljanja i signalizacije od značaja za
interoperabilnost
Da bi se postigla interoperabilnost, prilikom izvođenja podsistema kontrole, upravljanja i
signalizacije u vozilu i pružnog podsistema treba da:
1. Konstrukcija, izvođenje i upotreba podsistema kontrole, upravljanja i signalizacije u vozilu ili
pružnog podsistema ne smiju nametati nove zahtjeve:
a) kroz interfejs između podsistema kontrole, upravljanja i signalizacije u vozilu i pružnog
podsistema, uz zahtjeve koji su već navedeni ovom TSI;
b) bilo kom drugom podsistemu, osim zahtjeva navedenih u odgovarajućoj TSI.
2. Zahtjevi utvrđeni u Odjeljcima 4.2.1.1. i 4.2.1.2. su:
4.2.1.1. Bezbjednost
Podsistem kontrole, upravljanja i signalizacije u vozilu i pružni podsistem moraju ispunjavati
zahtjeve za opremu i postrojenja ERTMS/ETCS navedene ovom TSI.
Za rizik ,,prekoračenje graničnih vrijednosti brzine i/ili rastojanja preporučenih za ERTMS/ETCSˮ
prihvatljiva stopa (THR) je 10- 9 h- 1 za slučajne otkaze i za ERTMS/ETCS u vozilu i za pružni
ERTMS/ETCS. Vidjeti Dio A 4.2.1.a
Da bi se postigla interoperabilnost, ERTMS/ETCS mora u potpunosti ispunjavati sve zahtjeve
navedene u Dijelu A 4.2.1. Bez obzira na to, prihvatljivi su manje strogi bezbjednosni zahtjevi za
pružni ERTMS/ETCS pod uslovom da se, u kombinaciji sa podsistemima kontrole upravljanja i
signalizacije u vozilu koji su usklađeni sa TSI, poštuje nivo bezbjednosti usluge.
Zahtjevi za rizike koji su povezani sa greškama na interfejsu između mašinovođe i ERTMS/ETCS u
vozilu su otvoreno pitanje.
4.2.1.2. Raspoloživost /Pouzdanost
Ovaj odjeljak odnosi se na pojavu režima otkaza koji ne prouzrokuju opasnost po bezbjednost već
dovode do rada u otežanim uslovima, pri čemu bi njihovo savladavanje moglo smanjiti sveukupnu
bezbjednost sistema.
"Otkaz" je prestanak sposobnosti neke jedinice da obavlja potrebnu funkciju sa zahtjevanim
učinkom, a "režim otkaza" je efekat po kojem se otkaz opaža.
Da bi se obezbjedilo da upravljači infrastukture i željeznička preduzeća dobiju sve informacije koje
su im potrebne da definišu odgovarajuće postupke za upravljanje otežanim situacijama, tehnička
dokumentacija koja prati EZ deklaraciju o verifikaciji za podsistem CCS u vozilu i za pružni
podsistem CCS mora da sadrži proračunate vrijednosti za raspoloživost/pouzdanost, u vezi sa
režimima otkaza koji utiču na sposobnost podsistema CCS da nadzire bezbjedno kretanje jednog ili
više vozila ili da uspostavi glasovnu radio komunikaciju između kontrole saobraćaja i mašinovođa.
Mora se obezbjediti usklađenost sa sljedećim proračunatim vrijednostima:
1)
srednje vrijeme radnih sati između otkaza podsistema CCS u vozilu, koji
iziskuju isključivanje funkcija zaštite voza: [otvoreno pitanje];
2)
srednje vrijeme radnih sati između otkaza podsistema CCS u vozilu, koji
sprečavaju glasovnu radio komunikaciju između kontrole saobraćaja i
mašinovođe: [otvoreno pitanje].
Kako bi se upravljačima infrastrukture i željezničkim preduzećima omogućilo da tokom životnog
vijeka podsistema prate stepen rizika i poštovanje vrijednosti za raspoloživost/pouzdanost koji se
koriste za definisanje postupaka za upravljanje radom u otežanim uslovima, moraju se poštovati
zahtjevi za održavanje navedeni u odjeljku 4.5 (Pravila održavanja).
4.2.2.
Funkcionalnost sistema ERTMS/ETCS u vozilu
Osnovni parametar za funkcionalnost ERTMS/ETCS u vozilu opisuje sve funkcije neophodne da se
vozom upravlja na bezbjedan način. Primarna funkcija je da se obezbjede automatska zaštita voza i
kabinska signalizacija.
1. podešavanje karakteristika voza (npr. maksimalna brzina voza, performanse kočenja);
2. biranje načina nadzora na osnovu informacija sa pruge;
3. obavljanje funkcija mjerenja dužine puta i brzine;
4. lociranje voza u koordinatnom sistemu na osnovu lokacija Eurobalize;
5. izračunavanje dinamičkog profila brzine za vožnju na osnovu karakteristika voza i informacija
sa pruge;
6. nadziranje dinamičkog profila brzine u toku vožnje;
7. omogućavanje funkcije intervencije.
Ove funkcije se izvode u skladu sa Dijelom A 4.2.2.b, a njihove performanse moraju biti u skladu
sa Dijelom A 4.2.2.a.
Zahtjevi za ispitivanja definisani su u Dijelu A 4.2.2.c.
Identitetima opreme u ETCS upravlja se u skladu sa Odjeljkom 4.2.9 (Upravljanje ETCS - ID).
Glavnu funkcionalnost podržavaju druge funkcije na koje se takođe primjenjuju Dio A 4.2.2.a i Dio
A 4.2.2.b, zajedno sa dodatnim specifikacijama navedenim u nastavku.
1. Komunikacija sa pružnim podsistemom kontrole, upravljanja i signalizacije.
a) prenos podataka Eurobalizom u skladu sa Odjeljkom 4.2.5.2 (Komunikacija sa vozom preko
Eurobalize);
b) prenos podataka Europetljom u skladu sa Odjeljkom 4.2.5.3 (Komunikacija sa vozom preko
Europetlje). Ova funkcionalnost je izborna u vozilu izuzev ako je Europetlja instalirana na pruzi u
nivou 1 ERTMS/ETCS, a brzina približavanja je, iz bezbjednosnih razloga, podešena na nulu (npr.
zaštita opasnih tačaka);
c) Radio prenos podataka za radio in-fill dat je Dijelu A 4.2.2.d, Odjeljcima 4.2.5.1. (Radio
komunikacija sa vozom), 4.2.6.2 (Interfejs između radio prenosa podataka GSM-R i
ERTMS/ETCS) i 4.2.8 (Upravljanje ključevima). Ova funkcionalnost je izborna u vozilu izuzev
ako je radio prenos podataka za radio in-fill instaliran na pruzi u nivou 1 ERTMS/ETCS, a brzina
približavanja je podešena na nulu iz bezbjednosnih razloga (npr. zaštita opasnih tačaka);
d) Radio prenos podataka dat je u Odjeljcima 4.2.5.1 (Radio komunikacija sa vozom), 4.2.6.2
(Interfejs između radio prenosa podataka GSM-R i ERTMS/ETCS) i 4.2.8 (Upravljanje
ključevima, koji je obavezan u vozilu samo kod primjene ERTMS/ETCS nivoa 2 ili ETCS nivoa 3.
2. Komuniciranje sa mašinovođom dat je u Dijelu A 4.2.2.d i Odjeljku 4.2.12 (ERTMS/ETCS DMI).
3. Komuniciranje sa STM dato je u Odjeljku 4.2.6.1 (Interfejs između ERTMS/ETCS i STM). Ova
funkcija obuhvata:
a) upravljanje izlaznim podacima STM;
b) obezbjeđivanje podataka koje koristi STM;
c) upravljanje prelazima STM.
4. Upravljanje informacijama o cjelovitosti voza (integritet voza) - obavezno za nivo 3, ne zahtjeva se
za nivoe 1 i 2.
5. Praćenje stanja opreme i podrška u radu u otežanim uslovima. Ova funkcija obuhvata:
a) pokretanje funkcionalnosti sistema ERTMS/ETCS u vozilu;
b) obezbjeđivanje podrške radu u otežanim uslovima;
c) isključivanje funkcionalnosti sistema ERTMS/ETCS u vozilu.
6. Podrška bilježenju podataka u regulatorne svrhe u skladu sa Odjeljkom 4.2.14 (Interfejs sa beleženjem
podataka u regulatorne svrhe)
7. Proslijeđivanje informacija/naloga i prijem izvještaja o stanju sa voznih sredstava
a) ka DMI dato je u Odjeljku 4.2.12 (ERTMS/ETCS DMI);
b) ka jedinici interfejsa voza i od nje u skladu sa Dijelom A 4.2.2.f.
4.2.3.
Funkcionalnost pružnog sistema ERTMS/ETCS
Ovaj osnovni parametar opisuje funkcionalnost pružnog sistema ERTMS/ETCS. On sadrži svu
funkcionalnost opreme ERTMS/ETCS za obezbjeđivanje bezbjednog puta vožnje konkretnog voza.
Glavna funkcionalnost je:
1. lociranje konkretnog voza u koordinatnom sistemu zasnovanom na lokacijama Eurobalize (nivoi
2 i 3);
2. prevođenje informacija sa pružne opreme za signalizaciju u standardni format za podsistem
kontrole, upravljanja i signalizacije u vozilu;
3. slanje odobrenja za vožnju uključujući opis pruge i naloge dodjeljene konkretnom vozu.
Ove funkcije se sprovode u skladu sa Dijelom A 4.2.3.b, a njihove performanse moraju biti u
skladu sa Dijelom A 4.2.3.a.
Zahtjevi za ispitivanja definisani su u Dijelu A 4.2.3.c.
Identitetima opreme u ETCS upravlja se u skladu sa Odjeljkom 4.2.9 (Upravljanje ETCS - ID).
Glavnu funkcionalnost podržavaju druge funkcije na koje se takođe primjenjuju Dio A 4.2.3.a i Dio
A 4.2.3.b, zajedno sa dodatnim specifikacijama navedenim u nastavku:
1. Komunikacija sa podsistemom kontrole, upravljanja i signalizacije u vozilu obuhvata:
a) prenos podataka Eurobalizom, dato u Odjeljcima 4.2.5.2 (Komunikacija sa vozom preko
Eurobalize) i 4.2.7.4 (Eurobaliza/pružna elektronska jedinica (LEU));
b) prenos podataka Europetljom, dato u Odjeljcima 4.2.5.3 (Komunikacija sa vozom preko
Europetlje) i 4.2.7.5 (Europetlja/LEU). Europetlja je od značaja samo za nivo 1, na kome je
izborna;
c) Radio prenos podataka za radio in-fill, dato u Aneksu A 4.2.3.d i Odjeljcima 4.2.5.1 (Radio
komunikacije sa vozom), 4.2.7.3 (Funkcionalnost pružnog ETCS/ GSM-R) i 4.2.8
(Upravljanje ključevima). Radio in-fill je od značaja samo za nivo 1, na kome je izborni;
d) Radio prenos podataka, dato u Odjeljcima 4.2.5.1 (Radio komunikacije sa vozom), 4.2.7.3
(Funkcionalnost pružnog ETCS/GSM-R) i 4.2.8 (Upravljanje ključevima). Radio prenos
podataka je od značaja samo za nivoe 2 i 3;
2.
Generisanje informacija/naloga za ERTMS/ETCS u vozilu, npr. informacija koje se odnose na
zatvaranje/otvaranje zakrilaca, spuštanje/podizanje pantografa, otvaranje/zatvaranje glavnog
prekidača napajanja, promjenu sa sistema vuče A na sistem vuče B. Omogućavanje ove
funkcionalnosti je izborno za pružnu opremu.
3. Upravljanje prelazima između područja pod nadzorom različitih radio blok centara (RBC) (od
značaja samo za nivoe 2 i 3). Detalji o ovome dati su u Odjeljcima 4.2.7.1 (Funkcionalni
interfejs između radio blok centara) i 4.2.7.2 (Tehnički interfejs između radio blok centara).
4.2.4. Mobilne komunikacione funkcije za željeznice - GSM-R
Ovaj osnovni parametar opisuje funkcije radio komunikacije. Te funkcije se izvode u podsistemima
kontrole, upravljanja i signalizacije u vozilu i pružnom podsistemu, u skladu sa specifikacijama
navedenim u nastavku.
4.2.4.1. Osnovna komunikaciona funkcija
Opšti zahtjevi navedeni su u Dijelu A 4.2.4.a.
Pored toga, moraju se poštovati sledeće specifikacije:
1) karakteristike ASCI; Dio A 4.2.4.b;
2) SIM kartica; Dio A 4.2.4.v;
3) signalizacija korisnik ka korisniku; Dio A 4.2.4.g;
4) adresiranje zavisno od lokacije; Dio A 4.2.4.d.
4.2.4.2. Govorne i operativne komunikacione aplikacije
Opšti zahtjevi definisani su u Dio A 4.2.4.f.
Zahtjevi za ispitivanja navedeni su u Dio A 4.2.4.g.
Pored toga, moraju se poštovati sledeće specifikacije:
1) potvrda interventnih poziva; Dio A 4.2.4.h;
2) funkcionalno adresiranje; Dio A 4.2.4.j;
3) prikaz funkcionalnih brojeva; DioA 4.2.4.k.
4.2.4.3. Aplikacije prenosa podataka za ETCS
Opšti zahtjevi definisani su u Dio A 4.2.4.f.
Zahtjevi za ispitivanja navedeni su u Dio A 4.2.4.g.
Ova funkcionalnost je obavezna jedino u slučaju ETCS nivoa 2 i 3 i za aplikacije kod radio in-fill.
4.2.5. Interfejsi vazdušnog međuprostora ERTMS/ETCS i GSM-R
Ovim osnovnim parametrom navode se zahtjevi za interfejs vazdušnog međuprostora između
pružnog podsistema kontrole, upravljanja i signalizacije i podsistema kontrole, upravljanja i
signalizacije u vozilu koji se mora uzeti u obzir zajedno sa zahtjevima za interfejse između opreme
ERTMS/ETCS i GSM-R, kako je navedeno u Odjeljcima 4.2.6 (Interni interfejsi kontrole,
upravljanja i signalizacije u vozilu) i 4.2.7 (Interni pružni interfejsi kontrole, upravljanja i
signalizacije).
Ovaj osnovni parametar obuhvata:
1. fizičke, električne i elektromagnetne vrijednosti koje se moraju ispunjavati da bi se omogućilo
bezbjedno funkcionisanje;
2. komunikacioni protokol koji se koristi;
3. raspoloživost komunikacionog kanala.
U nastavku su navedene specifikacije koje se primjenjuju.
4.2.5.1. Radio komunikacija sa vozom
Interfejsi Klase A funkcionišu u opsegu GSM-R - u skladu sa Dijelom A 4.2.5.a.
Protokoli moraju biti usklađeni sa Dijelom A 4.2.5.b.
Kada se primjenjuje radio in-fill, moraju se ispunjavati zahtjevi navedeni u Dijelu A 4.2.5.c.
4.2.5.2. Komunikacija sa vozom preko Eurobalize
Komunikacioni interfejsi Eurobalize moraju biti usklađeni sa Dijelom A 4.2.5.d.
4.2.5.3. Komunikacija sa vozom preko Europetlje
Komunikacioni interfejsi Europetlje moraju biti usklađeni sa Dijelom A 4.2.5.e.
4.2.6. Interni interfejsi podsistema kontrole, upravljanja i signalizacije u vozilu
Ovaj osnovni parametar sastoji se od tri djela.
4.2.6.1. ERTMS/ETCS i zaštita voza Klase B
Kada su u vozilu instalirane funkcije ERTMS/ETCS i funkcije za zaštitu voza Klase B, prelazima
između njih može se upravljati preko standardizovanog interfejsa, kako je navedeno u Dijelu A
4.2.6.a.
Dio A 4.2.6.b određuje interfejs K (koji omogućava da izvjesni STM očitavaju informacije sa baliza
Klase B preko antene ERTMS/ETCS u vozilu), a Dio A 4.2.6.c određuje interfejs G (vazdušni
međuprostor između antene ETCS u vozilu i baliza Klase B).
Izvedba interfejsa K je izborna, ali ukoliko se primjeni, to mora biti u skladu sa Dijelom A 4.2.6.b.
Štaviše, ukoliko se primjeni interfejs K, funkcionalnost prenosnog kanala u vozilu mora biti u stanju
da upravlja karakteristikama iz Dijelu A 4.2.6.c.
Ukoliko se prelazom između ERTMS/ETCS i zaštite voza Klase B u vozilu ne upravlja uz upotrebu
standardizovanog interfejsa navedenog u Dijelu A 4.2.6.a, moraju se preduzeti koraci da se
obezbjedi da korišćeni metod ne nameće dodatne zahtjeve za pružni podsistem kontrole, upravljanja
i signalizacije
4.2.6.2. Interfejs između prenosa podataka putem GSM-R i ERTMS/ETCS
Zahtjevi za interfejs između radia Klase A i funkcionalnosti ERTMS/ETCS u vozilu navedeni su u
Dijelu A 4.2.6.d.
Kada se sprovodi radio in-fill, moraju se ispunjavati zahtjevi navedeni u Dijelu A 4.2.6.e.
4.2.6.3. Mjerenje brzine i pređenog puta (odometrija)
Interfejs između funkcije mjerenja brzine i pređenog puta i ETCS u vozilu mora zadovoljiti zahtjeve
iz Diejlu A 4.2.6.f. Interfejs doprinosi ovom osnovnom parametru samo kada je oprema za mjerenje
brzine i pređenog puta obezbjeđena kao zaseban činilac interoperabilnosti (vidjeti Odjeljak 5.2.2,
Grupisanje činilaca interoperabilnosti).
4.2.7. Interni interfejsi pružnog podsistema kontrole, upravljanja i signalizacije
Ovaj osnovni parametar sastoji se od pet djelova.
4.2.7.1. Funkcionalni interfejs između RBC
Ovaj interfejs definiše podatke koji se razmenjuju između susednih RBC da bi se o mogućilo
bezbjedno kretanje voza od jednog područja RBC do sledećeg:
1. informacije od "predajnog" RBC ka "prijemnom" RBC;
2. informacije od "prijemnog" RBC ka "predajnom" RBC.
Zahtjevi su navedeni u Dijelu A 4.2.7.a.
4.2.7.2. RBC/RBC
Ovo je tehnički interfejs između dva RBC. Zahtjevi su navedeni u Dijelu A 4.2.7.b.
4.2.7.3. GSM-R/ pružni ETCS
Ovo je interfejs između radio sistema Klase A i funkcionalnosti pružnog ETCS. Zahtjevi su
navedeni u Dijelu A 4.2.7.c.
4.2.7.4. Eurobaliza/LEU
Ovo je interfejs između Eurobalize i LEU (pružne elektronske jedinice). Zahtjevi su navedeni u
Dijelu A 4.2.7.d.
Ovaj interfejs doprinosi ovom osnovnom parametru samo kada su Eurobaliza i LEU obezbjeđeni
kao
zasebni
činioci
interoperabilnosti
(dato
u
Odjeljku
5.2.2,
Grupisanje
činilaca
interoperabilnosti).
4.2.7.5. Europetlja/LEU
Ovo je interfejs između Europetlje i LEU. Zahtjevi su navedeni u Dijelu A 4.2.7.d.
Ovaj interfejs doprinosi ovom osnovnom parametru samo kada su Europetlja i LEU obezbjeđeni
kao
zasebni
činioci
interoperabilnosti
(dato
u
Odjeljku
5.2.2,
Grupisanje
činilaca
interoperabilnosti).
4.2.8. Upravljanje ključevima
Ovaj osnovni parametar određuje zahtjeve za upravljanje kriptografskim ključevima korišćenim za
zaštitu podataka koji se prenose radio vezom.
Zahtjevi su navedeni u Dijelu A 4.2.8.a. Samo zahtjevi koji se odnose na interfejse opreme za
kontrolu, upravljanje i signalizaciju spadaju pod područje primjene ove TSI.
4.2.9. Upravljanje ETCS-ID
Ovaj osnovni parametar odnosi se na identitete u ETCS (ETCS-ID) za opremu u pružnom podsistemu
kontrole, upravljanja i signalizacije, kao i u podsistemu u vozilu.
Zahtjevi su navedeni u Dijelu A 4.2.9.a.
4.2.10. Pružni sistemi za detekciju voza
Ovaj osnovni parametar određuje zahtjeve interfejsa između pružnih sistema detekcije i voznih
sredstava.
Zahtjevi za interfejse koje sistemi za detekciju voza moraju ispunjavati su navedeni u Dijelu A
4.2.10.a.
4.2.11. Elektromagnetna kompatibilnost voznih sredstava i opreme pružnog podsistema kontrole,
upravljanja i signalizacije
Ovaj osnovni parametar određuje zahtjeve interfejsa za elektromagnetnu kompatibilnost voznih
sredstava i opreme pružnog sistema kontrole, upravljanja i signalizacije.
Zahtjevi za interfejse koje sistem za detekciju voza mora ispunjavati su navedeni u Dijelu A
4.2.11.a.
4.2.12. ERTMS/ETCS DMI (interfejs mašinovođa - voz)
Ovaj osnovni parametar opisuje informacije koje ERTMS/ETCS obezbjeđuje mašinovođi i koje
mašinovođa unosi u ERTMS/ETCS u vozilu u skladu u Dijelom A 4.2.12.a.
Ovo obuhvata:
1. ergonomiju (uključujući i vidljivost);
2. funkcije ERTMS/ETCS koje treba da se prikažu;
3. funkcije ERTMS/ETCS koje se aktiviraju unosom podataka od strane mašinovođe.
4.2.13. GSM-R DMI (interfejs mašinovođa - voz)
Ovaj osnovni parametar opisuje informacije koje GSM-R obezbjeđuje mašinovođi i koje mašinovođa
unosi u GSM-R u vozilu u skladu u Dijelom A 4.2.13.a.
Ovo obuhvata:
1. ergonomiju (uključujući i vidljivost);
2. funkcije GSM-R koje treba prikazati;
3. izlazne informacije u vezi sa pozivom;
4. ulazne informacije u vezi sa pozivom.
4.2.14. Interfejs sa bilježenjem podataka u regulatorne svrhe
Ovaj osnovni parametar opisuje:
1. razmjenu podataka između ERTMS/ETCS u vozilu i uređaja za bilježenje u voznom sredstvu;
2. komunikacione protokole;
3. fizički interfejs u skladu u Dijelom A 4.2.14.a.
4.2.15. Vidljivost pružnih objekata za kontrolu, upravljanje i signalizaciju
Ovaj osnovni parametar opisuje:
1. karakteristike retro-reflektujućih znakova da bi se obezbjedila propisana vidljivost;
2. karakteristike interoperabilnih signalnih oznaka u skladu u Dijelom A 4.2.15.a.
Pored toga, ugradnja pružnih objekata za kontrolu, upravljanje i signalizaciju mora biti usklađena sa
vidnim poljem mašinovođe i zahtjevima infrastrukture.
4.2.16. Uslovi okruženja
Moraju se ispunjavati uslovi okruženja propisani u specifikacijama na koje upućuje ova TSI.
4.3.
Funkcionalne i tehničke specifikacije za interfejse sa drugim podsistemima
4.3.1. Interfejs sa podsistemom odvijanja i upravljanja saobraćajem
Interfejs sa TSI OPE
Referentna TSI CCS
Referentna
TSI OPE
Parametar
odredba
P
odredba
Operativna pravila (u normalnim
uslovima i u otežanim uslovima
rada)
4.4
Pravilnik
4.2.1.2.1
Operativna pravila
4.4
Vidljivost pružnih objekata za
kontrolu, upravljanje i signalizaciju
4.2.15
Opažanje signala i pružnih
oznaka
4.2.2.8
Performanse i karakteristike kočenja
voza
4.2.2
Performanse kočenja
4.2.2.6
Upotreba opreme za pjeskarenje
4.2.10
Pravilnik
4.2.1.2.1
Podmazivanje venca točka u
vozilu
Upotreba kočnih papuča od
kompozitnih materijala
Interfejs sa beleženjem podataka
u regulatorne svrhe
4.2.14
Beleženje podataka u vozilu
4.2.3.5
ETCS DMI
4.2.12
Broj voza
4.2.3.2.1
GSM-R DMI
4.2.13
Broj voza
4.2.3.2.1
4.3.2. Interfejs sa podsistemom voznih sredstava
Interfejs sa TSI RS
Referentna TSI CCS
Referentne TSI RS
Parametar
Odredba
Parametar
Odredba
Usklađenost sa
pružnim sistemom za
detekciju voza:
konstrukcija vozila
4.2.10
Karakteristike voznih
sredstava koje treba da
budu usklađene sa
sistemom detekcije voza
zasnovanim na šinskim
strujnim kolima
TSI HS RS
-
lokacija osovinskih
sklopova
-
osovinsko opterećenje
-
peskarenje
-
električni otpor
između točkova
4.2.7.9.2
4.2.3.2
4.2.3.10
4.2.3.3.1
4.2.3.3.1.1
4.2.3.2
TSI LOC & PAS
TSI WAG
Karakteristike voznih
sredstava koje treba da
budu usklađene sa
sistemima detekcije voza
zasnovanim na
brojačima osovina
TSI HS RS
-
geometrija osovinskih
sklopova
-
točkovi
4.2.7.9.2
4.2.7.9.3
4.2.3.3.1.2
4.2.3.3.1
TSI LOC & PAS
TSI WAG
Karakteristike
voznih
sredstava usklađene sa
opremom petlje
TSI HS RS
Nema
4.2.3.3.1.3
Nema
TSI LOC & PAS
TSI WAG
Elektromagnetna
kompatibilnost voznih
sredstava i pružne
opreme za kontrolu,
upravljanja i
signalizacije
4.2.11
Karakteristike voznih
sredstava koje treba da
budu usklađene sa
sistemom za detekciju
voza zasnovanim na
šinskim strujnim kolima
TSI HS RS
4.2.6.6.1
4.2.3.3.1
Nema
TSI LOC & PAS
TSI WAG
Karakteristike voznih
sredstava koje treba da
budu usklađene sa
sistemom za detekciju
voza zasnovanim na
brojačima osovina
TSI HS RS
4.2.6.6.1
4.2.3.3.2
Nema
TSI LOC & PAS
TSI WAG
Performanse i
karakteristike kočenja
voza
4.2.2
Performanse brzog
kočenja
TSI HS RS
Brzo kočenje
Normalno kočenje
4.2.4.1
4.2.4.4
4.2.4.5.2
4.2.4.5.3
4.2.4.1.2
TSI LOC & PAS
Brzo kočenje
Normalno kočenje
TSI WAG
Položaj antena
podsistema kontrole
upravljanja i
signalizacije u vozilu
4.2.2
Kinematički profil
TSI HS RS
4.2.3.1
4.2.3.1
Nema
TSI LOC & PAS
TSI WAG
Isključivanje
4.2.2
Operativna pravila
TSI HS RS
4.2.7.9.1
Interfejs sa TSI
Referentna TSI CCS
Referentne TSI RS
Parametar
Odredba
Parametar
Odredba
funkcionalnosti sistema
ERTMS/ETCS u vozilu
TSI LOC & PAS
4.2.12.3
Nema
TSI WAG
Interfejsi za podatke
4.2.2
Koncepti praćenja i
dijagnostike
TSI HS RS
4.2.7.10
TSI LOC & PAS
4.2.1.1
TSI WAG
Nema
Vidljivost pružnih
objekata za kontrolu,
upravljanje i signalizaciju
4.2.15
Spoljašnja vidljivost
Čeona svjetla
TSI HS RS
4.2.7.4.1.1
TSI LOC & PAS
4.2.7.1.1
TSI WAG
Nema
Spoljno vidno polje
mašinovođe
TSI HS RS
linija optičke vidljivosti
vetrobransko staklo
4.2.2.6 (b)
4.2.2.7
TSI LOC & PAS
linija optičke vidljivosti
vetrobransko staklo
4.2.9.1.3.1
4.2.9.2
TSI WAG
Nema
Interfejs sa bilježenjem
podataka u regulatorne
svrhe
4.2.14.
Uređaj za bilježenje
TSI HS RS
4.2.7.10
TSI LOC & PAS
4.2.9.6
TSI WAG
Nema
Komande za opremu
u voznim sredstvima
4.2.2.
4.2.3
Razdvajanje faza
TSI HS RS
4.2.8.3.6.7
TSI LOC & PAS
4.2.8.2.9.8
TSI WAG
Nema
Komanda za brzo
kočenje
4.2.2
Komanda za brzo kočenje
TSI HS RS
Nema
TSI LOC & PAS
4.2.4.4.1
TSI WAG
Nema
4.3.3. Interfejs sa podsistemom infrastrukture
Interfejs sa TSI INF
Referentna TSI CCS
Referentna TSI INF
Parametar
Odredba
Parametar
Odredba
Sistemi za detekciju
voza (prostor za
ugradnju)
4.2.10
Minimalni infrastrukturni profil
HS
4.2.3
Slobodni profil
CR
4.2.4.1
Komunikacija preko
Eurobalize (prostor za
ugradnju)
4.2.5.2
Minimalni infrastrukturni profil
HS
4.2.3
Slobodni profil
CR
4.2.4.1
Komunikacija preko
Europetlje (prostor za
ugradnju)
4.2.5.3
Minimalni infrastrukturni profil
HS
4.2.3
Slobodni profil
CR
4.2.4.1
Vidljivost pružnih
objekata za kontrolu,
upravljanje i
signalizaciju
4.2.15
Minimalni infrastrukturni profil
HS
4.2.3
Slobodni profil
CR
4.2.4.1
4.3.4. Interfejs sa podsistemom energije
Interfejs sa TSI ENE
Referentna TSI CCS
Referentna TSI ENE
Parametar
Odred
ba
Parametar
Odredba
Komande
za opremu
u voznim
sredstvima
4.2.2
Sekcije razdvajanje faza
TSI HS ENE
4.2.21
4.2.3
Sekcije razdvajanje sistema
4.2.22
Sekcije razdvajanje faza
TSI CR ENE
4.2.19
Sekcije razdvajanje
sistema
4.2.20
4.3.5. Karakteristike voznih sredstava bitne za usklađenost sa sistemima za detekciju voza
Karakteristike voznih sredstava bitne za usklađenost sa sistemima za detekciju voza su date kao skup karakteristika voznih sredstava bitnih za usklađenost sa ciljnim sistemima za detekciju voza u odredbama 4.2.3.3.1.1, 4.2.3.3.1.2 i 4.2.3.3.1.3. iz Dijela A, Indeks 77 TSI CCS.
Skup karakteristika sa kojima su vozna sredstva usklađena se unosi u registar voznih sredstava kako je definisano u tački 4.8 ovog Priloga.
Karakteristike željezničkih voznih sredstava bitne za usklađenost sa sistemom detekcije voza zasnovanog na šinskim strujnim kolima:
-
Geometrija vozila - Maksimalno rastojanje između dvije uzastopne osovine je navedeno u specifikaciji iz odredbe 3.1.2 u Aneksu A, Indeks 77 TSI CCS (razdaljina ,,ai" na slici 1).
- Maksimalno rastojanje između kraja odbojnika i prve osovine je navedeno u specifikaciji iz odredbe 3.1.2 u Dijelu A, Indeks 77 TSI CCS (razdaljina ,,b1" na slici 1).
-
Konstrukcija vozila - Minimalno osovinsko opterećenje u svim uslovima opterećenja je navedeno u specifikaciji iz odredbe 3.1.7. u Dijelu A, Indeks 77 TSI CCS.
- Električni otpor između voznih površina naspramnih točkova osovinskog sklopa je naveden u
specifikaciji iz odredbe 3.1.9 u Dijelu A, Indeks 77 TSI CCS, kao i metod njegovog mjerenja.
- Za električne jedinice sa pantografom minimalna impedansa između pantografa i svakog
točka voza je otvoreno pitanje u specifikaciji iz odredbe 3.2.2. u Dijelu A, Indeks 77 TSI
CCS.
-
Emisije izolacionih materijala
-
Ograničenja korišćenja opreme za pjeskarenje data su u specifikaciji iz odredbe 3.1.4. u
Dijelu A, Indeks 77 TSI CCS.
-
Ograničenja upotrebe kočnih papuča od kompozitnih materijala data su u specifikaciji iz
odredbe 3.1.6. u Dijelu A, Indeks 77 TSI CCS.
-
Elektromagnetna kompatibilnost (EMC)
-
Zahtjevi koji se odnose na elektromagnetnu kompatibilnost su otvorena pitanja u specifikaciji
iz odredaba 3.2.1. i 3.2.2. u Dijelu A, Indeks 77 TSI CCS.
-
Nivoi graničnih vrijednosti elektromagnetnih smetnji koje nastaju zbog struje vuče su
otvoreno pitanje u specifikaciji iz odredbe 3.2.2. u Dijelu A, Indeks 77 TSI CCS.
Karakteristike voznih sredstava bitne za usklađenost sa sistemom za detekciju voza zasnovanom na brojačima osovina (odredba 4.2.3.3.1.2)
-
Geometrija vozila
-
Maksimalno rastojanje između dvije uzastopne osovine je navedeno u specifikaciji iz odredbe
3.1.2. u Dijelu A, Indeks 77 TSI CCS.
-
Minimalno rastojanje između dvije uzastopne osovine voza je navedeno u specifikaciji iz
odredbe 3.1.2 u Dijelu A, Indeks 77 TSI CCS.
-
Na kraju jedinice predviđene za kvačenje, minimalno rastojanje između krajnje i prve osovine
jedinice je polovina vrijednosti navedena u specifikaciji iz odredbe 3.1.2, Indeks 77 TSI CCS.
-
Maksimalno rastojanje između krajnje i prve osovine je navedeno u specifikaciji iz odredbe
3.1.2. u Dijelu Indeks 77 A TSI CCS (razdaljina ,,b1" na slici 1).
-
Minimalno rastojanje između krajnjih osovina jedinice je navedeno u specifikaciji iz odredbe
3.1.2. u Aneksu A, Indeks 77 TSI CCS.
-
Geometrija točka
-
Geometrija točka navedena je u odredbi 4.2.3.5.2.2. postojeće TSI.
-
Minimalni prečnik točka (zavisan od brzine) je naveden u specifikaciji iz odredbe 3.1.3. u
Dijelu A, Indeks 77 TSI CCS.
-
Konstrukcija vozila
-
Bezmetalni prostor oko točkova je otvoreno pitanje u specifikaciji iz odredbe 3.1.3.5. u Dijelu
A, Indeks 77 TSI CCS.
-
Karakteristike materijala za točkove u vezi sa magnetnim poljem su navedene u specifikaciji
iz odredbe 3.1.3.6. u Dijelu A, Indeks 77 TSI CCS.
-
EMC
-
Zahtjevi koji se odnose na elektromagnetnu kompatibilnost su navedeni u specifikaciji iz
odredaba 3.2.1. i 3.2.2. u Dijelu A, Indeks 77 TSI CCS.
-
Nivoi graničnih vrijednosti elektromagnetnih smetnji koje nastaju zbog elektromagnetnih
šinskih kočnica ili kočnica sa vrtložnim strujama su otvoreno pitanje u specifikaciji iz
odredbe 3.2.2. u Dijelu A, Indeks 77 TSI CCS.
Karakteristike voznih sredstava bitne za usklađenost sa opremom petlje (odreba 4.2.3.3.1.3):
-
Konstrukcija vozila Metalna masa vozila je otvoreno pitanje u specifikaciji iz odredbe 3.1.7.2. u Dijelu A, Indeks 77 TSI CCS
Interfejs sa podsistemom kontrole, upravljanje i signalizacije
Upućivanje na TSI LOC & PAS za konvencionalnu željeznicu
Upućivanje na TSI CCS
Parametar
Odredba
Parametar
Odredba Karakteristike voznih sredstava usklađene sa sistemom detekcije voza zasnovanom na šinskim strujnim kolima
4.2.3.3.1.1
Geometrija vozila
Konstrukcija vozila
Emisije izolacionih materijala
EMC
Upućuje se na
specifikacije navedene u
Dijelu A, Indeks 77 TSI
CCS
Karakteristike voznih sredstava usklađene sa sistemom detekcije voza zasnovanom na brojačima osovina
4.2.3.3.1.2
Geometrija vozila
Geometrija točkova
Konstrukcija vozila EMC
Upućuje se na
specifikacije navedene u
Dijelu A, Indeks 77 TSI
CCS Karakteristike voznih sredstava usklađene sa opremom petlje
4.2.3.3.1.3
Konstrukcija vozila
Upućuje se na
specifikacije navedene u
Dijelu A, Indeks 77 TSI
CCS Komanda za brzo kočenje
4.2.4.4.1
Funkcionalnost sistema
ETCS u vozilu
4.2.2
Performansa brzog kočenja
4.2.4.5.2
Garantovana performansa
kočenja voza i karakteristike
4.2.2
Spoljašnja vidljivost
4.2.9.1.3
Vidljivost pružnih objekata za
upravljanje i kontrolu
4.2.15
4.4.
Operativna pravila
Operativna pravila za željezničke saobraćajne usluge sa ERTMS/ETCS su navedena u TSI
odvijanja i upravljanja saobraćajem.
4.5.
Pravila održavanja
Pravila održavanja podsistema obuhvaćenih ovom TSI obezbjeđuju da se vrijednosti navedene u
osnovnim parametrima iz Poglavlja 4 održe u zahtjevanim granicama tokom životnog vijeka ovih
podsistema. Međutim, tokom preventivnog ili korektivnog održavanja, podsistem možda neće biti
u stanju da postigne vrijednosti navedene u osnovnim parametrima; pravila održavanja
obezbjeđuju da se ne ugrozi bezbjednost tokom ovih aktivnosti.
Lice zaduženo za podsisteme kontrole, upravljanja i signalizacije uspostavlja pravila održavanja
da bi se postigli gore navedeni ciljevi. Kao pomoć pri pripremi ovih pravila, moraju se ispunjavati
sledeći zahtjevi.
4.5.1. Odgovornost proizvođača opreme
Proizvođač opreme ugrađene u podsistem ima obavezu da navede:
1. sve zahtjeve i postupke održavanja (uključujući i praćenje pravilnog funkcionisanja, dijagnozu
događaja, metode i alate za ispitivanja, kao i stručnu osposobljenost) neophodne za postizanje
osnovnih zahtjeva i vrijednosti navedenih u obaveznim zahtjevima ove TSI kroz čitav životni
vijek opreme (transport i skadištenje prije ugradnje, normalan rad, otkazi, popravke, kontrola i
održavanje, stavljanje van upotrebe, itd.);
2. rizike po zdravlje i bezbjednost javnosti i osoblja angažovanog na održavanju;
3. za održavanje na licu mjesta, t.j. definisanje standardnih zamenljivih jedinica (LRU), definisanje
odobrenih usklađenih verzija hardvera i softvera, postupke za zamjenu LRU koje su u kvaru,
uslove za skladištenje LRU i popravku onih LRU koje su u kvaru;
4. provjere koje treba izvršiti ukoliko je oprema podložna izuzetnom opterećenju (npr. nepovoljni
uslovi okruženja ili neuobičajeni udari);
5. provjere koje treba sprovesti prilikom održavanja opreme koja nije dio opreme za kontrolu,
upravljanje i signalizaciju, a koja utiče na podsisteme kontrole, upravljanja i signalizacije (npr.
promjena prečnika točka).
4.5.2. Odgovornost podnosioca zahtjeva za verifikaciju podsistema
Podnosilac zahtjeva ima obavezu da:
1. obezbjedi da zahtjevi održavanja kako su opisani u Odjeljku 4.5.1. (Odgovornost proizvođača
opreme) budu definisani za sve komponente u okviru područja primjene ove TSI, bez obzira na to
da li su to činioci interoperabilnosti ili ne;
2. ispuni gore navedene zahtjeve uzimajući u obzir rizike koji nastaju zbog interakcija između
različitih komponenti podsistema i interfejsa sa drugim podsistemima.
4.6.
Stručna ospososbljenost
Proizvođači opreme i podsistema obezbjeđuju dovoljno informacija za definisanje stručne
osposobljenosti koja se zahtjeva za ugradnju, završnu inspekciju i održavanje podsistema kontrole,
upravljanja i signalizacije u skladu sa Odjeljkom 4.5. (Pravila održavanja).
4.7.
Zdravstveni i bezbjednosni uslovi
Mora se voditi računa o zdravlju i bezbjednosti osoblja angažovanog na održavanju i radu, u skladu
sa propisima EU i nacionalnim propisima koji su usklađeni sa evropskim zakonodavstvom.
Proizvođači imaju obavezu da naznače rizike po zdravlje i bezbjednost koji proizilaze iz korišćenja
i održavanja njihove opreme i podsistema u skladu sa Odjeljkom 4.4. (Operativna pravila) i
Odjeljkom 4.5 (Pravila održavanja).
4.8.
Registri
Podaci koje treba obezbjediti za register su definisani propisima o interoperabilnosti željezničkog
sistema.
5.
ČINIOCI INTEROPERABILNOSTI
5.1.
Definicija
Činioci interoperabilnosti su "svaka osnovna komponenta, grupa komponenata, pod-sklop ili
kompletan sklop opreme ugrađen ili planiran za ugradnju u podsistem, od koga direktno ili
indirektno zavisi interoperabilnost željezničkog sistema. Koncept činilaca obuhvata materijalne
objekte kao i nematerijalne kao što je softver.ˮ
5.2.
Lista činilaca interoperabilnosti
5.2.1. Osnovni činioci interoperabilnosti
Osnovni činioci interoperabilnosti u podsistemima kontrole, upravljanja i signalizacije definisani su
u:
1. Tabeli 5.1.a za podsistem kontrole, upravljanja i signalizacije u vozilu;
2. Tabeli 5.2.a za pružni podsistem kontrole, upravljanja i signalizacije.
5.2.2. Grupisanje činilaca interoperabilnosti
Funkcije osnovnih činilaca interoperabilnosti mogu se kombinovati da čine grupu. Ova grupa se
dalje definiše prema tim funkcijama i prema svojim preostalim eksternim interfejsima. Ukoliko se
grupa formira na ovaj način, ona se smatra činiocem interoperabilnosti.
1. Tabela 5.1.b navodi grupe činilaca interoperabilnosti za podsistem kontrole, upravljanja i
signalizacije u vozilu.
2. Tabela 5.2.b navodi grupe činilaca interoperabilnosti za pružni podsistem kontrole, upravljanja i
signalizacije.
5.3.
Performanse i specifikacije činilaca
Za svaku osnovnu grupu činilaca interoperabilnosti tabele u Poglavlju 5 opisuju:
1. U koloni 3, funkcije i interfejse. Obratiti pažnju na to da neki činioci interoperabilnosti imaju
funkcije i/ili interfejse koji su izborni;
2. U koloni 4, obavezne specifikacije za ocjenu usaglašenosti svake funkcije ili interfejsa (po
potrebi) upućivanjem na relevantni odjeljak poglavlja 4.
Tabela 5.1.a
Osnovni činioci interoperabilnosti u podsistemu kontrole, upravljanja i signalizacije u vozilu
Br.
Činilac interoperabilnosti IC
Karakteristike
Specifičn i
zahtjevi
koje treba
ocjeniti
prema
Poglavlju 4
1.
ERTMS/ETCS u vozilu
Pouzdanost, raspoloživost, mogućnost održavanja, bezbjednost
(RAMS)
4.2.1
4.5.1
Funkcionalnost sistema ETCS u vozilu (isključujući mjerenje
brzine i pređenog puta )
4.2.2
Interfejsi vazdušnog međuprostora ERTMS/ETCS i GSM-R
4.2.5
- RBC (nivoi 2 i 3)
4.2.5.1
- Jedinica radio in-fill (izborno, nivo 1)
4.2.5.1
- Vazdušni međuprostor Eurobalize
4.2.5.2
- Vazdušni međuprostor Europetlje (izborno, nivo 1)
4.2.5.3
Interfejsi
- STM (ugradnja interfejsa K izborno)
4.2.6.1
- ERTMS/ETCS GSM-R u vozilu
4.2.6.2
- Mjerenje brzine i pređenog puta
4.2.6.3
- Sistem upravljanja ključevima
4.2.8
- Upravljanje ETCS-ID
4.2.9
- ERTMS/ETCS DMI interfejs mašinovođa - voz
4.2.12
- Interfejs voza
4.2.2
- Uređaj za beleženje u vozilu
4.2.14
Fizički uslovi okruženja
4.2.16
2
Oprema za mjerenje brzine i
pređenog puta
Pouzdanost, raspoloživost, mogućnost održavanja, bezbjednost
(RAMS)
4.2.1
4.5.1
Funkcionalnost sistema ERTMS/ETCS u vozilu: samo mjerenje
brzine i pređenog puta
4.2.2
Interfejsi
- ERTMS/ETCS u vozilu
4.2.6.3
Uslovi okruženja
4.2.16
3
Interfejs eksternog
STM
Interfejsi
4.2.6.1
- ERTMS/ETCS u vozilu
4
Kabinski radio GSM-R za govornu
komunikaciju NapomenaIM
kartica, antena, priključni kablovi i
filteri nisu dio ovog činioca
interoperabilnosti
Pouzdanost, raspoloživost, mogućnost održavanja, bezbjednost
(RAMS)
4.2.1
Napomena: Nema bezbjednosnih zahtjeva
4.5.1
Osnovne komunikacione funkcije
4.2.4.1
Primjena za govornu i operativnu komunikaciju
4.2.4.2
Interfejsi
- vazdušni međuprostor GSM-R
4.2.5.1
- GSM-R interfejs mašinovođa - voz
4.2.13
Uslovi okruženja
4.2.16
5
Uređaj GSM-R samo za za ETCS
podatke Napomena: SIM kartica,
antena, priključni kablovi i filteri
nisu dio ovog činioca
interoperabilnosti
Pouzdanost, raspoloživost, mogućnost održavanja, bezbjednost
(RAMS)
4.2.1
Napomena: nema bezbjednosnih zahtjeva
4.5.1
Osnovne komunikacione funkcije
4.2.4.1
Primjena za prenos podataka za ETCS
4.2.4.3
Interfejsi
- ERTMS/ETCS u vozilu
4.2.6.2
- vazdušni međuprostor GSM-R
4.2.5.1
Uslovi okruženja
4.2.16
6
GSM-R SIM kartica
Osnovne komunikacione funkcije
4.2.4.1
Uslovi okruženja
4.2.16
Tabela 5.1.b
Grupe činilaca interoperabilnosti u podsistemu kontrole, upravljanje i signalizacije u vozilu
Ova tabela je jedan primjer na kome se prikazuje struktura. Dozvoljene su i druge grupe.
Br.
Grupa
činilaca
interoperabiln osti
Karakteristike
Specifični zahtjevi
koje treba ocjeniti
upućivanjem na
Poglavlje 4
1.
ERTMS/ETCS u
vozilu
Oprema za
mjerenje brzine i
pređenog puta
Pouzdanost, raspoloživost, mogućnost održavanja,
bezbjednost (RAMS)
4.2.1
4.5.1
Funkcionalnost sistema ERTMS/ETCS u vozilu
4.2.2
Interfejsi vezdušnog međuprostora ERTMS/ETCS i GSM- R
4.2.5
- RBC (nivoi 2 i 3)
4.2.5.1
- Jedinica radio in-fill (izborno nivo 1)
4.2.5.1
- Vazdušni međuprostor Eurobalize
4.2.5.2
- Vazdušni međuprostor Europetlje (izborno, nivo 1)
4.2.5.3
Interfejsi
- STM (ugradnja interfejsa K izborno)
4.2.6.1
- ERTMS/ETCS
- GSM-R u vozilu
4.2.6.2
- Sistem upravljanja ključevima
4.2.8
- Upravljanje ETCS-ID
4.2.9
- ERTMS/ETCS interfejs mašinovođa - voz
4.2.12
- Interfejs voza
4.2.2
- Uređaj za beleženje u vozilu
4.2.14
Fizički uslovi okruženja
4.2.16
Tabela 5.2.a
Osnovni činioci interoperabilnosti pružnog podsistema kontrole, upravljanja i signalizacije
Br.
Činilac
interoperabilnosti IC
Karakteristike
Specifični zahtjevi
koji se ocjenjuju
upućivanjem na
Poglavlje 4
1.
RBC
Pouzdanost, raspoloživost, mogućnost održavanja,
bezbjednost (RAMS)
4.2.1
4.5.1
Funkcionalnost pružnog sistema ERTMS/ETCS
(isključujući komunikaciju preko Eurobalize,
jedinice radio in-fill i Europetlje)
4.2.3
Interfejsi vazdušnog međuprostora ERTMS/ETCS i
GSM-R: samo radio komunikacija sa vozom
4.2.5.1
Interfejsi
- Susedni RBC
4.2.7.1, 4.2.7.2
- Pružni ERTMS/ETCS - GSM-R
4.2.7.3
- Sistem upravljanja ključevima
4.2.8
- Upravljanje ETCS-ID
4.2.9
Uslovi okruženja
4.2.16
2
Jedinica radio in-fill
Pouzdanost, raspoloživost, mogućnost održavanja,
bezbjednost (RAMS)
4.2.1
4.5.1
Funkcionalnost pružnog sistema ERTMS/ETCS
(isključujući komunikaciju preko Eurobaliza,
Europetlje i funkcionalnost nivoa 2/3)
4.2.3
Interfejsi vazdušnog međuprostora ERTMS/ETCS i
GSM-R: samo radio komunikacija sa vozom
4.2.5.1
Interfejsi
- Pružni ERTMS/ETCS - GSM-R
- Sistem upravljanja ključevima
- Upravljanje ETCS-ID
- Postavnica i LEU
4.2.7.3
4.2.8\
4.2.9
4.2.3
Uslovi okruženja
4.2.16
3
Eurobaliza
Pouzdanost, raspoloživost, mogućnost održavanja,
bezbjednost (RAMS)
4.2.1
4.5.1
Interfejsi vazdušnog međuprostora ERTMS/ETCS i GSM-R: komunikacija sa vozom samo preko Eurobalize
4.2.5.2
Interfejsi
- LEU - Eurobaliza
Uslovi okruženja
4.2.16
4
Europetlja
Pouzdanost, raspoloživost, mogućnost održavanja,
bezbjednost (RAMS)
4.2.1
4.5.1
Interfejsi vazdušnog međuprostora
ERTMS/ETCS i GSM-R: komunikacija sa vozom samo
preko Europetlje
4.2.5.3
Interfejsi
- LEU - Europetlja
4.2.7.5
Uslovi okruženja
4.2.16
5
LEU - Eurobaliza
Pouzdanost, raspoloživost, mogućnost održavanja,
bezbjednost (RAMS)
4.2.1
4.5.1
Funkcionalnost pružnog sistema ERTMS/ETCS
(isključujući komunikaciju preko jedinice radio in- fill,
Europetlje i funkcionalnost nivoa 2 i 3)
4.2.3
Interfejsi
4.2.7.4
- LEU - Eurobaliza
Uslovi okruženja
4.2.16
6
LEU - Europetlja
Pouzdanost, raspoloživost, mogućnost održavanja,
bezbjednost (RAMS)
4.2.1
4.5.1
Funkcionalnost pružnog sistema ERTMS/ETCS
(isključujući komunikaciju preko jedinice radio in- fill,
Eurobalize i funkcionalnost nivoa 2 i 3)
4.2.3
Interfejsi
4.2.7.5
- LEU - Europetlja
Uslovi okruženja
4.2.16
Tabela 5.2.b
Grupe činilaca interoperabilnosti u pružnom podsistemu kontrole, upravljanja i signalizacije
Br.
Grupa činilaca
interoperabilnos ti
Karakteristike
Specifični
zahtjevi koji se
ocjenjuju
upućivanjem na
Poglavlje 4
1
Eurobaliza LEU -
Eurobaliza
Pouzdanost, raspoloživost, mogućnost održavanja,
bezbjednost (RAMS)
4.2.1
4.5.1
Funkcionalnost pružnog sistema ERTMS/ETCS
(isključujući komunikaciju preko Europetlje i
funkcionalnost nivoa 2 i 3)
4.2.3
Interfejsi vazdušnog međuprostora ERTMS/ETCS i GSM-R:
komunikacija sa vozom samo preko Eurobalize
4.2.5.2
Uslovi okruženja
4.2.16
2
Europetlja LEU -
Europetlja
Pouzdanost, raspoloživost, mogućnost održavanja,
bezbjednost (RAMS)
4.2.1
4.5.1
Funkcionalnost pružnog sistema ERTMS/ETCS
(isključujući komunikaciju preko Eurobalize i
funkcionalnost nivoa 2 i 3)
4.2.3
Interfejsi vazdušnog međuprostora ERTMS/ETCS i GSM-R:
komunikacija sa vozom samo preko Europetlje
4.2.5.3
Uslovi okruženja
4.2.16
6.
OCJENjIVANjE USAGLAŠENOSTI I/ILI POGODNOSTI ZA UPOTREBU ČINILACA I VERIFIKOVANjE PODSISTEMA
6.1.
Uvod
6.1.1. Opšta načela
Ispunjavanje osnovnih zahtjeva utvrđenih u Poglavlju 3 ovog Priloga obezbjeđuje se
usaglašavanjem sa osnovnim parametrima navedenim u Poglavlju 4 ovog Priloga.
Ova usaglašenost se dokazuje na sledeći način:
1. ocjenjivanjem usaglašenosti činilaca interoperabilnosti navedenih u Poglavlju 5 (Odjeljak 6.2);
2. verifikovanjem podsistema (Odjeljak 6.3).
Međutim, u određenim slučajevima neki od osnovnih zahtjeva mogu biti ispunjeni u skladu sa
nacionalnim propisima zbog:
1. korišćenja sistema Klase B;
2. otvorenih pitanja u TSI;
3. odstupanja u skladu sa propisima o interoperabilnosti željeznice;
4. specifičnih slučajeva opisanih u Odjeljku 7.2.9.
U pogledu provjere da li su ispunjeni osnovni zahtjevi kroz usklađenost sa osnovnim parametrima,
a ne dovodeći u pitanje obaveze navedene u poglavlju 7. ove TSI, činioci interoperabilnosti i
podsistemi kontrole, upravljanja i signalizacije kod kojih se ne primjenjuju sve funkcije,
performanse i kako je utvrđeno u Poglavlju 4 (uključujući specifikacije iz Dijela A), mogu dobiti
EZ sertifikate o usaglašenosti, odnosno EZ sertifikate o verifikaciji, pod sledećim uslovima za
izdavanje i korišćenje sertifikata:
1)
podnosilac zahtjeva za EZ verifikaciju pružnog podsistema kontrole, upravljanja i signalizacije
odgovoran je za odlučivanje o tome koje funkcije, radne karateristike i interfejse treba primjeniti
da bi se ispunili ciljevi usluge i obezbjedilo da se na podsisteme kontrole, upravljanja i
signalizacije u vozilu ne prenese nijedan zahtjev koji je u suprotnosti sa TSI ili ih nadmašuje;
2)
rad podsistema kontrole, upravljanja i signalizacije u vozilu, kod koga se ne primjenjuju sve
funkcije, performanse i interfejsi navedeni u ovoj TSI, može podleći određenim uslovima ili
ograničenjima zbog usklađenosti i/ili bezbjedne integracije sa pružnim podsistemima kontrole,
upravljanja i signalizacije;
3)
iz opravdanih razloga može se odbiti odobrenje za puštanje u rad ili postaviti uslove i
ograničenja za rad podsistema kontrole, upravljanja i signalizacije koji ne primjenjuju sve
funkcije, performanse i interfejse utvrđene u ovom Priloga.
Ako su osnovni zahtjevi ispunjeni ili ako se kod činioca interoperabilnosti ili podsistema kontrole,
upravljanja i signalizacije ne primjenjuju sve funkcije, performanse i interfejsi utvrđeni u ovoj TSI,
primjenjuju se odredbe odjeljka 6.4.2.
6.1.2. Načela za ispitivanje ERTMS/ETCS i GSM-R
Podsistem kontrole, upravljanja i signalizacije u vozilu obuhvaćen EZ deklaracijom o verifikaciji
treba da bude u mogućnosti da funkcioniše na svakom pružnom podsistemu kontrole, upravljanja i
signalizacije na koji se odnosi EZ deklaracija o verifikaciji, pod uslovima navedenim u ovoj TSI,
bez ikakvih dodatnih verifikacija.
Postizanje ovog cilja olakšava se na sljedeći način:
1. pravilima za projektovanje i ugradnju podsistema kontrole, upravljanja i signalizacije u vozilu
i pružnog podsistema kontrole, upravljanja i signalizacije;
2. specifikacijama za ispitivanje kojima se dokazuje da su podsistem kontrole, upravljanja i
signalizacije u vozilu i pružni podsistem zadovoljili zahtjeve ove TSI i međusobno su
usklađeni.
Da bi ocjena usaglašenosti opreme ERTMS/ETCS i GSM-R bila efikasnija i kako bi se pomoglo u
postizanju navedenog cilja, svaka država članica dostavlja Komisiji scenarije ispitivanja u radnim
uslovima provjeru ERTMS/ETCS i GSM-R djela pružnog podsistema kontrole, upravljanja i
signalizacije i njegove interakcije sa odgovarajućim djelom podsistema kontrole, upravljanja i
signalizacije u vozilu. Scenario za ispitivanje:
1. mora biti dosljedan sa specifikacijama iz ove TSI i mora da daje tehnički opis funkcija i
performansi (npr. vremena reakcije) kada su one od značaja za interakciju između pružnog
podsistema i posistema u vozilu;
2. mora da se dostavi u standardnom formatu.
3. mora obuhvatiti najmanje početak vožnje, prelaz između nivoa, prelaz između načina koji se
mogu koristiti na pruzi, glavne identifikovane situacije rada u otežanim uslovima, slanje hitnih
poruka i svaki drugi aspekt od značaja koji je specifičan za konkretnu prugu.
6.2.
Činioci interoperabilnosti
6.2.1. Postupci ocjene za činioce interoperabilnosti podsistema kontrole, upravljanja i signalizacije
Prije puštanja na tržište nekog činioca interoperabilnosti i/ili grupe činilaca interoperabilnosti
proizvođač ili njegov ovlašćeni zastupnik osnovan u Evropskoj uniji sastavlja EZ deklaraciju o
usaglašenosti u skladu sa propisom o interoperabilnosti željeznice i Zakonom.
Postupak ocjene obavlja se korišćenjem jednog od modula (Moduli za činioce interoperabilnosti za
kontrolu, upravljanje i signalizaciju).
EZ deklaracija o pogodnosti za upotrebu ne zahtjeva se za činioce interoperabilnosti za kontrolu,
upravljanje i signalizaciju, zbog toga što oni u potpunosti moraju da budu u skladu sa svim
relevantnim osnovnim parametrima. Ova usaglašenost se iskazuje deklaracijom o usaglašenosti i
dovoljna je za njihovo puštanje na tržište1.
6.2.2. Moduli za činioce interoperabilnosti za kontrolu, upravljanje i signalizaciju
Za ocjenjivanje činilaca interoperabilnosti u podsistemima kontrole, upravljanja i signalizacije,
proizvođač ili njegov ovlašćeni zastupnik osnovan u Evropskoj uniji, može odabrati:
1. postupak ispitivanja tipa (modul CB) za fazu projektovanja i razvoja u kombinaciji sa
1 provjeravanje da se činilac interoperabilnosti pravilno koristi je dio sveukupne EZ verifikacije podsistema kontrole, upravljanja i signalizacije na pruzi i u vozilu, kako je objašnjeno u 6.3.3. i 6.3.4.
postupkom upravljanja kvalitetom proizvodnje (modul CD) za fazu proizvodnje; ili
2. postupak ispitivanja tipa (modul CB) za fazu projektovanja i razvoja u kombinaciji sa postupkom
verifikacije proizvoda (modul CF); ili
3. potpuni sistem upravljanja kvalitetom sa postupkom pregleda projekta (modul CH1).
Pored toga, za provjeru činioca interoperabilnosti - SIM kartice, proizvođač ili njegov zastupnik
mogu odabrati modul CA.
Sledeća pojašnjenja se primjenjuju na upotrebu nekih modula:
1. pozivanjem na Poglavlje 2 ,,Modul CB", EZ ispitivanje tipa mora se obaviti kombinacijom tipa
proizvodnje i tipa projektovanja;
2. pozivanjem na Poglavlje 3. ,,Modul CF" (verifikacija proizvoda) statistička verifikacija nije
dozvoljena, t.j. svi činioci interoperabilnosti moraju biti pojedinačno ispitani.
6.2.3. Zahtjevi za ocjenu
Nezavisno od odabranog modula:
1. zahtjevi navedeni u Odjeljku 6.2.4.1 ove TSI moraju biti ispunjeni za činilac interoperabilnosti
,,ERTMS/ETCS u vozilu";
2. aktivnosti prikazane u tabeli 6.1 obavljaju se prilikom ocjene usaglašenosti činioca
interoperabilnosti ili grupe činilaca interoperabilnosti kako je definisano u Poglavlju 5 ove TSI.
Sve verifikacije se obavljaju prema tabeli u Poglavlju 5 i osnovnim parametrima koji su tamo
naznačeni.
Tabela 6.1
Aspekt
Šta se ocjenjuje
propratni dokazi
Funkcije, interfejsi i performanse
Provjeriti da li su izvedene sve
obavezne funkcije, performanse i svi
interfejsi kako je opisano u
osnovnim parametrima na koje se
upućuje u relevantnoj tabeli u
Poglavlju 5 i da li su svi usaglašeni
sa zahtjevima ove TSI.
Projektna dokumentacija i izvođenje
primjera i scenarija ispitivanja, kako je
opisano u osnovnim parametrima na koje se
upućuje u relevantnoj tabeli u Poglavlju 5
Provjeriti koje su izborne funkcije i
interfejsi sprovedeni, kako je opisano u
osnovnim parametrima na koje se
upućuje u relevantnoj tabeli u
Poglavlju 5 i da li su svi usaglašeni sa
zahtjevima ove TSI.
Provjeriti koje su dodatne funkcije i
dodatni interfejsi (koji nisu navedeni u
ovoj TSI) sprovedeni a da nisu u
suprotnosti sa sprovedenim funkcijama
navedenim u ovoj TSI
Provjeriti usaglašenost sa obaveznim
uslovima okruženja, kad je to
navedeno u osnovnim parametrima na
koje se upućuje u relevantnoj tabeli u
Poglavlju 5
Pored toga, provjeriti da činilac
interoperabilnosti funkcioniše ispravno
u uslovima okruženja za koje je
projektovan Pouzdanost, raspoloživost, mogućnost održavanja, bezbjednost (RAMS)
Provjeriti usaglašenost sa
bezbjednosnim zahtjevima, kad je to
navedeno u osnovnim parametrima
na koje se upućuje u relevantnoj
tabeli u Poglavlju 5
1.
poštovati
kvantitativne
prihvatljive
stope
rizika
(THR) koji su uzrokovani
slučajnim otkazima;
2
razvojni proces je u
mogućnosti da detektuje i eliminiše
sistematske otkaze
1. Izračunavanje THR koji su uzrokovani
slučajnim otkazima na osnovu izvora
dokazivih podataka o pouzdanosti .
2.1 Proizvođačevo upravljanje kvalitetom
i bezbjednošću preko projekta,
proizvodnje i ispitivanja usklađeno je sa
priznatim standardom (vidjeti napomenu).
2.2 Razvojni ciklusi softvera i hardvera i
integrisanje softvera i hardvera su
preduzeti u skladu sa priznatim
standardom (vidjeti napomenu).
2.3. Postupak verifikacije i validacije
bezbjednosti preduzet je u skladu sa
priznatim standardom (vidjeti
napomenu) i uz poštovanje
bezbjednosnih zahtjeva opisanih u
osnovnim parametrima na koje se
upućuje u relevantnoj tabeli u
Poglavlju 5.
2.4 Zahtjevi funkcionalne i tehničke
bezbjednosti (ispravno funkcionisanje u
uslovima bez kvarova, efekti kvarova i
spoljni uticaj) provjeravaju se u skladu sa
priznatim standardom (vidjeti napomenu).
Napomena: Standard mora zadovoljiti najmanje
sledeće zahtjeve:
1. mora da bude opšte priznat u domenu
željeznice.Ukoliko ovo ne bude slučaj,
standard se mora obrazložiti i biti prihvaćen
od strane notifikovanog tijela;
2. mora da bude od značaja za kontrolu
razmatranih rizika u sistemu koji se ocjenjuje;
3. mora biti javno dostupan svim akterima
koji želje da ga koriste u skladu sa Dijelom A
tabelu A 3.
Provjeriti da je zadovoljen
kvantitativni cilj pouzdanosti
naznačen od strane podnosioca
zahtjeva
Proračuni
Provjeriti usaglašenost sa zahtjevima
održavanja - Odjeljak 4.5.1
Provjera dokumenata
6.2.4. Posebna pitanja
6.2.4.1. ERTMS/ETCS u vozilu
Posebna pažnja se posvećuje ocjeni usaglašenosti činioca interoperabilnosti "ERTMS/ETCS u
vozilu", budući da je složen a igra ključnu ulogu u postizanju interoperabilnosti.
Bez obzira na to da li je odabran modul CB ili CH1, notifikovano tijelo provjerava da je uzorak
činioca interoperabilnosti prošao kroz potpuni niz obaveznih ispitivanja na koja se upućuje u
Odjeljku 4.2.2. (funkcionalnost ERTMS/ETCS u vozilu) i da su ova ispitivanja sprovedena u
laboratoriji akreditovanoj za vršenje ovakvih ispitivanja.
Pored toga, kako bi se povećala pouzdanost da ERTMS/ETCS u vozilu može ispravno
funkcionisati sa različitim aplikacijama na pruzi, preporučuje se da se ERTMS/ETCS ispita uz
korišćenje scenarija iz baze podataka a što nije dio obaveznih specifikacija za ispitivanje, prema
Odjeljku 6.1.2 (Načela ispitivanja ERTMS/ETCS i GSM-R). U dokumentima koja se prilažu uz
sertifikat naznačavaju se scenariji baze podataka u odnosu na koje je ispitan konkretni činilac
interoperabilnosti.
6.2.4.2. Specifični prenosni modul (STM)
Verifikacija interfejsa STM sa ERTMS/ETCS u vozilu zahtjeva ocjenu usaglašenosti koju obavlja
notifikovano tijelo.
6.2.4.3. Sadržaj EZ deklaracije o usaglašenosti
EZ Deklaracija o usaglašenosti koja je navedena u propisima o interoperabilnosti željeznice
obuhvata sledeće detalje o činiocu interoperabilnosti:
1. koje su izborne i dodatne funkcije primjenjene;
2. primjenljive uslove okruženja.
6.3.
Podsistemi kontrole, upravljanja i signalizacije
6.3.1. Postupci ocjene za podsisteme kontrole, upravljanja i signalizacije
Na zahtjev podnosioca notifikovano tijelo obavlja EZ verifikaciju podsistema kontrole, upravljanja
i signalizacije u vozilu ili pružnog podsistema u skladu sa propisom o interoperabilnosti željeznice.
Podnosilac zahtjeva sastavlja EZ deklaraciju o verifikaciji podsistema kontrole, upravljanja i
signalizacije u vozilu ili pružni podsistem u skladu sa propisom o interoperabilnosti željeznice.
Sadržaj EZ deklaracije o verifikaciji mora biti u skladu sa propisom o interoperabilnosti željeznice.
Postupci ocjene se vrše uz upotrebu jednog od modula (Moduli za podsisteme kontrole, upravljanja
i signalizacije).
Deklaracije EZ o verifikaciji za podsistem kontrole, upravljanja i signalizacije u vozilu i za pružni
podsistem kontrole, upravljanja i signalizacije, zajedno sa sertifikatima o usaglašenosti smatraju se
dovoljnim da garantuju da su ovi podsistemi usklađeni pod uslovima navedenim u ovoj TSI.
6.3.2. Moduli za podsisteme kontrole, upravljanja i signalizacije
6.3.2.1. Podsistem u vozilu
Za verifikovanje podsistema kontrole, upravljanja i signalizacije u vozilu, podnosilac zahtjeva može
odabrati ili:
1. postupak ispitivanja tipa (modul SB) za fazu projektovanja i razvoja u kombinaciji sa postupkom
upravljanja kvalitetom proizvodnje (modul SD) za fazu proizvodnje; ili
2. postupak ispitivanja tipa (modul SB) za fazu projektovanja i razvoja u kombinaciji sa postupkom
verifikacije proizvoda (modul SF); ili
3. potpuni sistem upravljanja kvalitetom sa postupkom pregleda projekta (modul SH1).
6.3.2.2. Pružni podsistem
Za verifikovanje pružnog podsistema kontrole, upravljanja i signalizacije, podnosilac zahtjeva može
odabrati:
1. postupak verifikacije jedinice (modul SG), ili
2. postupak ispitivanja tipa (modul SB) za fazu projektovanja i razvoja u kombinaciji sa
postupkom upravljanja kvalitetom proizvodnje (modul SD) za proizvodnu fazu; ili
3. postupak ispitivanja tipa (modul SB) za fazu projektovanja i razvoja u kombinaciji sa
postupkom verifikacije proizvoda (modul SF); ili
4. potpuni sistem upravljanja kvalitetom sa postupkom pregleda projekta (modul SH1).
6.3.2.3. Uslovi za korišćenje modula za podsisteme u vozilu i na pruzi
Pozivanjem na modul SB (ispitivanje tipa), zahtjeva se razmatranje projekta.
Pozivanjem na modul SH1 (potpuni sistem upravljanja kvalitetom sa pregledom projekta),
zahtjeva se testiranje tipa.
6.3.3. Zahtjevi za ocjenu podsistema u vozilu
Tabela 6.2 prikazuje provjere koje se moraju obaviti prilikom verifikovanja podsistema kontrole,
upravljanja i signalizacije u vozilu i osnovne parametre koji se moraju ispuniti.
Nezavisno od odabranog modula:
1. verifikacijom se dokazuje da je podsistem kontrole, upravljanja i signalizacije na vozilu
usaglašen sa osnovnim parametrima kada se ugrađuje u vozilo;
2. funkcionalnost i performanse činilaca interoperabilnosti već obuhvaćenih njihovom EZ
deklaracijom o usaglašenosti ne zahtjevaju nikakvu dodatnu verifikaciju.
Tabela 6.2
Aspekt
Šta se ocjenjuje
propratni dokazi
Korišćenje činilaca
interoperabilnosti
Provjeriti da li su činioci interoperabilnosti koje
treba ugraditi u podsistem svi obuhvaćeni EZ
deklaracijom o usaglašenosti i odgovarajućim
sertifikatom.
Postojanje i sadržaj dokumenata
Provjeriti ograničenja u korišćenju činilaca
interoperabilnosti u odnosu na karakteristike
podsistema i okruženja
Analiza provjerom dokumenata
Za činioce interoperabilnosti koji su dobili
sertifikat u skladu sa starijim verzijama TSI CCS,
provjeriti da taj sertifikat i dalje obezbjeđuje
usaglašenost sa zahtjevima trenutno važeće TSI.
Analiza uticaja provjerom
dokumenata
Integrisanje činilaca
interoperabilnosti u
podsistem
Provjeriti ispravnu ugradnju i funkcionisanje
internih interfejsa podsistema - Osnovni parametar
4.2.6
Provjere u skladu sa
specifikacijama
Provjeriti da dodatne funkcije (koje nisu
navedene u ovoj TSI) ne utiču na obavezne
Analiza uticaja
Provjeriti da li su vrijednosti ETCS ID u
dozvoljenom opsegu - osnovni parametri 4.2.6
Provjera specifikacija projekta
Integrisanje u vozna
sredstva
Provjeriti ispravnu ugradnju opreme - osnovni
parametri 4.2.2, 4.2.4, 4.2.14 i uslove za ugradnju
opreme, prema uputstvima proizvođača
Rezultati provjera (u skladu sa
specifikacijama na koje se upućuje u
osnovnim parametrima i sa propisima o
ugradnji koje sastavlja proizvođač)
Provjeriti da li je podsistem kontrole, upravljanja i
signalizacije u vozilu, usklađen sa okruženjem u
voznom sredstvu
Provjeriti dokumenta (sertifikati
činilaca interoperabilnosti i moguće
metode ugradnje provjerene u odnosu
na karakteristike voznih sredstava)
Aspekt
Šta se ocjenjuje
propratni dokazi
Provjeriti da su parametri (npr. parametri kočenja)
ispravno konfigurisani i da se kreću u
dozvoljenom opsegu
Provjeriti dokumenta (vrijednosti
parametara provjeriti u odnosu na
karakteristike voznih sredstava)
Integrisanje u Klasu B
Provjeriti da li je eksterni STM povezan sa
ERTMS/ETCS u vozilu preko interfejsa koji su
usaglašeni sa TSI
Ničeg nema za ispitivanje: postoji
standardni interfejs koji je već ispitan
na nivou činioca
interoperabilnosti.Njegovo
funkcionisanje je već ispitano
prilikom provjere integrisanja
činilaca interoperabilnosti u
podsistem
Provjeriti da li funkcije Klase B primjenjene u
ERTMS/ETCS u vozilu- osnovni parametar
4.2.6.1 - ne nameću dodatne zahtjeve za pružni
podsistem kontrole, upravljanja i signalizacije, kao
posledicu prelaza (sa jednog sistema na drugi)
Ničeg nema za ispitivanje: sve je već
ispitano na nivou činioca
interoperabilnosti
Provjeriti da li posebna oprema Klase B koja nije
povezana sa ERTMS/ETCS u vozilu- osnovni
parametar 4.2.6.1 - ne nameće dodatne zahtjeve
za pružni podsistem kontrole, upravljanja i
signalizacije, kao posljedicu prelaza
Ničeg nema za ispitivanje: Nema
interfejsa1
Provjeriti da li posebna oprema Klase B povezana
sa ERTMS/ETCS u vozilu koja koristi (djelimično)
interfejse koji nisu usaglašeni sa TSI- osnovni
parametar 4.2.6.1 - ne nameće dodatne zahtjeve za
pružni podsistem kontrole, upravljanja i
signalizacije, kao posledicu prelaza.Takođe
provjeriti da ERTMS/ETCS funkcije nisu ugrožene
Analiza uticaja
Integracija sa pružnim
podsistemima
kontrole, upravljanja i
signalizacije
Provjeriti da li se telegrami Eurobalize mogu
pročitati (obim ovog ispitivanja je ograničen na
provjeru toga da li je antena ispravno
ugrađena.Ispitivanja već obavljena na nivou
činioca interoperabilnosti ne treba da se
ponavljaju) - osnovni parametar 4.2.5
Ispitati uz upotrebu sertifikovane
Eurobalize: Mogućnost da se ispravno
pročita telegram je propratni dokazni
materijal.
Provjeriti da li se telegrami Europetlje
(ukoliko je primjenljivo) mogu pročitati -
osnovni parametar 4.2.5
Ispitati uz upotrebu sertifikovane
Europetlje: Mogućnost da se ispravno
pročita telegram je propratni dokazni
materijal.
Provjeriti da li oprema može podržati GSM-R za
prenos govora i podataka (ukoliko je primjenljivo)
- osnovni parametar 4.2.5
Ispitati uz upotrebu sertifikovane GSM-
R mreže:Mogućnost da se uspostavi,
održava i prekine veza je propratni
dokazni materijal.
Pouzdanost,
raspoloživost,
mogućnost
održavanja,
bezbjednost (RAMS)
Provjeriti da li je oprema usaglašena sa
bezbjednosnim zahtjevima - osnovni parametar 4.2.1
Primjena postupaka navedenih u
Zajedničkoj bezbjednosnoj metodi
Provjeriti da je zadovoljen kvantitativni cilj
pouzdanosti - osnovni parametar 4.2.1
Proračuni
Provjeriti usaglašenost sa zahtjevima održavanja
Provjera dokumenata
Integracija sa pružnim
podsistemima
kontrole, upravljanja i
signalizacije i drugim
podsistemima:
ispitivanja u radnim
uslovima
Ispitati ponašanje podsistema pod onoliko različitih
radnih uslova koliko je moguće (npr. nagib pruge,
brzina voza, vibracije, napon vuče, vremenski
uslovi, projekat funkcionalnosti pružnog
podsistema kontrole, upravljanja i signalizacije).
Ispitivanje mora biti u stanju da verifikuje:
1.
da se funkcije mjerenja brzine i pređenog
puta ispravno odvijaju - osnovni parametar
4.2.2
2.
da je podsistem kontrole, epravljanja i
signalizaciju u vozilu usklađen sa
okruženjem u voznom sredstvu - Osnovni
parametar 4.2.16
Ova ispitivanja moraju biti takva da povećaju
pouzdanost da neće doći do sistematskih
Izveštaji o toku ispitivanja.
Napomena: Navesti u sertifikatu koji
uslovi su ispitivani, koji standardi
primjenjeni i prema kojim
kriterijumima su ispitivanja smatrana
završenim
1 U ovom slučaju, ocjena upravljanja prelazima će se odvijati u skladu sa nacionalnim specifikacijama.
6.3.4. Zahtjevi za ocjenu pružnog podsisteme
Svrha ocjena izvršenih u okviru ove TSI je da verifikuje da je oprema usaglašena sa zahtjevima
navedenim u Poglavlju 4.
Međutim, za projektovanje djela koji se odnosi na ERTMS/ETCS pružnog podsistema kontrole,
upravljanja i signalizacije, potrebne su specifične informacije za primjenu. To uključuje:
1. karakteristike pruge kao što su nagibi, razdaljine, položaji elemenata trase i lokacije
Eurobaliza/Europetlji koje treba štititi itd;
2. podatke za signalizaciju i pravila kojima se bavi sistem ERTMS/ETCS.
Ova TSI ne obuhvata provjere za ocjenjivanje toga da li su informacije specifične za primjenu
ispravne. Nezavisno od odabranog modula:
1. Tabela 6.3 prikazuje provjere koje se moraju obaviti prilikom verifikovanja pružnog podsistema
kontrole, upravljanja i signalizacije i osnovne parametre koji se moraju poštovati;
2. funkcionalnosti i radne performanse koje su već ispitane na nivou činilaca interoperabilnosti ne
zahtjevaju dodatnu verifikaciju.
Tabela 6.3
Aspekt
Šta se ocjenjuje
propratni dokazi
Korišćenje činilaca
interoperabilnost i
Provjeriti da li su činioci interoperabilnosti koje treba
ugraditi u podsistem svi obuhvaćeni EZ deklaracijom o
usaglašenosti i odgovarajućim sertifikatom.
Postojanje i sadržaj dokumenata
Provjeriti ograničenja u korišćenju činilaca
interoperabilnosti u odnosu na karakteristike
podsistema i okruženja
Analiza uticaja provjerom
dokumenata
Za činioce interoperabilnosti koji su dobili
sertifikat u skladu sa starijim verzijama TSI CCS,
provjeriti da taj sertifikat i dalje obezbjeđuje
usaglašenost sa zahtjevima trenutno važeće TSI
Analiza uticaja poređenjem
specifikacija na koje se upućuje u
TSI i sertifikata činilaca
interoperabilnosti
Korišćenje
sistema za
detekciju voza
Provjeriti da li su odabrani tipovi usaglašeni sa
zahtjevima TSI CCS - osnovni parametri 4.2.10,
4.2.11
Provjera dokumenata
Integracija činilaca
interoperabilnost i u
podsistem
Provjeriti da li su interni interfejsi podsistema
propisno ugrađeni i da li funkcionišu ispravno -
osnovni parametri 4.2.5, 4.2.7
Provjere u skladu sa
specifikacijama
Provjeriti da dodatne funkcije (koje nisu
navedene u ovoj TSI) ne utiču na obavezne
Analiza uticaja
Provjeriti da li su vrijednosti ETCS ID u
Provjera specifikacija projekta
Aspekt
Šta se ocjenjuje
Propratni dokazi
otkaza.
Obim ovih ispitivanja isključuje ispitivanja koja
su već vršena u ranijim fazama:
ispitivanja vršena na činiocima interoperabilnosti i
ispitivanja vršena na podsistemu u simuliranoj
sredini moraju se uzeti u obzir.
Ispitivana u radnim uslovima nisu neophodna za
opremu za prenos govora GSM-R u vozilu.
Aspekt
Šta se ocjenjuje
propratni dokazi
dozvoljenom opsegu - osnovni parametri 4.2.9
Integracija sa
infrastrukturom
Provjeriti ispravnu ugradnju opreme - osnovni parametri
4.2.3, 4.2.4, i uslove ugradnje opreme, prema
uputstvima proizvođača
Rezultati provjera (u skladu sa
specifikacijama na koje se upućuje u
osnovnim parametrima i sa propisima o
ugradnji koje sastavlja proizvođač)
Provjeriti da li je pružni podsistem kontrole,
upravljanja i signalizacije usklađen sa okruženjem
Provjeriti dokumenta (sertifikate o
činiocima interoperabilnosti i moguće
metode integrisanja provjerenie u odnosu
na karakteristike pruge)
Integracija sa
pružnom
signalizacijom
Provjeriti da li su sve funkcije koje zahtjeva
aplikacija sprovedene u skladu sa
specifikacijama na koje upućuje ova TSI -
osnovni parametar 4.2.3
Provjera dokumenta (projektna
specifikacija podnosioca zahtjeva i
sertifikati činilaca interoperabilnosti)
Provjeriti da li je ispravna konfiguracija parametara
(telegrami Eurobalize, RBC poruke, položaj
oznaka. itd)
Provjera dokumenta (vrijednosti
parametara provjerene u odnosu na
karakteristike pružnih uređaja i
signalizacije)
Provjeriti da li su interfejsi ispravno ugrađeni i da li
funkcionišu po propisu.
Verifikacija projekta i ispitivanje u
skladu sa informacijama koje je
dostavio podnosilac zahtjeva
Provjeriti da li pružni podsistem kontrole,
upravljanja i signalizacije funkcioniše ispravno u
skladu sa informacijama na interfejsima sa
pružnom signalizacijom (npr. odgovarajuće
kreiranje telegrama Eurobalize od strane LEU ili
poruka od strane RBC)
Verifikacija projekta i ispitivanje u
skladu sa informacijama koje je
dostavio podnosilac zahtjeva
Integracija sa
podsistemima
kontrole,
upravljanja i
signalizacije u
vozilu i sa voznim
sredstvima
Provjeriti GSM-R pokrivanje - Osnovni parametar
4.2.4
Mjerenja na licu mesta
Provjeriti da li su sistemi za detekciju voza
usaglašeni sa zahtjevima ove TSI - Osnovni
parametar 4.2.10
Mjerenja na licu mesta
Provjeriti da li su sistemi za detekciju voza
usaglašeni sa zahtjevima ove TSI - Osnovni
parametri 4.2.10 i 4.2.11
Provjeriti dokaze sa postojećih
postrojenja (za sisteme koji su već u
upotrebi); obaviti ispitivanja u skladu
sa standardima za nove tipove
Provjeriti da li su sve funkcije koje zahtjeva primjena
sprovedene u skladu sa specifikacijama na koje
upućuje ova TSI - osnovni parametri 4.2.3, 4.2.4 i
4.2.5
Izvještaji o ispitivanjima radnih
scenarija navedenih u Odjeljku 6.1.2 sa
različitim sertifikovanim podsistemima
kontrole, upravljanja i signalizacije u
vozilu. Izvještaj naznačava koji su
radni scenariji bili ispitani, koja
oprema u vozilu je bila korišćena i da
li su ispitivanja obavljena u
laboratorijama, na ispitnim prugama ili
u stvarnim uslovima.
Pouzdanost,
raspoloživost,
mogućnost
održavanja,
bezbjednost (RAMS)
Provjeriti usaglašenost sa bezbjednosnim
zahtjevima - Osnovni parametar 4.2.1
Primjena postupaka navedenih u
Zajedničkoj bezbjednosnoj metodi
Provjeriti da su zadovoljeni kvantitativni ciljevi
pouzdanosti - Osnovni parametar 4.2.1
Proračuni
Provjeriti usaglašenost sa zahtjevima održavanja -
Odjeljak 4.5.2
Provjera dokumenata
Integracija sa podsistemima kontrole, upravljanja i signalizacije u vozilu i sa voznim sredstvima:
ispitivanja u radnim uslovima
Ispitati ponašanje posistema u onoliko različitih radnih
uslova koliko je realno moguće (npr. brzina voza, broj
vozova na pruzi, vremenski uslovi). Ispitivanje mora
biti u stanju da verifikuje:
1. performanse sistema za detekciju voza -
osnovni parametri 4.2.10, 4.2.11,
2. da je pružni podsistem kontrole, upravljanja i
signalizacije usklađen sa okruženjem pruge -
osnovni parametar 4.2.16
Izvještaji o toku ispitivanja.
Napomena:Navesti u sertifikatu koji
uslovi su ispitivani, koji standardi
primjenjeni i prema kojim kriterijumima
su ispitivanja smatrana završenim
Aspekt
Šta se ocjenjuje
propratni dokazi
Integracija sa
podsistemima
kontrole,
upravljanja i
signalizacije u
vozilu i sa voznim
sredstvima:
ispitivanja u radnim
uslovima
Ova ispitivanja će takođe povećati pouzdanost da neće
doći sistematskih otkaza.
Obim ovih ispitivanja isključuje ispitivanja koja su već
vršena u ranijim koracima: moraju se uzeti u obzir
ispitivanja vršena na nivou činilaca interoperabilnosti i
ispitivanja vršena na podsistemu u simuliranoj sredini.
Izvještaji o toku ispitivanja.
Napomena:Navesti u sertifikatu koji
uslovi su ispitivani, koji standardi
primjenjeni i prema kojim
kriterijumima su ispitivanja smatrana
završenim
6.4. Odredbe u slučaju djelimične ispunjenosti zahtjeva TSI
6.4.1. Ocjena delova podsistema kontrole, upravljanja i signalizacije
U skladu sa propisom o interoperabilnosti željeznice, notifikovano tijelo može izdati sertifikate o
verifikaciji za određene djelove podsistema ukoliko je to dopušteno prema relevantnoj TSI.
Kako je istaknuto u odjeljku 2.2. (Oblast primjene) ove TSI, pružni podsistem kontrole, upravljanja i
signalizacije sadrži tri dijela, dok podsistem kontrole, upravljanja i signalizacije u vozilu sadrži dva
dijela, i oni su navedeni u odjeljku 4.1 (Uvod).
Sertifikat o verifikaciji može se izdati za svaki dio naveden u ovoj TSI; notifikovano tijelo samo
provjerava da li taj određeni dio ispunjava zahtjeve TSI.
Bez obzira na to koji je modul odabran, notifikovano tijelo provjerava:
1)
da li su zahtjevi TSI za taj dio ispunjeni; i
2)
da li su zahtjevi TSI koji su već ocjenjeni za druge djelove istog podsistema i dalje
ispunjeni.
6.4.2. Djelimična ispunjenost zahtjeva podsistema kontrole, upravljanja i signalizacije zbog
ograničene primjene TSI
Ako su neki osnovni zahtjevi ispunjeni prema nacionalnim propisima, EZ sertifikat o usaglašenosti
činioca interoperabilnosti i EZ sertifikat o verifikaciji podsistema precizno upućuju na djelove ove
TSI čija je usaglašenost ocjenjena i djelove čija usaglašenost nije ocjenjena.
Ako se kod činioca interoperabilnosti ne primjenjuju sve funkcije, performanse i interfejsi navedeni u
ovoj TSI, EZ sertifikat o usaglašenosti može se izdati samo ako neprimjenjene funkcije, interfejsi ili
performanse nisu potrebni za integraciju činioca interoperabilnosti u podsistem prema upotrebi koju
je naveo podnosilac zahtjeva, kao što su:
a) ERTMS/ETCS interfejs sa STM u vozilu, ako je činilac interoperabilnosti namjenjen za ugradnju u vozila u kojima nije potreban spoljašnji STM;
b) RBC interfejs sa drugim RBC, ako je RBC namjenjen za upotrebu u aplikaciji za koju nisu predviđeni susjedni RBC.
EZ sertifikat o usaglašenosti (ili prateći dokumenti) činioca interoperabilnosti mora ispunjavati sve
sledeće zahtjeve:
a) navodi funkcije, interfejse ili performanse koji se ne primjenjuju;
b) sadrži dovoljno informacija da se omogući identifikovanje uslova pod kojima se činilac
interoperabilnosti može koristiti;
c) sadrži dovoljno informacija da se omogući identifikovanje uslova i ograničenja
korišćenja koji se primjenjuju na interoperabilnost podsistema u koji je taj činilac
ugrađen.
Ako podsistem kontrole, upravljanja i signalizacije ne primjenjuje sve funkcije, performanse i
interfejse iz ove TSI (npr. zbog toga što ih ne primjenjuje činilac interoperabilnosti koji je ugrađen u
njega), EZ sertifikat o verifikaciji navodi zahtjeve koji su ocjenjeni i odgovarajuće uslove i
ograničenja korišćenja podsistema kao i njegovu usklađenost sa drugim podsistemima.
6.4.3. Prelazna izjava o verifikaciji
Ako se ocjenjuje usaglašenost djelova podsistema koje je naveo podnosilac zahtjeva, a koji su
razlikuju od djelova dopuštenih prema odjeljku 4.1 (Uvod) ove TSI, ili ako su obavljene samo
određene faze postupka verifikacije, može se izdati samo prelazna izjava o verifikaciji.
7.
SPROVOĐENjE TSI KONTROLE, UPRAVLjANjA I SIGNALIZACIJE
7.1.
Uvod
Prilikom sprovođenja kontrole mora se uzeti u obzir činjenica da primjena jedne TSI povremeno
mora da se koordinira sa primjenom drugih TSI.
7.2.
Pravila sa opštom primjenom
7.2.1. Unapređenje ili obnavljanje pružnog podsistema kontrole i upravljanja ili njegovih djelova
Unapređenje ili obnavljanje pružnog podsistema kontrole, upravljanja i signalizacije može se
odnositi na bilo koji ili na sve sledeće aspekte:
1. zaštitu voza
2. radio komunikaciju
3. detekciju voza
Ovi različiti djelovi pružnog podsistema kontrole, upravljanja i signalizacije mogu se stoga
unaprijediti ili obnoviti zasebno ukoliko se pri tom ne ugrožava interoperabilnost. Radovi će se
odnositi na:
1. funkcije i interfejse GSM-R
2. funkcije i interfejse ERTMS/ETCS
3. usklađenost sistema za detekciju voza sa voznim sredstvima
7.2.2. Postojeći sistemi
Funkcionalnost postojećih sistema i njihovih interfejsa ostaje nepromjenjena, osim kada su
potrebne izmjene radi ublažavanja bezbjednosnih nedostataka u ovim sistemima.
7.2.3. Raspoloživost specifičnih prenosnih modula (STM)
Ukoliko pruge koje potpadaju pod područje primjene ove TSI nisu opremljene sistemima za zaštitu
voza Klase A, ulažu sr napore da obezbjede raspoloživost eksternog specifičnog prenosnog modula
(STM) za svoj postojeći sistem/sisteme zaštite voza Klase B.
U ovom kontekstu, dužna pažnja se mora posvetiti obezbjeđivanju otvorenog tržišta STM pod fer
komercijalnim uslovima.
7.2.4. Dodatna oprema Klase B na pruzi opremljenoj opremom Klase A
Na pruzi opremljenoj sa ERTMS/ETCS i/ili GSM-R, može se instalirati dodatna oprema Klase B,
kako bi se u toku prelazne faze omogućilo odvijanje saobraćaja voznim sredstvima koja nisu
kompatibilna sa Klasom A. Oprema Klase B može se koristiti u vozilu kao rezervno rješenje za
sistem Klase A. Međutim, upravljaču infrastrukture nije dozvoljeno da za vožnju takvim prugama
zahtjeva sisteme Klase B u interoperabilnim vozovima.
Oprema na pruzi mora da podržava prelaz između Klase A i Klase B bez nametanja dodatnih
zahtjeva za podsistem kontrole, upravljanja i signalizacije u vozilu pored onih koji su već navedeni
ovom TSI.
7.2.5. Vozna sredstva sa opremom Klase A i Klase B
Vozna sredstva mogu biti opremljena i sistemima Klase A i Klase B da bi se omogućilo
saobraćanje na nekoliko pruga.
Mogu se uvesti ograničenja za korišćenje sistema Klase B u vozilu na prugama gdje odgovarajući
sistem nije ugrađen na pruzi.
Prilikom saobraćanja na pruzi koja je opremljena i sistemom Klase A i sistemom Klase B, voz koji
je takođe opremljen sistemima Klase A i Klase B može koristiti sisteme Klase B kao rezervno
rješenje. Ovo ne može biti zahtjev za interoperabilnost.
Sistemi zaštite voza Klase B mogu se izvesti:
1. korišćenjem STM koji funkcioniše preko standardnog interfejsa (,,eksterni STM"); ili 2. kao integrisani u ERTMS/ETCS ili povezani preko nestandardnog interfejsa; ili 3. nezavisno od ERTMS/ETCS opreme, na primjer preko sistema koji omogućuje
prebacivanje sa jedne opreme na drugu. željezničko preduzeće mora da obezbjedi da se
prelazi između zaštite voza Klase A i Klase B odvijaju u skladu sa zahtjevima ove TSI i
nacionalnih propisa za sistem Klase B.
7.2.6. Uslovi za obavezne i izborne funkcije
Zavisno od karakteristika pružnog podsistema kontrole, upravljanja i signalizacije i njegovih
interfejsa sa drugim podsistemima, neke pružne funkcionalnosti koje nisu svrstane u obavezne
mogu postati nužne za sprovođenje u izvjesnim aplikacijama, da bi se ispunili osnovni zahtjevi.
Primjena funkcija na pruzi ne smije spriječiti voz koji je usaglašen samo sa obaveznim zahtjevima
sistema Klase A u vozilu da koristi konkretnu infrastrukturu izuzev ako se to zahtjeva zbog
sledećih izbornih funkcija u vozilu:
-
primjena na na pruzi nivoa 3 ETCS zahtjeva nadzor integriteta voza u vozilu,
-
primjena na pruzi nivoa 1 ETCS sa korišćenjem in-fill funkcionalnosti zahtjeva
odgovarajuću in-fill funkcionalnost u vozilu ukoliko je iz bezbjednosnih razloga brzina
približavanja postavljena na nulu (npr. zaštita opasnih tačaka);
-
kada ETCS zahtjeva prenos podataka radio vezom, GSM-R usluga za prenos podataka
mora ispuniti zahtjeve ETCS za prenos podataka,
-
može se dogoditi da je neophodno ugraditi interfejs K na sklopu u vozilu koji sadrži KER
STM.
7.2.7. Specifična pravila izvođenja GSM-R
7.2.7.1. Oprema na pruzi
Ugradnja GSM-R je obavezna u sledećim slučajevima:
1. kada se po prvi put ugrađuje radio kao dio pružnog podsistema kontrole, upravljanja i
signalizacije;
2. kada se unapređuje radio dio pružnog podsistema kontrole, upravljanja i signalizacije koji se
već koristi, na takav način da mjenja funkcije ili performanse podsistema. Ovo ne uključuje
izmjene koje se smatraju neophodnim radi ublažavanja bezbjednosnih nedostataka na postojećoj
opremi.
7.2.7.2. Oprema u vozilu
Ugradnja sistema GSM-R u vozna sredstva namjenjena za korišćenje na prugama na kojima je
bar jedna dionica opremljena interfejsima Klase A (čak i ako su oni nadređeni sistemu Klase B)
je obavezna u sledećim slučajevima:
1. kada se po prvi put ugrađuje radio kao dio podsistema kontrole, upravljanja i signalizacije u
vozilu;
2. kada se unapređuje radio dio podsistema kontrole, upravljanja i signalizacije u vozilu koji se
već koristi, na takav način da menja funkcije ili performanse podsistema. Ovo se ne primjenjuje
na izmjene koje se smatraju neophodnim radi ublažavanja bezbjednosnih nedostataka na
postojećoj opremi.
7.2.8. Specifična pravila izvedbe sistema za detekciju voza
Sistem detekcije voza označava opremu postavljenu na pruzi, koja detektuje prisustvo ili odsustvo
vozila ili na cjeloj pruzi ili samo na određenoj dionici pruge.
Pružni sistemi (npr. kontrolni sistemi postavnica ili putnih prelaza u nivou) koji koriste
informacije iz opreme za detekciju ne smatraju se djelovima sistema za detekciju voza.
TSI navodi zahtjeve za interfejs sa voznim sredstvima jedino do nivoa neophodnog da se
obezbjedi usklađenost između voznih sredstava koja su usaglašena sa TSI, i infrastrukture.
Ugradnja sistema za detekciju voza koji je usaglašen sa zahtjevima TSI podsistema kontrole,
upravljanja i signalizacije može se obaviti nezavisno od ugradnje ERTMS/ETCS ili GSM-R, ali
može zavisiti od sistema signalizacije Klase B ili od posebnih zahtjeva, npr. onih za opremu
putnih prelaza u nivou.
Zahtjevi ove TSI koji se odnose na sisteme za detekciju voza se ispunjavaju:
1. prilikom unapređenja sistema za detekciju voza;
2. prilikom obnavljanja sistema za detekciju voza, pod uslovom da ispunjavanje zahtjeva TSI ne
podrazumeva neželjene izmjene ili unapređenja drugih sistema na pruzi ili u vozilima;
3. prilikom obnavljanja sistema za detekciju voza, kada se ono zahtjeva zbog unapređenja ili
obnove sistema na pruzi koji koriste informacije iz sistema za detekciju voza;
4. prilikom uklanjanja sistema zaštite voza Klase B (kada su sistemi detekcije i zaštite voza
integrisani).
U fazi prelaska mora se voditi briga o tome da se obezbjedi da ugradnja sistema detekcije voza koji
je usaglašen sa TSI ima najmanji mogući uticaj na postojeća vozna sredstva koja nisu usaglašena
sa TSI.
Da bi se ovo postiglo, preporučuje se da upravljač infrastrukture odabere sistem za detekciju voza
koji je usaglašen sa TSI i koji je istovremeno usklađen sa voznim sredstvima koja nisu usaglašena
sa TSI a koja već saobraćaju na toj infrastrukturi.
7.3.
Pravila ERTMS
7.3.1.
Uvođenje ERTMS
Faze koje se moraju sprovesti kako bi se izvršila postepena tranzicija od postojeće situacije do
konačne situacije u kojoj usaglašavanje sa TSI postaje pravilo.
7.3.2.
Primjena ERTMS na pruzi
Cilj uvođenja ERTMS je da se postepeno obezbjedi da lokomotive, motorna kola i druga
željeznička vozila opremljena ERTMS-om mogu postepeno da dobiju pristup sve većem broju
pruga, luka, terminala i ranžirnih stanica bez dodatne nacionalne opreme uz ERTMS.
Područja terminala kao što su luke, ili specifične pruge u luci, koje nisu opremljene sistemom
Klase B ispunjavaju zahtjeve utvrđene u Odjeljku 7.3.2.2. pod uslovom da željeznička vozila
dobiju pristup ovim područjima na terminalima bez nametanja zahtjeva koji se odnose na
opremanje sistemom automatske zaštite voza.
Pruga koja se sastoji od dva ili više kolosjeka smatra se opremljenom čim su dva od tih kolosjeka
opremljeni tako da omogućuju saobraćaj u oba smjera. Kada postoji više od jedne pruge na
dionici ili koridoru, najmanje jedna pruga na toj dionici mora biti opremljena ERTMS-om, a cijeli
koridor smatra se opremljenim čim se najmanje jedna pruga opremi dužinom cijelog koridora.
7.3.2.1. Koridori
Šest koridora opisanih u Odjeljku 7.3.4. opremaju se ERTMS-om u skladu sa rasporedom
naznačenim u ovom odjeljku3.
7.3.2.2. Povezivanje sa glavnim lukama, ranžirnim stanicama, robnim terminalima i područjima za transport
robe
Luke, ranžirne stanice, robni terminali i područja za transport robe navedeni u 7.3.5. povezuju se sa
najmanje jednim od šest koridora navedenih u 7.3.4 do datuma i pod uslovima navedenim u 7.3.5.
7.3.2.3. Mreža željezničkih pruga za velike brzine
Ugradnja pružnog sistema ERTMS/ETCS obavezna je:
1. kada se po prvi put ugrađuje oprema za zaštitu voza kao dio pružnog podsistema kontrole,
upravljanja i signalizacije (sa sistemom Klase B ili bez njega); ili
3 Odjeljak 7.3.4. utvrđuje krajnje rokove za opremanje ovih koridora, sa ciljem da se izgradi konzistentna Mreža ERTMS korak po korak. U izvjesnom broju slučajeva, postoje dobrovoljni sporazumi koji se odnose na ranije rokove
2. kada se unapređuje postojeći dio zaštite voza u pružnom podsistemu kontrole, upravljanja i
signalizacije tamo gdje će to promjeniti funkcije i performanse i/ili interfejse od značaja za
interoperabilnost (vazdušni međuprostori) u postojećem sistemu. Ovo se ne primjenjuje na
izmjene koje se smatraju neophodnim radi ublažavanja bezbjednosnih nedostataka u postojećoj
opremi.
Preporučuje se ugradnja sistema ERTMS/ETCS pri svakom unapređenju, obnovi ili održavanju
podsistema infrastrukture ili energije na pružnoj dionici koja je već u upotrebi, pod uslovom da
ugradnja ERTMS/ETCS na toj pružnoj dionici predstavlja manje od 10% ukupne investicije u
unapređenje /obnovu/održavanje.
7.3.2.4. Projekti koje finansira EU
Ugrađivanje sistema ERTMS/ETCS treba da se vrši:
1. kada se po prvi put ugrađuje zaštita voza kao dio podsistema kontrole, upravljanja i signalizacije;
ili
2. kada se unapređuje zaštita voza kao dio podsistema kontrole, upravljanja i signalizacije koji je
već u upotrebi na takav način da se mjenjaju funkcije ili performanse podsistema.
7.3.2.5. Prijavljivanje
Za svaku odsjek koridora opisan u 7.3.4, države članice ili prijavljuju Komisiji detaljni vremenski
plan za opremanje tog odseka koridora ERTMS-om ili potvrđuju da je konkretan odsjek koridora
već opremljen. Ta informacija se dostavlja Komisiji najkasnije 3 godine prije isteka roka za
opremanje tog odsjeka koridora, kako je utvrđeno u 7.3.4.
Za svaku luku, ranžirnu stanicu, robni terminal ili područje za transport robe koji su navedeni u
7.3.5 države članice prijavljuju priključne pruge koje će se koristiti za njihovo povezivanje sa
jednim od koridora navedenih u 7.3.4. Te informacije se dostavljaju Komisiji najkasnije 3 godine
pre isteka roka navedenog u 7.3.5 i sadrže naznaku krajnjeg roka za opremanje konkretne luke,
ranžirne stanice, robnog terminala ili područja za transport robe. Po potrebi, Komisija može
zahtjevati prilagođenja, naročito da bi se obezbjedila usklađenost između opremljenih pruga na
granicama. Države članice ili prijavljuju Komisiji detaljni vremenski plan za opremanje
priključnih pruga ERTMS-om ili potvrđuju da su ove priključne pruge već opremljene. Te
informacije se dostavljaju Komisiji najkasnije 3 godine prije isteka roka navedenog u 7.3.5 i sadrže
naznaku krajnjeg roka za opremanje konkretne luke, ranžirne stanice, robnog terminala ili područja
za transport robe.
Detaljni vremenski planovi posebno moraju sadržati naznaku datuma do kog se završava tender za
opremanje konkretne pruge, postupke koji se koriste za obezbjeđivanje interoperabilnosti sa
susjednim državama na koridoru i ključne etape koje se odnose na projekat. Svakih 12 meseci
države članice obavještavaju Komisiju o napretku opremanja ovih pruga dostavljanjem ažuriranog
vremenskog plana aktivnosti.
7.3.3.
Primjena ERTMS u vozilu
7.3.3.1 Nova vozila
Nova vozila koja su po prvi put odobrena za puštanje u saobraćaj moraju biti opremljena ERTMS-
om u skladu sa skupom specifikacija # 1 ili skupom specifikacija # 2 navedenim u Tabeli A2 Dijela A. Od 1. januara 2018. godine nova vozila koja su po prvi put odobrena za puštanje u saobraćaj moraju biti opremljena ERTMS-om isključivo u skladu sa skupom specifikacija # 2
navedenim u Tabeli A2 Aneksa A.
Zahtjevi za opremljenost ERTMS-om ne primjenjuju se na novu pokretnu opremu za izgradnju i
održavanje željezničke infrastrukture, nove manevarske lokomotive ili druga nova vozila koja nisu
predviđena za velike brzine, ukoliko su namjenjena isključivo za nacionalni saobraćaj izvan
koridora definisanih u odjeljku 7.3.4. i izvan pruga koje obezbjeđuju veze sa glavnim evropskim
lukama, ranžirnim stanicama, robnim terminalima i područjima transporta robe definisanim u
odjeljku 7.3.5, ili ako su namjenjeni za prekogranični saobraćaj van - TEN, tj. za saobraćaj do prve
stanice u susjednoj zemlji ili do prve stanice u susjednoj zemlji na kojoj postoje dalje veze.
7.3.3.2. Unapređenje i obnova postojećih vozila
Ugradnja ERTMS/ETCS na postojećim vozilima je obavezna ako se na postojeća vozila namjenjena
za velike brzine ugrađuje neki novi dio za zaštitu voza kao dio podsistema kontrole, upravljanja i
signalizacije.
7.3.3.3. Dodatni zahtjevi mogu uvesti dodatne zahtjeve na nacionalnom nivou, naročito sa ciljem
da
7.3.3.3.1.
pristup prugama opremljenim ERTMS-om dozvole samo vozilima opremljenim
ERTMS-om, tako da postojeći nacionalni sistemi mogu biti stavljeni van upotrebe;
7.3.3.3.2.
zahtjevaju da nova i unapređena ili obnovljena pokretna oprema za izgradnju i
održavanje željezničke infrastrukture, manevarske lokomotive i/ili druga vozila
budu opremljeni ERTMS-om čak i onda kada su namjenjeni isključivo za
nacionalni saobraćaj.
Dio A
Upućivanja
Za svako upućivanje navedeno u osnovnim parametrima (Poglavlje 4. ove TSI), sljedeće tabela navodi odgovarajuće obavezne specifikacije preko indeksa u tabeli A-2.
Tabela 1.
Upućivanje
u
Poglavlju 4.
Tačka (vidi Tabelu A
2)
Upućivanje u Poglavlju
4.
Tačka (vidi Tabelu A
2)
4.1
4.2.4 c
67
4.1 a
1, 4
4.2.4 d
68
4.1 b
32
4.2.4 e
73, 74
4.1 c
3
4.2.4 f
32, 33
4.2.4 g
48
4.2.1
4.2.4 h
69, 70
4.2.1 a
27, 28
4.2.4 j
71, 72
4.2.1 b
4.2.4 k
75, 76
4.2.2
4.2.5
4.2.2.a
14
4.2.5 a
64, 65
4.2.2.b
1, 4, 13, 15, 60
4.2.5 b
10, 39, 40
4.2.2.c
31, 37b, c, d
4.2.5 v
19, 20
4.2.2.d
18, 20
4.2.5 g
9, 43
4.2.2.e
6
4.2.5 d
16, 50
4.2.2.f
7
4.2.6
4.2.3
4.2.6 a
8, 25, 26, 36 c, 49,
52
4.2.3 a
14
4.2.6 b
29, 45
4.2.3 b
1, 4, 13, 15, 60
4.2.6 c
46
4.2.3 c
31, 37b, v, g
4.2.6 d
34
4.2.3 d
18, 21
4.2.6 e
20
4.2.6 f
44
4.2.4
4.2.4 a
64, 65
4.2.7
4.2.4 b
66
4.2.7 a
12
4.2.7 b
62, 63
4.2.11
4.2.7 c
34
4.2.11 a
77 (Odjeljak 3.2)
4.2.7 d
9
4.2.7 e
16
4.2.12
4.2.12 a
6, 51
4.2.8
4.2.8 a
11, 79
4.2.13
4.2.13 a
32, 33, 51, 80
4.2.9
4.2.9.a
23
4.2.14
4.2.14 a
5
4.2.10
4.2.10 a
77 (Odjeljak 3.1)
4.2.15
4.2.15 a
38
Specifikacije
Primjenjuje se jedan od dva navedena skupa specifikacija nabrojanih u Tabeli A-2 ovog Dijela.
Dokumenti na koje se upućuje u specifikaciji iz Tabele A-2 samo su informativnog karaktera, osim ako u Tabeli A-2 nije drugačije navedeno.
Napomena: specifikacije označene kao "rezervisano" u Tabeli A-2 nabrojane su i kao otvorena pitanja u Dijelu G, kada je za rješavanje odgovarajućih pitanja potrebno prijavljivanje nacionalnih propisa. Rezervisani dokumenti, koji nisu nabrojani kao otvorena pitanja, namjenjeni su poboljšanjima sistema.
Specifikacije
U svrhu primjene ove TSI, sve specifikacije navedene u Tabeli A2 u nastavku su zakonski
obavezujuće u verziji koja je navedena u Tabeli A2. Dokumenta na koja se upućuje u
specifikacijama a navedena su u tabeli A2 smatraju se samo informacijom, ako drugačije nije
naznačeno u Tabeli A2.
U slučajevima kada su iskazi u specifikacijama navedenim u Tabeli A2 u suprotnosti sa gore
navedenim odredbama, ove druge imaju prednost.
Napomena: Specifikacije navedene kao ,,rezervisane’’ u Tabeli A2 odgovaraju otvorenim
pitanjima navedenim u Dijelu G.
Tabela A2
Ind.
Eks
Br.
Skup specifikacija # 1
(ETCS osnovna konfiguracija 2 i GSM-R
osnovna konfiguracija 0)
Skup specifikacija # 2
(ETCS osnovna konfiguracija 3 i GSM-R
osnovna konfiguracija 0)
Upućivanje
Naziv
specifikacije
Verzija Napo
mene
Upućivanje
Naziv
specifikacije
Verzija Napo
mene
1
ERA/ERTMS/0
03204
ERTMS/ETCS
Functional
requirement
specification
5.0
Namjerno
izbrisano
2
Namjerno
izbrisano
Namjerno
izbrisano
3
SUBSET-023
Glossary of
Terms and
Abbreviations
2.0.0
SUBSET-023
Glossary of Terms
and Abbreviations
3.1.0
4
SUBSET-026
System
Requirements
Specification
2.3.0
SUBSET-026
System
Requirements
Specification
3.4.0
5
SUBSET-027
FFFIS Juridical
recorder-
downloading tool
2.3.0
Napo mena 1
SUBSET-027
FIS Juridical
Recording
3.1.0
6
SUBSET-033
FIS for man-
machine interface
2.0.0
ERA_ERTMS_0
15560
ETCS Driver
Machine interface
3.4.0
7
SUBSET-034
FIS for the train
interface
2.0.0
SUBSET-034
Train Interface
FIS
3.1.0
8
SUBSET-035
Specific
Transmission
Module FFFIS
2.1.1
SUBSET-035
Specific
Transmission
Module FFFIS
3.1.0
9
SUBSET-036
FFFIS for
Eurobalise
2.4.1
SUBSET-036
FFFIS for
Eurobalise
3.0.0
10
SUBSET-037
EuroRadio FIS
2.3.0
SUBSET-037
EuroRadio FIS
3.1.0
11
SUBSET-038
Offline key
management FIS
2.3.0
SUBSET-038
Offline key
management FIS
3.0.0
12
SUBSET-039
FIS for the
RBC/RBC
handover
2.3.0
SUBSET-039
FIS for the
RBC/RBC
handover
3.1.0
13
SUBSET-040
Dimensioning
and Engineering
rules
2.3.0
SUBSET-040
Dimensioning
and Engineering
rules
3.3.0
SUBSET-041
Performance
Requirements for
Interoperability
2.1.0
SUBSET-041
Performance
Requirements for
Interoperability
3.1.0
15
SUBSET-108
Interoperability
related
consolidation on
TSI Annex A
documents
1.2.0
Namjerno
izbrisano
16
SUBSET-044
FFFIS for
Euroloop
2.3.0
SUBSET-044
FFFIS for
Euroloop
2.4.0
17
Namjerno
izbrisano
Namjerno
izbrisano
18
SUBSET-046
Radio infill FFFS 2.0.0
Namjerno
izbrisano
19
SUBSET-047
Trackside-
Trainborne FIS
for Radio infill
2.0.0
SUBSET-047
Trackside-
Trainborne FIS
for Radio infill
3.0.0
20
SUBSET-048
Trainborne
FFFIS for Radio
infill
2.0.0
SUBSET-048
Trainborne
FFFIS for Radio
infill
3.0.0
21
SUBSET-049
Radio infill FIS
with
LEU/interlocking
2.0.0
Namjerno
izbrisano
22
Namjerno
izbrisano
Namjerno
izbrisano
23
SUBSET-054
Responsibilities
and rules for the
assignment of
values to ETCS
variables
2.1.0
SUBSET-054
Responsibilities
and rules for the
assignment of
values to ETCS
variables
3.0.0
24
Namjerno
izbrisano
Namjerno
izbrisano
25
SUBSET-056
STM FFFIS Safe
time layer
2.2.0
SUBSET-056
STM FFFIS Safe
time layer
3.0.0
26
SUBSET-057
STM FFFIS Safe
link layer
2.2.0
SUBSET-057
STM FFFIS Safe
link layer
3.0.0
27
SUBSET-091
Safety
Requirements for
the Technical
Interoperability
of ETCS in Levels
1 and 2
2.5.0
SUBSET-091
Safety
Requirements for
the Technical
Interoperability
of ETCS in Levels
1 and 2
3.3.0
28
Namjerno
izbrisano
Napo mena 8
Namjerno
izbrisano
Nap
ome na
8
SUBSET-102
Test specification
for interface "K"
1.0.0
SUBSET-102
Test specification
for interface "K"
2.0.0
30
Namjerno
izbrisano
Namjerno
izbrisano
31
SUBSET-094
Functional
requirements for
an onboard
reference test
facility
2.0.2
SUBSET-094
Functional
requirements for
an onboard
reference test
facility
3.0.0
32
EIRENE FRS GSM-R
Functional
requirements
specification
7.4.0
Napo mena
10
EIRENE FRS
GSM-R
Functional
requirements
specification
7.4.0
Nap
ome na
10
33
EIRENE SRS
GSM-R System
requirements
specification
15.4.
0
Napo mena
10
EIRENE SRS
GSM-R System
requirements
specification
15.4.
0
Nap
ome na
10
Ind
Eks
Br.
Skup specifikacija # 1
(ETCS osnovna konfiguracija 2 i GSM-R
osnovna konfiguracija 0)
Skup specifikacija # 2
(ETCS osnovna konfiguracija 3 i GSM-R
osnovna konfiguracija 0)
Upućivanje
Naziv
specifikacije
Verzija Napo
mene
Upućivanje
Naziv
specifikacije
Verzija Nap
ome
ne
34
A11T6001
(MORANE)
Radio
Transmission
FFFIS for
EuroRadio
12.4
A11T6001
(MORANE)
Radio
Transmission
FFFIS for
EuroRadio
12.4
35
Namjerno
izbrisano
Namjerno
izbrisano
36 a
Namjerno
izbrisano
Namjerno
izbrisano
36 b
Namjerno
izbrisano
Namjerno
izbrisano
36 c
SUBSET-074-
2
FFFIS STM Test
cases document
1.0.0
SUBSET-074-2 FFFIS STM Test
cases document
3.0.0
37 a
Namjerno
izbrisano
Namjerno
izbrisano
37 b
SUBSET-076-
5-2
Test cases related
to features
2.3.3
SUBSET-076- 5-
2
Test cases related
to features
Nap
ome
na 11
37 c
SUBSET-076-
6-3
Test sequences
2.3.3
Rezervisano
Test sequences
generation:
methodology and
rules
Nap
ome
na 11
37 d
SUBSET-076-7 Scope of the test
specifications
1.0.2
SUBSET-076-7 Scope of the test
specifications
3.0.0
37 e
Namjerno
izbrisano
Namjerno
izbrisano
38
06E068
ETCS Marker-
board definition
2.0
06E068
ETCS Marker-
board definition
2.0
39
SUBSET-092-1 ERTMS
EuroRadio
Conformance
Requirements
2.3.0
SUBSET-092-1 ERTMS
EuroRadio
Conformance
Requirements
3.0.0
40
SUBSET-092-2 ERTMS
EuroRadio test
cases safety layer
2.3.0
SUBSET-092-2 ERTMS
EuroRadio test
cases safety layer
3.0.0
41
Namjerno
Namjerno
Ind
eks
Br.
Skup specifikacija # 1
(ETCS osnovna konfiguracija 2 i GSM-R
osnovna konfiguracija 0)
Skup specifikacija # 2
(ETCS osnovna konfiguracija 3 i GSM-R
osnovna konfiguracija 0)
Upućivanje
Naziv
specifikacije
Verzija Napo
mene
Upućivanje
Naziv
specifikacije
Verz
ija
Napo
mene
izbrisano
izbrisano
42
Namjerno
izbrisano
Namjerno
izbrisano
43
SUBSET 085
Test specification
for Eurobalise
FFFIS
2.2.2
SUBSET 085
Test specification
for Eurobalise
FFFIS
3.0.0
44
Namjerno
izbrisano
Namjerno
izbrisano
Nap
ome
na 9
45
SUBSET-101
Interface "K"
Specification
1.0.0
SUBSET-101
Interface "K"
Specification
2.0.0
46
SUBSET-100
Interface "G"
Specification
1.0.1
SUBSET-100
Interface "G"
Specification
2.0.0
47
Namjerno
izbrisano
Namjerno
izbrisano
48
Rezervisano
Test specification
for mobile
equipment GSM-
R
Napo mena 4
Rezervisano
Test specification
for mobile
equipment GSM-
R
Nap
ome
na 4
49
SUBSET-059
Performance
requirements for
STM
2.1.1
SUBSET-059
Performance
requirements for
STM
3.0.0
50
SUBSET-103
Test specification
for Euroloop
1.0.0
SUBSET-103
Test specification
for Euroloop
1.1.0
51
Rezervisano
Ergonomic
aspects of the
DMI
Namjerno
izbrisano
52
SUBSET-058
FFFIS STM
Application layer
2.1.1
SUBSET-058
FFFIS STM
Application layer
3.1.0
53
Namjerno
izbrisano
Namjerno
izbrisano
54
Namjerno
izbrisano
Namjerno
izbrisano
Ind
eks
Br.
Skup specifikacija # 1
(ETCS osnovna konfiguracija 2 i GSM-R
osnovna konfiguracija 0)
Skup specifikacija # 2
(ETCS osnovna konfiguracija 3 i GSM-R
osnovna konfiguracija 0)
Upućivanje
Naziv
specifikacije
Verzija Napo
mene
Upućivanje
Naziv
specifikacije
Verzija
ija
Napo
mene
55
Namjerno
izbrisano
Namjerno
izbrisano
56
Namjerno
izbrisano
Namjerno
izbrisano
57
Namjerno
izbrisano
Namjerno
izbrisano
58
Namjerno
izbrisano
Namjerno
izbrisano
59
Namjerno
izbrisano
Namjerno
izbrisano
60
Namjerno
izbrisano
SUBSET-104
ETCS System
Version
Management
3.2.0
61
Namjerno
izbrisano
Namjerno
izbrisano
62
Rezervisano
RBC-RBC Test
specification for
safe
communication
interface
Namjerno
izbrisano
63
SUBSET-098
RBC-RBC Safe
Communication
Interface
1.0.0
SUBSET-098
RBC-RBC Safe
Communication
Interface
3.0.0
64
EN 301 515
Global System for
Mobile
Communication
(GSM);
Requirements for
GSM operation
on railways
2.3.0
Napo mena 2
EN 301 515
Global System for
Mobile
Communication
(GSM);
Requirements for
GSM operation
on railways
2.3.0
Nap
ome
na 2
65
TS 102 281
Detailed
requirements for
GSM operation
on railways
2.3.0
Napo mena 3
TS 102 281
Detailed
requirements for
GSM operation
on railways
2.3.0
Nap
ome
na 3
66
TS 103169
ASCI Options for
Interoperability
1.1.1
TS 103169
ASCI Options for
Interoperability
1.1.1
67
(MORANE) P
38 T 9001
FFFIS for GSM-
R SIM Cards
4.2
(MORANE) P
38 T 9001
FFFIS for GSM-
R SIM Cards
4.2
Ind
eks
Br.
Skup specifikacija # 1
(ETCS osnovna konfiguracija 2 i GSM-R
osnovna konfiguracija 0)
Skup specifikacija # 2
(ETCS osnovna konfiguracija 3 i GSM-R
osnovna konfiguracija 0)
Upućivanje
Naziv
specifikacije
Verzija Napo
mene
Upućivanje
Naziv
specifikacije
Verzija Napo
mene
68
ETSI TS 102
610
Railway
Telecommunicati
on; GSM; Usage
of the UUIE for
GSM operation
on railways
1.3.0
ETSI TS 102
610
Railway
Telecommunicati
on; GSM; Usage
of the UUIE for
GSM operation
on railways
1.3.0
69
(MORANE) F
10 T 6002
FFFS for
Confirmation of
High Priority
Calls
5.0
(MORANE) F
10 T 6002
FFFS for
Confirmation of
High Priority
Calls
5.0
70
(MORANE) F
12 T 6002
FIS for
Confirmation of
High Priority
Calls
5.0
(MORANE) F
12 T 6002
FIS for
Confirmation of
High Priority
Calls
5.0
71
(MORANE) E
10 T 6001
FFFS for
Functional
Addressing
4.1
(MORANE) E
10 T 6001
FFFS for
Functional
Addressing
4.1
72
(MORANE) E
12 T 6001
FIS for
Functional
Addressing
5.1
(MORANE) E
12 T 6001
FIS for
Functional
Addressing
5.1
73
(MORANE) F
10
T6001(MORA
NE) F 10
T6001
FFFS for
Location
Dependent
Addressing
4
(MORANE) F
10 T6001
FFFS for
Location
Dependent
Addressing
4
74
(MORANE) F
12 T6001
FIS for Location
Dependent
Addressing
3
(MORANE) F
12 T6001
FIS for Location
Dependent
Addressing
3
75
(MORANE) F
10 T 6003
FFFS for
Presentation of
Functional
Numbers to
Called and
Calling Parties
4
(MORANE) F
10 T 6003
FFFS for
Presentation of
Functional
Numbers to
Called and
Calling Parties
4
76
(MORANE) F
12 T 6003
FIS for
Presentation of
Functional
Numbers to
Called and
Calling Parties
4
(MORANE) F
12 T 6003
FIS for
Presentation of
Functional
Numbers to
Called and
Calling Parties
4
Ind
eks
Br.
Skup specifikacija # 1
(ETCS osnovna konfiguracija 2 i GSM-R
osnovna konfiguracija 0)
Skup specifikacija # 2
(ETCS osnovna konfiguracija 3 i GSM-R
osnovna konfiguracija 0)
Upućivanje
Naziv
specifikacije
Verzija Napo
mene
Upućivanje
Naziv
specifikacije
Verzija Napo
mene
77
ERA/ERTMS/0
33281
Interfaces
between CCS
track-side and
other subsystems
2.0
Napo mena 7
ERA/ERTMS/0
33281
Interfaces
between CCS
track-side and
other subsystems
2.0
Nap
ome
na 7
78
Rezervisano
Safety
requirements for
ETCS DMI
functions
Namjerno
izbrisano
Nap
ome
na 6
79
Nije
primjenjivo
Nije primjenjivo
SUBSET-114
KMC-ETCS
Entity Off-line
KM FIS
1.0.0
80
Nije
primjenjivo
Nije primjenjivo
Namjerno
izbrisano
Nap
ome
na 5
81
Nije
primjenjivo
Nije primjenjivo
SUBSET-119
Train Interface
FFFIS
Nap
ome
na 12
8
Nije
primjenjivo
Nije primjenjivo
SUBSET-120
FFFIS TI -
Safety Analysis
Nap
ome
na 12
Napomena 1: obavezan je samo funkcionalni opis informacija koje treba zabilježiti, a ne i tehničke
karakteristike interfejsa.
Napomena 2: odredbe specifikacija nabrojane u odjeljku 2.1 standarda MEST EN 301 515 na koje se
upućuje u Indeksu 32 i Indeksu 33 kao "MI" su obavezujujuće.
Napomena 3: zahtjevi za izmjene (CRs) nabrojani u tabelama 1 i 2 specifikacije TS 102 281 koje utiču
na odredbe na koje se upućuje u Indeksu 32 i Indeksu 33 kao "MI" su obavezujuće.
Napomena 4: Indeks 48 odnosi se samo na slučajeve ispitivanja mobilne opreme GSM-R. Za sada se označava kao "Rezervisano". Smjernica za primjenu sadržaće katalog raspoloživih harmonizovanih slučajeva ispitivanja za ocjenu mobilne opreme i mreža, prema koracima navedenim u odjeljku 6.1.2 ove
TSI.
Napomena 5: proizvodi koji su na tržištu već su prilagođeni potrebama upravljača infrastrukture u vezi
sa GSM-R interfejsom mašinovođa -voz i potpuno su interoperabilni tako da ne postoji potreba za
standardom u TSI CCS.
Napomena 6:
informacije o ETCS.
Napomena 7:
ovaj dokument nezavisan je od osnovne konfiguracije ETCS i GSM-R.
Napomena 8:
zahtjevi za pouzdanost/ raspoloživost su sada u TSI (odjeljak 4.2.1.2).
Napomena 9: analiza Evropske željezničke agencije pokazala je da ne postoji potreba za obavezujućom
specifikacijom za interfejs brzine i pređenog puta..
Napomena 10: Samo su (MI) zahtjevi propisani kao obavezni u TSI CCS.
Napomena 11: Specifikacijama će se upravljati pomoću Tehničkog mišljenja Evropske željezničke
agencije.
Napomena 12: Upućivanje na ove specifikacije objaviće se u Uputstvima za primjenu, pošto se čeka
objašnjenje interfejsa na strani voznih sredstava.";
Tabela A 3
Lista obaveznih standarda
Standardi navedeni u tabeli u nastavku primjenjuju se u postupku sertifikacije, ne
dovodeći u pitanje odredbe Poglavlja 4 i 6 ovog priloga.
Br.
Upućivanje
Naziv dokumenta i komentari
Verzija
Napomena
1
EN 50126
(MEST EN 50126)
Primjene na željeznici - Specifikacija i
dokazivanje pouzdanosti, raspoloživosti,
mogućnosti održavanja i bezbjednosti
(RAMS)
1999
(2018)
1
2
EN 50128
(MEST EN 50128)
Primjene na željeznici - Sistemi za
telekomunikacije, signalizaciju i obradu
podataka - Softver za upravljanje željeznicom i sistemi zaštite
2011 ili 2001
(2011)
3
EN 50129
(MEST EN 50129)
Primjene na željeznici - Sistemi za
telekomunikacije, signalizaciju i obradu
podataka- Bezbjednost elektronskih
sistema za signalizaciju
2003
1
4
EN 50159
Primjene na željeznici - Sistemi za
telekomunikacije, signalizaciju i obradu
podataka- Bezbjednost komunikacija u
u prenosnim sistemima
2010
1
Dio G
OTVORENA PITANjA
Otvorena tačka
Napomene
Aspekti kočenja
Važi samo za ERTMS/ETCS Osnovna
konfiguracija 2 (Dio A tabela A2, tačku 15.).
Rješeno za ERTMS/ETCS Osnovna
konfiguracija 3 (Dio A tabela A2, tač. 4. i
13.).
Tačka 28 - Zahtjevi za pouzdanost/dostupnost Česte pojave rada u otežanim uslovima,
prouzrokovane otkazima na
kontrolno-upravljačkoj i signalnoj opremi,
uticaće na smanjenje bezbjednosti sistema
Minimalni prečnik točka za brzinu veću od
350 km/h
Dio A tabela A2, indeks 77.
Minimalni razmak osovina za brzinu veću od
350 km/h
Dio A tabela A2, indeks 77.
Slobodan prostor između točkova u kome
nema metala i induktivnih komponenti
Dio A tabela A2, indeks 77.
Ovo nije otvoreno pitanje za teretna kola.
Karakteristike pjeska kojim se posipaju šine
Dio A tabela A2, indeks 77.
Metalna masa vozila
Dio A tabela A2, indeks 77.
Kombinacija karakteristika voznih sredstava,
koja utiče na impedansu kratkog spoja
Dio A tabela A2, indeks 77.
Elektromagnetne smetnje (struja vuče)
Dio A tabela A2, indeks 77.
Elektromagnetne smetnje (elektromagnetna
polja)
Dio A tabela A2, indeks 77.
Ovo nije otvoreno pitanje za elektroenergetske
sisteme, osim jednosmernih (DC)
Impedansa vozila
Dio A tabela A2, indeks 77.
Jednosmjerne i niskofrekventne komponente
struje vuče
Dio A tabela A2, indeks 77.
Korišćenje magnetnih kočnica/kočnica na
vrtložne struje
Dio A tabela A2, indeks 77.
Tačka 28 - Bezbjednosni zahtjevi za funkcije
ETCS DMI
Ovo otvoreno pitanje se odnosi na interfejs
između ETCS u vozilu i mašinovođe, tj. na
greške kod prikazivanja informacija i kod
unosa podataka i naredbi."
