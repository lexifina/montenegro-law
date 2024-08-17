PRILOG 1
APLIKATIVNI PROGRAMIBILNI INTERFEJS ZAHTJEV
Izvor podataka - IP adresa
Priređivač treba da dostavi "IP Adresu" sa koje će slati podatke na Transakcioni API. Ta adresa mora biti "white list"- ovana. Priređivač će dobiti jedinstveni ključ koji treba da se pošalje u zaglavlju (header) svake poruke. Ime zaglavlja je x-api- key.
IP adresa se može koristiti samo u svrhe rada ovog servisa.
API Putanje Postoje sljedeće API putanje koje je potrebno integrisati od strane priređivača

/betting - (kladioničke igre, online i landbase);

/slot - (automat klubovi);

/slot-periodic (automat klubovi);

/online-slot - (online);

/online-player - (online).
Svaka putanja vraća ID transakcije koja je kreirana u sistemu. ID transakcije je polje tipa UUID. Sljedeći odgovori su
mogući:
Status
Opis 201 Created
Uspješno kreirana transakcija. Primjer:
{"uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6"} 404 Not Found
Putanja ne postoji na serveru 422 Unprocessable Entity
Greška u formatu poruke. Odgovor je objašnjenje o grešci u formatu:
{
"detail": [
{
"loc": [
"string"
],
"msg": "string",
"type": "string"
}
]
}
Trenutna verzija API-ja je v1, što znači da prije svake putanje treba dodati /v1. Pri pojavi nove verzije API-ja ovaj dio putanje će se promijeniti, ali će stara verzija ostati aktivna dok se ne izvrši kompletna migracija priređivača na novu veziju.
Primjer jedne putanje:
/v1/slot-periodic
Putanja - /betting
API putanje koje počinju sa /betting/ se odnose na podatke koji se prikupljaju sa terminala i iz kladionica, kao i kladioničke igre putem interneta. Ove transakcije se prikupljaju u realnom vremenu.
Tabela sa poljima potrebnim za ove tipove transakcija:
Ime polja
Obavezno
Opis transaction_time
da
Vrijeme transakcije sa vremenskom zonom
2020-05-25T08:48:28+02:00 (primjer u vremenskoj zoni Crne Gore)
2020-05-25T06:48:28Z (primjer u UTC formatu) transaction_id
da
ID transakcije iz sistema priređivača. Tekstualnog tipa (string) transaction_amount
da
Vrijednost transakcije u EUR. Maksimalno 2 decimalne cifre (float,
decimal, double).
betting_place_id
*
ID kladionice dodijeljen od strane Uprave. Tekstualnog tipa (string).
betting_terminal_id
*
ID kladomata dodijeljen od strane Uprave. Teksutalnog tipa (string).
game_name
da
Ime igre. Ako je u pitanju sportsko klađenje ime igre je sports_betting, u
ostalim slučajevima ime igre je ime iz sistema priređivača (npr.
greek_kino, lucky6, …).
jmb
**
Jedinstveni matični broj igrača koji je odigrao tiket. Podložno provjeri o
ispravnosti JMB-a.
passport_number
**
Broj pasoša ili lične karte igrača koji je odigrao tiket. Tekstualnog tipa
(string).
identification_document_countr y
**
Zemlja izdavanja pasoša ili lične karte. Tekstualnog tipa (string). Lista
kodova identification_document_type
**
Vrsta identifikacionog dokumenta. Moguće vrijednosti su {ID card,
Passport}. Tekstualnog tipa (string)
source
da
Oznaka da li je transakcija nastala na zemaljskom klađenju ili online
(Landbase, Web)
*Transakcije koje stižu sa uplatnog mjesta treba da imaju popunjeno polje betting_place_id. Transakcije koje stižu sa kladomata, pored polja betting_place_id moraju imati popunjeno i polje betting_terminal_id
** Uplate koje stižu s veb-a treba da imaju popunjen ili jmb (za državljane Crne gore) ili passport_number i identification_document_country i identification_document_type (za nerezidente), a ne smiju da imaju popunjeno polje betting_place_id, niti betting_terminal_id, osim u slučaju landbase transakcija sa iznosima 2000 EUR ili više, kada je uz polja potrebna za landbase transakcije, potrebno poslati i identifikaciju igrača.
U okviru /betting putanja imamo konkretne akcije:

/betting/bet - uplata tiketa

/betting/win - isplata tiketa

/betting/rollback - storniranje transakcije

