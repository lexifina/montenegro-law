_____________________
pečat i potpis lica ovlašćenog za zastupanje
PRILOG 2
_________________ štambilj učesnika
ZAHTJEV ZA OTVARANJE IP RAČUNA
____________________________________________________________
(pun naziv učesnika)
Osnovni podaci podnosioca računa :
1. Naziv pravnog lica: _________________________________________________ 2. Mjesto - sjedište, adresa i broj telefona:_________________________________ 3. Djelatnost - predmet poslovanja:______________________________________ 4. PIB pravnog lica:___________________________________________________ 5. Tip računa: _______________________________________________________
Mjesto i datum: __________________________
_____________________
pečat i potpis lica ovlašćenog za zastupanje
Broj IP računa: ______________________________________________________ (upisuje Centralna banka)
PRILOG 3
_________________ štambilj učesnika
a) ZAHTJEV ZA PRENOS LIKVIDNOSTI SA RTGS RAČUNA NA IP RAČUN
UČESNIKA
NAZIV UČESNIKA
BIC KOD UČESNIKA
RAČUN UČESNIKA U RTGS SISTEMU
RAČUN UČESNIKA U IPS SISTEMU
IZNOS
DATUM
Mjesto i datum: __________________________
_____________________
pečat i potpis lica ovlašćenog za zastupanje
_________________ štambilj učesnika
b) ZAHTJEV ZA PRENOS LIKVIDNOSTI SA IP RAČUNA NA RTGS RAČUN
UČESNIKA
NAZIV UČESNIKA
BIC KOD UČESNIKA
RAČUN UČESNIKA U RTGS SISTEMU
RAČUN UČESNIKA U IPS SISTEMU
IZNOS
DATUM
Mjesto i datum: __________________________
_____________________
pečat i potpis lica ovlašćenog za zastupanje
PRILOG 4
VRSTE I TEHNIČKE KARAKTERISTIKE PORUKA U IPS SISTEMU
1. Vrste poruka u IPS sistemu
Poruke u IPS sistemu zasnivaju se na XML ISO 20022 standardu i definisane su u skladu su sa SCTInst šemom i drugim pravilima koja je propisao Evropski savjet za plaćanja (EPC).
Različiti tipovi poruka koriste se za 4 osnovna poslovna domena:
1) Payments Clearing and Settlement (pacs) - Kliring i poravnanje platnih transakcija
2) Cash Management (camt) - Upravljanje novčanim sredstvima
3) Account Management (acmt) - Upravljanje računima
4) Reference Data (reda) - Referentni podaci
Poruke iz domena kliringa i poravnanja platnih transakcija predstavljaju poruke koje se koriste za izvršavanje i realizaciju instant kreditnih transfera odnosno plaćanja.
Poruke iz domena upravljanja novčanim sredstvima koriste se kako bi se obezbijedilo potpuno pokriće SCTInst investigation i recall procesa, u skladu sa SCTInst šemom EPC-a, kao i kako bi se učesnicima omogućilo da iniciraju transfere likvidnosti i vrše upite o stanju na IP računima u IPS sistemu.
Poruke iz domena upravljanja računima (acmt) predstavljaju poruke koje se koriste kako bi se učesnicima omogućila promjena statusa (blokada/deblokada) IP računa.
Poruke iz domena referentnih podataka (reda) predstavljaju poruke koje se koriste kako za promjenu podataka vezanih za informacije o učesniku ili sam račun učesnika.
2. Lista poruka u IPS sistemu
Kliring i poravnanje platnih transakcija
pacs.008.001.08
FIToFICustomerCreditTransfer
Poruka namijenjena iniciranju i
izvršenju međubankarskog instant
kreditnog transfera odnosno
prenosa novčanih sredstava sa
računa platioca na račun primaoca
plaćanja.
pacs.002.001.10
FIToFIPaymentStatusReport
Statusna poruka namijenjena
izvještavanju odnosno potvrdi
statusa platne transakcije u
procesu njene obrade.
pacs.004.001.09
PaymentReturn
Poruka koja se koristi za povraćaj
prethodno primljenog instant
plaćanja njegovom pošiljaocu. Ova
poruka se koristi kao pozitivan
odgovor na zahtjev za opoziv
prethodno izvršenog instant
plaćanja.
pacs.028.001.03
FIToFIPaymentStatus
Request
Poruka koja se koristi za iniciranje
upita o statusu prethodno poslate
platne instrukcije. Poruka je
informativnog karaktera i ne
pokreće prenos sredstava.
Upravljanje novčanim sredstvima
camt.003.001.06
GetAccount
Poruka koja se koristi za
podnošenje zahtjeva za
dostavljanje informacija o jednom
ili više računa.
camt.004.001.07
ReturnAccount
Poruka kojom se dostavljaju
tražene informacije o jednom ili
vise računa kao odgovor na
prethodno poslatu poruku
camt.003.
camt.005.001.07
GetTransaction
Poruka koja se koristi kao zahtjev
za dostavljanje informacija o
transakcijama bez obzira na status
transakcija.
camt.006.001.07
ReturnTransaction
Poruka kojom se dostavljaju
informacije o jednoj ili više
transakcija kao odgovor na
prethodno poslatu poruku
camt.005.
camt.019.001.07
ReturnBusinessDay
Information
Poruka kojom RTGS dostavlja IPS
sistemu informaciju o poslovnom
danu, cut off vremenu za obradu
transakcija kao i raspoloživosti
platnog sistema, odnosno promjeni
poslovnog dana.
camt.025.001.05
Receipt
Poruka koja se koristi za tehničku
potvrdu prijema prethodno
primljene poruke bez potvrđivanja
njene obrade, validacije ili
izvršenja.
Poruka se koristi za komunikaciju
IPS i RTGS sistema prilikom
obrade transfera likvidnosti.
camt.029.001.09
ResolutionOfInvestigation
Poruka kojom se učesniku
dostavlja rezultat obrade
prethodno pokrenutog slučaja
provjere (investigation) uključujući
informaciju o ishodu, korektivnim
radnjama i eventualnim
finansijskim ili operativnim
efektima. Ovu poruku dostavlja
banka primaoca kao negativan
odgovor na prethodno primljeni
zahtjev za opoziv.
camt.050.001.05
LiquidityCreditTransfer
Poruka kojom se zahtijeva prenos
sredstava između dva računa u
svrhu upravljanja likvidnošću.
Nalog za prenos sredstava sa
tranzitnog računa CBCG na IP
račun učesnika i obrnuto.
camt.052.001.06
BankToCustomerAccount
Report
Dnevni izvještaj o zbirnim
informacijama na računu učesnika.
camt.053.001.06
BankToCustomerStatement
Izvještaj o detaljnim informacijama
na računu učesnika.
camt.054.001.06
BankToCustomerDebit
CreditNotification
Poruka kojom se potvrđuje
odobrenje/zaduženje računa.
camt.056.001.08
FIToFIPaymentCancellation
Request
Poruka kojom se podnosi zahtjev
za opoziv prethodno poslate platne
poruke. Banka pošiljalac ga šalje
kako bi pokrenula proceduru
istrage (investigation) i povraćaja
sredstava po osnovu već
izvršenog instant plaćanja.
Upravljanje računima
acmt.010.001.02
AccountRequest
Acknowledgement
Poruka kojom sistem obavještava
učesnika o uspješnoj promjeni
statusa računa.
acmt.011.001.02
AccountRequestRejection
Poruka kojom sistem obavještava
učesnika da je zahtjev za
promjenu statusa računa odbijen
uz obrazloženje razloga odbijanja.
acmt.015.001.02
AccountExcludedMandate
MaintenanceRequest
Zahtjev za promjenu statusa
računa.
Referentni podaci
reda.016.001.01
PartyStatusAdvice
Poruka koju IPS sistem dostavlja
CBCG obavještenje o statusu
izvršenog zahtjeva za izmjenu
podataka.
reda.022.001.01
PartyModificationRequest
Poruka kojom CBCG dostavlja IPS
sistemu zahtjev za izmjenu statusa
određenog učesnika.
3. Dozvoljeni karakteri
U porukama se smiju navoditi samo sljedeći karakteri:
a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9 / - ? : ( ) . , ' + Space Detaljni pregled poruka u IPS sistemu, čini sastavni dio tehničke dokumentacije iz člana 4 stav 6 ovih pravila.
PRILOG 5
OSNOVNI ELEMENTI NALOGA ZA PRENOS
Osnovni elementi naloga za prenos i način popunjavanja osnovnih elemenata naloga za prenos u odgovarajuće elektronske poruke daju se u sljedećoj tabeli:
Re
-
dn
i
br.
Naziv
elemenata
podataka
Način
popunjavanj
a elemenata
podataka
Elektonski
format
Napomena
1.
Naziv
platioca
Naziv i sjedište
pravnog lica ili
preduzetnika;
odnosno ime,
prezime i adresa
prebivališta fizičkog
lica
3*35x
3*35x - predstavlja
slovno, numeričke i
znakovne karaktere
2.
Transakcioni
račun
platioca
Transakcioni račun
koji se zadužuje
18n
Po odluci kojom se
uređuje struktura
transakcionih
računa
18 numeričkih polja
(3+13+2)
Ne popunjava se
kod naloga za
uplatu
3.
Naziv
primaoca
Naziv i sjedište
pravnog lica ili
preduzetnika;
odnosno ime,
prezime i adresa
prebivališta
fizičkog lica
3*35x
3*35x - predstavlja
slovno, numeričke i
znakovne karaktere
4.
Transakcioni
račun
primaoca
Transakcioni
račun koji će
biti odobren
18n
Po odluci kojom se
uređuje struktura
transakcionih
računa
18 numeričkih polja
(3+13+2)
Ne popunjava se
kod naloga za
isplatu.
5.
Iznos
Iznos sredstava
sa dvije cifre iza
12n,nn
Limitiran na 15
znakova (iznos od
12 cifara odvojenih
decimalnog
zareza
zarezom od dvije
naredne cifre
(decimale)
6.
Svrha
plaćanja
Namjera,
odnosno
osnov
plaćanja
5*35x
5*35x - predstavlja
slovno, numeričke i
znakovne karaktere
Popunjava se za
sve namjene.
7.
Šifra
plaćanja
Numerički podatak
3n
Popunjava se po
potrebi
8.
Model (broj
modela
poziva na
broj
zaduženja)
Kontrolni broj
poziva na broj
izračunat po
modulu 97.
Upisivanje
kontrolnog broja
nije uslov za
izvršavanje naloga,
ali ako se upiše,
mora odgovarati
propisanom
modulu.
2n
Popunjava se po
potrebi
9.
Poziv na
broj
zaduženja
Upisuju se podaci
u skladu sa
propisima ili prema
potrebama radi
dobijanja
dopunskih
informacija o
platnoj transakciji.
20x
Popunjava se po
potrebi
10
.
Model (broj
modela
poziva na
broj
odobrenja)
Kontrolni broj
poziva na broj
izračunat po
modulu 97.
Upisivanje
kontrolnog broja
nije uslov za
izvršavanje naloga,
ali ako se upiše,
mora odgovarati
propisanom
modulu.
2n
Popunjava se po
potrebi
11
.
Poziv na
broj
odobrenja
Upisuju se podaci
u skladu sa
propisima ili prema
potrebama radi
dobijanja
dopunskih
informacija o
platnoj transakciji.
20x
Popunjava se po
potrebi
12
.
Datum
izvršavanja
Datum kad je
nalog za plaćanje
izvršen.
DDMMGG
Numerički podaci
13
.
Oznaka
hitnosti
Oznaka hitnosti u
nalogu platioca
označava prenos
kroz platni sistem
za izvršavanje
instant kreditnih
transfera, a
popunjava platilac
pri prenosu
sredstava,
opciono.
U
odgovarajući
namjenski
prostor
upisuje se
oznaka X
Slovni podaci
PRILOG 6
UPUTSTVO ZA DOSTAVLJANJE INFORMACIJA U SLUČAJU TEHNIČKIH PROBLEMA I NEPREDVIĐENIH SITUACIJA
1. SVRHA Ovim Uputstvom definišu se aktivnosti koje su učesnici u IPS sistemu dužni da preduzmu u slučaju nepredviđenih situacija u radu IPS sistema.
2. PODRUČJE PRIMJENE Ovo uputstvo koristi se u slučaju tehničkih problema i nepredviđenih situacija u radu IPS sistema ili u internom sistemu učesnika koje mogu dovesti do problema učesnika da uspostavi komunikaciju sa IPS sistemom i učestvuje u radu IPS sistema.
3. OTKRIVANJE I PRIJAVA INCIDENTA Učesnik je dužan da bez odlaganja obavijesti Centralnu banku o incidentu koji uoči u radu IPS sistema kao i u svom internom sistemu, ako je interni sistem učesnika pogođen operativnim ili tehničkim prekidom koji traje duže od 10 minuta.
Učesnik je dužan da obavijesti Centralnu banku o utvrđenom incidentu pisanim putem, na način što će popuniti i dostaviti obrazac Izvještaja o incidentu koji se daje u tehničkoj dokumentaciji iz člana 4 stav 6 ovih pravila. Izvještaj, sadrže najbitnije podatke o utvrđenom incidentu (vrijeme registrovanja i opis nepredviđenog događaja, procijenjeno vrijeme za rješavanje problema, podatke o preduzetim radnjama, uzrok incidenta i dr).
Pri podnošenju prvog izvještaja, učesnik navodi one podatke o incidentu koji su u tom trenutku raspoloživi.
U slučaju tehničkih poteškoća u ostvarivanju komunikacije sa IPS sistemom, nakon što o tome obavijesti Centralnu banku, učesnik je dužan da, u najkraćem mogućem roku, u koordinaciji sa izabranim NSP-jem, otkloni nedostatke i obezbijedi redovno učešće u IPS sistemu.
Pored incidenata koji utiču na dostupnost internog sistema učesnika i drugih incidenata vezanih za funkcionalnost sistema, učesnik je dužan da prijavi i bezbjednosne probleme u vezi sa povjerljivošću i integritetom podataka, uključujući i bezbjedonosne incidente u tehničkoj infrastrukturi treće strane koja je učesnikov pružalac usluga.
4. POSTUPAK Nakon utvrđivanja postojanja incidenta učesnik popunjava izvještaj u kojem navodi one podatke o incidentu koji su u tom trenutku raspoloživi (inicijalni izvještaj).
Učesnik je dužan da u roku od tri radna dana od nastanka incidenta Centralnoj banci dostavi detaljniji izvještaj o incidentu.
Ako je incident:
1) okončan u trenutku dostavljanja detaljnijeg izvještaja i poznat je njegov uzrok,
detaljniji izvještaj o incidentu smatra se konačnim izvještajem o tom incidentu,
2) još uvijek pod istragom, detaljniji izvještaj o incidentu smatra se privremenim
izvještajem.
Konačni izvještaj o incidentu, koji dopunjuje informacije date u privremenom izvještaju, učesnik je dužan da dostavi Centralnoj banci najkasnije mjesec dana nakon što se incident dogodio.
Nakon dostavljanja konačnog izveštaja o incidentu Centralna banka cprocjenjuje njegovu potpunost i može od učesnika zahtijevati dopunu izvještaja.
Ako procjena incidenta otkrije da učesnik može stvoriti rizik za IPS sistem u cjelini, Centralna banka će razmotriti i dati dalje smjernice o potencijalnim korektivnim mjerama.
Obrazac za izvještavanje o incidentima dostavlja se učesnicima u sklopu tehničke dokumentacije iz člana 4 stav 6 ovih pravila.
