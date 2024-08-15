# Član 15
Ova odluka stupa na snagu osmog dana od dana objavljivanja u "Službenom listu Crne Gore", a primjenjivaće se od 01.11.2024.godine.
O. br. 0101-5825- 3/2024 Podgorica,31.07.2024. godine
Savjet Centralne banke Crne Gore
Predsjedavajuća Guvernerka,
dr Irena Radović, s.r.
PRILOG 1
1.
Karakteri koji definišu format poruke Struktura SWIFT polja:
Vrsta
karaktera
Opis
Primjeri
n
Numeričko polje
18n - numeričko polje do 18 karaktera
!
Iza nekog broja predstavlja fiksnu dužinu
određenu tim brojem
18!n - polje od fiksno 18 numeričkih
karaktera
a
Isključivo slovno polje (velika slova)
4!a - fiksno četiri slovna karaktera
d
Decimalno polje
15d - numeričko polje sa dvije decimale
do 15 karaktera (12n,nn)
x
Slovno,numeričko i znakovno polje
35x
-
predstavlja
do
35
slovno,
numeričkih i znakovnih karaktera
c
Slovno numeričko polje
3c - polje koje ima 3 slovna, 3 numerička
ili 3 slovno numerička karaktera
3*35x
Prvi broj određuje broj linija a drugi broj
karaktera po liniji
3*35x - 3 linije od kojih svaka ima do 35
karaktera
[ ]
Polja u uglastim zagradama su opciona
polja
[1!a] - polje u određenim uslovima ima
fiksno jedan karakter dok u drugim
uslovima se ne popunjava
----I
Polja koja se nalaze između ova dva
znaka mogu se
ponavljati više puta
Dozvoljeni karakteri u SWIFT-u:
a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0123456789 / - ? : ( ) . , + { }
2. SMT SWIFT poruke za dostavljanje podataka o transakcionim računima u Centralni registar transakcionih računa i depozita i sefova
2.1. Poruka SMT 740
Porukom SMT 740 kreditne institucije iz člana 6 ove odluke dostavljaju podatke o otvorenim transakcionim računima pravnih lica, preduzetnika i fizičkih lica, njihovim promjenama i ukidanju tih računa.
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
Podtip poruke sopstvenog
formata koji se nalazi u omotnici
poruke a to je SMT 740.
77E
Sadržaj omotnice
poruke koji odgovara
navedenom podtipu
poruke sopstvenog
formata
Da
Sadržaj omotnice u poruci
sopstvenog formata čine samo
unaprijed standardizovana polja
prema uputstvu.
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
‘’YYYYMMDD HH:MM:SS’’
40
Matični broj pravnog lica
rezidenta
Matični broj ili JMB
preduzetnika
8n
8n ili 13n
Da
Za pravno lice - rezidenta
upisuje se matični broj po modulu
11.
Za preduzetnika upisuje se
matični broj po modulu 11.
Za fizičko lice - rezidenta upisuje 7. август 2024.
СЛУЖБЕНИ ЛИСТ ЦРНЕ ГОРЕ
Страна 42 - Број 78
JMB fizičkog lica -
rezidenta
Identifikacioni broj pravnog
lica ili fizičkog lica -
nerezidenta
U slučaju zajedničkog
računa: matični brojevi
pravnih lica, matični brojevi
ili JMB preduzetnika i JMB
fizičkih lica, kao i
identifikacioni brojevi
nerezidenata - svih
imalaca zajedničkog
računa
13n
20x
139x
Da
se matični broj po modulu 11.
Za nerezidenta pravno lice
upisuje se broj iz izvoda iz
registra u koji je upisan, odnosno
iz drugog validnog dokumenta o
osnivanju, a za nerezidenta
fizičko lice upisuje se
identifikacioni broj iz pasoša ili
druge odgovarajuće lične isprave
fizičkog lica - nerezidenta.
Matični brojevi ili JMB ili
identifikacioni brojevi za
zajednički račun pišu se u nizu i
odvajaju zarezom.
50
Poreski identifikacioni broj
pravnog lica ili
preduzetnika
U slučaju zajedničkog
računa:
poreski brojevi svih pravnih
lica i svih preduzetnika -
imalaca zajedničkog
računa
13n
139x
Da
Da
Za rezidenta upisuje se poreski
identifikacioni broj (PIB) pravnog
lica ili preduzetnika i to: za
pravno lice - osam numeričkih
znakova, a za preduzetnika - 13
numeričkih znakova i upisuje se
matični broj po modulu 11.
Za nerezidente upisuje se, kada
je to primjenljivo poreski
identifikacioni broj (PIB) pravnog
lica - osam numeričkih znakova.
Poreski brojevi za zajednički
račun pišu se u nizu i odvajaju
zarezom.
DRUGI DIO PORUKE Polje
Element poruke
Format
Obavezno
Napomena 79
Polje sopstvenog formata
Da
U ovom redu obavezno samo
crtica -, polja sopstvenog formata
imaju dvije tačke na početku.
74005:
Transakcioni račun
1!x18!n ili
1!x2!a2!n18!n
Da