/betting/jackpot - džekpot
Putanja /betting/bet
Putanja skuplja sve uplatne transakcije. Pored prethodno definisanih polja potrebno je poslati i polja iz sljedeće tabele:
Ime polja
Obavezno
Opis min_odds
da
Minimalna kvota na tiketu. Maksimalno 8 decimalnih cifara (float, decimal, double).
Potrebno je obratiti pažnju na igre koje shodno rezulatu mogu imatu dvije drugačije
kvote - npr Azijski hendikep.
max_odds
da
Maksimalna kvota na tiketu. Maksimalno 8 decimalnih cifara (float, decimal, double). min_win
da
Minimalni dobitak na tiketu u EUR. Maksimalno 2 decimalne cifre (float, decimal,
double).
max_win
da
Maksimalni dobitak na tiketu u EUR. Maksimalno 2 decimalne cifre
(float, decimal, double).
min_bonus
da
Minimalni bonus na tiketu u EUR. Maksimalno 2 decimalne cifre
(float, decimal, double).
max_bonus
da
Maksimalni bonus na tiketu u EUR. Maksimalno 2 decimalne cifre
(float, decimal, double).
max_payout
da
Maksimalna isplata na tiketu u EUR. Maksimalno 2 decimalne cifre
(float, decimal, double).
Uglavnom predstavlja sumu max_win + max_bonus osim ako pomenuta suma nije
veća od maksimalne isplate koju priređivač dozvoljava.
ticket_id
da
ID tiketa iz sistema priređivača. Tekstualnog tipa (string).
bet_type
da
Tip beta može biti (Real, Promo).
promo_amount
*
Vrijednost promo dijela transakcije u EUR. Maksimalno 2 decimalne cifre
(float, decimal, double).
ticket
da
JSON objekat definisan ispod.
* polje je obavezno ukoliko ja tip beta Promo i prikazuje koliki je iznos promo novca u samom betu
Tiket
Ime polja
Obavezno
Opis sy
da
Opis tiketa. Tekstualnog tipa (string).
U slučaju "fiks" tiketa sistem je n/n pri čemu n predstavlja broj događaja na tiketu.
U slučaju "sistemskog" tiketa sistem je m/n.
U slučaju da se tiket sastoji od kombinacija (fiks + sistem ili više sistema)
kombinacije se razvdajaju zarezom (,) - prijmer n1/n1,m2/n2.
U slučaju multisistema prvi elementi se razdvajaju plusom (+) - primjer m1+m2/n2.
nc
da
Broj kombinacija na tiketu. Cijeli broj (integer).
ac
da
Uplata po kombinaciji. Maksimalno 2 decimalne cifre (float, decimal, double).
e
da
Niz događaja koji se nalaze na tiketu.
Niz e predstavlja grupe koje su definisane u polju sy i shodno tome ima određeni broj elemenata. Svaki element predstavlja niz događaja za jednu grupu. Primjer - u slučaju n1/n1,m2/n2 niz e će imati dva člana, pri čemu će prvi član biti niz događaja od n1 elemenata, a drugi član niz događaja od n2 elemenata.
Postoje dva tipa elemenata:

element vezan za sportsko klađenje,

element vezan za igre brojeva.
Elemenat vezan za sportsko klađenje
Ime polja
Obavezno
Opis h
*
Domaćin. Tekstualnog tipa (string).
a
*
Gost. Tekstualnog tipa (string).
c
*
Takmičar. Tekstualnog tipa (string).
ot
*
Antepost. Tekstualnog tipa (string).
s
da
Sport za koji je vezan događaj. Tekstualnog tipa (string).
ct
Takmičenje za koje je vezan događaj. Tekstualnog tipa (string).
st
da
Vrijeme transakcije sa vremenskom zonom 2020-05-25T08:48:28+02:00 (primjer u
vremenskoj zoni Crne Gore)
2020-05-25T08:48:28Z (primjer u UTC formatu) o
da
Niz ishoda. Ishodi su tekstualnog tipa (string).
od
da
Niz kvota. Kvote imaju maksimalno 3 decimalne cifre (float, decimal, double).
* Zavisno od tipa događaja. Potrebno je poslati:

za dualne događaje - h, a

za događaje vezane za takmičare - c (mogu se poslati i h, a)

