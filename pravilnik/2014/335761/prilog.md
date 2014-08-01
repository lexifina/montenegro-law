PRILOG 1
MINIMALNI ZAHTJEVI KOJE ISPUNJAVA OPREMA ZA PRIJEM SIGNALA DRUGE GENERACIJE ZEMALJSKE TELEVIZIJE (DVB-T2)
1.
SPECIFIKACIJA PRIJEMNIKA
1.1.
Opšti zahtjevi
Prijemnik mora da zadovolji sve zahtjeve utvrđene zakonima i regulativom donijetom od strane Evropske Unije (EU) i relevantnih nacionalnih institucija.
Prijemnik mora da zadovolji zahtjeve u pogledu energeteske efikasnosti u cilju minimizovanja potrošnje energije u svim modovima rada. Proizvođačima se preporučuje da proizvodnja prijemnika slijedi ugovore o potrošnji energije za složene STB uređaje u skladu sa EU regulativom i/ili regulacijom Evropske Komisije (EC - European Commision) broj 1275/2008 o implementaciji direktive 2005/32/EC Evropskog Parlamenta i Savjeta, koja se odnosi na zahtjeve za eko-dizajnom kod standby i off mode potrošnje električne energije električne i elektronske opreme u domaćinstvima i kancelarijama.
Prijemnik mora da zadovolji zahtjeve u pogledu materijala korišćenih za izradu, a u skladu sa direktivom 2002/95/EC.
Ako nije drugačije naznačeno, pod pojmom prijemnik će se podrazumijevati svi uređaji koji su u mogućnosti da prime i dekodira ju DVB-T2 signal u cilju reprodukcije audio i prikazivanja video sadržaja (iDTV - Integrated Digital TV set1, STB - Set-Top Box2, drugi uređaji).
1.2.
Hardverski zahtjevi
1.2.1. RF dio
Od prijemnikase zahtjeva da omogući prijem i demodulaciju DVB-T2 prenosnog toka u skladu sa standardom ETSI EN 302 755.
Prijemnik mora omogućiti prijem DVB-T2 prenosnog toka u jednofrekvencijskim 3 (SFN) ili višefrekvencijskim4 (MFN) mrežama.
Prijemnik mora omogućiti prijem signala po svim kanalima u opsegu 174-230 MHz (VHF III opseg, kanali 5-12 širine 7 MHz) i u opsegu 470-790 MHz (UHF opsegu IV i dio opsega V, kanali 21-60 širine 8 MHz).
Prijemnik mora omogućiti prijem DVB-T2 signala sa svim dozvoljenim kombinacijama parametara u skladu sa ETSI EN 302 755 standardom:
- mod prenosa (veličina FFT-a): 1k, 2k, 4k, 8k normalni i prošireni, 16k normalni i prošireni, 32k normalni i prošireni,
- modulacioni postupak: QPSK, 16QAM, 64QAM, 256QAM sa rotiranim ili nerotiranim konstalacionim dijagramom,
- kodni odnos: 1/2, 3/5, 2/3, 3/4, 4/5, 5/6,
- zaštitni interval: 1/4, 19/256, 1/8, 19/128, 1/16, 1/32, 1/128,
- šema pilota: PP1, PP2, PP3, PP4, PP5, PP6, PP7, PP8,
- itd.
Prijemnik mora da bude otporan na smetnje susjednih ili ostalih kanala, bilo da se na njima emituje digitalni ili analogni si gnal.
Unutar korisničkog interfejsa prijemnik mora obezbijediti informacije o nivou i kvalitetu signala. Za implementaciju korisničkog interfejsa odgovoran je proizvođač prijemnika.
1.2.1.1. Nivo signala na ulazu prijemnika DVB-T2 prijemnik sa 8 MHz širinom kanala će podržavati rad sa QEF5 (Quasi Error Free), koji podrazumjeva P(min) nivo signala na ulazu prijemnika bez degradacije dekodirane slike i zvuka (QEF prijem), gdje je
.
U VHF III, UHF IV i UHF V opsegu, maksimalna vrijednost NF-a (Noise Figure) za DVB-T2 prijemnik neće prevazilaziti 6dB.
Minimalni proračunati nivo signala kod DVB-T2 prijemnika za QEF prijem sa 8 MHz širinom kanala i Gausovim profilom za UHF opsege IV i V će biti u rasponu od:

- 95,6dBm za QPSK, kodnog odnosa 1/2 i zaštitnog intervala 1/4 i

