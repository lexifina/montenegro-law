# Član 7
Softversko rješenje iz člana 3 stav 1 tačka 5 ovog pravilnika, sadrži fajl sa kojeg će nadležni organ preuzimati zadržane podataka o saobraćaju i lokaciji, kao i odgovarajuće podatake potrebne za identifikaciju i registraciju krajnjih korisnika koji se zadržavaju za fiksnu i mobilnu mrežu za svog korisnika, korisnika druge mreže koji koristi mrežu operatora (inbound roamer), tako i za korisnika druge mreže u obimu i sa sadržajem podataka sa kojim raspolaže u sljedećem formatu:
Naziv kolona
Sadržaj
Format
DATUM
Datum početka komunikacije
yyyy-mm-dd
VRIJEME
Vrijeme početka komunikacije
hh:mm:ss
ABROJ
Objekat provjere MSISDN ili
broj fiksnog telefonskog broja
U međunarodnom formatu, bez
razmaka, crtica i drugih znakova
AIMSI
Objekat provjere IMSI, IMSI
za ABROJ
15 cifara, bez razmaka
AIMEI
Objekat provjere IMEI, IMEI
za ABROJ
15 cifara, 15-ta cifra "0"
A_BS_START
Ćelija, na početku
komunikacije
Jedinstveni identifikator ćelije
A_BS_START_NAZIV
Naziv ćelije, na početku
komunikacije
Tekst
A_BS_START_y
y koordinata ćelije, na početku
komunikacije
WGS84, zaokruženo na 6 decimala
A_BS_START_x
x koordinata ćelije, na početku
komunikacije
WGS84, zaokruženo na 6 decimala
A_BS_START_Azimut
Usmjerenost ćelije, azimut
Izraženo u stepenima
A_BS_START_Opstina
Opština u kojoj se nalazi ćelija
Tekst
A_BS_END
Ćelija, na kraju komunikacije
Jedinstveni identifikator ćelije
A_BS_NAZIV_END
Naziv ćelije, na kraju
komunikacije
Tekst
A_BS_END_y
y koordinata ćelije, na kraju
komunikacije
WGS84, zaokruženo na 6 decimala
A_BS_END_x
x koordinata ćelije, na kraju
komunikacije
WGS84, zaokruženo na 6 decimala
A_BS_END_ Azimut
Usmjerenost ćelije, azimut
Izraženo u stepenima
BBROJ
MSISDN sagovornika ili broj
fiksnog telefonskog broja
U međunarodnom formatu, bez
razmaka, crtica i drugih znakova
CBROJ
Broj sa ili na koji je izvršeno
preusmjeravanje
ili IP adresa preko koje je
pristupljeno internetu
U međunarodnom formatu, bez
razmaka, crtica i drugih znakova
VRSTA
Smjer komunikacije
Odlaz, Dolaz, Presumjeren
TIP
Korišćena komunikaciona
usluga
Voice, SMS, DATA…
OPIS
Uspješnost komunikacije
1 - ostvarena, 0 - neostvarena
TRAJANJE
Trajanje komunikacije
Prikazano u sekundama
ROMING
Država objekata provjere kada
je u romingu
Tekst
A_VLASNIK
Prezime i ime, registrovanog
korisnika za ABROJ
Tekst
A_ADRESA
Adresa, registrovanog
korisnika za ABROJ
Tekst
A_OPSTINA
Opština, registrovanog
korisnika za ABROJ
Tekst
A_JMB
Jedinstveni matični broj
odnosno jedinstveni
Tekst
identifikacioni broj ili broj
lične karte ili broj pasoša ili
poreski identifikacioni broj za
fizička lica, poreski ili
registarski broj za pravna lica
za ABROJ
B_VLASNIK
Prezime i ime, registrovanog
korisnika za BBROJ
Tekst
B_ADRESA
Adresa, registrovanog
korisnika za BBROJ
Tekst
B_OPSTINA
Opština, registrovanog
korisnika za BBROJ
Tekst
B_JMB
Jedinstveni matični broj
odnosno jedinstveni
identifikacioni broj ili broj
lične karte ili broj pasoša ili
poreski identifikacioni broj za
fizička lica, poreski ili
registarski broj za pravna lica
za BBROJ
Tekst
