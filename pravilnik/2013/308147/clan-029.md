# Član 29
## Otkrivanje slučajeva i/ili grešaka
Funkcija otkrivanja slučajeva i/ili grešaka, otkriva sljedeće slučajeve i/ili greške:
Slučaj stavljanja nevažeće kartice se aktivira stavljanjem bilo koje nevažeće kartice i/ili ukoliko istekne rok važenja stavljene kartice.
Slučaj sukoba kartica se aktivira ako se javi bilo koja kombinacija sa važećim karticama označena u tabeli sa X :
Sukob kartica
Otvor za vozača
Bez kartice (ili
neispravna kartica)
Kartica
vozača
Kartica kontrolnog
organa
Kartica
radionice
Kartica
prevoznika
Otvor za
suvozača
Bez kartice (ili neispravna kartica)
Kartica vozača
X
Kartica kontrolnog organa
X
X
X
Kartica radionice
X
X
X
X
Kartica prevoznika
X
X
X Slučaj vremenskog preklapanja se aktivira kada datum/vrijeme posljednjeg vađenja kartice, učitan sa kartice, slijedi tekući datum/vrijeme digitalnog tahografa u koji je stavljena kartica.
Slučaj vožnje bez odgovarajuće kartice se aktivira za bilo koju kombinaciju kartica označenu sa X u sljedećoj tabeli ukoliko se aktivnost vozača promijeni na "vožnju" ili ukoliko dođe do promjene režima rada kada je aktivnost vozača "vožnja".
Vožnja bez odgovarajuće kartice
Otvor za vozača
Bez kartice (ili
neispravna kartica)
Kartica
vozača
Kartica kontrolnog
organa
Kartica
radionice
Kartica
prevoznika
Otvor za
suvozača
Bez kartice (ili neispravna kartica)
X
X
X
Kartica vozača
X
X
X
X
Kartica kontrolnog organa
X
X
X
X
X
Kartica radionice
X
X
X
X
Kartica prevoznika
X
X
X
X
X Slučaj stavljanja kartice tokom vožnje se aktivira ako se kartica stavi u bilo koji otvor u vrijeme dok je aktivnost vozača "vožnja".
Slučaj prekoračenja brzine se aktivira pri svakom prekoračenju brzine.
Slučaj prekida napajanja se aktivira izvan režima kalibracije u slučaju svakog prekida napajanja senzora kretanja i/ili jedinice u vozilu dužeg od 200 ms.
Prag prekida utvrđuje proizvođač.
Pad napajanja zbog pokretanja motora vozila ne aktivira ovaj slučaj.
Slučaj greške u podacima o kretanju se aktivira u slučaju prekida redovnog protoka podataka između senzora kretanja i jedinice u vozilu i/ili u slučaju greške cjelovitosti podataka ili greške autentifikacije podataka tokom razmjene podataka između senzora kretanja i jedinice u vozilu. Slučaj pokušaja probijanja zaštite se aktivira za sve ostale slučajeve koji utiču na bezbjednost senzora kretanja i/ili jedinice u vozilu kako je navedeno u generičkim sigurnosnim ciljevima za takve sastavne dijelove dok nijesu u režimu kalibracije.
Greška kartice se aktivira ako se tokom rada javi greška na kartici.
Greška digitalnog tahografa se aktivira za neku od sljedećih grešaka, dok nije u režimu kalibracije:
1)
interna greška jedinice u vozilu;
2)
greška štampača;
3)
greška displeja;
4)
greška pri preuzimanju podataka;
5)
greška senzora.