za događaje vezane za antepost (outright) - ot Elemenat vezan za igre brojeva
Ime polja
Obavezno
Opis cm
da
Niz brojeva koji su odigrani (predstavljen kao tekst pri čemu su brojevi razdvojeni
zarezom) ili opis specijalne kombinacije ako nisu odigrani brojevi (primjer: odd, even,
red_ball, ...) od
*
Niz kvota. Kvote imaju maksimalno 3 decimalne cifre (float, decimal, double).
*obavezno za igre koje imaju kvote (primjer Grčki kino). Nije obavezno za igre gdje se dobitak određuje na osnovu redosljeda izvlačenja (primjer Lucky6)
Primjeri
Primjer tiketa sportskog klađenja:
{ "transaction_time": "2020-05-20T20:15:25+02:00", "transaction_id": "89f5b9f0-ac80-4cfe-9b7a-9fd96e264468", "transaction_amount": 200, "betting_place_id": "2c2aa9eb", "sticker_no": "0002231", "min_odds": 9.79855987, "max_odds": 9.79855988, "min_win": 1959.71, "max_win": 1959.71, "min_bonus": 97.98, "max_bonus": 97.98, "max_payout": 2057.69, "game_name": "sports_betting", "ticket_id": "123-333-11qa", "bet_type": "real", "source": "Landbase", "ticket": { "sd": "5/5", "nc": 1, "ac": 200, "e": [ [ {"h": "Man.City", "a": "Man.Utd.", "s": "fudbal", "ct": "Engleska 1", "st": "2020-05-20T20:30:00+02:00", "o": ["KI1"], "od": [1.51]}, {"h": "Liverpool", "a": "Arsenal", "s": "fudbal", "ct": "Engleska 1", "st": "2020-05-20T20:30:00+02:00", "o": ["KI2"], "od":
[1.70]}, {"h": "Chelsea", "a": "Everton", "s": "fudbal", "ct": "Engleska 1", "st": "2020-05-20T20:30:00+02:00", "o": ["1-1&3+"], "od": [1.95]}, {"h": "Real.M.", "a": "Barcelona", "s": "fudbal", "ct": "Španija 1", "st": "2020-05-20T20:30:00+02:00", "o": ["ppGG"], "od": [1.45]}, {"h": "Valencia", "a": "Atletico.M.", "s": "fudbal", "ct": "Španija 1", "st": "2020-05-20T20:30:00+02:00", "o": ["h1(1)"], "od": [2.35]} ] ] } }
Primjer anteposta s web-а:
{ ...
"game_name": "sports_betting", "ticket": { "sd": "1/1", "nc": 1, "ac": 200, "e": [ [{"ot": "Čelzi osvaja Englesku 1 - 2020", "s": "fudbal", "st": "2020-05-20T20:30:00+02:00" "od": [5]}] ] }}
Primjer tiketa igre greek kino:
{ ...
"game_name": "greek_kino", "ticket": { "sd": "3/3", "nc": 1, "ac": 200, "e": [ [ {"cm": "2,22,32", "od": [3.5]} ] ] }}
Primjer tiketa igre greek kino br. 2:
{ ...
"game_name": "greek_kino", "ticket": { "sd": "1/1", "nc": 1, "ac": 200, "e": [ [ {"combination": "even_sum", "od": [2.5]} ] ] }}
Putanja /betting/win
Putanja skuplja sve isplatne transakcije vezane za dobitak na tiketu. Pored pomenutih podataka potrebno je poslati još i:
Ime polja
Obavezno
Opis
bet_transaction_id
*
ID referentne uplatne transakcije. Tekstualnog tipa
(string).
ticket_id
*
ID tiketa za koji se isplaćuje isplata. Tekstualnog tipa
(string).
win_odds
da
Dobitna kvota. Maksimalno 2 decimalne cifre
(float, decimal, double).
win_type
da
Polje obilježava tip dobitka (Regular, Cashback, Cashout)
bonus
da
Bonus osvojen na tiketu u EUR. Maksimalno 2 decimalne cifre
(float, decimal, double).
cancel
da
Polje koje može imati vrijednosti true i false zavisno od toga da li je na
tiketu bilo događaja koji su odloženi ili prekinuti.
canceled_events
U slučaju da cancel polje ima vrijednost true potrebno je poslati niz
događaja koji su odloženi ili prekinut. Format jednog događaja je isti kao i
u pozivu /betting/bet.
* Jedno od ova dva polja je obavezno. Preferenca je da se pošalju oba.
Primjeri
Primjer isplatne transakcije:
{
"transaction_time": "2020-05-21T20:00:00+02:00",
"transaction_id": "0eda1e35-78a7-4e3b-b727-1ce105507d1b",
"transaction_amount": 2057.69,
"betting_place_id": "2c2aa9eb",
"sticker_no": "0002231",
"game_name": "sports_betting",
"bet_transaction_id": "89f5b9f0-ac80-4cfe-9b7a-9fd96e264468",
"ticket_id": "123-333-11qa",
"win_odds": 9.79855987,
"win_type": "regular",
"bonus": 97.98,
"promo_amount": 0,
"cancel": false,
"source": "Landbase"
}
Primjer isplatne transakcije sa odloženom jednom utakmicom:
{
"transaction_time": "2020-05-21T20:00:00+02:00",
"transaction_id": "0eda1e35-78a7-4e3b-b727-1ce105507d1b",
"transaction_amount": 1362.7,
"betting_place_id": "2c2aa9eb",
"sticker_no": "0002231",
"game_name": "sports_betting",
"bet_transaction_id": "89f5b9f0-ac80-4cfe-9b7a-9fd96e264468", "ticket_id": "123-333-11qa",
"win_odds": 6.4891125,
"win_type": "regular",
"bonus": 0,
"promo_amount": 0,
"cancel": true,
"source": "Landbase",
"canceled_events": [
[
{"h": "Man.City", "a": "Man.Utd.", "s": "fudbal", "ct": "Engleska 1", "st": "2020-05-20T20:30:00+02:00", "o": ["KI1"], "od":
[1]}
]
]
}
Putanja /betting/rollback
Putanja skuplja sve transakcije vezane za poništavanje transakcije (storniranje tiketa, greška pri isplati). Pored
pomenutih podataka potrebno je poslati još i:
Ime polja
Obavezno
Opis
rollback_ transaction_id
*
ID referentne transakcije. Tekstualnog tipa (string).
ticket_id
*
ID tiketa za koji se vrši poništavanje. Tekstualnog tipa (string).
rollback_transaction_type
da
Polje koje može imati vrijednosti Bet, Win i Jackpot zavisno od toga koji se
tip transakcije stornira.
* Jedno od ova dva polja je obavezno. Preferenca je da se pošalju oba.
Primjeri
Primjer storno transakcije:
{
"transaction_time": "2020-05-20T20:17:15+02:00",
"transaction_id": "e92b8fc1-5d88-44d4-b84e-39a7bdf6afd7",
"transaction_amount": 200,
"betting_place_id": "2c2aa9eb",
"sticker_no": "0002231",
"rollback_transaction_id": "46232c94-5fe0-4222-aaaa-358aec52f860",
"ticket_id": "31267832-32ds-vda",
"game_name": "sports_betting", "source": "Landbase"
}
Putanja /betting/jackpot
Putanja skuplja sve transakcije vezane za dobitak džekpot-a. Pored pomenutih podataka potrebno je poslati još i:
Ime polja
Obavezno
Opis
bet_transaction_id
*
ID referentne uplatne transakcije. Tekstualnog tipa (string).
ticket_id
*
ID tiketa za koji se isplaćuje isplata. Tekstualnog tipa (string).
* Jedno od ova dva polja je obavezno. Preferenca je da se pošalju oba.
Primjeri
Primjer džekpot transakcije:
{
"transaction_time": "2020-05-20T20:17:26",
"transaction_id": "1f14d3b1-069e-4117-8ea5-27a339fe4ea7",
"transaction_amount": 10000,
"jmb": "1101999710111",
"bet_transaction_id": "e7681632-e804-4f40-b62a-980fdebfda9c",
"ticket_id": "324dsv-23",
"game_name": "greek_kino",
"source": "Web"
}
Putanja /slot API putanje koje počinju sa /slot/ odnose se na podatke koji se prikupljaju u realnom vremenu iz automat klubova, kao i sa automata koji se nalaze u kazinima.
U okviru /slot putanja imamo 4 konkretne akcije:

