PRILOG
PROCEDURE
knjiženja uplata i isplata gotovine u radu Banke i Agenta u platnom prometu
a) Procedura preuzimanja dotacije i
otpremanje suvišaka
1) Preuzimanje dotacije za potrebe blagajne Pošte
Kad Pošta preuzima dotaciju kod Banke iz blagajne-trezora Banke, ispostavlja nalog za isplatu Banci.
Knjiženje na osnovu iniciranog naloga:
- duguje 110 - račun dotacija gotovine Pošti
- potražuje 100 - račun gotovine u blagajni-trezoru Banke
Za primljenu dotaciju, Pošta ispostavlja nalog za uplatu Banci:
Knjiženje na osnovu iniciranog naloga:
- duguje 101 - račun gotovine banke kod Pošte
- potražuje 110 - račun dotacija gotovine Pošti
2) Otprema suvišaka Pošte
Kad Pošta otpremi suvišak Banci, ispostavlja Banci nalog za isplatu.
Knjiženje na osnovu iniciranog naloga:
- duguje 111 - račun suvišaka gotovine Pošte
- potražuje 101 - račun gotovine banke kod Pošte
Kada Pošta uplaćuje suvišak Banci, ispostavlja Banci nalog za uplatu.
Knjiženje na osnovu iniciranog naloga:
- duguje 100 - račun gotovine u blagajni-trezoru Banke
- potražuje 111 - račun suvišaka gotovine Pošte
b) Procedura uplate i isplate gotovine preko Pošte
1) Uplata gotovine
Kada fizičko lice uplaćuje gotovinu, ispostavlja nalog za uplatu Pošti.
Knjiženje na osnovu iniciranog naloga:
- duguje 101 - račun gotovine Banke kod Pošte
- potražuje račun klijenta (npr. 601)
Ispostavljanjem naloga za uplatu, Pošta uplaćuje Banci gotovinu.
Knjiženja na osnovu softverski generisanih naloga:
- duguje 509 - račun zbirnog obračuna sredstava deponenata
- potražuje 620 - poslovni račun Banke
- duguje 620 - poslovni račun Banke
- potražuje 103 - račun zbirnog obračuna gotovine deponenata Banke
2) Isplata gotovine fizičkim licima
Kada isplatilac prenosi sredstva sa svog poslovnog računa XXX na račun Banke za isplatu preko Pošte (sa osnovnom oznakom 533), ispostavlja nalog za prenos.
Knjiženje na osnovu iniciranog naloga:
- duguje XXX - poslovni račun isplatioca (Banka X)
- potražuje 533 - račun Banke za isplatu preko Pošte
Knjiženja na osnovu softverski generisanih naloga:
- duguje 620 - poslovni račun Banke X
- potražuje 509 - račun zbirnog obračuna sredstava deponenata (Banka X)
- duguje 509 - račun zbirnog obračuna sredstava
deponenata Banke
- potražuje 620 - poslovni račun Banke kod koje je Pošta deponent
Pošta preuzima dotaciju kod Banke za potrebe isplate fizičkih lica (penzija) i ispostavlja Banci nalog za isplatu.
Knjiženje na osnovu iniciranog naloga:
- duguje 110 - račun dotacija Banke kod Pošte
- potražuje 100 - račun gotovine u blagajni-trezoru Banke
Za primljenu dotaciju, Pošta ispostavlja Banci nalog za uplatu.
Knjiženje na osnovu iniciranog naloga:
- duguje 101 - račun gotovine Banke kod Pošte
- potražuje110 - račun dotacija gotovine Pošti
Po izvršenoj isplati penzija, Pošta ispostavlja Banci nalog za prenos.
Knjiženje na osnovu iniciranog naloga:
- duguje 533 - račun za isplatu preko Pošta
- potražuje 101 - račun gotovine Banke kod Pošte
Knjiženje na osnovu softverski generisanih naloga:
- duguje 620 - poslovni račun Banke
- potražuje 509 - račun zbirnog obračuna sredstava deponenata Banke
- duguje 103 - račun zbirnog obračuna gotovine deponenata Banke
- potražuje 620 - poslovni račun Banke
c) Procedura utvrđivanja blagajničkih manjkova ili viškova u Dnevniku uplata i isplata i Stanju kase
Nakon utvrđenog manjka u Stanju kase u odnosu na Dnevnik uplata, Banka ispostavlja nalog za prenos.
Knjiženje na osnovu iniciranog naloga za utvrđeni manjak:
- duguje 187 - račun obračuna blagajnički manjkovi kod Pošta
- potražuje 101 - račun gotovine Banke kod Pošte
Da zatvori račun 187, Banka ispostavlja naloge za prenos sredstava.
Knjiženje na osnovu iniciranog naloga:
- duguje 538 - račun otvorenih stavki kod Pošte
- potražuje 187 - račun obračuna blagajničkih manjkova kod Pošta
Nakon utvrđenog viška u Stanju kase u odnosu na Dnevnik uplate, Banka ispostavlja naloge za prenos.
Knjiženje na osnovu iniciranog naloga:
- duguje 101 - račun gotovine Banke kod Pošte
- potražuje 188 - račun obračuna blagajničkih viškova kod Pošte
Da zatvori račun 188, Banka ispostavlja nalog za prenos.
Knjiženje na osnovu iniciranog naloga:
- duguje 188 - račun obračuna blagajničkih viškova kod Pošte
- potražuje 538 - račun otvorenih stavki kod Pošte
d) Procedura rada se netačnim i nejasnim plaćanjima
Kada se ustanovi da nalozi za uplatu, odnosno nalozi za isplatu ne mogu biti izvršeni, Banka, odnosno Centralna banka - Platni promet, ako Banka nije uočila grešku ili propust, ispostavlja naloge za prenos.
Knjiženje na osnovu iniciranog naloga za sporne naloge iz Dnevnika uplata:
- duguje 101 - račun gotovine Banke kod Pošte
- potražuje 538 - račun otvorenih stavki kod Pošte
Knjiženje na osnovu iniciranog naloga iz Dnevnika isplata:
- duguje 538 - račun otvorenih stavki kod Pošte
- potražuje 101 - račun gotovine Banke kod Pošte
