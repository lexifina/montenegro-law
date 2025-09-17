PRILOG 1
METODOLOGIJA ZA PRORAČUN I PRIKAZIVANJE UDJELA SVIH VRSTA IZVORA ENERGIJE U ISPORUČENOJ ELEKTRIČNOJ ENERGIJI KRAJNJIM KUPCIMA
Proračun udjela
Član 1
(1) Udjeli svih vrsta izvora energije u isporučenoj električnoj energiji krajnjim kupcima
izračunavaju se primjenom odgovarajućih matematičkih formula utvrđenih ovom
metodologijom.
(2) Sve matematičke formule u ovoj metodologiji koriste matematičke matrice kojima se
opisuje električna energija za potrebe proračuna iz stava 1 ovog člana, čiji su elementi,
simboli, značenja i način upotrebe u formulama bliže opisani u članu 2 ove metodologije.
Podjela električne energije i matematičke operacije
Član 2
(1) Atributi se koriste kao elementi u matematičkim matricama, po sljedećem redosledu:
1) solarna energija,
2) energija vjetra,
3) hidroenergija,
4) geotermalna energija,
5) energija iz biomase,
6) energija iz obnovljivih izvora čiji izvor nije određen,
7) energija iz kamenog uglja,
8) energija iz mrkog uglja i lignita,
9) energija iz prirodnog gasa,
10) energija iz nafte i naftnih derivata,
11) energija iz fosilnih goriva čiji izvor nije određen, i
12) nuklearna energija.
(2) Struktuirana energija je matematička matrica izražena kao vektor vrste sa 12 elemenata.
Struktuirana energija simbolički se predstavlja sa uglastim zagradama [SE], pri čemu simbol
"SE" u uglastim zagradama u ovoj tački ima samo apstraktno značenje za potrebe
objašnjenja, inače se u konkretnim formulama za struktuiranu energiju u uglaste zagrade
stavljaju različiti simboli u zavisnosti od toga šta simbolizuju (npr. [RM], [IE], [FiT] i sl.)
(3) Svaki element matrice struktuirane energije predstavlja po jedan atribut od utvrđenih 12
atributa iz stava 1 ovog člana.
(4) Elementi matrice struktuirane energije izražavaju količinu energije i njihova jedinica je
MWh.
(5) Kada se u matematičkim formulama iza uglaste zagrade stavi znak "i" na sljedeći način:
"[]i", to znači da je predstavljen i-ti element matrice struktuirane energije, odnosno da znak "i"
može imati vrijednost od 1 do 12, zavisno od atributa koji predstavlja.
(6) Ukupna energija je suma 12 elemenata matrice struktuirane energije i izražava se u
MWh.
(7) Matematički, ukupna energija izražava se kao E = ∑[SE].
(8) Ako je iznos ukupne energije poznat, ali nije poznata njena struktura, ukupna energija u
matematičkim formula označava se samo kao E.
(9) Struktura energije se izražava u formi matematičke matrice i to kao vektor vrste sa 12
elemenata, pri čemu svaki element vektora predstavlja po jedan atribut od utvrđenih 12
atributa iz stava 1 ovog člana.
(10) Struktura energije simbolički se predstavlja sa vitičastim zagradama "{SE}", pri čemu
simbol "SE" u vitičastim zagradama u ovoj tački ima samo apstraktno značanje za potrebe
objašnjenja, inače se u konkretnim formulama za strukturu energije stavljaju različiti simboli
u vitičastim zagradama u zavisnosti od toga šta simbolizuju (npr. {RMbI},{Si},{SS} i sl.).
(11) Elementi vektora strukture energije predstavljaju procentualnu vrijednost udjela
atributa, pri čemu je zbir svih 12 elementa jednog vektora 100%.
(12) Kada se u matematičkim formulama neki simbol stavi u vitičaste zagrade "{}" to znači da
je predstavljena struktura energije.
(13) Kada se u matematičkim formulama iza vitičaste zagrade stavi znak "i" na sljedeći
način: "{}i", to znači da je predstavljen i-ti element matrice strukture energije, odnosno da
znak "i" može imati vrijednost od 1 do 12, zavisno od atributa koji predstavlja.
(14) Računske operacije sabiranja i oduzimanja matematičkih matrica se obavljaju tako što
se naznačene računske operacije obavljaju isključivo između odgovarajućih elementa
matrica. Na primjer, sabiranje dvije matrice [SEa] i [SEb], od kojih svaka ima 12 elemenata
koji odgovaraju prethodno utvrđenim atributima, a čiji je zbir treća matrica [SEc], matematički
se opisuje sljedećom jednačinom:
[SEa] + [SEb] = [SEc]
pri čemu se sa pojedinim elementima obavljaju sljedeće operacije:
[SEa]1 + [SEb]1 = [SEc]1
...
[SEa]i + [SEb]i = [SEc]i
...
[SEa]12 + [SEb]12 = [SEc]12
(15) Struktura energije se izračunava kao količnik struktuirane energije i ukupne energije,
što se matematički opisuje količnikom matrice struktuirane energije i ukupne energije:
{SE} = [SE] / ∑[SE]
pri čemu se vrijednosti pojedinih elemenata strukture energije izračunavaju za svaki atribut
pojedinačno prema jednačini:
{SE}i = [SE]i / ∑[SE]
(16) Svi podaci odnose se na period prethodne kalendarske godine, osim ako Pravilima o
načinu proračuna, prikazivanja i objavljivanja udjela svih vrsta izvora energije u proizvedenoj
odnosno isporučenoj električnoj energiji (u daljem tekstu: Pravila) nije drugačije određeno.
Proračun nacionalnog rezidualnog miksa
Član 3
(1) Nacionalni rezidualni miks električne energije bez korekcije sa evropskim miksom
atributa [NRMbE] računa se prema formuli:
[NRMbE] = [NRMbI] - [IE]
gdje je:
[NRMbI] - struktuirana energija nacionalnog rezidualnog miksa električne energije bez
korekcije za izvoz u treće države koja se računa prema sljedećoj formuli:
[NRMbI] = [UP] + [ISGP] + [UE] - [IZGP]
gdje je:
[UP] - struktuirana ukupna proizvedena električna energija u Crnoj Gori koju utvrđuje
operator tržišta,
[ISGP] - struktuirana energija isteklih garancija porijekla električne energije u registru
garancija porijekla u periodu od 1. aprila prethodne godine do 31. marta tekuće godine,
[UE] - struktuirana neto električna energija ušla u prenosni sistem iz trećih država koja se
izračunava kao:
[UE] = ∑(Ej * {Sj})
gdje je:
Ej - neto električna energija ušla u prenosni sistem na granici sa državom j.
{Sj} - struktura energije države j iz koje je izvršen uvoz, a utvrđuje se na temelju podataka o
proizvodnji električne energije u toj državi koje objavljuje Evropska mreža operatora
prenosnih sistema za električnu energiju (ENTSO-E) ili Internacionalna agencija za
energetiku (IEA). Izuzetno, struktura neto uvezene električne energije iz svake treće države
sa kojom se graniči Crma Gora može da se zasniva na posljednje dostupnim podacima koje
objavljuje ENTSO-e, IEA ili druga relevantna institucija koja objavljuje podatke o proizvodnji
električne energije u toj državi,
[IZGP] - struktuirana energija izdatih garancija porijekla električne energije u registru
garancija porijekla za proizvodnju iz prethodne kalendarske godine,
[IE] - struktuirana energija električne energije izašle iz prenosnog sistema koja se određuje
prema formuli:
[IE] = {NRMbI} * ∑ Eiz
gdje je:
∑ Eiz - ukupna električna energija izašla iz prenosnog sistema,
{NRMbI} - struktura energije nacionalnog rezidualnog miksa električne energije bez
korekcije za izvoz u treće države.
(2) Nacionalni rezidualni miks električne energije [NRM] računa se prema formuli:
[NRM] = [NRMbE] + [EM]
gdje je:
[NRMbE] - nacionalni rezidualni miks električne energije bez korekcije sa evropskim
miksom atributa,
[EM] - struktuirana energija razmjene sa evropskim miksom atributa. Ova energija razmjene
može biti ili predata iz nacionalnog razidualnog miksa u evropski miks atributa električne
energije ili preuzeta u nacionalni rezidualni miks električne energije iz evropskog miksa
atributa električne energije. Pri tome se energija razmjene sa evropskim miksom atributa EM
izračunava prema sljedećoj formuli:
EM = Euk - ∑ [ISKGP] - ∑ [NRMbE]
gdje je:
Euk - ukupna energija koja je isporučena svim krajnjim kupcima u Crnoj Gori, uključujući
energiju za pokrivanje gubitaka u prenosnom, distributivnom, odnosno zatvorenom
distributivnom sistemu,
∑ [ISKGP] - ukupna energija iskorišćenih garancija porijekla električne energije za potrošnju
u prethodnoj kalendarskoj godini za potrebe dokazivanja krajnjem kupcu iz Crne Gore da je
određena količina potrošene električne energije proizvedena iz obnovljivih izvora energije,
Ako je EM > 0 nacionalni rezidualni miks preuzima atribute iz evropskog miksa atributa i u
tom slučaju struktuirana energija razmjene sa evropskim miksom atributa se izračunava kao:
[EM] = EM* {EAM}
gdje je:
{EAM} - struktura evropskog miksa atributa
Ako je EM < 0 nacionalni rezidualni miks predaje atribute u evropski miks atributa i u tom
slučaju struktuirana energija razmjene sa evropskim miksom atributa se izračunava kao:
[EM]= EM* {NRMbE}
Proračun udjela svih vrsta izvora energije u isporučenoj električnoj energiji snabdjevača krajnjim kupcima
Član 4
(1) Udio svih vrsta izvora energije u isporučenoj električnoj energiji koju je snabdjevač
isporučio svim krajnjim kupcima {SS} izračunava se kao:
{SS}=[IG]+( Es−∑[IG])∗{NRM }
Es
gdje je:
[IG] - struktuirana energija iskorišćenih garancija porijekla snabdjevača za potrošnju u
prethodnoj kalendarskoj godini za potrebe dokazivanja krajnjem kupcu iz Crne Gore da je
određena količina potrošene električne energije proizvedena iz obnovljivih izvora energije,
Es - ukupna energija koju je snabdjevač isporučio svojim krajnjim kupcima
{NRM} - struktura energije nacionalnog rezidualnog miksa električne energije
U slučaju da je (Es-∑[IG] )<0, pri proračunu udjela svih vrsta izvora energije u isporučenoj
električnoj energiji koju je snabdjevač isporučio svim krajnjim kupcima {SS}, koristi se
vrijednost 0.
(2) Udio svih vrsta izvora energije u isporučenoj električnoj energiji koju je snabdjevač
isporučio krajnjim kupcima koji koriste isti tarifni model snabdjevača {STM} izračunava se
kao:
{STM }=([IGtm]+( Etm−∑[IGtm])∗{SRM })
ETM
gdje je:
[IGtm] - struktuirana energija iskorišćenih garancija porijekla snabdjevača za potrošnju u
prethodnoj kalendarskoj godini za potrebe dokazivanja krajnjem kupcu iz Crne Gore da je
određena količina potrošene električne energije proizvedena iz obnovljivih izvora energije, a
namijenjenih za određeni tarifni model
Etm - ukupna energija koju je snabdjevač isporučio krajnjim kupcima koji koriste isti tarifni
model
{SRM} - struktura energije rezidualnog miksa snabdjevača, a čija se struktuirana energija
računa prema sljedećoj formuli:
[SRM] = (Es - ∑[IG] ) * {NRM}
gdje je:
Es - ukupna energija koju je snabdjevač isporučio svim svojim krajnjim korisnicima,
[IG] - struktuirana energija iskorišćenih garancija porijekla snabdjevača za potrošnju u
prethodnoj kalendarskoj godini za potrebe dokazivanja krajnjem kupcu iz Crne Gore da je
određena količina potrošene električne energije proizvedena iz obnovljivih izvora energije,
{NRM} - struktura energije nacionalnog rezidualnog miksa.
