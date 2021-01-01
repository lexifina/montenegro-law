PRILOG 1
DOSTAVLJANJE FISKALNOG RAČUNA
Obveznik fiskalizacije treba da dostavlja podatke o računu pojedinačno za svaki izdati račun u trenutku izdavanja računa.
Podaci o računu sadrže stavke računa kao što su opis, iznos, poreska stopa. Maksimalan broj stavki računa po jednom računu je ograničen na 1000 stavki po računu.
Informacioni sistem Uprave omogućava primanje XML poruke zahtjeva za račun koju obveznik fiskalizacije potvrđuje odgovarajućim aplikativnim certifikatom izdatim u svrhu fiskalizacije. Centralni informacioni sistem Uprave za svaku ispravnu XML poruku zahtjeva generiše jedinstveni identifikacioni kod računa, sprema podatke o računu i jedinstveni identifikacioni kod računa u sistem, te vraća XML poruku odgovora s jedinstvenim identifikacionim kodom računa ovjerenu aplikativnim certifikatom. Sistem čuva svaku ispravnu originalnu XML poruku pozivaoca. Sistem ne čuva originalnu XML poruku odgovora.
Sistem prima samo ispravne XML poruke zatjeva. Za neispravne XML poruke zatjeva sistem vraća XML poruku odgovora koja sadrži šifru i opis greške. Sistem ne evidentira neispravne originalne XML poruke zatjeva.
Proces razmjene podataka započinje u trenutku kad operater na naplatnom uređaju (blagajnik) treba izdati kupcu račun. Naplatni uređaj (ili informacioni sistem) obveznika fiskalizacije priprema podatke za račun i na osnovu istih izračunava identifikacioni kod obveznika fiskalizacije prema definisanom algoritmu i priprema XML poruku zahtjeva i digitalno je potpisuje s privatnim ključem aplikativnog certifikata koji je izdan obvezniku u svrhu fiskalizacije (u testnom okruženju koristi se testni aplikativni certifikat). Zatim se inicira jednostruku TLS1 komunikaciju pri čemu se server Poreske uprave predstavlja sa serverskim certifikatom. Nakon uspješno uspostavljene TLS komunikacije vrši se poziv servisa.
Elektronski naplatni uređaj ili informacioni sistem obveznika zaprima poruku odgovora i provjerava digitalni potpis sa javnim ključem aplikativnog certifikata. Nakon toga operater na naplatnom uređaju (blagajnik) izdaje kupcu račun sa ispisanim jedinstvenim identifikacionim kodom računa.
Broj fiskalnog računa odnosno pravilo sljedivosti broja računa, obveznik fiskalizacije utvrđuje odvojeno za fiskalne račune za gotovinsko plaćanje i fiskalne račune za bezgotovinsko plaćanje.
Obveznik fiskalizacije samostalno određuje pravilo sljedivosti za gotovinsko plaćanje ili na nivou poslovnog prostora ili na nivou elektronskog naplatnog uređaja, pri čemu numerička oznaka računa na početku kalendarske godine ili na početku rada poslovnog prostora ili na početku korišćenja elektronskog naplatnog uređaja počinje od 1 i nastavlja se bez preskakanja numeričkog redoslijeda brojeva za svaku godinu pojedinačno.
Za bezgotovinska plaćanja obveznik fiskalizacije pravilo sljedivosti određuje na nivou poslovnog prostora pri čemu numerička oznaka računa na početku kalendarske godine ili na početku rada poslovnog prostora počinje od 1 i nastavlja se bez preskakanja numeričkog redoslijeda brojeva za svaku godinu pojedinačno.
Storniranje prethodnih računa i računa u kojima se iskazuje povraćaj robe ili usluga
U slučaju povraćaja robe ili usluge u cijelosti ili djelomično, sprovodi se postupak ispravka računa. U postupku ispravke računa u kojima se iskazuje povraćaj robe ili usluga, izdaje se korektivni fiskalni račun u kojem se navodi jedinstveni identifikacioni kod fiskalnog računa koji se ispravlja i navode se svi ostali podaci koji čine konačno stanje fiskalnog računa. U provođenju postupka ispravka, mogući je korektivni račun ukupnog iznosa 0,00.
Prijava početnog stanja depozita i promjene stanja depozita novčanih sredstava u elektronskom naplatnom uređaju
Korišćenjem fiskalnog servisa obveznik fiskalizacije koji koristi elektronski naplatni uređaj za gotovinska plaćanja treba da na početku svakog radnog dana za svaki pojedinačni uređaj, prije prvog izdavanja fiskalnog računa, prijavi početno stanje depozita novčanih sredstava.
U prijavi početnog stanja depozita novčanih sredstava moguće je prijaviti iznos 0,00.
Obveznik fiskalizacije treba da prijavi svaku promjenu stanja depozita novčanih sredstava u elektronskom naplatnom uređaju u trenutku kada promjena nastaje i to:
-
stavljanje dodatnog iznosa novčanih sredstava depozita i/ ili
-
povlačenje određenog iznosa novčanih sredstava depozita tokom radnog dana.
PRILOG 2
OBLIK I STRUKTURA PORUKA FISKALNOG RAČUNA
Fiskalni račun treba da sadrži oblik i strukturu poruka u skladu sa tabelom 1.
Tabela 1
Podatak
Opis/Napomena
Obavezan DA/NE
Identifikator poruke
ID poruke (UUID). Svaka poruka koja se šalje prema centralnom sistemu mora sadržati različiti ID poruke. Isto važi i u slučaju kad se ponavlja
slanje poruke zbog greške u razmjeni poruka.
DA
Datum i vrijeme slanja
Datum i vrijeme slanja poruke zahtjeva.
DA Vrsta dokumenta
Oznaka da li se radi o gotovinskom ili bezgotovinskom računu (fakturi)
DA PIB obveznika
PIB obveznika fiskalizacije
DA U sistemu PDV
Oznaka je li obveznik u sistemu PDV-a ili nije.
DA PIB ili ID kupca
Ako je kupac pravno ili fizičko lice iz CG upisuje se PIB, ako se radi o
stranom preduzeću upisuje se ID iz države iz koje dolazi
DA, ako se radi o fakturi Naziv kupca
DA, ako se radi o fakturi Kupac iz CG
Oznaka da li je kupac pravno ili fizičko lice iz CG
DA, ako se radi o fakturi Oznaka države kupca
Naziv države kupca ako nije iz CG
DA, ako se radi o fakturi i
ako nije CG Datum i vrijeme izdavanja
Datum i vrijeme izdavanja koji se ispisuju na računu.
DA Oznaka sljedivosti
Oznaka sljedivosti brojeva računa. Oznaka koja govori gdje se određuje
dodjela broja računa centralno na nivou poslovnog prostora ili
DA
1 Transport Layer Security je kriptografski protokol koji omogućava sigurnu komunikaciju putem Interneta
pojedinačno na svakom naplatnom uređaju.
Dodjela brojeva računa može biti na nivou poslovnog prostora ili
naplatnog uređaja:
Broj računa
Propisaće se izgled broja računa kako ga treba ispisivati na fizičkom
računu u sljedećem obliku:
brojčana oznaka računa/oznaka poslovnog prostora/oznaka naplatnog
uređaja
Primjer: 1234567890/POSL1/12
Podaci će se Poreskoj upravi dostavljati odvojeni u XML-u radi kasnije
lakše manipulacije u izvještajima i analizama.
DA
Brojčana oznaka računa
Može sadržati samo cifre 0-9. Nijesu dozvoljene vodeće nule.
DA Oznaka poslovnog prostora
Može sadržati samo cifre i slova 0-9, a-z, A-Z. Mora biti jedinstvena na
nivou poreskog obveznika.
DA
Oznaka naplatnog uređaja
Može sadržati samo cifre 0-9. Nijesu dozvoljene vodeće nule.
Mora biti jedinstvena na nivou jednog poslovnog prostora.
DA
PDV
Porez na dodatu vrijednost.
Podatak se dostavlja Poreskoj upravi samo ako na računu postoji PDV.
Podatak se sastoji od poreske stope, osnovice i iznosa poreza.
Može postojati lista poreskih stopa.
NE
Poreska stopa
Iznos poreske stope.
DA, ako postoji porez Osnovica
Iznos osnovice
DA, ako postoji porez Iznos poreza
DA, ako postoji porez
Iznos oslobođenja
Ukupan iznos oslobođenja na računu. Oslobođenja u slučajevima kada se isporučuju dobra ili obavljaju usluge koje su oslobođene od plaćanja
PDV-a.
Podatak se dostavlja Poreskoj upravi samo ako na računu postoji
oslobođenje.
NE
Iznos koji ne podliježe oporezivanju
Ukupan iznos koji ne podliježe oporezivanju na računu.
Podatak se dostavlja Poreskoj upravi samo ako na računu postoji iznos
koji ne podliježe oporezivanju.
NE
Naknade
Naknade koje se mogu pojaviti na računu.
Podatak se dostavlja Poreskoj upravi samo ako na računu postoje
naknade.
Podatak se sastoji od naziva naknade i iznosa naknade.
Može postojati lista naknada.
NE
Naziv naknade
Opisno naziv naknade.
DA, ako postoji naknada Iznos naknade
DA, ako postoji naknada Ukupan iznos
Ukupan iznos iskazan na računu.
DA
Način plaćanja
G - gotovina
K - kartice
C - ček
T - transakcioni račun
O - ostalo
U slučaju više načina plaćanja po jednom računu, isto je potrebno
prijaviti pod 'Ostalo'.
Za sve načine plaćanja koji nijesu prije navedeni koristiće se oznaka
'Ostalo'.
DA
Identifikacioni kod obveznika fiskalizacije
Alfanumerički zapis kojim se potvrđuje veza između obveznika
fiskalizacije i izdatog računa.
Identifikacioni kod generiše obveznik fiskalizacije u skladu sa
definisanim algoritmom i ispisuje na računu.
32-cifreni broj zapisan u heksadecimalnom formatu.
Može sadržati cifre 0-9 i mala slova a-f.
Primjer: e4d909c290d0fb1ca068ffaddf22cbd0
DA
MB operatera
Matični broj operatera koji je izdao račun - 13 broj
DA Oznaka naknadne dostave računa
Naknadnom dostavom računa Poreskoj upravi smatra situacija kad je isti prethodno izdat kupcu bez IBR-a (npr. prekid Internet veze ili potpuni
prestanak rada naplatnog uređaja).
DA
Serijski broj iz uvezane knjige računa (paragon bloka)
U slučaju potpunog prestanka rada naplatnog uređaja izdaju se računi iz uvezane knjige računa. Naknadom dostavom računa Poreskoj upravi
mora se dostaviti i serijski broj računa iz knjige računa.
DA u slučaju potpunog pre-
stanka rada naplatnog uređa-
ja kada su se računi izdavali
iz evezane knjige računa. Stavke računa
Stavke računa treba da budu navedene uz pojedinačne opise proizvoda
ili usluga, novčanog iznosa i iznosa poreza
DA
PRILOG 3
PROTOKOLI I SIGURNOSNI MEHANIZMI ZA RAZMJENU PORUKA
Izdavanje fiskalnih računa vrši se korišćenjem fiskalnog servisa. Proces razmjene podataka o računu, između fiskalnog servisa obveznika fiskalizacije i sistema eFiskalizacije, započinje u trenutku kad operator izdaje račun za gotovinsko ili bezgotovinsko plaćanje.
Razmjena podataka iz stava 1 ovog priloga, sastoji se od sljedećih koraka:
1)
fiskalni servis priprema podatke za fiskalni račun i na osnovu istih izračunava jedinstveni identifikacioni kod računa,
2)
fiskalni servis priprema XML poruku zahtjeva za račun i elektronski je potpisuje sa privatnim ključem aplikacijskog certifikata
za potrebe fiskalizacije,
3)
fiskalni servis inicira sigurnu komunikaciju prema Sistemu eFiskalizacije,
4)
nakon uspješno uspostavljene sigurne komunikacije poziva se Sistem eFiskalizacije,
5)
sistem eFiskalizacije zaprima i obrađuje poruku zahtjeva za račun, a ako je zahtjev uspješno obrađen sistem eFiskalizacije
priprema XML poruku odgovora koja sadrži jedinstveni identifikacioni kod računa, elektronski je potpisuje sa privatnim ključem
aplikacijskog certifikata i šalje fiskalnom servisu obveznika fiskalizacije,
6)
fiskalni servis prima poruku odgovora i provjerava elektronski potpis sa javnim ključem aplikacijskog certifikata,
7)
operator izdaje fiskalni račun sa ispisanim jedinstvenim identifikacionim kodom računa kupcu ili primaocu računa.
Ako se prilikom obrade poruke zahtjeva za račun utvrdi neispravnost računa, Sistem eFiskalizacije vraća XML poruku odgovora koja sadrži opis neispravnosti i ne sadrži jedinstveni identifikacioni kod računa, nakon čega operator izdaje fiskalni račun bez jedinstvenog identifikacionog koda računa. Postupak izdavanja računa ne treba da bude onemogućen zbog nastale nesipravnosti računa. Obveznik fiskalizacije ispravlja nepravilnosti u poruci zahtjeva za račun i naknadno ponovlja slanje poruke u roku od dva dana.
Provjera u realnom vremenu obuhvata provjeru:
-
zaprimljene poruke prema definisanoj XML šemi (XSD2);
-
digitalnog certifikata3:
-
provjera digitalnog potpisa poruke - da je potpis valjan
-
PIB-a, da postoji u registru obveznika fiskalizacije
-
identifikatora poruke4
-
datuma i vremena slanja5
-
datuma i vremena izdavanja6:
-
poreske stope PDV-a7
-
osnovice PDV-a (u slučaju da je iskazano da obveznik nije u sistemu PDV-a i "Ukupan iznos" ne odgovara formuli za
izračun)8
-
podataka o PDV-u9
-
iznosa poreza PDV-a (u slučaju da je iskazano da je obveznik u sistemu PDV-a i "Ukupan iznos" ne odgovara formuli za
izračun)10
-
iznosa oslobođenja (kada je iskazanu da je obveznik u sistemu PDV-a i "Ukupan iznos" ne odgovara formuli za izračun)11
-
iznosa koji ne podliježe oporezivanju (kada je iskazano da je obveznik u sistemu PDV-a i "Ukupan iznos" ne odgovara formuli
za izračun)12
-
ukupnog iznosa (ako je iskazano da je obveznik u sistemu PDV-a)13
PRILOG 4
DOSTAVLJANJE FISKALNOG RAČUNA UPRAVI KADA SE NE MOŽE DODIJELITI JEDINSTVENI IDENTIFIKACIONI KOD RAČUNA
Maksimalno vrijeme (time-out) u kojem fiskalni servis obveznika fiskalizacije treba čekati poruku odgovora sa jedinstvenim identifikacionim kodom računa od Sistema eFiskalizacije, obveznik fiskalizacije treba da odredi uzimajući u obzir:
-
vrstu i dostupnost stalne internet veze koju koristi i poslovno prihvatljivo vrijeme za dobijanje odgovora sistema eFiskalizacije i
-
maksimalno vrijeme od dvije sekunde u kojem sistem eFiskalizacije treba obraditi poruku zahtjeva za račun i vrati poruku
odgovora (vrijeme od trenutka ulaska poruke zahtjeva za račun u sistem eFiskalizacije do trenutka izlaska poruke odgovora iz
sistema eFiskalizacije).
PRILOG 5
NAČIN GENERISANJA DUŽINE I IZGLEDA ZAPISA ZA JEDINSTVENI IDENTIFIKACIONI KOD RAČUNA
Informacioni sistem Uprave za svaku ispravnu XML poruku zahtjeva generiše jedinstveni identifikacioni kod računa, sprema podatke o računu i jedinstveni identifikacioni kod računa u sistem, i vraća XML poruku odgovora s jedinstvenim identifikacionim kodom računa ovjerenu aplikativnim certifikatom pošiljaocu. Sistem čuva svaku ispravnu originalnu XML poruku zahtjeva.
2 XSD - XML Schema Definition - jezik za definiranje strukture XML dokumenata, preporuka WWW konzorijuma (W3C) . Šema treba da precizno definiše strukturu podataka i ograničenja u okviru mogućnosti XSD standarda kako bi u što boljoj mjeri reflektirala definisane podatke i ograničenja (moguće vrijednosti, raspone vrijednosti, obaveznost i sl.) 3 da je vrijeme važenja certifikata valjano, da je izdan od ovlašćenih izdavaoca certifikata - provjera cijelog lanca izdavanja, da je izdan po posebnom profilu za potrebe fiskalizacije, da nije opozvan - provjera na listi opozvanih certifikata (CRL - Certificate Revocation List) ili OCSP (Online Certificate Status Protocol) upitom da PIB na certifikatu odgovara PIB-u na računu 4 ne smije postojati poruka s istim identifikatorom u sistemu fiskalizacije 5mora biti unutar 6 sati od vremena zaprimanja u sistemu fisklizacije 6ne smije biti više od 6 sati nakon datuma i vremena zaprimanja u sistemu fiskalizacije ne smije biti više od onoliko dana koliko je propisano zakonom kao maksimalni rok za dostavu računa u slučaju kvara ili prekida veze, prije datuma i vremena zaprimanja u sistem fiskalizacije ne smije biti nakon datuma i vremena slanja 7 u slučaju da je iskazano da obveznik nije u sistemu PDV-a poreska stopa mora biti unutar dozvoljenog skupa PDV stopa koje su određene Zakonom 8 suma svih osnovica ne smije biti veća od podatka "Ukupan iznos" kada je "Ukupan iznos" pozitivnog predznaka ili je jednak 0. Suma svih osnovica ne smije biti manja od podatka "Ukupan iznos" kada je "Ukupan iznos" negativnog predznaka ili je jednak 0. Mora biti istog predznaka kao i "Ukupan iznos" 9ne smiju postojati podaci o PDV-u ako je iskazano da obveznik nije u sistemu PDV-a 10 mora odgovarati po formuli osnovica * stopa 11 ne smije biti veći od podatka "Ukupan iznos" kada je "Ukupan iznos" pozitivnog predznaka ili je jednak 0. Mora biti 0 u slučaju da je iskazano da ne smije biti manji od podatka "Ukupan iznos" kada je "Ukupan iznos" negativnog predznaka ili je jednak 0. Mora biti istog predznaka kao i "Ukupan iznos" 12 ne smije biti veći od podatka "Ukupan iznos" kada je "Ukupan iznos" pozitivnog predznaka ili je jednak 0. Ne smije biti manji od podatka "Ukupan iznos" kada je "Ukupan iznos" negativnog predznaka ili je jednak 0. Mora biti istog predznaka kao i "Ukupan iznos". Mora biti 0 ako je iskazano da obveznik nije u sistemu PDV-a 13 mora biti po formuli: suma svih osnovica + suma svih iznosa poreza + iznos oslobođenja + iznos koji ne podliježe oporezivanju + suma iznosa naknada
Sistem ne čuva originalnu XML poruku odgovora.
Sistem prima samo ispravne XML poruke zatjeva.
Za neispravne XML poruke zatjeva sistem vraća XML poruku odgovora koja sadrži šifru i opis greške.
Sistem ne evidentira neispravne originalne XML poruke zatjeva.
Proces razmjene podataka započinje u trenutku kad operater na naplatnom uređaju (blagajnik) treba izdati kupcu račun.
Elektronski naplatni uređaj (ili informacioni sistem) obveznika fiskalizacije priprema podatke za račun i temeljem istih izračunava identifikacioni kod obveznika fiskalizacije prema definisanom algoritmu i priprema XML poruku zahtjeva i digitalno je potpisuje sa privatnim ključem aplikativnog certifikata koji je izdat obvezniku u svrhu fiskalizacije (u testnom okruženju koristi se testni aplikativni certifikat).
Nakon toga inicira jednostruku TLS komunikaciju pri čemu se server Poreske uprave predstavlja sa serverskim certifikatom. Nakon uspješno uspostavljene TLS komunikacije vrši se poziv servisa.
Jedinstveni identifikacioni kod računa izračunava se metodom UUID (universally unique identifier) i sastavljen od 32 znaka.
Znakovi jedinstvenog identifikacionog koda računa sastoje se od brojeva 0 - 9 i slova a - f, koji se iskazuju u pet grupa odvojenih povlakom (-) u obliku 8-4-4-4-12.
PRILOG 6
MODEL PRIMJENE KOD KOJEG SE KORISTI CENTRALNI INFORMACIONI SISTEM OBVEZNIKA FISKALIZACIJE ZA SLANJE
I POTPISIVANJE ELEKTRONSKIH PORUKA
Postupak fiskalizacije računa ne provodi se za dokumente koji se izdaju prema propisu o porezu na dodatu vrijednost, a koji se ne smatraju računima.
1)
Obveznik fiskalizacije izdaje fiskalne račune.
2)
Izdavanje fiskalnih računa sprovodi se korištenjem fiskalnog servisa.
3)
Jedinstveni identifikacioni kod računa se dodjeljuje svakom računu ako je potpisan valjanim elektroničkim potpisom i
dostavljen u propisanoj strukturi Sistemu eFiskalizacije u trenutku izdavanja računa.
Proces razmjene podataka o računu, između fiskalnog servisa obveznika fiskalizacije i sistema eFiskalizacije, započinje u trenutku kad operator izdaje račun za gotovinsko ili bezgotovinsko plaćanje.
Proces razmjene podataka sastoji se od sljedećih koraka:
1)
fiskalni servis priprema podatke za fiskalni račun i na osnovu istih izračunava identifikacioni kod obveznika fiskalizacije,
2)
fiskalni servis priprema XML poruku zahtjeva za račun i elektronski je potpisuje s privatnim ključem aplikacijskog certifikata za
potrebe fiskalizacije. Elektronski potpis izvršava se koristeći RSA-SHA256 elektronski potpis sa certifikatom za fiskalizaciju,
3)
fiskalni servis inicira sigurnu komunikaciju prema Sistemu eFiskalizacije,
4)
nakon uspješno uspostavljene sigurne komunikacije poziva se Sistem eFiskalizacije,
5)
sistem eFiskalizacije zaprima i obrađuje poruku zahtjeva za račun. Ako je zahtjev uspješno obrađen Sistem eFiskalizacije
priprema XML poruku odgovora koja sadrži jedinstveni identifikacioni kod računa, elektronski je potpisuje s privatnim ključem
aplikacijskog certifikata i šalje fiskalnom servisu obveznika fiskalizacije,
6)
fiskalni servis zaprima poruku odgovora i provjerava elektronski potpis s javnim ključem aplikacijskog certifikata,
7)
operator izdaje fiskalni račun s ispisanim jedinstvenim identifikacionim kodom računa kupcu ili primaocu računa.
Ako se prilikom obrade poruke zahtjeva za račun utvrdi neispravnost računa, Sistem eFiskalizacije vraća XML poruku odgovora koja sadrži opis neispravnosti i ne sadrži jedinstveni identifikacioni kod računa te operator izdaje fiskalni račun bez jedinstvenog identifikacionog koda računa.
Poslovni proces izdavanja računa ne smije biti onemogućen zbog nastale nesipravnosti računa. Obveznik fiskalizacije ispravlja nepravilnosti u poruci zahtjeva za račun i naknadno ponovlja slanje poruke u roku od dva dana, a fiskalni servis daje prioritet porukama zahtjeva za račun kojima se prijavljuje fiskalni račun koji se trenutno izdaje.
PRILOG 7
MODEL PRIMJENE U KOJEM SE SLANJE I POTPISIVANJE PORUKA OBAVLJA POJEDINAČNO NA ELEKTRONSKIM NAPLATNIM UREĐAJIMA
Samonaplatnim uređajem (automatom) koji ostvaruje promet od prodaje roba ili usluga smatra se svaki automatizirani uređaj koji nije u obvezi izdavanja računa, putem kojega se obavlja neposredna prodaja robe ili usluge pri čemu u prodaji i naplati robe ili usluga ne sudjeluje osoba.
Samonaplatni uređaji (automati) sprovode postupak fiskalizacije prijavom podataka o prodaji u trenutku prodaje robe ili usluga.
Za samonaplatne uređaje (automati) koji se pokreću žetonima i sličnim sredstvima za čiju je kupovinu je već proveden postupak fiskalizacije računa. ne provode postupak fiskalizacije.
Svaki samonaplatni uređaj (automat) smatra se poslovnim prostorom i neophodno je dostaviti podatke o poslovnom prostoru.
Obveznik fiskalizacije kao podatak o tipu poslovnog prostora navodi samonaplatni uređaj. Kao podatak o adresi samonaplatnog uređaja (automata) navodi adresu gdje se samonaplatni uređaj nalazi odnosno njegovu najbližu geolokacijsku adresu te dodatno opisuje smještaj u određenom prostoru.
Oznaku poslovnog prostora dodijeljenu od Uprave, obveznik fiskalizacije vidno ističe na svakom samonaplatnom uređaju (automatu).
Protokoli i sigurnosni mehanizmi, modeli primjene za slanje i potpisivanje elektronskih poruka, standardne poruke o nepravilnostima i protokole o postupanju u slučaju nepravilnosti za potrebe sprovođenja postupka fiskalizacije podataka o prodaji samonaplatnih uređaja (automata) vrše se u skladu sa Prilogom 3 ovog pravilnika.
U poruci zahtjeva za fiskalizaciju podatka o prodaji putem samonaplatnog uređaja (automata) podaci se prilagođavaju fiskalizaciji podataka o prodaji, na način da se:
-
pravilo sljedivosti određuje se kao pravilo na nivou poslovnog prostora,
-
kao brojčana oznaka računa iskazuje i broji svaka izvršena prodaja roba ili usluge - svaka transakcija i
-
kao oznaka operatora navodi jedinstveni matični broj lica obveznika fiskalizacije.
PRILOG 8
STANDARDNE PORUKE O GREŠKAMA
Informacioni sistem Uprave prima samo ispravne XML poruke zatjeva. Za neispravne XML poruke zatjeva sistem vraća XML poruku odgovora koja sadrži šifru i opis greške. Sistem ne evidentira neispravne originalne XML poruke zatjeva.
Podatak
Opis/Napomena
Obavezan DA/NE Identifikator poruke
ID poruke (UUID).
Kao identifikator poruke odgovora uzima se ID iz poruke zahtjeva.
DA
Datum i vrijeme obrade
Datum i vrijeme obrade poruke zahtjeva.
DA Jedinstveni identifika- cioni kod računa
Jedinstveni identifikacioni kod računa.
U slučaju greške, jedinstveni identifikacioni kod računa se ne šalje u odgovoru.
NE
Šifra greške
Šifra greške je u formatu NNN gdje je NNN trocifreni prirodni broj.
Šifre grešaka u skladu sa šifrarnikom grešaka.
DA, ako ima greške
Poruka
Poruka greške je tekstualni opis greške u skladu sa šifrarnikom grešaka.
DA, ako ima greške
Definisani skupovi podataka predstavljaju minimalni set podataka, ako se za vrijeme sprovođenja projekta identifikuje potreba za dodatnim podacima izvođač će iste ugraditi u sistem.
PRILOG 9
PROTOKOLI O POSTUPANJU U SLUČAJU GREŠAKA
Ako se prilikom obrade poruke zahtjeva dogodi greška (poruka neispravna po XML shemi, neispravan digitalni potpis) Informacioni sistem Uprave vraća XML poruku odgovora koja sadrži opis greške.
U tom slučaju odgovor ne sadrži jedinstveni identifikacioni kod računa i operater na naplatnom uređaju (blagajnik) izdaje kupcu račun bez jedinstvenog identifikacionog koda računa.
Izdavanje računa kupcu ne smije biti onemogućen zbog nastale greške ali obveznik fiskalizacije je dužan ispraviti nepravilnosti u slanju poruke i poruku naknadno dostaviti.
Ako obveznik nije dobio jedinstveni identifikacioni kod računa za izdani račun (prekid Internet veze, potpuni prestanak rada elektronskog naplatnog uređaja, greška u poruci odgovora, privremena nedostupnost IS-a) obveznik fiskalizacije treba da naknadno ponoviti slanje poruke.
Nakon dobijanja ispravne poruku odgovora od sistema Uprave koja sadrži jedinstveni identifikacioni kod računa obveznik fiskalizacije može da smatra da je račun prijavljen Upravi.
Ako obveznik fiskalizacije ne može dobiti jedinstveni identifikacioni kod računa, zbog prekida Internet veze, a veza se ponovo uspostavi, prioritet imaju poruke kojima se prijavljuju tekući računi koji se izdaju kako bi oni dobili jedinstveni identifikacioni kod računa.
Poruke koje nijesu dobile jedinstveni identifikacioni kod računa treba dostaviti naknadno u periodu manjeg opterećenja.
Maksimalno vrijeme (time-out) koje naplatni uređaj (ili IS) obveznika treba čekati poruku odgovora s jedinstvenim identifikacionim kodom računa procjenjuje obveznik fiskalizacije uzimajući u obzir vrstu i dostupnost Internet veze koju koristi i poslovno prihvatljivo vrijeme za dobijanje odgovora.
Kod procjene u obzir treba uzeti i maksimalno vrijeme od dvije sekunde u kojem IS treba obraditi poruku zahtjeva i vratiti poruku odgovora (vrijeme od trenutka ulaska poruke zahtjeva u IS do trenutka izlaska poruke odgovora iz sistema Uprave).
PRILOG 10
NAČIN DOSTAVLJANJA RAČUNA KOJI SU IZDATI U SLUČAJU PRIVREMENOG PREKIDA STALNE INTERNET VEZE
Ako se prilikom obrade poruke zahtjeva dogodi greška (poruka neispravna po XML shemi, neispravan digitalni potpis i sl.) informacioni sistem Uprave vraća XML poruku odgovora koja sadrži opis greške i u tom slučaju odgovor ne sadrži jedinstveni identifikacioni kod računa i kupcu se izdaje račun bez jedinstvenog identifikacionog koda računa.
Ako obveznik fiskalizacije nije dobio jedinstveni identifikacioni kod računa za izdati račun (prekid internetske veze, potpuni prestanak rada naplatnog uređaja, greška u poruci odgovora, privremena nedostupnost informacionog sistema Uprave), treba naknadno da ponovi slanje poruke.
Smatra da je račun prijavljen Upravi kada obveznik fiskalizacije dobije ispravnu poruku odgovora od centralnog sistema koja sadrži jedinstveni identifikacioni kod računa.
Prilikom ponovnog slanja poruke iz stava 2 ovog priloga, prioritet imaju poruke kojim se prijavljuju računi koji se u tom trenutku izdaju kako bi oni dobili jedinstveni identifikacioni kod računa.
Poruke koje nijesu dobile jedinstveni identifikacioni kod računa, a sačuvane su u elektronskom naplatnom uređaju ili informacionom sistemu poreskog obveznika, obveznik fiskalizacije treba poslati u periodu manjeg opterećenja nakon uspostavljanja internet veze.
U slučaju kvara naplatnog uređaja, fiskalni računi se izdaju iz knjige ovjerenih računa, nakon čega se naknadno unose u naplatni uređaj i šalju putem internet veze Upravi, radi dobijanja jedinstveni identifikacioni kod računa.
Računi iz stava 6 ovog priloga, treba da sadrže i serijski broj računa iz knjige ovjerenih računa.