- 74,0dBm za 256QAM, sa kodnim odnosom 5/6 i zaštitnim intervalom 1/8.
Maksimalni nivo signala na ulazu DVB-T2 prijemnika tipa STB je -23 dBm.
1.2.1.2. RF ulazni konektor Prijemnik mora imati najmanje jedan RF ulazni konektor u skladu sa IEC 60169-2, koji omogućava povezivanje eksterne antene muškim konektorom tipa IEC 60169-2. Ulazna impedansa je 75 Ω.
Prijemnik možeda ima i ulazni konektor za RF petlju koji obezbjeđuje dodatnopovezivanje za antenske instalacije.
RF ulazni signal može biti povezan petljom na RF izlazni konektor bez obzira na trenutno stanje prijemnika (aktivno ili stanje pripravnosti - standby), tako da povezana oprema (npr. TV oprema) može raditi čak i kada je prijemnik u stanju pripravnosti.
Prijemnik mora podržavati jednosmjerno napajanje za eksternu antenu sa pojačavačem. Ovo ne smije prouzrokovati degradaciju ulaznih RF karakteristika. Jednosmjerni izvor napajanja bi trebao biti zaštićen od kratkog spoja. U sistemskommeniju prijemnika mora postojati opcija za uključivanje, odnosno isključivanjejednosmjernog napajanja.Fabrički podešena vrijednost mora biti postavljena na isključeno stanje.
1.2.1.3. Procedure vezane za traženje/skeniranje radio spektra Prijemnik mora obezbijediti da, u slučaju istog Id transpornog toka (TS - Transport Stream) i Id servisa na dvije ili više različitih frekvencija snimi sve frekvencije, ili će izabrati samo frekvenciju sa boljim nivoom primljenog signala.
1
Prijemnik sa integrisanim uređajem za dekodiranje DVB-T2 prenosnog toka koji nosi signal kodiran prema ITU-T H.264/AVC (MPEG-4 Part
10) standardu, sa mogućnošću prikaza slike i reprodukcije zvuka, realizovan kao digitalni televizijski prijemnik.
2
Prijemnik sa mogućnošću dekodiranja DVB-T2 prenosnog toka koji nosi signalkodiran prema ITU-T H.264/AVC (MPEG-4 Part 10)
standardu, kao samostalan STB uređaj sa mogućnošću priključenja na TV uređaj ili monitor.
3
Jednofrekvencijska mreža (Single Frequency Network - SFN) je mreža sa više digitalnih zemaljskih radio-predajnika, koji su vremenski i
frekvencijski sinhronizovani i emituju istovjetan signal na istoj frekvenciji.
4
Višefrekvencijska mreža (Multiple Frequency Network - MFN) je mreža digitalnih zemaljskih radio-predajnika koji emituju signale na različitim
frekvencijama.
5
QEF(Quasi Error Free) znači "manje od jedne nekorigovane greške u satu prenosa, pri brzini od 5Mbit/s jednog dekodera TV servisa", što
približno odgovara vjerovatnoći greške po paketu transportnog toka (Transport Stream Packet Error Ratio) od PER<10-7 prije
demultipleksiranja.
Prijemnik mora biti u mogućnosti da primi i obradi, tokom traženja, parametre iz PSI/SI (Program-Specific Information/Service Information) tabele (npr. SDT - Service Description Table ili NIT - Network Information Table informacije).
Osim automatske, prijemnik mora omogućiti i ručnu pretragu u slučaju kada se frekvencija ili Id kanala unosi od strane korisnika. Prijemnik se mora podesiti na željeni kanal, pretražiti sve dostupne DVB-T2 modove, dodati nove servise i zamijeniti postojeće servise u servisnoj listi (bez razmatranja bilo kog kriterijuma vezanog za kvalitet).
1.2.1.4. Dinamičko upravljanje kanalima Prijemnik mora ažurirati modulacione parametre u skladu sa NIT tabelom. Prijemnik mora ažurirati i listu servisa u skladu sa SDT tabelom. 1.2.1.5. Dinamički PMT Prijemnik mora biti u mogućnosti da obradi dinamičke promjene u PMT -u(Program Map Table) na korektan način, pri čemu će se voditi računa da:
-
dinamičke promjene u PMT-u neće proizvesti bilo kakvu smetnju na prikazu audio-video sadržaja;
-
prekidanjem elementarnog audio i/ili video toka, maksimalno vrijeme prebacivanja (mjereno od PMT ažuriranja čiste slike) će biti 3
sekunde. Maksimalno vrijeme prebacivanja će biti određeno bez obzira da li je elementarni tok skremblovan ili ne.
Preporučuje se da video prikaz na izlazu bude zamrznut sve dok novi video tok ne bude dekodiran i prikazan. Ovo se odnosi kako na promjene u prenosnom toku, tako i na promjene zasnovane na zahtjevu korisnika, recimo prilikom izmjene programa.
1.2.2.
Interfejsi Treba istaći da broj i raznovrsnost interfejsa na prijemniku utiče na njegovu cijenu.
1.2.2.1. SCART interfejs Prijemnik tipa STB mora imati najmanje jedan SCART interfejs u skladu sa EN 50049-1 i EN 50157-2-1 standardom.
SCART interfejs je namijenjen za povezivanje audio i video opreme i predstavlja konektor za analogni audio i video signal, te stoga nije relevantan za iDTV. SCART interfejs ima 21 pin, od kojih svaki ima određenu ulogu - neki pinovi su namijenjeni za prenos audio signala, drugi za prenos video signala, a neki za prenos kontrolnih signala.
U Tabeli 1.1 je data specifikacija ulaznih/izlaznih signala omogućenih SCART interfejsom.
Tabela 1.1. Specifikacija ulaznih/izlaznih signala omogućenih SCART interfejsom
Zahtjev
CVBS/AUDIO
RGB
PIN 8
PIN 16* TV SCART
Obavezan
Izlaz
Izlaz
Izlaz (1)
Izlaz (2) VCR SCART
Opciono
Ulaz i izlaz (3)
Ulaz
Ulaz
Ulaz (2) * Opciono
Dakle, prijemnik tipa STB treba da ima jedan TV SCART interfejs za televiziju i opciono jedan VCR SCART interfejs. Takođe je u Tabeli 1.1 navedeno da SCART interfejs treba da ima potrebne ulaze i izlaze za CVBS/AUDIO i RGB video signal. Za kontrolne signale se ko riste pin 8, odnosno opciono pin 16. Pomoću ovih kontrolnih signala se identifikuje format slike i tip video signala (CVBS - Composite Video Baseband Signal ili RGB - Red Green Blue).
(1):
Kontrolni signal na pinu 8 ima sljedeću specifikaciju:
Nominalno 0 V/DC:
Označava zahtjev za korišćenje formata slike koji je prisutan na prijemnom uređaju,
Nominalno 6 V:
Označava zahtjev za korišćenje formata za prikaz slike sa odnosom dimenzija 16:9,
Nominalno 12 V:
Označava zahtjev za korišćenje formata za prikaz slike sa odnosom dimenzija 4:3.
(2):
Kontrolni signal na pinu 16 ima sljedeću specifikaciju:
Nominalno 0 V/DC: Označava prisustvo signala na CVBS izlazu,
1-3 V/DC Označava prisustvo signala na RGB izlazu.
(3):OSD (On Screen Display) grafika ne bi trebala biti prisutna na VCR SCART izlazu, osim ako se ne koristi za DVB transkript (ako je prisutan i izabran).
Audio interfejs na VCR SCART će isporučivati isti audio signal koji je dostupan na TV SCART interfejsu. Interna kontrola jačine zvuka bi trebala da utiče na audio signal na TV SCART interfejsu, ali ne i na audio signal od VCR SCART audio interfejsa.
1.2.2.2. Analogni video izlaz Prijemnik može posjedovati analogni video izlaz koji treba da ima sljedeće karakteristike:
-
interfejs je ženski koaksijalni RCA konektorrealizovan u skladu sa standardom IEC 60603-14,
-
izlaz je analogni video signal u formatu YPbPr u skladu sa CEA 770.3 .
1.2.2.3. Interfejs za uslovni pristup Prijemnik mora da podrži najmanje jedan DVB zajednički interfejs (CA - Conditional Access modul) za uslovni pristup. Na CA modulu se nalaze informacije o plaćenoj televizijskoj usluzi, odnosno o programima kojima korisnik može pristupiti. CI interfejs na prijemniku bi mora biti u skladu sa standardom EN50221.
1.2.2.4. Digitalni audio izlaz Prijemnik mora imati koaksijalni ili optički S/PDIF interfejs za digitalni audio signal kako bi obezbijedio isporuku PCM audio signala (PCM - Pulse Coded Modulation), u skladu sa standardom IEC 60958 ili nelinearnog PCM kodiranog audio toka u skladu sa IEC 61937 standardom.
1.2.2.5. Analogni audio izlaz Prijemnik može imati najmanje jedan analogni audio interfejs zasnovan na dva RCA konektora ženskog tipa u skladu sa IEC 60603-14 standardom.
1.2.2.6. HDMI interfejs Prijemnik HDTV nivoa tipa iDTV mora podržavati zahtjeve za video interfejse visoke definicije specificirane od strane EICTA asocijacije za HDTV Ready iDTV uređaje.
Prijemnik HDTV nivoa tipa STB mora imati najmanje jedan HDMI interfejs u formi konektora tipa A, kao podrška za displeje koji ispunjavaju EICTA HD-Ready zahtjeve.
Prijemnik HDTV nivoa tipa STB mora biti u mogućnosti da koristi EDID (Extended Display Identification Data) informaciju koja se dobija od digitalnog displeja kako bi automatski odredio STB izlaz.
Prijemnik HDTV nivoa tipa STB mora obezbjediti opciju "Original Format", tj. da izlazni signal bude istog formata kao primljeni, ako je isti podržan od displeja, saglasno EDID informacijama. Ako primljeni format nije podržan, STB će izabrati prikaz koji obezbjeđuje video najboljeg kvaliteta. Ovo je potrebno radi izbjegavanjasituacije da STB izlaz bude crn ukoliko postoji neusaglašenost između primljenog formata i karakteristika displeja.
Takođe mora postojati mogućnost da se ručno podesi osnovni format izlaza iz prijemnika HDTV nivoa tipa STB na fiksni format. Fiksni format uključuje sljedeće formate: 1920x1080i@25Hz,1280x720p@50Hzi 720x576p@25Hz. Opciono se mogu uključiti formati 1920x1080p@25Hz i 1920x1080p@50Hz.
Preferirani standardni format izlaza će biti smješten u STB.
HDMI izlaz mora obezbijediti stereo ili downmixstereo ili višekanalni audio i trebao bi biti opremljen sa Auto lip-synch funkcionalnošću. HDMI izlaz bi trebao biti Auto lip-synchi trebao bi zadržavati audio ili video signal u cilju kompenzacije kašnjenja u downstreamuređajima.
1.2.2.7. Interfejsi za protokole zasnovani na IP Prijemnik može da posjeduje jedan od sledećih interfejsa za povezivanje na IP mrežu: Ethernet (IEEE 802.3 ili noviji) i IEEE 802.11.
Ukoliko prijemnik posjeduje interfejs za IP mrežu namjenjen za prenos multimedijalnog sadržaja, on mora da funkcioniše kao DLNA Digital Media Player ili DLNA Digital Media Renderer, u skladu sa DLNA Home Networked Device Interoperability Guidelines V1.0 i Standardom ISO/IEC 29341-3-1, kao i da podrži Hbb TV u skladu sa specifikacijom ETSI TS 102 796.
1.2.2.8. USB interfejs Prijemnik može da posjeduje USB interfejs za prijem i smještanje multimedijalnih podataka, sa sljedećim zahtjevima:
-
čitanje multimedijalnog formata, pri čemu je potrebno podržati FAT (File Alocation Table) i NTFS (New Technology File System)
sistem datoteka,
-
reprodukcija minimalnog skupa multimedijalnih formata navedenih u Tabeli 1.2.
Tabela 1.2. Multimedijalni formati za reprodukciju posredstvom USB interfejsa
Format
Standard
MPEG-1 video
ISO/IEC 11172-2
MPEG-1 audio
ISO/IEC 11172-3
MPEG-2 video
ISO/IEC 13818-2
MPEG-2 audio
ISO/IEC 13818-3
MPEG-4 video
ISO/IEC 14496-2
MPEG-4 audio
ISO/IEC 14496-3
MPEG-4 verzija 10 video
ISO/IEC 14496-10
E-AC3 audio
ETSI TS 102 366
JPEG
ISO/IEC 10918-1
Ukoliko je USB interfejs podržan, potrebno je omogućiti ažuriranje sistemskog softvera prijemnika posredstvom USB interfejsa.
1.2.3.
Procesor
Prijemnik mora da ažurira i adekvatno prikaže datum i tačno vrijeme koje dobija od TDT (Time and Data Table) i TOT (Time Offfset Table) tabela. Prijemnik može imati interni tajmer radi mogućnosti automatskog prelaska iz standby moda u aktivni mod. Ovaj tajmer će biti iniciran lokalno prihvatanjem zahtjeva od krajnjeg korisnika.
1.2.4.
MPEG demultiplekser
MPEG demultiplekser mora biti u skladu sa MPEG-2 transportnim nivoom definisanim ISO/IEC 13818-1 i ETSI 101 154 standardom.
Demultiplekser mora biti u mogućnosti da dekoduje ISO/IEC 13818/1 tok sa brzinom podataka do 50,34 Mb/s za DVB-T2. Demultiplekser mora podržavati promjenljivu brzinu protoka elementarnih tokova unutar transportnog toka konstantne brzine.
1.2.5.
MPEG video dekoder Dekoder prijemnika mora biti u potpunosti usklađen sa standardom ISO/IEC 14496-10 za dekodiranje MPEG-4 i standardom ISO/IEC 13818-2 za dekodiranje MPEG-2 kodiranih signala. Dekoder mora biti usklađen sa ETSI TS 101 154 standardom i podržavaće promjenljivu (VBR) i konstantnu brzinu signaliziranja bita (CBR).
Dekoder prijemnika mora obezbijediti sinhronizaciju između audio i video signala i to na način da audio signal nikada neće prednjačiti video signalu za više od 20 ms, i nikada neće kasniti za video signalom više od 45 ms.
Dekoder u prijemniku mora imati elemente koji će obezbijediti konverziju video formata na izlazu dekodiranog videa na njegovom HDMI i/ili SCART ili nekom drugom analognom interfejsu. Formati signala između STB i displeja uređaja su:
-
linija 23 (LINE23),
-
WSS i/ili nivo napona na SCART PIN8 kako je definisano IEC 62216-1 standardom, ili
-
u slučaju HDMI u skladu sa EICTA proširenjem IEC 62216-1 (6.4.3.7.4. AFD obrada za HDMI izlaz).
Tipično manji granični region unutar svake ivice slike od 720x576 piksela nije vidljiv zbog preskeniranja na SD ekranu. Za se rvise koji prenose ISO/IEC 14496-10 video, emiter može koristiti overscan_info_presenti overscan_appropriateflag-ove da označi da li bi prijemnik trebao primijeniti standardno preskeniranje ili bi trebao prikazati kompletnu emitovanu sliku videa.
U Tabeli 1.3 su dati emitovani overscan flag-ovi.
Tabela 1.3. Emitovanioverscan flag-ovi
Overscan_info_present flag
Overscan_appropriateflag
Upotreba
0x0 ili ne emituje
n/a
Nema željene metode prikaza
0x1
0x0
Važne informacije u cijelom video regionu
0x1
0x1
Dekodirana slika pogodna za preskeniranje
Osim ako korisnik ne zahtjeva drugačije, integrisani digitalni TV prijemnici će interpretirati i slijediti overscan flag-ove prema Tabeli 1.4.
Tabela 1.4. Overscan flag-ovi kod integrisanih digitalnih TV prijemnika
Overscan_info_present flag
Overscan_appropriateflag
Ponašanje
0x0 ili ne emituje
n/a
Zavisno od implementacije
0x1
0x0
Preskeniranje se ne primjenjuje
0x1
0x1
Preskeniranje se primjenjuje
Za prijemnike sa HDMI izlazom, prijemnik će prenijeti video na izlaz bez preskeniranja koje se odnosi na ponovno oblikovanje, postavljanjem bita u AVI Infoframe-ove.
U Tabeli 1.5 je data signalizacija preskeniranja na HDMI.
Tabela 1.5. Signalizacija preskeniranja na HDMI
Overscan_info_present flag
Overscan_appropriate flag
<S1,S0> (u HDMI Infoframe-u)
0x0 ili ne emituje
n/a
<0,0>
0x1
0x0
<1,0>
0x1
0x1
<0,1> 1.2.5.1. Dekodiranje SDTV servisa Dekodiranje SDTV servisa je obavezno i kod prijemnika nivoa HDTV zato što se očekuje da neki sadržaji nikada neće biti emitovani u HD formatu.
Dekoder prijemnika mora podržavati profil "H.264/AVC Main Profile at Level 3" (koji se koristi za H.264/AVC SDTV) a u skladu sa ETSI TS 101 154 standardom.
Dekoder prijemnika će dokodirati video u rezoluciji 720x576 piksela sa minimalnom brzinom podataka od 600 kb/s.
Dekoder prijemnika mora biti u mogućnosti da vrši prelazak između 4:3 i 16:9 formata slike. U slučaju prijema anamorfneslike i unaprijed podešenog 4:3 formata slike na TV-u, prijemnik mora omogućiti konverziju na 16:9 format. Opciono, dekoder bi trebao obezbijediti konverziju i na 14:9 format. 16:9 konverzija će biti implementirana vertikalnim filtriranjem. Degradacija signala zbog postupka filtriranja bi trebala biti subjektivno neprimjetna. Linija 23 i linija 623 bi trebale biti maskirane prije same konverzije kako bi se izbjegle iritirajuće polulinij e.
1.2.5.2. Dekodiranje HDTV servisa Prijemnik nivoa HDTV mora u potpunosti dekodirati SDTV servisekao što je prethodno pokazano..
Video dekoder mora podržavati "H.264/AVC High Profile at Level 4", u skladu sa standardom ETSI TS 101 154.
Ako se koristi SCART ili neki drugi dostupni analogni video izlaz (Z, Pb, Pr ili drugi), dekodirani HD video mora biti kon vertovan u SD format. Smanjenje dimenzija slike će se izvršiti sa bilo kog punog HD prikaza rezolucije 1920x1080 i 1280x720 (kao opcija takođe mogu biti 1140x1080, 1280x1080, 960x1080, 960x720 i 640x720) na 720x576 rezoluciju standardne definicije (SD). Downkonvertovani video će biti prikazan kao 16:9 "letterbox" na 4:3 displejima.
1.2.6.
Audio dekoder
1.2.6.1. Zahtjevi za audio dekoder kod prijemnika nivoa SDTV Prijemnik mora obezbijediti najmanje jedan stereo audio dekoder koji je u mogućnosti da zadovolji minimum zahtjeva za dekodiranje zasnovano na MPEG 1 nivou II ("Musicam" ISO/IEC 11172-3) i dekoder za AC3. Audio dekoder mora podržavati takođe i MPEG-4 AAC dekodiranje u skladu sa ISO/IEC 14496-4, MPEG-4 HE-AAC v1 (ISO/IEC 14496-3:2001/Amd.1:2003) i MPEG-4 HE-AAC v2 (ISO/IEC 14496-3:2005/Amd.2:2006). Audio dekoder mora biti potpuno usklađen sa DVB implementacionim smjernicama za upotrebu MPEG-2 sistema, videa i audia kod satelita, kablovske i zemaljske radiodifuzne aplikacije u skladu sa ETSI TS 101 154 standardom.
1.2.6.2. Dodatni zahtijevi za audio dekoder kod prijemnika nivoa HDTV Prijemnik HDTV nivoa će podržavati prijem višekanalnog (do 5.1) audia pored obaveznih zahtjeva za prijem audia kod prijemnika SDTV nivoa. Prijemnik HDTV nivoa će obezbijediti analogni audio izlaz za stereo/mono, S/PDIF izlaz i HDMI izlaz za višekanalni audio. Opciono dodatnim analognim izlazima se mogu obezbijediti dodatni surroundili audio komponente za dodatne jezike i/ili za osobe sa oštećenim vidom.
Audio izlaz prijemnika tipa iDTV HDTV nivoa mora biti sinhronizovan sa prikazanim videom.
Prijemnik HDTV nivoa mora biti u mogućnosti da dekodira i miksuje nadolje (down-mixing) format za sljedeće analogne izlaze:
-
HE AAC (5.1 kanalni nadolje miksovani stereo), ako je HE AAC implementiran u prijemniku,
-
AC3 (5.1 kanalni nadolje miksovani stereo), ako je E-AC3 implementiran u prijemniku,
-
E-AC3 (5.1 kanalni nadolje miksovani stereo), ako je E-AC3 implementiran u prijemniku,
-
MPEG1 nivo II (Musicam ISO/IEC 11172-3)(2 kanala).
Prijemnik mora uvijek imati audio signal prisutan na analognim izlazima (SCART i stereo izlaz) kad god je neki od četiri podržana formata primljen.
Prijemnik mora podržavati prenos višekanalnog audia u formatima: HE-AACi E-AC3.
1.2.6.3. HDTV servisi sa višekanlnim audiom Eksterno povezivanoj opremi (poput TV prijemnika) neće biti potrebno da podržava više od 2 kanala PCM audia unutar glavnog video/audio interfejsa (HDMI/SCART).
Prijemnik nivoa HD mora imati interni digitalni audio referentni nivo ekvivalentan referentnom Dolbynivou.
Prijemnik nivoa HD mora uskladiti izlazni nivo svih audio dekodera u cilju slaganja sa internim referentnim nivoom, tako da j e nivo primljenih programa konzistentan za sve šeme audio kodiranja. Za prijemnike karakteristika E-AC3, ovo bi trebalo biti konzistentno sa Dolby tehničkim biltenom 11: Nadogradnja zahtjeva AC3 i E-AC3 kod DVB proizvoda. Prijemnici karakteristika AC3 ili E-AC3 dekodiranja moraju obuhvatiti PCM kontolu nivoa opisanih u njima.
1.2.6.4. Audio formati Prijemnik nivoa HDTV mora u dodatku audio zahtijevima za prijemnike nivoa SDTV podržavati formate E-AC3, AC3 i HE AAC.
1.2.6.5. Sistemi sa E-AC3 tokom podataka Prijemnik nivoa HDTV mora imati mogućnosti za obradu AC3 i E-AC3 toka podataka.
Prijemnik mora da obezbjedi sljedeće funkcionalnosti na HDMI izlaznominterfejsu:
-
Propuštanje originalnog toka podataka AC3 i E-AC3;
-
E-AC3 tok podataka transkodiran na AC3;
-
PCM stereo iz dekodiranog ili nadolje miksovanog tokapodataka.
Sljedećefunkcionalnosti su opcionena HDMI izlaznominterfejsu:
-
Višekanalni PCM iz dekodiranog toka podataka;
-
Propuštanje DTS toka podataka.
Prijemnik mora biti sposoban da obezbijedi sljedeće funkcionalnosti na S/PDIF interfejsu:
-
E-AC3 tok podataka transkodovan na AC3;
-
PCM stereo od dekodovanog ili nadolje miksovanog toka podataka;
-
Propuštanje AC3 toka podataka.
Propuštanje DTS toka podataka na S/PDIF interfejs je opcion.
Prijemnik mora imati mogućnost:
-
Dekodiranja AC3 audio toka podataka na svim brzinama signaliziranja i učestanostima odabiranja datih u ETSI TS 102 366
standardu (ne uključujući aneks E);
-
Dodatnog dekodiranja E-AC3 tokova podataka sa brzinom signaliziranja podataka od 32 kb/s do 3024 kb/s i podrške svih
učestanosti odabiranja datih u standardu ETSI TS 102 366Aneks E;
-
Transkodovanja E-AC3 toka podataka na AC3 tok podataka u skladu sa ETSI TS 102 366 standardom.
Transkodovanje na AC3 audio tok podataka mora biti na fiksnoj brzini signaliziranja bita od najmanje 640 kb/s.
Prijemnik mora podržavati upotrebu Dolby metapodatakaugrađenih u audio tok podataka kod dekodiranja AC3 ili E-AC3 toka podataka, transkodovanog E-AC3 toka podataka na AC3 ili kreiranju PCM sterea nadolje miksovanog od dekodiranog E-AC3 ili AC3 toka podataka. 1.2.6.6. Sistemi sa HE AAC tokom podataka Prijemnik nivoa HDTV mora imati mogućnosti za obradu HE AAC toka podataka.
Prijemnik mora biti sposoban da obezbjijedi sledeće funkcionalnosti na HDMI izlaznom interfejsu:
-
Propuštanje originalnog HE AAC toka podataka;
-
Višekanalni HE AAC tok podataka transkodovan na AC3 ili DTS;
-
PCM stereo iz dekodiranog ili nadolje miksovanog toka podataka.
Sljedećefunkcionalnosti su opcione za HDMI izlazni interfejs:
-
Višekanalni PCM iz dekodiranog toka podataka;
-
Propuštanje DTS toka podataka.
Prijemnik mora biti sposoban da obezbijedi sledeće funkcionalnosti na S/PDIF interfejsu:
-
PCM stereo iz dekodiranog ili nadolje miksovanog toka podataka;
-
Višekanalni HE AAC tok podataka transkodovan na AC3 ili DTS.
Propuštanje DTS toka podataka na S/PDIF interfejs je opcion.
Prijemnik mora omogućiti u skladu sa standardom ETSI TS 101 154 Aneks C:
-
Dekodiranje HE AAC nivo 2 (mono, stereo) učestanošću odabiranja od 48 kHz;
-
Dekodiranje HE AAC nivo 4 (više kanalni do 5.1) učestanošću odabiranja od 48 kHz.
-
Transkodiranje HE AAC nivo 4 (više kanalni do 5.1) uč estanošću odabiranja od 48 kHz u AC3 ili DTS.
Ako je podržano transkodiranje u AC3, audio tok podataka mora biti u skladu sa standardom ETSI TS 102 366, na fiksnoj brzini signaliziranja od 640 kb/s.
Ako je podržano transkodiranje u DTS, audio tok podataka mora biti u skladu sa standardom ETSI TS 102 114 na fiksnoj brzini signaliziranja od 1536 Mb/s.
Prijemnik nivoa HDTV mora podržati upotrebu sljedećih HE AAC metapodataka ugrađenih u audio tok podataka kada je dekodiranje HE AAC i transkodiranje višekanalnog HE AAC u AC3 ili DTS omogućeno:
-
Dinamičku kontrolu opsega u skladu sa ISO/IEC 14496-3;
-
Referentni nivo programa u skladu sa dijelom DVB specifikacije ETSI TS 101 154"Prenos MPEG-4 pomoćnih podataka".
1.2.7.
Radio mod
Prijemnik tipa STB mora omogućiti osnovni prijem DVB-T radija i operaciju prebacivanja između kanala bez upotrebe TV ekrana. Ovo prebacivanje može biti urađeno pomoću radio/TV tastera koji se nalazi na prednjoj strani prijemnika ili na daljinskom upravlj aču.
U slučaju alfanumeričkog displeja (opciono) kod prijemnika tipa STB, displej bi trebao biti dovoljne veličine da se prikaže puno ime stanice (do 8 karaktera).
Ukoliko je DVB tok podataka označen kao "Radio servis", on bi trebao uvijek biti prikazan na STB u listi radio kanala, čak i ako bi postojao jedan elementarni video tok podataka koji se šalje uporedo.
1.2.8.
Nadogradnja sistemskog softvera
Svaki prijemnik mora imati mogućnost nadogradnje sistemskog softvera. Prijemnik mora imati najmanje jedan mehanizam za nadogradnju sistemskog softvera.
Prijemnik nivoa HDTV će podržavati i koristiti OTA (Over the Air) proceduru za nadogradnju sistemskog softvera u skladu sa standardom ETSI TS 102 006. Proizvođač prijemnika mora obezbijediti procedure i funkcije za sprovođenje nadogradnje prijemnika.
Prijemnik mora obezbijediti mehanizam da detektuje oštećeni sistemski softver prije nego je isti iskorišćen da zamijeni postojeći radni softver. Ukoliko je primljeni sistemski softver oštećen prijemnik će zadržati trenutnu (radnu) verziju sistemskog softvera, održavajući na taj način prijemnik ponovo funkcionalnim. U tom slučaju, greška u preuzimanju će biti naznačena korisniku sa porukom o grešci koja može biti isko rišćena za kontakt sa kancelarijom za odnose sa korisnikom. Prijemnik mora imati mogućnost da korisnik prekine preuzimanje (u oblastima lošeg kvaliteta prijema preuzimanje može trajati dugo) a prijemnik će biti i dalje funkcionalan koristeći postojeću verziju sistemskog softve ra.
Proizvođač prijemnika mora obezbijediti zahtijevani MPEG-2 TS binarni fajl (koji sadrži samo primjenljive servise za nadogradnju sistemskog softvera i njihove PSI/SI signalizacije neophodne za uspješnu nadogradnju). Za svaku preuzetu novu verziju sistemskog softvera, proizvođač mora obezbijediti sva neophodna dokumenta mrežnom operatoru potrebna za prenos nove verzije sistemskog softvera. Proizvođač je odgovoran za obezbjeđivanje i distribuciju novih verzija sistemskog softvera.
1.2.9.Middleware
Middleware je softverski dio prijemnika koji povezuje mogućnosti opreme i sistemski softver, omogućavajući korisnicima interakciju.
1.2.9.1. Servisne informacije Prijemnik mora imati sistemski softver za interpretaciju i rukovanje informacijama o aktivnim servisima , kao i kontrolu lokalnog hardvera/softvera u skladu sa standardima EN 300 468 i ETSI TR 101 211.
Prijemnik mora biti u mogućnosti da obradi PCI/SI tabele za oba transportna toka podataka i to "aktuelni" i "naredni". Sljedeće tabele su obavezne i prijemnik mora biti u mogućnosti da obradi: NIT, CAT, PAT, PMT, SDT, EIT, TDT, TOT.
Prijemnik mora ponuditi osnovnu funkcionalnost za EPG (Electronic Program Guide) sa ciljem da prikaže sljedeće podatke:
-
EIT (Event Information Table) aktuelni (trenutni/sljedeći/planirani)
-
EIT naredni (trenutni/sljedeći/planirani).
1.2.9.2. Navigator (korisnički interfejs) Navigator, tj. korisnički interfejs mora biti predstavljen na jeziku i pismu u službenoj upotrebi u Crnoj Gori, tj. mora biti moguć prikaz slova latiničnog pisma prema kodnoj šemi definisanoj standardom ISO/IEC 8859-2 odnosno prikaz slova ćiriličnog pisma prema kodnoj šemi definisanoj standardom ISO/IEC 8859-5. Takođe će biti podržan i prikaz slova prema kodnoj šemi ISO/IEC 8859-1 i ISO/IEC 8859-16.
U Crnoj Gori u ravnopravnoj upotrebi su dva pisma: latinica i ćirilica. I latinica i ćirilica su slovna pisma. Sastoje se od 32 slova (grafema). U ćiriličnom pismu svaki fonem ima poseban grafem za obilježavanje, što znači da se ćirilično pismo sastoji od 32 monografa (jednoslova). Latinica ima 29 monografa (jednoslova) i 3 digrafa (dvoslova). Digrafi su: dž, lj i nj.
Svi jezici u službenoj upotrebi moraju biti podržani tako da korisnik može izabrati i memorisati svoj izbor.
Korisnik mora biti u mogućnosti da podesi i memoriše svoj izbor kao osnovni jezik zvuka tj. audia. Ukoliko audio tok podataka u datom servisu sadrži osnovni jezik zvuka shodno izboru korisnika, prijemnik će automatski izabrati tok podataka na osnovnom jeziku izabranom i podešenom od strane korisnika.
Prijemnik mora obezbijediti osnovni EPG za prikaz EIT trenutnog i sljedećeg sadržaja (kratak opis emisije, prošireni opis emi sije, opis sadržaja). Takođe, tabela EIT planiranog programa bi trebala biti prezentovana unutar odgovarajućeg navigatora prijemnika.
1.2.9.3. Teletekst Prijemnik nivoa SDTV mora imati najmanje jednu od sljedećih opcija za prikaz teleteksta:
-
Insertovanje podataka u EBU (European Broadcasting Union) teletekstu VBI (Vertical Blanking Information) analognog CVBS
(Composite Video Baseband Signal) video signala. Insertovanje podataka će biti u skladu sa ITU-R BT.653-3 preporukom i
zahtjevima za nivo 1.5 definisan ETS 300 706 standardom;
-
Putem navigatora (korisničkog interfejsa) prijemnika.
Prijemnik nivoa HDTV mora biti u mogućnosti da prikaže teletekst (normalne stranice teleteksta i stranice teletekst transkripta) pomoću OSD-a (On-Screen Display), u skladu sa zahtjevima za nivo 1.5 definisanih standardom ETSI EN 300 706.
1.2.9.4. Transkript Prijemnik mora biti u mogućnosti da dekodira i prikazuje DVB transkript servise koji su prenošeni u skladu sa standardom ETSI EN 300 743,uključujući i karaktere iz kodnih tabela datih u dijelu specifikacije koja se odnosi na navigator, tj. korisnički interfejs.
Prijemnik nivoa HDTV mora uključiti standardne fontove sa dobrom čitljivošću za sve izlazne SDTV i HDTV video rezolucije.
Prijemnik nivoa HDTV bi trebao biti u mogućnosti da poveća veličinu DVB SDTV transkripta i EBU teletekst transkript za servise sa HDTV videom, sa ciljem da zadrži istu relativnu veličinu koju ima DVB SDTV transkript i teletekst transkript unutar SDTV videa. Povećanje veličine bi trebalo biti urađeno sa dobrom čitljivošću na HDTV izlazu.
1.2.9.5. Podešavanja korisnika Korisnik mora biti u mogućnosti da snimi prioritete u trajnu memoriju, bez obzira na isključivanje prijemnika.
Prijemnik mora obezbijediti funkciju resetovanja svih parametara na fabrička podešavanja, uklanjajući sve servisne liste, korisnikove prioritete itd. Poslije resetovanja prijemnik će ući u stanje za podešavanje (instalaciju).
1.2.9.6. Roditeljska kontrola Prijemnik može da omogući podršku za zaključavanje (zabranu gledanja) određenih emisija od strane roditelja, zasnovano na pod atku o uzrastu ispod kojeg se ne preporučuje gledanje emisije. U sluč aju da zabrana gledanja postoji prijemnik mora da podrži:
-
izbor zaključavanja i otključavanja sa lozinkom;
-
mogućnost izbora minimalnog uzrasta za određivanje zaključanih emisija;
-
automatsko onemogućavanja prikaza slike i zvuka nakon promjene programa na onaj program na kome se prikazuje emisija
iznad dozvoljenog uzrasta, uz prikaz odgovarajuće poruke korisniku;
-
da svi izlazni interfejsi onemoguće prenos signala zaključanih emisija.
1.2.10. Daljinski upravljač Prijemnik mora imati i daljinski upravljač koji će biti lagan za korišćenje. Funkcionalnost daljinskog upravljača može biti definisana od strane proizvođača.
Prijemnik mora omogućiti izvršavanje svih funkcija (osim isključivanja napajanja), korišćenjem daljinskog upravljača.
Sve funkcije moraju biti dostupne putem pretrage menija navigatora uz korišćenje tastera strelica, tastera za potvrđivanje, tastera za povratak i dodatnog komandnog tastera. Proizvođač može da odredi dodatne tastere za izvršavanje brzih komandi.
1.2.11. Fabrička podešavanja
Za prijemnike nivoa SDTV i HDTV sljedeća podešavanja moraju biti obezbjeđena:
-
osnovni jezik korisničkog interfejsa i podešavanje titlovanja na jednom od jezika u službenoj upotrebi u Crnoj Gori;
-
osnovna kodna stranica jezika podešena na jednom od jezika u službenoj upotrebi u Crnoj Gori;
-
jednosmjerno napajanje antene:
isključeno
-
transkript:
uključeno
-
analogni video izlaz format:
4:3
-
konverzija na format 16:9:
uključeno
-
OTA nadogradnja sistemskog softvera:
uključeno
-
osnovni digitalni audio izlaz podešen na PCM stereo u skladu sa IEC 60958.
PRILOG 2
NAČIN POPUNJAVANJA TABELE SA OPISOM TEHNIČKIH PODATAKA PRIJEMNIKA DIGITALNOG TELEVIZIJSKOG SIGNALA
Svaki TV prijemnik za prijem digitalnog televizijskog signala koji se stavlja na tržište ima odgovarajući opis tehničkih podataka uređaja, i to:
-
"Vrsta signala" upisuje se DVB-T2. Za uređaje koji mogu koji mogu primiti više vrsta signala navode se sve vrste signala koji
se primaju;
-
"Vrsta usluge" navode se sve usluge koje prijemnik može dekodirati: TV programi, elektronski programski vodič (EPG),
mogućnost uslovnog pristupa (CI), mogućnost hibridnog broadband radio-difuznog pristupa (HbbTV) i druge usluge;
-
"Radio-frekvencijski opseg" upisuje se odgovarajući opseg odnosno 470-790 MHz (UHF kanali 21-60), i/ili 174-230 MHz (VHF
kanali 5-12);
-
"Način prijema signala" upisuje se odgovarajuća opcija prijema zavisno od uređaja: odnosno "spoljašnjom antenom koja se
spaja na prijemnik" ili "prijem u pokretu" ili "prijem na prenosnom uređaju";
-
"Standard kodiranja/dekodiranja" upisuje se H.264/AVC (MPEG-4).
Tabela sa tehničkim podacima može sadržati i dodatne napomene navedene od strane proizvođača ili distributera opreme.