/slot/deposit (uplata);

/slot/withdraw (isplata);

/slot/jackpot (džekpot);

/slot/rollback (poništavanje).
Za sve transakcije je potrebno poslati:
Ime polja
Obavezno
Opis
transaction_time
da
vrijeme transakcije sa vremenskom zonom
2020-05-25T08:48:28+02:00 (primjer u vremenskoj zoni Crne Gore)
2020-05-25T08:48:28Z (primjer u UTC formatu)
transaction_id
da
ID transakcije iz sistema priređivača. Tekstualnog tipa (string) transaction_amount
da
Vrijednost transakcije u EUR. Maksimalno 2 decimalne cifre (float,
decimal, double).
transaction_type
Tip transakcije. Tekstualnog tipa (string). Potrebno je naznačiti kako
je izvršena transakcija, da li je u pitanju akceptor novca, uplata
kredita i slično.
slot_club_id
da
Id slot kluba (dodjeljuju se pri integraciji, a ubuduće će biti dostavljen
na rješenju)
sticker_no
da
Broj oznake za automat dodijeljen od strane ovlašćene laboratorije.
jmb
*
Jedinstveni matični broj građanina igrača koji je odigrao tiket.
Podložno provjeri o ispravnosti JMB-a.
passport_number
*
Broj pasoša ili lične karte igrača koji je odigrao tiket. Tekstualnog tipa
(string).
identification_document_countr y
*
Zemlja izdavanja pasoša ili lične karte. Tekstualnog tipa (string).
identification_document_type
*
Vrsta identifikacionog dokumenta. Moguće vrijednosti su {ID card,
Passport}. Tekstualnog tipa (string)
*Za transakcije iznad iznosa od 2000 EUR, potrebno je poslati identifikaciju igrača u vidu polja jmb, ili kombinacije identification_document_number, identification_document_country, identification_document_type
Putanja /slot/rollback
Putanja skuplja sve transakcije vezane za storniranje. Pored pomenutih podataka potrebno je poslati još i:
Ime polja
Оbavezno
Оpis
rollback_ transaction_id
da
Id refrerentne transakcije koja se poništava
rollback_transaction_type
*
Informacija o tipu transakcije koja se stornira (Deposit, Withdrawal,
Jackpot)
* Neobavezno polje, koje će nakon usklađivanja postati obavezno
Putanja /slot/jackpot
Putanja skuplja sve transakcije vezane za dobitak džekpot-a. Pored pomenutih podataka potrebno je poslati još i:
Ime polja
Obavezno
Opis
transaction_withdraw_amount
da
Vrijednost isplaćena kroz promet aparata u EUR. Maksimalno 2
decimalne cifre (float, decimal, double).
Primjeri
Primjer uplatne transakcije (/slot/deposit):
{
"transaction_time": "2020-05-20T20:15:25",
"transaction_id": "64acdf63-45ff-44d5-a38b-a20c3d7151a1",
"transaction_amount": 1001,
"passport_number":"12345",
"identification_document_country":"DZA",
"identification_document_type": "Passport",
"transaction_type": "deposit_acceptor",
"slot_club_id": "2c2aa9eb",
"sticker_no": "0123456"
}
Primjer isplatne transakcije (/slot/withdraw):
{
"transaction_time": "2020-05-20T20:15:25",
"transaction_id": "64acdf63-45ff-44d5-a38b-a20c3d7151a1",
"transaction_amount": 1001,
"passport_number":"09876",
"identification_document_country":"BEL",
"identification_document_type": "ID card",
"transaction_type": "withdraw_acceptor",
"slot_club_id": "8944e0d4",
"sticker_no": "0002234"
}
Primjer stornirane transakcije (/slot/rollback):
{
"transaction_time": "2020-05-20T20:15:25",
"transaction_id": "64acdf63-45ff-44d5-a38b-a20c3d7151a2",
"transaction_amount": 990,
"transaction_type": "withdraw_acceptor",
"slot_club_id": "8944e0d4", "sticker_no": "0002234",
"rollback_transaction_id": "64acdf63-45ff-44d5-a38b-a20c3d7151a1"
}
Primjer džekpot transakcije (/slot/jackpot):
{
"transaction_time": "2020-05-20T20:15:25",
"transaction_id": "64acdf63-45ff-44d5-a38b-a20c3d7151a1",
"transaction_amount": 25000,
"jmb":"0106972752051"
"transaction_withdraw_amount": 15000,
"slot_club_id": "8944e0d4",
"sticker_no": "0002234"
}
Putanja /slot-periodic
API putanja služi da se periodično šalju informacije o brojačima na slot mašinama priređivača. Potrebno je slati informacije na svakih 300 sekundi. Potrebno je poslati:
Ime polja
Obavezno
Opis
date
da
vrijeme transakcije sa vremenskom zonom 2020-05-25T08:48:28+02:00
(primjer u vremenskoj zoni Crne Gore)
2020-05-25T08:48:28Z (primjer u UTC formatu)
machines
da
niz automata koje priređivač ima u sistemu
Izgled jednog elementa niza machines:
Ime polja
Obavezno
Opis
sn
da
Broj oznake za automat dodijeljen od strane ovlašćene laboratorije.
pi
da
Vrijednost brojača za uplatu.
po
da
Vrijednost brojača za isplatu.
b
da
Vrijednost brojača za opklade.
w
da
Vrijednost brojača za dobitak.
g
da
Vrijednost brojača za broj igara.
j
da
Vrijednost brojača za džekpot.
dn
da
Denominacija, vrijednost poena u EUR
Maksimalno 4 decimalne cifre (float, decimal, double)
Kada se npr. vrijednost brojača za uplatu pomnoži ovim brojem dobija se ukupna
vrijednost uplate u EUR.
Primjeri
Primjer sa 3 automata:
{"date": "2020-05-25T10:05:00.000000+02:00",
"machines": [{
"sn": "001232141",
"pi": 12300,
"po": 2300,
"b": 123000,
"w": 113450,
"g": 22222,
"j": 234512,
"dn": 0.1
},{
"sn": "001232142",
"pi": 12412,
"po": 1200,
"b": 223000,
"w": 213450,
"g": 22444,
"j": 236512,
"dn": 0.1
},{
"sn": "001232222",
"pi": 12412,
"po": 1200,
"b": 223000,
"w": 213450,
"g": 22444,
"j": 236512,
"dn": 0.1
}]}
Putanja /online-slot
API putanja služi da prikuplja informacije vezano za igre na sreću u virtualnim kazinima ili na virtualnim automatima. Na ovu rutu priređivači šalju jedan zahtjev na svakih 300 sekundi. Potrebno je poslati:
Ime polja
Obavezno
Opis
start_date
da
vrijeme početka perioda zbirne transakcije sa vremenskom zonom 2020-
05-25T08:48:28+02:00 (primjer u vremenskoj zoni Crne Gore)
2020-05-25T08:48:28Z (primjer u UTC formatu)
end_date
da
vrijeme kraja perioda zbirne transakcije sa vremenskom zonom 2020-05-
25T08:48:28+02:00 (primjer u vremenskoj zoni Crne Gore)
2020-05-25T08:48:28Z (prijmer u UTC formatu)
batch_id
*
oznaka ove agregirane transakcije. Ukoliko se pošalje transakcija sa
identičnim identifikatorom, biće ignorisana.
sessions
da
niz sesija koje su se desile unutar pomenutog perioda
* Ukoliko je polje prazno, transakcija neće biti odbijena, niti ignorisana. Nakon prilagođavanja integracije priređivača
polje će postati obavezno.
Izgled jednog elementa sesije:
Ime polja
Obavezno
Opis
jmb
*
jedinstveni matični broj građanina igrača koji je odigrao tiket. Podložno proveri o
ispravnosti JMB-a.
Potrebno ukoliko je u pitanju uplata sa veb-a i ukoliko je igrač državljanin Crne Gore.
pn
*
broj pasoša igrača koji je odigrao tiket. Tekstualnog tipa (string).
Potrebno ukoliko je u pitanju uplata sa veb-a i ukoliko igrač nije državljanin Crne Gore.
idc
*
Zemlja izdavanja pasoša ili lične karte. Tekstualnog tipa (string).
idt
*
Vrsta identifikacionog dokumenta. Moguće vrijednosti su {ID card, Passport}. Tekstualnog
tipa (string)
ftd
da
vrijeme prve transakcije sa vremenskom zonom 2020-05-25T08:48:28+02:00 (primjer u
vremenskoj zoni Crne Gore)
2020-05-25T08:48:28Z (primjer u UTC formatu)
ltd
da
vrijeme poslednje transakcije sa vremenskom zonom 2020-05-25T08:48:28+02:00
(primjer u vremenskoj zoni Crne Gore)
2020-05-25T08:48:28Z (primjer u UTC formatu)
tb
da
ukupan ulog koji je igrač ostvario u pomenutom periodu u EUR. Maksimalno 2 decimalne
cifre (float, decimal, double).
tw
da
ukupan dobitak koji je igrač ostvario u pomenutom periodu u EUR. Maksimalno dvije
decimalne cifre (float, decimal, double)
trb
da
suma poništenih bet transakcija koje su se dogodile igraču u pomenutom periodu u EUR.
Maksimalno dvije decimalne cifre (float, decimal, double).
trw
da
suma poništenih win transakcija koje su se dogodile igraču u pomenutom periodu u EUR.
Maksimalno dvije decimalne cifre (float, decimal, double).
tpb
da
suma promo bet transakcija koje su se dogodile igraču u pomenutom periodu u EUR.
Maksimalno dvije decimalne cifre (float, decimal, double).
tj
da
Ukupan džekpot ostvaren u pomenutom periodu u EUR. Maksimalno dvije decimalne cifre
(float, decimal, double).
tr
da
rezultat koji je priređivač ostvario vezano za ovog igrača u EUR. Maksimalno dvije
decimalne cifre (float, decimal, double).
gs
Niz sesija po igri unutar sesije
* Potrebno je poslati ili JMB (za državljane Crne Gore), ili kombinaciju pn i idc i idt (za nerezidente), tačnije broj pasoša ili lične karte, zemlju izdavanja pasoša ili lične karte, vrstu identifikacionog dokumenta.
Izgled jednog elementa sesije po igri (gs):
Ime polja
Obavezno
Opis
gn
da
Naziv odigrane igre
ftd
da
Vrijeme prve transakcije sa vremenskom zonom
2020-05-25T08:48:28+02:00 (primjer u vremenskoj zoni Crne Gore)
2020-05-25T08:48:28Z (primjer u UTC formatu)
ltd
da
Vrijeme transakcije sa vremenskom zonom
2020-05-25T08:48:28+02:00 (primjer u vremenskoj zoni Crne Gore)
2020-05-25T08:48:28Z (primjer u UTC formatu)
tb
da
Ukupan ulog u EUR koji je igrač ostvario u pomenutom periodu Maksimalno dvije decimalne cifre (float, decimal, double)
tw
da
Ukupan dobitak u EUR koji je igrač ostvario u pomenutom periodu Maksimalno dvije
decimalne cifre (float, decimal, double)
trb
da
Suma poništenih bet transakcija u EUR, koje su se dogodile igraču u pomenutom periodu
Maksimalno dvije decimalne cifre (float, decimal, double)
trw
da
Suma poništenih win transakcija u EUR, koje su se dogodile igraču u pomenutom periodu
Maksimalno dvije decimalne cifre (float, decimal, double)
tpb
da
Suma promo bet transakcija u EUR, koje su se dogodile igraču u pomenutom periodu
Maksimalno dvije decimalne cifre (float, decimal, double)
tj
da
Ukupan iznos jackpot-a u EUR ostvaren u pomenutom periodu Maksimalno dvije decimalne cifre (float, decimal, double)
tr
da
Rezultat u EUR, koji je priređivač ostvario u ovom periodu Maksimalno dvije decimalne cifre (float, decimal, double)
Primjeri
Primjer za sesiju u kojoj su bila aktivna dva igrača:
{"start_date": "2020-05-25T10:00:00",
"end_date": "2020-05-25T10:05:00", "batch_id": "bid123322123",
"sessions": [{
"jmb": "1111001750022",
"ftd": "2020-05-25T10:00:25",
"ltd": "2020-05-25T10:04:33",
"tb": 12300.00,
"tw": 11345.54,
"trb": 955.54,
"trw": 0,
"tpb": 0,
"tj": 0,
"tr": 1.08,
"gs": [{
"gn": "Pragmatic Play - Sweet Bonanza",
"ftd": "2020-05-25T10:00:25",
"ltd": "2020-05-25T10:04:33",
"tb": 12300.00,
"tw": 11345.54,
"trb": 955.54,
"trw": 0,
"tpb": 0,
"tj": 0,
"tr": 1.08
}]
},{
"pn": "123456",
"idc": "AUT",
"idt": "Passport",
"ftd": "2020-05-25T10:02:12",
"ltd": "2020-05-25T10:04:48",
"tb": 1000.00,
"tw": 3542.12,
"trb": 0,
"trw": 0.12,
"tpb": 0,
"tj": 0,
"tr": -2542.00, "gs": [{
"gn": "Pragmatic Play - Sweet Bonanza",
"ftd": "2020-05-25T10:02:12",
"ltd": "2020-05-25T10:04:48",
"tb": 500.00,
"tw": 3542.12,
"trb": 0,
"trw": 0.12,
"tpb": 0,
"tj": 0,
"tr": -3042.00
},{
"gn": "Play n Go - Book of dead",
"ftd": "2020-05-25T10:00:25",
"ltd": "2020-05-25T10:04:33",
"tb": 500.00,
"tw": 0,
"trb": 0,
"trw": 0,
"tpb": 0,
"tj": 0,
"tr": 500.00
}]
}]}
Putanja /online-slot/daily
API putanja služi za slanje sumirane dnevne transakcije za online kazino. Putanja prima identične podatke kao i putanja /online-slot ali je potrebno da period obuhvata cijeli dan (od 00:00:00 do 23:59:59).
Putanja /online-player/
API putanja služi da zabilježi sve uplate i isplate na račun igrača u realnom vremenu za igre na sreću putem interneta.
U okviru /online-player putanja imamo 4 konkretne akcije:

