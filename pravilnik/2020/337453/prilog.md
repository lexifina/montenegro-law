OBRAZAC 1
OPŠTI PODACI OBVEZNIK FISKALIZACIJE PIB ADRESA
PRIJAVA OZNAKE OPERATERA
Oznaka obrasca
PRIJAVA
DOPUNA
ODJAVA
PROMJENA
RED
BR
OZNAKA
OPERATERA
MBG
IME I PREZIME
ADRESA
DATUM
PODACI O POSLOVNICI
POSEBNOSTI
OZNAKA
PROMJENJIVO
DATUM POPUNJAVANJA Potpis i pečat _________________________ _________________________________ Uputstvo za popunjavanje:
1. Opšti podaci - Obveznik fiskalizacije popunjava podatke - ime i prezime/naziv, PIB i adresa 2. Oznaka obrasca - obveznik fiskalizacije stavlja oznaku x kod:
-
prijava - kod prve prijave
-
dopuna - za prijavu novog operatera, pri čemu ostaju vrijediti svi do sada prijavljeni podaci kroz prijavu ili ranije
nadopune
-
odjava - ako se popunjavaju podaci za operatora koji se odjavljuje
-
promjena - ako se za postojećeg operatora navodi promjena nekog od podataka 3. Red br - stavlja se oznaka rednog broja 4. Oznaka operatora - određuje obveznik fiskalizacije kao alfanumerički zapis od 6 znakova koja se prikazuje na fiskalnom računu 5. JMB - upisuje se JMB operatora 6. Ime i prezime - upisuje se ime i prezime operatora 7. Adresa - upisuje se adresa prebivališta operatora 8. Datum - upisuje se datum od kada vrijedi promjena koja se prijavljuje 9. Podaci o poslovnici - upisuje se oznaka poslovnici gdje će operator raditi te se stavlja oznaka ukoliko operator mijenja poslovnicu u kojoj radi 10. Posebnosti - upisuje se odnos operator prema obvezniku fiskalizacije ukoliko se ne radi o radnom odnosu
PRILOG 1
PRIJAVA OZNAKE OPERATORA FISKALNOG SERVISA RADI IDENTIFIKACIJE OPERATORA
Obveznik fiskalizacije treba da oznaku operatora poveže sa jedinstvenim matičnim brojem lica koje izdaje račun.
Oznaku operatora određuje obveznik fiskalizacije kao alfanumerički zapis od šest znakova koja se prikazuje na fiskalnom računu. Određenu oznaku operatora povezanu sa jedinstvenim matičnim brojem operatora, obveznik fiskalizacije dostavlja Upravi korišćenjem aplikacije za podršku fiskalizaciji.
Oznaka operatora povezana je jedinstvenim matičnim brojem za lice i obveznik fiskalizacije jednom dodijeljenu i korišćenu oznaku operatora ne može da dodijeli drugom licu odnosno operatoru.
Ako operator nije lice u radnom odnosu kod obveznika fiskalizacije taj podatak se navodi u Prijavi oznake operatora uz naznaku odnosa o kojem se radi.
Obveznik fiskalizacije dostavlja Prijavu oznake operatora najkasnije 24 sata prije početka izdavanja računa, odnosno najkasnije 24 sata prije promjene bilo kojeg od podataka koji se prijavljuje putem Prijave oznake operatora.
Ako je operator sam obveznik fiskalizacije kao fizičko lice ili se radi o samonaplatnom uređaju (automatu) kod dostave poruke zahtjeva podatak o operatoru navodi se jedinstveni matični broj fizičkog lica obveznika fiskalizacije.
PRILOG 2
GENERISANJE PODATAKA O IDENTIFIKACIONOM KODU OBVEZNIKA FISKALIZACIJE PRILIKOM IZDAVANJA
FISKALNOG RAČUNA
Identifikacioni kod obveznika fiskalizacije je alfanumerički zapis kojim se potvrđuje veza između obveznika fiskalizacije i izdatog fiskalnog računa.
Identifikacioni kod obveznika fiskalizacije generiše obveznik fiskalizacije, odnosno programsko rješenje koje obveznik fiskalizacije koristi za fiskalizaciju i dostavlja ga prilikom fiskalizacije računa Sistemu eFiskalizacije.
Identifikacioni kod obveznika fiskalizacije iz stava 2 ovog priloga nakon dostavljanja sistemu eFiskalizacije ispisuje se na fiskalnom računu.
Identifikacioni kod obveznika fiskalizacije se generiše na osnovu sljedećih podataka:
1)
PIB obveznika,
2)
datum i vrijeme izdavanja fiskalnog računa,
3)
redni broj fiskalnog računa,
4)
jedinstvena identifikaciona oznaka programskog rješenja i
5)
ukupni iznos računa
Prilikom generisanja identifikacionog koda obveznika fiskalizacije koristi se UTF-8 kodiranje (Unicode Transformation Format 8), a za upis datuma i vremena upisuju se lokalni datum i vrijeme u formatu standard ISO 8601.
Radi generisanja identifikacionog koda obveznika fiskalizacije koristi se MD5 kriptografska hash funkciju (po standardu RFC 1321 The MD5 Message-Digest Algorithm).
Korišćenjem MD5 kriptografska hash funkcije iz stava 6 ovog priloga dobija se 32-znaka u heksadecimalnom formatu (brojevi 0-9 i mala slova a-f).
