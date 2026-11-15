# Član 13
Ova odluka stupa na snagu osmog dana od dana objavljivanja u "Službenom listu Crne Gore", a primjenjivaće se od 09. januara 2015. godine.
O. br. 0101-4014/63-3 Podgorica, 10.11.2014. godine
Savjet Centralne banke Crne Gore
Predsjedavajući guverner,
mr Milojica Dakić, s.r.
PRILOG 1 1. Karakteri koji definišu format poruke
Struktura SWIFT polja:
Vrsta karaktera
Opis
Primjeri
n
Numeričko polje
18n - numeričko polje do 18 karaktera
!
Iza nekog broja predstavlja fiksnu
dužinu određenu tim brojem
18!n - polje od fiksno 18 numeričkih karaktera
a
Isključivo slovno polje (velika slova)
4!a - fiksno četiri slovna karaktera
d
Decimalno polje
15d - numeričko polje sa dvije decimale do 15
karaktera (12n,nn)
x
Slovno,numeričko i znakovno polje
35x - predstavlja do 35 slovno, numeričkih i
znakovnih karaktera
c
Slovno numeričko polje
3c - polje koje ima 3 slovna, 3 numerička ili 3
slovno numerička karaktera
3*35x
Prvi broj određuje broj linija a drugi
broj karaktera po liniji
3*35x - 3 linije od kojih svaka ima do 35
karaktera
[ ]
Polja u uglastim zagradama su
opciona polja
[1!a] - polje u određenim uslovima ima fiksno
jedan karakter dok u drugim uslovima se ne
popunjava

----I
Polja koja se nalaze između ova
dva znaka mogu se ponavljati više
puta
Dozvoljeni karakteri u SWIFT-u:
a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0123456789 / - ? : ( ) . , + { }
2. SMT SWIFT poruke za dostavljanje podataka o transakcionim računima u Centralni registar transakcionih računa
2.1. Poruka SMT 740
Porukom SMT 740 pružaoci platnih usluga iz član 4 ove odluke dostavljaju podatke o otvaranju novih transakcionih računa pravnih lica i preduzetnika, njihovim izmjenama i ukidanju.
Prvi dio poruke
Polje
Element poruke
Format
Obavezno
Napomena
20
Referenca
16x
Da
TRN poruke SMT 740
12
Podtip poruke
3!n
Da
Podtip poruke sopstvenog formata
koji se nalazi u omotnici poruke a to
je SMT 740
77E
Sadržaj omotnice poruke
koji odgovara
navedenom podtipu
poruke sopstvenog
formata
Da
Sadržaj omotnice u poruci
sopstvenog formata čine samo
unaprijed standardizovana polja
prema uputstvu
59A
BIC primaoca
4!a2!a2!c[3!c]
Da
54A
BIC pošiljaoca
4!a2!a2!c[3!c]
Da
30
Datum slanja
17!x
Da
Format datuma je:
‘’YYYYYMMDD HH:MM:SS’’
40
Matični broj pravnog lica
ili JMB preduzetnika
U slučaju zajedničkog
računa:
matični brojevi svih
pravnih lica i JMB svih
preduzetnika - imalaca
zajedničkog računa
13n
139x
Da
Da
Matični brojevi ili JMB za zajednički
račun pišu se u nizu i odvajaju
zarezom
50
Poreski broj
pravnog lica ili
preduzetnika
U slučaju zajedničkog
računa:
poreski brojevi svih
pravnih lica i svih
preduzetnika - imalaca
zajedničkog računa
13n
139x
Da
Da
Poreski brojevi za zajednički račun
pisu se u nizu i odvajaju zarezom
Drugi dio poruke
Polje
Element poruke
Format
Obavezno
Napomena
79
Polje sopstvenog
formata
Da
U ovom redu obavezno samo crtica,
polja sopstvenog formata nemaju
dvije tačke na početku
74005:
Transakcioni račun
1!x18!n ili
1!x2!a2!n18!n
Da