/online-player/deposit (uplata);

/online-player/withdraw (isplata);

/online-player/promo (dobitak promo novca);

/online-player/rollback (poništavanje).
Potrebno je poslati:
Ime polja
Obavezno
Opis
transaction_time
da
vrijeme transakcije sa vremenskom zonom 2020-05-
25T08:48:28+02:00 (primjer u vremenskoj zoni Crne Gore)
2020-05-25T08:48:28Z (primjer u UTC formatu)
transaction_id
da
ID transakcije iz sistema priređivača. Tekstualnog tipa (string)
transaction_amount
da
Vrijednost transakcije u EUR. Maksimalno 2 decimalne cifre (float,
decimal, double).
jmb
*
jedinstveni matični broj građanina igrača koji je uplatio ili podigao.
Podložno provjeri o ispravnosti JMB-a.
Potrebno ukoliko je u pitanju transakcija sa veb-a i ukoliko je igrač
državljanin Crne Gore.
passport_number
*
broj pasoša ili lične karte igrača koji je odigrao tiket. Tekstualnog tipa
(string).
Potrebno ukoliko je u pitanju transakcija sa veb-a i ukoliko je igrač nije
državljanin Crne Gore.
identification_document_countr y
*
Zemlja izdavanja pasoša ili lične karte. Tekstualnog tipa (string).
identification_document_type
*
Vrsta identifikacionog dokumenta. Moguće vrijednosti su {ID card,
Passport}. Tekstualnog tipa (string)
balance_after_ transaction
da**
Balans korisnika nakon izvršene transakcije u EUR
* Unosi JMB ili broj dokumenta, vrsta dokumenta ili država izdavanja dokumenta
** Ne šalje se u slučaju da se prijavljuje promo transakcija, u suprotnom je obavezno.
Putanja /online-player/deposit
Pored pomenutih podataka potrebno je dodatno poslati i:
Ime polja
Obavezno
Opis
deposit_type
*
Način uplate sredstava na evidencioni račun
(Account transfer, On site payment, Prepaid card, Third party, Other)
deposit_details
**
Dodatni detalji o samoj uplati
U zavisnosti od vrijednosti deposit_type, potrebno je poslati sledeće:
Account transfer - Broj računa sa kojeg je izvršena uplata
On site payment - Broj oznake kladionice sa koje je izvršena uplata
Prepaid card - Identifikacioni broj iskorišćene kartice
Third party - Dodatni podaci o mestu sa koga je izvršena uplata, kao na
primjer identifikator, ili lokacija i naziv
Other - Dodatni podaci, ukoliko postoje
* Account transfer - predstavlja prenos sredstava sa računa igrača, On site payment - predstavlja uplatu sredstava preko uplatnog mesta priređivača, Prepaid card - predstavlja uplatu putem prepaid kartica, Third party - predstavlja uplatu preko posrednika, npr. trafike, Other - ukoliko ni jedan od prethodnih tipova ne odgovara, ovo je oznaka transakcije. Polje će postati obavezno nakon prilagođavanja integracija priređivača.
Primjeri
Primjer transakcije (depozit):
{
"transaction_time": "2020-05-20T20:00:25",
"transaction_id": "64acdf63-45ff-44d5-a38b-a20c3d7151a1",
"transaction_amount": 10000,
"jmb": "1101001710234",
"source": "Betting"
"balance_after_transaction": 10500
}
Putanja /online-player/rollback
Putanja skuplja sve transakcije vezane za storniranje. Pored pomenutih podataka potrebno je poslati još i:
Ime polja
Obavezno
Opis
rollback_ transaction_id
da
Id refrerentne transakcije koja se poništava
rollback_transaction_type
da
Informacija o tipu transakcije koja se stornira (Deposit, Withdrawal, Promo)
Primjeri
Primjer transakcije (rollback):
{
"transaction_time": "2020-05-20T20:02:33",
"transaction_id": "eccf92e3-676e-415a-809e-62f46830215c",
"transaction_amount": 10000,
"passport_number": "123456",
"identification_document_country ": "AUT",
"passport_number": "Passport",
"source": "Betting",
"balance_after_transaction": 9500,
"rollback_transaction_id": "64acdf63-45ff-44d5-a38b-a20c3d7151a1"
}
