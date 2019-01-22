PRILOG 1
PRAVILA INTEROPERABILNOSTI KOJIMA SE OBEZBJEĐUJE POVEZANOST IZMEĐU PROSTORNIH PODATAKA I SERVISA PROSTORNIH PODATAKA
1. Zajednički tipovi, definicije i zahtjevi
1. 1 Tipovi prostornih objekata
(1) Tip prostornih podataka: Any, Angle, Area, Boolean, CharacterString, Date, DateTime, Decimal, Distance, Integer, Length, Measure,
Number, Probability, Real, RecordType, Sign, UnitOfMeasure, Velocity i Volume treba da bude u skladu sa standardom MEST ISO/TS
19103:2005.
(2) Tip prostornih podataka: DirectPosition, GM_Boundary, GM_Curve, GM_MultiCurve, GM_MultiSurface, GM_Object, GM_Point,
GM_Primitive, GM_Solid, GM_Surface i GM_Tin treba da bude u skladu sa standardom MEST ISO 19107:2005.
(3) Tip prostornih podataka: TM_Duration, TM_GeometricPrimitive, TM_Instant, TM_Object, TM_Period i TM_Position treba da bude u
skladu sa standardom MEST ISO 19108:2005/AC:2008.
(4) Tip prostornih podataka: GF_PropertyType treba da bude u skladu sa standardom MEST ISO 19109:2006.
(5) Tip prostornih podataka: CI_Citation, CI_Date, CI_RoleCode, EX_Extent, EX_VerticalExtent, MD_Distributor, MD_Resolution i URL treba
da bude u skladu sa standardom MEST ISO 19115:2005/AC:2008.
(6) Tip prostornih podataka: CV_SequenceRule treba da bude u skladu sa standardom MEST ISO 19123:2007.
(7) Tip prostornih podataka: AbstractFeature, Quantity i Sign treba da bude u skladu sa standardom MEST ISO 19136:2009.
(8) Tip prostornih podataka: LocalisedCharacterString, PT_FreeText i URI treba da bude u skladu sa standardom MEST CEN ISO/TS
19139:2009.
(9) Tip prostornih podataka: LC_LandCoverClassificationSystem treba da bude u skladu sa standardom MEST ISO 19144-2:2012.
(10) Tip prostornih podataka: GFI_Feature, Location, NamedValue, OM_Observation, OM_Process, SamplingCoverageObservation,
SF_SamplingCurve, SF_SamplingPoint, SF_SamplingSolid, SF_SamplingSurface i SF_SpatialSamplingFeature treba da bude u skladu sa
standardom MEST ISO 19156:2011.
(11) Tip prostornih podataka: Category, Quantity, QuantityRange i Time primjenjuju se definicije iz Robin, Alexandre (ed.), OGC®SWE
Common Data Model Encoding Standard, version 2.0.0, Open Geospatial Consortium, 2011.
(12) Tip prostornih podataka: TimeValuePair i Timeseries primjenjuju se definicije iz Taylor, Peter (ed.), OGC®WaterML 2.0: Part 1 -
Timeseries, v2.0.0, Open Geospatial Consortium, 2012.
(13) Tip prostornih podataka: CGI_LinearOrientation i CGI_PlanarOrientation primjenjuju se definicije iz CGI Interoperability Working
Group, Geoscience Markup Language (GeoSciML), version 3.0.0, Commission for the Management and Application of Geoscience
Information (CGI) of the International Union of Geological Sciences, 2011."
2. ZAJEDNIČKE TIPA PODATAKA
2.1. Identifikator (Identifier) Spoljni jedinstveni identifikator objekta koji objavljuje javna institucija koji spoljnim aplikacijama omogućava upućivanje na prostorni objekt.
Atributi tipa podataka Identifier
Atribut
Definicija
Tip podatka
Voidability
localId
Lokalni identifikator koji dodjeljuje server. Lokalni identifikator u okviru atributa "namespace"
jedinstven je, tj. ni jedan drugi prostorni objekat nema isti lokalni identifikator.
CharacterString
namespace Prostor za naziv koji jednoznačno određuje izvor podataka prostornog objekta.
CharacterString versionId
Identifikator posebne verzije prostornog objekta dužine od najviše 25 znakova. Ako specifikacija
tipa prostornog objekta sa spoljnim identifikatorom objekta sadrži informacije o životnom
ciklusu, identifikator verzije upotrebljava se za razlikovanje različitih verzija prostornog objekta.
U nizu svih verzija prostornog objekta, verzija identifikator je jedinstvena.
CharacterString voidable
Ograničenja identifikatora tipa podataka localId i namespace smiju koristiti samo sljedeći skup znakova: {"A" …"Z", "a"…"z", "0"…"9", "_", ".", "-" }, odnosno, dopuštena su samo latinična slova, cifre, povlaka, tačka i crtica".
2.2. Povezana strana (RelatedParty) Organizacija ili osoba koja ima ulogu povezanu s izvorom.
Atributi tipa podataka RelatedParty
Atribut
Definicija
Tip
Voidability
individualName
Ime osobe koja ima ulogu povezanu s izvorom.
PT_FreeText
voidable
organisationName Naziv organizacije koja ima ulogu povezanu s izvorom.
PT_FreeText
voidable
positionName
Položaj osobe u organizaciji koja ima ulogu povezanu s izvorom (npr. načelnik odjeljenja). PT_FreeText
voidable
contact
Podaci o kontakt osobi u organizaciji koja ima ulogu povezanu s izvorom.
Contact
voidable
role
Uloga strane povezane s izvorom (npr. vlasnika).
PartyRoleValue voidable
Ograničenja tipa podataka RelatedParty Mora biti navedeno najmanje ime osobe, naziv organizacije ili naziv položaja osobe u organizaciji koja ima ulogu povezanu s izvorom.
2.3. Kontakt (Contact) Komunikacioni kanali putem kojih je moguće dobiti pristup nekome ili nečemu.
Atributi tipa podataka Contact
Atribut
Definicija
Tip
Voidability
address
Adresa navedena kao slobodan tekst.
AddressRepresentation voidable
contactInstructions
Dodatna uputstva o tome kako ili kada kontaktirati osobu ili organizaciju.
PT_FreeText
voidable
electronicMailAddress E-mail adresa organizacije ili osobe.
CharacterString
voidable
hoursOfService
Vremenski periodi tokom kojih se osoba ili organizacija mogu kontaktirati.
PT_FreeText
voidable
telephoneFacsimile
Broj faksimila organizacije ili osobe.
CharacterString
voidable
telephoneVoice
Telefonski broj organizacije ili osobe.
CharacterString
voidable
website
Stranica na World Wide Webu organizacije ili osobe.
URL
voidable 2.4. Citiranje dokumenta (DocumentCitation) Citiranje sa ciljem jasnog upućivanja na dokument.
Atributi tipa podataka DocumentCitation
Atribut
Definicija
Tip
Voidability
name
Naziv dokumenta.
CharacterString
shortName
Kratak naziv ili alternativni naslov dokumenta.
CharacterString
voidable
date
Datum izrade, objavljivanja ili revizije dokumenta.
CI_Date
voidable
link
Dionica na mrežnu verziju dokumenta.
URL
voidable
specificReference
Upućivanje na određeni dio dokumenta.
CharacterString
voidable
2.5. Citiranje propisa (LegislationCitation) Citiranje u svrhu jasnog upućivanja na pravni propis ili određeni dio pravnog propisa.
Citiranje propisa je podtip tipa DocumentCitation.
Atributi tipa podataka LegislationCitation
Atribut
Definicija
Tip
Voidability
identificationNumber
Kod (identifikacioni broj) koji se koristi za identifikovanje pravnog
propisa.
CharacterString
officialDocumentNumber Broj službenog dokumenta uporijebljen za jedinstveno identifikovanje
pravnog propisa.
CharacterString
dateEnteredIntoForce
Datum stupanja na snagu pravnog propisa.
TM_Position
dateRepealed
Datum ukidanja pravnog propisa.
TM_Position
level
Nivo na kojem je pravni propis donijet.
LegislationLevelValue
journalCitation
Navod službenog lista u kojem je pravni propis objavljen.
OfficialJournalInformation
Ograničenja tipa podataka LegislationCitation Ako je atribut dionicaa poništen (void), mora se navesti Službeni list.
2.6. Informacije iz Službenog lista (OfficialJournalInformation) Navođenje lokacije pravnog propisa u Službenom listu.
Atributi tipa podataka OfficialJournalInformation
Atribut
Definicija
Tip
Voidability
officialJournalIdentification Upućivanje na lokaciju u službenom listu u kojem je objavljen pravni propis. To
upućivanje mora se sastojati od tri dijela:
-
naziva Službenog lista
-
toma i/ili serijskog broja
-
broja stranica.
CharacterString
ISSN
Međunarodni standardni broj serijske publikacije (ISSN) je osmocifreni broj koji
označava periodične publikacije u kojima je objavljen pravni propis.
CharacterString
ISBN
Međunarodni standardni knjižni broj (ISBN) je devetocifreni broj koji na
jedinstven način označava knjige u kojima je objavljen pravni propis.
CharacterString
linkToJournal
Dionica na mrežnu verziju službenog lista.
URL
2.7. Tematski identifikator (ThematicIdentifier) Tematski identifikator za jedinstveno identifikovanje prostornog objekta.
Atributi tipa podataka ThematicIdentifier
Atribut
Definicija
Tip
Voidability
identifier
Jedinstveni identifikator koji se koristi za identifikovanje prostornog objekta u okviru
određene identifikacione šeme.
CharacterString
identifierScheme Identifikator koji definiše šemu upotrijebljenu za dodjeljivanje identifikatora.
CharacterString"
3. ZAJEDNIČKE ENUMERACIJE
3.1. Vertikalni položaj (VerticalPositionValue) Relativni vertikalni položaj prostornog objekta.
Vrijednosti dopuštene za enumeraciju VerticalPositionValue
Vrijednost
Definicija
onGroundSurface
Prostorni objekat je na nivou površine zemlje.
suspendedOrElevated
Prostorni objekat visi iznad zemlje ili je uzdignut iznad zemlje.
underground
Prostorni objekat je ispod zemlje.
4. ZAJEDNIČKI POPISI KODOVA (ŠIFRARNIK)
4.1. Stanje industrijskog objekta (ConditionOfFacilityValue) Status industrijskog objekta u pogledu njegove dovršenosti i upotrebe.
Dopuštene vrijednosti za ovaj popis kodova sastoje se od vrijednosti u nastavku i ograničenih vrijednosti koje su definisali provideri podataka.
Vrijednosti za popis kodova ConditionOfFacilityValue
Vrijednost
Naziv
Definicija
functional
funkcionalno Objekat je funkcionalan.
projected
projektovana Objekat je projektovan. Izgradnja još nije započeta.
underConstruction u izgradnji
Industrijski objekat se gradi i još nije funkcionalan. Ovo se primjenjuje samo na početku izgradnje
industrijskog objekta, a ne na posao održavanja.
disused
zastarjelo
Industrijski objekat se više ne koristi, ali se ne stavlja niti je stavljeno van pogona.
decommissioned
izvan pogona Objekat se više ne koristi, ali se stavlja ili je stavljena van pogona.
4.2. Oznaka države (CountryCode) Oznaka države u skladu sa Međuinstitucionalnim stilskim priručnikom.
4.3. Zakonodavna vrijednost (LegislationLevelValue) Nivo na kojem je pravni propis donešen ili sporazum potpisan.
Dopuštene vrijednosti za ovaj popis kodova sastoje se od svih vrijednosti koje su definisali provideri podataka.
Provajderi podataka mogu upotrijebiti vrijednosti određene u dokumentu "Tehnički vodič INSPIRE o generičkom konceptualnom modelu INSPIRE (INSPIRE Generic Conceptual Model)".
4.4. Uloga strane (PartyRoleValue) Uloge ili odgovornost strane povezane s nekim izvorom.
Dopuštene vrijednosti za ovaj popis kodova sastoje se od vrijednosti sljedećih popisa kodova ili drugih popisa kodova koje su odredili provajderi:
- Kod uloge (CI_RoleCode): Funkcije koje sprovodi odgovorna strana treba da bude u skladu sa standardom MEST ISO
19115:2005/AC:2008.
- Uloga povezane strane (RelatedPartyRoleValue): Klasifikacija uloga povezanih strana kako je određeno u tabeli u nastavku.
Vrijednosti za popis kodova RelatedPartyRoleValue
Vrijednost
Naziv
Definicija
authority
nadležni organ
Strana koja je ovlašćena da nadzire izvor i/ili strane povezane s izvorom.
operator
rukovodilac
Strana koja upravlja izvorom.
owner
vlasnik
Strana koja posjeduje izvor, tj. ona kojoj izvor pripada.
4.5. Nazivi klimatoloških i prognostičkih standarda (CFStandardNamesValue) Definicije fenomena koji se posmatraju u meteorologiji i okeanografiji.
Dopuštene vrijednosti za ovaj popis kodova sastoje se od svih vrijednosti koje su definisali provajderi podataka.
Provajderi podataka mogu koristiti vrijednosti određene u dokumentu "Tehnički vodič INSPIRE o generičkom konceptualnom modelu INSPIRE (INSPIRE Generic Conceptual Model)".
4.6. Pol (GenderValue) Pol osobe ili grupe osoba.
Dopuštene vrijednosti za ovaj popis kodova sastoji se samo od vrijednosti određenih u tabeli u nastavku.
Vrijednosti za popis kodova GenderValue
Vrijednost
Naziv
Definicija
female
žensko
Osoba ili grupa osoba ženskog pola.
male
muško
Osoba ili grupa osoba muškog pola.
unknown
nepoznato
Osoba ili grupa osoba nepoznatog pola.
5. GENERIČKI MODEL MREŽE
5.1. Tip prostornog objekta
5.1.1. Unakrsna referenca (CrossReference) Referenca između dva elementa u istoj mreži.
Asocijacijske uloge tipa prostornog objekta (CrossReference)
Asocijacijska uloga
Definicija
Tip podatka
Voidability
element
Unakrsno referentni elementi.
NetworkElement
5.1.2. Generalizovana dionica (GeneralisedLink) Generalizovana dionica je Apstraktni osnovni tipkoja prikazuje linijski element mreže koji se pri linearnom upućivanju može upotrijebiti kao cilj.
Generalizovana dionica je podtip tipa NetworkElement.
5.1.3. Prelaz na odvojenim nivoima (GradeSeparatedCrossing) Indikator koji pokazuje koji od dva ili više elemenata koji se sijeku leži ispod, a koji iznad i koji se upotrebljava ako nema visinskih koordinata ili nisu pouzdane.
Prelaz na odvojenim nivoima je podtip tipa NetworkElement.
Asocijacijske uloge tipa prostornog objekta GradeSeparatedCrossing
Asocijacijska uloga
Definicija
Tip podatka Voidability
element
Niz dionica koje se ukrštaju. Redoslijed odražava njihovu visinu; prva dionica leži najniže.
Link
5.1.4. Dionica (Link) Zakrivljen element mreže koji povezuje dva položaja i predstavlja homogeni put u mreži. Povezani se položaji mogu prikazati kao čvorovi. Dionica je podtip tipa GeneralisedLink.
Dionica je apstraktni tip.
Atributi tipa prostornog objekta Link
Atribut
Definicija
Tip
podatka
Voidability
centrelineGeometry Geometrija koja predstavlja središnju liniju dionice.
GM_Curve fictitious
Indikator koji pokazuje da je geometrija središnje linije dionice prikazana ravnom crtom bez neposrednih kontrolnih tačaka, osim ako ravna crta na odgovarajući način ne predstavlja
geografiju na nivou rezolucije skupa podataka.
Boolean
Asocijacijske uloge tipa prostornog objekta Link
Asocijacijska uloga
Definicija
Tip podatka Voidability
endNode
Izborni završni čvor za ovu dionica. Završni čvor može biti isti primjer kao i početni čvor.
Node
startNode
Izborni početni čvor za ovu dionica.
Node
5.1.5. Niz dionica (LinkSequence) Element mreže koji pokazuje neprekidni put u mreži bez grananja.
Element ima određen početak i kraj i svaki položaj u dijelu dionice može se odrediti samo jednim parametrom, npr. dužinom.
Niz dionica je podtip tipa GeneralisedLink.
Riječ je o apstraktnom tipu.
Atributi tipa prostornog objekta LinkSequence
Atribut
Definicija
Tip podatka
Voidability
link
Uređena zbirka usmjerenih dionica koje čine niz dionica.
DirectedLink
5.1.6. Skup dionica (LinkSet) Zbirka niza dionica i/ili pojedinačnih dionica koja ima posebnu funkciju ili značenje u mreži.
Skup dionica je podtip tipa NetworkElement.
Riječ je o apstraktnom tipu.
Asocijacijske uloge tipa prostornog objekta LinkSet
Asocijacijska uloga
Definicija
Tip podatka
Voidability
link
Serija dionica ili niz link koje prave skup dionica.
GeneralisedLink
5.1.7. Mreža (Network) Mreža je zbirka mrežnih elemenata.
Atributi tipa prostornog objekta Network
Atribut
Definicija
Tip podatka
Voidability
geographicalName
Geografsko ime mreže.
GeographicalName
voidable
Asocijacijske uloge tipa prostornog objekta Network
Asocijacijska uloga
Definicija
Tip podatka
Voidability
elements
Zbirka elemenata koji formiraju mrežu.
NetworkElement
5.1.8. Područje mreža (NetworkArea) Dvodimenzionalni element u mreži.
Područje mreža je podtip tipa NetworkElement.
Riječ je o apstraktnom tipu.
Atributi tipa prostornog objekta NetworkArea
Atribut
Definicija
Tip podatka
Voidability
geometry
Prikazuje geometrijska svojstva područja
GM_Surface
5.1.9. Povezanost mreža (NetworkConnection) Prikazuje logičku povezanost između dva ili više elemenata mreže u različitim mrežama.
Povezanost mreža je podtip tipa NetworkElement.
Atributi tipa prostornog objekta NetworkConnection
Atribut
Definicija
Tip podatka
Voidability
type
Kategorizacija povezanosti mreža.
ConnectionTypeValue
voidable
Asocijacijske uloge tipa prostornog objekta NetworkConnection
Asocijacijska uloga
Definicija
Tip podatka
Voidability
element
Elementi mreže u različitim mrežama.
NetworkElement
Ograničenja tipa prostornog objekta NetworkConnection Svi elementi moraju biti u različitim mrežama.
5.1.10. Element mreže (NetworkElement) Apstraktni osnovni tip koja prikazuje element u mreži. Svaki element u mreži osigurava određenu funkciju koja je u interesu mreže.
Ovaj tip je apstraktni.
Atributi tipa prostornog objekta NetworkElement
Atribut
Definicija
Tip
podatka
Voidability
beginLifespanVersion Datum i vrijeme kad je ova verzija prostornog objekta unešena u skup prostornih
podataka ili u njemu izmijenjena.
DateTime
voidable
endLifespanVersion
Datum i vrijeme kad je ta verzija prostornog objekta izmijenjena u skupu prostornih
podataka ili iz njega izbrisana.
DateTime
voidable
inspireId
Spoljni identifikator objekta prostornog objekta.
Identifier
Asocijacijske uloge tipa prostornog objekta NetworkElement
Asocijacijska uloga
Definicija
Tip podatka
Voidability
inNetwork
Mreže koje sadrže element mreže.
Network
voidable
5.1.11. Svojstvo mreže (NetworkProperty) Apstraktni osnovni tip koji prikazuje pojave na elementu mreže ili duž nje, i osigurava opšta svojstva za povezivanje pojava u vezi s mrežom (mrežna svojstva) s elementima mreže.
Riječ je o apstraktnom tipu.
Atributi tipa prostornog objekta NetworkProperty
Atribut
Definicija
Tip podatka
Voidability
beginLifespanVersion Datum i vrijeme kad je ta verzija prostornog objekta unešena u skup prostornih
podataka ili u njemu izmijenjena.
DateTime
voidable
endLifespanVersion
Datum i vrijeme kad je ta verzija prostornog objekta izmijenjena u skupu prostornih
podataka ili iz njega izbrisana.
DateTime
voidable
inspireId
Spoljni identifikator prostornog objekta.
Identifier
networkRef
Prostorna referentna svojstva koje se odnosi na mrežu.
NetworkReference voidable 5.1.12. Čvor (Node) Prikazuje važan položaj u mreži koji se uvijek nalazi na početku ili na kraju dionice (link).
Čvor je podtip tipa NetworkElement.
Riječ je o apstraktnom tipu.
Atributi tipa prostornog objekta Node
Atribut
Definicija
Tip podatka
Voidability
geometry
Položaj čvora.
GM_Point
Asocijacijske uloge tipa prostornog objekta Node
Asocijacijska uloga
Definicija
Tip podatka
Voidability
spokeEnd
Dionice koje ulaze u čvor.
Link
voidable
spokeStart
Dionice koje napuštaju čvor.
Link
voidable
5.2. Tipa podataka 5.2.1. Usmjerena dionica (DirectedLink) Dionica u pozitivnom ili negativnom smjeru.
Atributi tipa podataka DirectedLink
Atribut
Definicija
Tip
podatka
Voidability
direction Pokazuje usklađuje li se (pozitivan smjer) usmjerene dionice ili ne usklađuje (negativan smjer) s
pozitivnim smjerom dionice.
Sign
Asocijacijske uloge tipa podatka DirectedLink
Asocijacijska uloga
Definicija
Tip podatka
Voidability
link
Dionica
Link
5.2.2. Referentna dionica (LinkReference) Mrežna referenca na linijski element mreže.
Referentna dionica je podtip tipa NetworkReference.
Atributi tipa podataka LinkReference
Atribut
Definicija
Tip podatka
Voidability
applicableDirection Smjerovi generalizovane dionice na koju se odnosi referenca. U slučaju kad se
svojstvo ne odnosi na smjer uzduž dionice, nego prikazuje pojavu duž dionice,
"inDirection" se odnosi na desnu stranu dionice.
LinkDirectionValue voidable
Ograničenja tipa podatka LinkReference Ciljevi linearne reference moraju biti linijski mrežni elementi. To znači da je cilj mrežne reference dionice ili niza dionice, ako se upotrebljava linearno referenciranje ili ako je važan smjer.
5.2.3. Mrežna referenca (NetworkReference) Referenca na mrežni element.
Asocijacijske uloge tipa podatka NetworkReference
Asocijacijska uloga
Definicija
Tip podatka
Voidability
element
Referentni mrežni element.
NetworkElement
5.2.4. Jednostavna linearna referenca (SimpleLinearReference) Mrežna referenca koja je ograničena na dio linijskog mrežnog elementa. Dio mrežnog elementa je između položaja fromPosition i položaja toPosition.
Jednostavna linearna referenca je podtip tipa LinkReference.
Atributi tipa podataka SimpleLinearReference
Atribut
Definicija
Tip
podatka
Voidability
fromPosition Početni položaj linijskog elementa, izraženog kao udaljenost od početka linijskog mrežnog elementa
uzduž geometrije njegove krive.
Length
offset
Pomak od geometrije središnje linije generalizovane dionice, kad je to potrebno; pozitivan je pomak
na desno u smjeru dionice, a negativan je pomak na lijevo.
Length
voidable
toPosition
Konačni položaj linijskog elementa, izraženog kao udaljenost od početka linijskog mrežnog
elementa uzduž geometrije njegove krive.
Length
5.2.5. Jednostavna tačkasta referenca (SimplePointReference) Mrežna referenca koja je ograničena na tačku na linijskom mrežnom elementu. Ta se tačka nalazi na mrežnom elementu na položaju atPosition uzduž mreže.
Jednostavna tačkasta referenca je podtip tipa LinkReference.
Atributi tipa podatka SimplePointReference
Atribut
Definicija
Tip
podatka
Voidability
atPosition Položaj tačke, izražene kao udaljenost od početka linijskog mrežnog elementa uzduž geometrije
njegove krive.
Length
offset
Pomak od geometrije središnje linije generalizovane dionice, kad je potrebno; pozitivan pomak je na
desno u smjeru dionice, a negativan je pomak na lijevo.
Length
voidable
5.3. Popisi kodova
5.3.1. Tip povezanosti (ConnectionTypeValue) Tipa povezanosti između različitih mreža.
Popis kodova vodi se u zajedničkom registru popisa kodova.
Vrijednosti dopuštene za popis kodova ConnectionTypeValue
Vrijednost
Definicija
crossBorderConnected Povezanost između dva elementa mreže u različitim mrežama iste tipa, ali u susjednim područjima. Referentni
mrežni elementi predstavljaju različite, ali prostorno povezane pojave u stvarnom svijetu.
crossBorderIdentical
Povezanost između dva elementa mreže u različitim mrežama iste tipa, ali u susjednim područjima. Referentni
mrežni elementi predstavljaju iste pojave u stvarnom svijetu.
intermodal
Povezanost između dva elementa mreže u različitim saobraćajnim mrežama koje upotrebljavaju različite načine
prevoza. Povezanost predstavlja mogućnost promjene transportovanog medija (ljudi, roba, itd.) s jednog oblika
prevoza na drugi.
5.3.2. Smjer dionice (LinkDirectionValue) Popis vrijednosti za smjerove u odnosu na dionicu.
Popis kodova vodi se u zajedničkom registru popisa kodova.
Vrijednosti dopuštene za popis kodova LinkDirectionValue
Vrijednost
Definicija
bothDirections
U oba smjera.
inDirection
U smjeru dionice.
inOppositeDirection
U smjeru suprotnom od smjera dionice.
6. MODEL POKRIVENOSTI (COVERAGE MODEL) Model pokrivenosti infrastrukture prostornih podataka (INSPIRE) sastoji se od sljedećih paketa:
- Pokrivenost (osnovna) (Coverages (Base)) - Pokrivenost (domen i raspon) (Coverages (Domain And Range)) 6.1. Pokrivenost (osnovna)
6.1.1. Tipovi prostornih objekata Paket Pokrivenost (osnovni) sadrži tip prostornih objekata Pokrivenost.
6.1.1.1. Pokrivenost (Coverage) Prostorni objekt koji djeluje kao funkcija na povratne vrijednosti iz vlastitog raspona za bilo koji direktni položaj unutar svog prostornog, temporalnog ili prostorno-temporalnog domena.
Ovaj tip je apstraktni.
Atributi prostornog objekta tipa Coverage
Atribut
Definicija
Tip
Voidability
metadata
Specifični metapodaci paketa pokrivenosti.
Any
rangeType
Opis strukture vrijednosti raspona.
RecordType
6.2. Pokrivenost (domen i raspon)
6.2.1. Tipovi prostornih objekata Paket Pokrivenosti (domena i raspon) sadrži sljedeće tipove prostornih objekata:
-
Pokrivenost (prikaz domena i raspona);
-
Pokrivenost ispravljenom mrežom; i -
Pokrivenost mrežom na koju je moguće upućivati.
6.2.1.1. Pokrivenost (prikaz domena i raspona) (CoverageByDomainAndRange) Pokrivenost koja navodi domen i raspon kao posebna svojstva.
Pokrivenost je podtip tipa Coverage.
Ovaj tip je apstraktni.
Atributi prostornog objekta tipa CoverageByDomainAndRange
Atribut
Definicija
Tip
Voidability
coverageFunction Opis načina dobijanja vrijednosti raspona na lokacijama u domenu pokrivenosti.
CoverageFunction domainSet
Konfiguracija domena pokrivenosti opisana koordinatama.
Any
rangeSet
Skup vrijednosti koje su prema funkciji pridružene elementima domena pokrivenosti.
Any
Ograničenja prostornog objekta tipa CoverageByDomainAndRange Funkcija mreže odgovara samo za domene koji su u mreži.
6.2.1.2. Pokrivenost ispravljenom mrežom (RectifiedGridCoverage) Pokrivenost čiji se domen sastoji od ispravljene mreže.
Pokrivenost ispravljenom mrežom je podtip tipa CoverageByDomainAndRange.
Ograničenja prostornog objekta tipa RectifiedGridCoverage Domen mora biti ispravljena mreža.
Tačke mreže tipa RectifiedGridCoverage moraju se poklapati sa središtima ćelija geografskih mreža definisanih u dijelu 2.2. Priloga 2 na bilo kojem nivou rezolucije.
6.2.1.3. Pokrivenost mrežom na koju je moguće upućivati (ReferenceableGridCoverage) Pokrivenost čiji se domen sastoji od mreže na koju je moguće upućivati.
Pokrivenost mrežom na koju je moguće upućivati je podtip tipa CoverageByDomainAndRange.
Ograničenja prostornog objekta tipa ReferenceableGridCoverage Domen mora biti mreža na koju je moguće upućivati.
6.2.2. Tipovi podataka
6.2.2.1. Funkcija pokrivenosti (CoverageFunction) Opis načina dobijanja vrijednosti raspona na lokacijama u domenu pokrivenosti.
Funkcija pokrivenosti je tip unije.
Atributi tipa unije CoverageFunction
Atribut
Definicija
Tip
Voidability
ruleDefinition
Službeni ili neslužbeni opis funkcije pokrivenosti u tekstualnom obliku.
CharacterString
ruleReference
Službeni ili neslužbeni opis funkcije pokrivenosti kao reference.
URI
gridFunction
Pravilo mapiranja za geometrije mreže.
GridFunction
6.2.2.2. Funkcija mreže (GridFunction) Eksplicitno pravilo mapiranja za geometriju mreže.
Atributi tipa podataka GridFunction
Atribut
Definicija
Tip
Voidability
sequenceRule Opis načina na koji su tačke mreže poređane za pridružavanje s elementima vrijednosti u
skupu raspona pokrivenosti.
CV_SequenceRule
startPoint
Tačka mreže koja će se pridružiti prvom zapisu u skupu raspona pokrivenosti.
Integer
7. MODEL POSMATRANJA (OBSERVATIONS MODEL) Model posmatranja infrastrukture prostornih podataka (INSPIRE) sastoji se od sljedećih paketa:
- Reference posmatranja (Observation References);
- Procesi (Processes);
- Svojstva koja je moguće posmatrati (Observable Properties); i - Specijalizovana posmatranja (Secialised Observations).
7.1. Reference posmatranja
7.1.1. Tipovi prostornih objekata Paket Reference posmatranja sadrži tip prostornog objekta Skup posmatranja.
7.1.1.1. Skup posmatranja (ObservationSet) Povezuje skup Posmatranja.
Atributi prostornog objekta tipa ObservationSet
Atribut
Definicija
Tip
Voidability
inspireId
Identifikator spoljnog prostornog objekta.
Identifier
extent
Informacije o prostornoj i temporalnoj granici.
EX_Extent
Uloge pridruživanja prostornog objekta tipa ObservationSet
Uloga pridruživanja
Definicija
Tip
Voidability
member
Jedan član tipa ObservationSet.
OM_Observation
7.2. Procesi
7.2.1. Tipovi prostornih objekata Paket Procesi sadrži tip prostornih objekata Process.
7.2.1.1. Proces (Process) Opis procesa posmatranja.
Proces je podtip tipa OM_Process.
Atributi prostornog objekta tipa Process
Atribut
Definicija
Tip
Voidability
inspireId
Identifikator spoljnjeg prostornog objekta.
Identifier
voidable
name
Naziv procesa.
CharacterString
voidable
type
Tip procesa.
CharacterString
voidable
documentation
Dodatne informacije (na mreži/van mreže) povezane s procesom.
DocumentCitation
voidable
processParameter
Parametar koji kontroliše paket procesa i njene rezultate.
ProcessParameter
voidable
responsibleParty
Pojedinac ili organizacija povezani s procesom.
RelatedParty
voidable
7.2.2. Tipovi podataka
7.2.2.1. Parametar procesa (ProcessParameter) Opis navedenog parametra.
Atributi tipa podataka ProcessParameter
Atribut
Definicija
Tip
Voidability
name
Naziv parametra procesa.
ProcessParameterNameValue
description
Opis parametra procesa.
CharacterString
7.2.3. Popisi kodova
7.2.3.1. Naziv parametra procesa (ProcessParameterNameValue) Popis kodova naziva parametara procesa.
Dopuštene vrijednosti za ovaj popis kodova sastoje se od svih vrijednosti koje su definisali provajderi podataka.
7.3. Svojstva koja je moguće posmatrati
7.3.1. Tipovi podataka
7.3.1.1. Ograničenje (Constraint) Ograničenje za neko svojstvo, npr. talasna dužina = 200 nm.
Atributi tipa podataka Constraint
Atribut
Definicija
Tip
Voidability
constrainedProperty
Svojstvo koje je ograničeno. Npr. "boja" ako je ograničenje "boja = plava".
PhenomenonTypeValue
label
Naslov ograničenja kao cjeline koji može pročitati čovjek.
CharacterString
7.3.1.2. Ograničenje kategorije (CategoryConstraint) Ograničenje koje se temelji na nekoj kategoriji kvalifikovanja, npr. boja = "crvena".
Ograničenje kategorije je podtip tipa Constraint.
Atributi tipa podataka CategoryConstraint
Atribut
Definicija
Tip
Voidability
comparison Operator poređenja. U slučaju ograničenja kategorije on mora biti "jednako" ili
"različito od".
ComparisonOperatorValue
value
Vrijednost svojstva koje je ograničeno, npr. "plava" (ako je ograničeno svojstvo boja).
CharacterString 7.3.1.3. Ograničenje raspona (RangeConstraint) Ograničenje numeričkog raspona nekog svojstva, npr. talasna dužina ≥ 300 nm ili talasna dužina ≤ 600 nm.
Ograničenje raspona je podtip tipa Constraint.
Atributi tipa podataka RangeConstraint
Atribut
Definicija
Tip
Voidability
value
Raspon numeričkih vrijednosti svojstva koje je ograničeno.
RangeBounds
uom
Jedinica mjere upotrebljena u ograničenju.
UnitOfMeasure
7.3.1.4. Granice raspona (RangeBounds) Početna i završna vrijednost numeričkog raspona (npr. početak ≥ 50, kraj ≤ 99).
Atributi tipa podataka RangeBounds
Atribut
Definicija
Tip
Voidability
startComparison
Poređenje upotrijebljeno za donju granicu raspona
(npr. greaterThanOrEqualTo).
ComparisonOperatorValue
rangeStart
Donja granica raspona.
Real
endComparison
Poređenje upotrijebljeno za gornju granicu raspona (npr. lessThan).
ComparisonOperatorValue
rangeEnd
Gornja granica raspona.
Real
7.3.1.5. Skalarno ograničenje (ScalarConstraint) Numeričko skalarno ograničenje nekog svojstva, npr. dužina ≥ 1 m.
Skalarno ograničenje je podtip tipa Constraint.
Atributi tipa podataka ScalarConstraint
Atribut
Definicija
Tip
Voidability
value
Numerička vrijednost svojstva koje je ograničeno.
Real
comparison
Poređenje za upotrebu u ograničenju, npr. greaterThan.
ComparisonOperatorValue
uom
Jedinica mjere upotrijebljena u ograničenju.
UnitOfMeasure
7.3.1.6. Drugo ograničenje (OtherConstraint) Ograničenje koje nije oblikovano na strukturisan način, ali se može opisati upotrebom atributa slobodnog teksta "description".
Drugo ograničenje je podtip tipa Constraint.
Atributi tipa podataka OtherConstraint
Atribut
Definicija
Tip
Voidability
description
Opis ograničenja.
CharacterString
7.3.1.7. Statistička mjera (StatisticalMeasure) Opis neke statističke mjere, npr. "dnevni maksimum".
Atributi tipa podataka StatisticalMeasure
Atribut
Definicija
Tip
Voidability
label
Naslov statističke mjere koji može pročitati čovjek.
CharacterString
statisticalFunction
Statistička funkcija, npr. srednja vrijednost.
StatisticalFunctionTypeValue aggregationTimePeriod Temporalni raspon na kojem se statistička vrijednost izračunava. Npr. TM_Duration
dan, sat.
aggregationLength
Jednodimenzionalni opseg prostora na kojem se izračunava statistička
vrijednost, npr. 1 metar.
Length
aggregationArea
Dvodimenzionalni raspon prostora na kojem se izračunava statistička
vrijednost, npr. 1 kvadratni metar.
Area
aggregationVolume
Trodimenzionalni raspon prostora na kojem se izračunava statistička
vrijednost, npr. 1 kubni metar.
Volumen
otherAggregation
Bilo koji drugi tip agregacije.
Any
Uloga pridruživanja tipa podataka StatisticalMeasure
Uloga
pridruživanja
Definicija
Tip
Voidability
derivedFrom
Jedna statistička mjera može biti izvedena iz druge, npr. maksimalne mjesečne
temperature mogu biti izvedene iz srednjih dnevnih temperatura.
StatisticalMeasure
7.3.2. Nabrajanja
7.3.2.1. Funkcija poređenja (ComparisonOperatorValue) Nabrajanje funkcija poređenja (npr. veće od).
Vrijednosti za nabrajanje ComparisonOperatorValue
Vrijednost
Definicija
equalTo
tačno jednako
notEqualTo
različito od
lessThan
manje od
greaterThan
veće od
lessThanOrEqualTo
manje ili jednako
greaterThanOrEqualTo
veće ili jednako
7.3.3. Popisi kodova
7.3.3.1. Tip fenomena (PhenomenonTypeValue) Popis kodova fenomena (npr. temperatura, brzina vjetra).
Dopuštene vrijednosti za ovaj popis kodova sastoje se od vrijednosti sljedećih popisa kodova ili drugih popisa kodova koje su definisali provajderi servisa:
- Nazivi klimatoloških i prognostičkih standarda (CFStandardNamesValue): Definicije fenomena zapaženih u meteorologiji i okeanografiji
kako je određeno u dijelu 4.5. ovog Priloga.
- Naziv parametra elementa profila (ProfileElementParameterNameValue): Svojstva koja se mogu zapaziti da bi se okarakterisao element
profila.
- Naziv parametra izvedenog iz zemljišta (SoilDerivedObjectParameterNameValue): Svojstva koja se odnose na zemljišta i koja se mogu
izvesti iz zemljišta i drugih podataka.
- Naziv parametra profila zemljišta (SoilProfileParameterNameValue): Svojstva koja se mogu zapaziti da bi se okarakterisao profil zemljišta. - Naziv parametra lokacije zemljišta (SoilSiteParameterNameValue): Svojstva koja se mogu zapaziti da bi se okarakterisala lokacija
zemljišta.
- Komponenta reference kvaliteta vazduha (EU_AirQualityReferenceComponentValue): Definicija fenomena koja se odnosi na kvalitet
vazduha u kontekstu izvještavanja.
- Tabela 4.2. kodova i zastavica Svjetske meteorološke organizacije (GRIB_CodeTable4_2Value): Definicije fenomena zapaženih u
meteorologiji i okeanografiji.
- Definicije fenomena zapaženih u okeanografiji (BODC P01 upotreba parametra - BODC_P01ParameterUsageValue).
7.3.3.2. Tip statističke funkcije (StatisticalFunctionTypeValue) Popis kodova statističkih funkcija (npr. maksimum, minimum, srednja vrijednost).
Dopuštene vrijednosti za ovaj popis kodova sastoje se od svih vrijednosti koje su definisali provajderi podataka.
7.4. Specijalizovana posmatranja
7.4.1. Tipovi prostornih objekata Paket Specijalizovana posmatranja sadrži sljedeće tipove prostornih objekata:
-
Posmatranje mreže;
-
Posmatranje niza mreža;
-
Posmatranje tačke;
-
Zbirka posmatranja;
-
Posmatranje višestrukih tačaka;
-
Posmatranje niza vremenskih tačaka;
-
Posmatranje profila; i -
Posmatranje putanje.
7.4.1.1. Posmatranje mreže (GridObservation) Posmatranje koje predstavlja polje s mrežom u jednom trenutku vremena.
Posmatranje mreže je podtip tipa SamplingCoverageObservation.
Ograničenja prostornog objekta tipa GridObservation featureOfInterest mora biti SF_SamplingSolid ili SF_SamplingSurface.
phenomenonTime mora biti TM_Instant.
result mora biti RectifiedGridCoverage ili RefererencableGridCoverage.
7.4.1.2. Posmatranje niza mreža (GridSeriesObservation) Posmatranje koje predstavlja polje s mrežom koje se razvija u jednom trenutku vremena.
Posmatranje niza mreža je podtip tipa SamplingCoverageObservation.
Ograničenja prostornog objekta tipa GridSeriesObservation featureOfInterest mora biti SF_SamplingSolid.
phenomenonTime mora biti TM_Period.
result mora biti RectifiedGridCoverage ili ReferenceableGridCoverage.
7.4.1.3. Posmatranje zbirke tačaka (PointObservation) Posmatranje koje predstavlja mjerenje svojstva u jednoj tački vremena i prostora.
Posmatranje zbirke tačaka je podtip tipa SamplingCoverageObservation.
Ograničenja prostornog objekta tipa PointObservation featureOfInterest mora biti SF_SamplingPoint.
phenomenonTime mora biti TM_Instant.
7.4.1.4. Zbirka Posmatranje tačke (PointObservationCollection) Zbirka posmatranje tačke.
Zbirka Posmatranje tačke je podtip tipa ObservationSet.
Ograničenja prostornog objekta tipa PointObservationCollection Svaki član mora biti PointObservation.
7.4.1.5. Posmatranje višestrukih tačaka (MultiPointObservation) Posmatranje koje predstavlja skup mjerenja koja su sprovedena u istom trenutku, ali na različitim lokacijama.
Posmatranje višestrukih tačaka je podtip tipa SamplingCoverageObservation.
Ograničenja prostornog objekta tipa MultiPointObservation featureOfInterest mora biti SF_SamplingCurve, SF_SamplingSurface ili SF_SamplingSolid.
phenomenonTime mora biti TM_Instant result mora biti MultiPointCoverage.
7.4.1.6. Posmatranje niza vremenskih tačaka (PointTimeSeriesObservation) Posmatranje koje predstavlja vremenski niz mjerenja tačke nekog svojstva na fiksnoj lokaciji u prostoru.
Posmatranje niza vremenskih tačaka je podtip tipa SamplingCoverageObservation.
Ograničenja prostornog objekta tipa PointTimeSeriesObservation featureOfInterest mora biti SF_SamplingPoint.
phenomenonTime mora biti TM_Period.
result mora biti Timeseries.
7.4.1.7. Posmatranje profila (ProfileObservation) Posmatranje koje predstavlja mjerenje svojstva zajedno s vertikalnim profilom u prostora u jednom trenutku vremena.
Posmatranje profila je podtip tipa SamplingCoverageObservation.
Ograničenja prostornog objekta tipa PointObservation featureOfInterest mora biti SF_SamplingCurve.
phenomenonTime mora biti TM_Instant.
result mora biti ReferenceableGridCoverage ili RectifiedGridCoverage.
Prostorni domen rezultata mora sadržati jednu osu i mora biti vertikalna.
7.4.1.8. Posmatranje putanje (TrajectoryObservation) Posmatranje koje predstavlja mjerenje svojstava duž neke krive u vremenu i prostoru.
Posmatranje putanje je podtip tipa SamplingCoverageObservation.
Ograničenja prostornog objekta tipa TrajectoryObservation phenomenonTime mora biti TM_Period.
result mora biti Timeseries.
Svaka tačka u result mora biti TimeLocationValueTriple.
featureOfInterest mora biti SF_Sampling Curve.
7.4.2. Tipovi podataka
7.4.2.1. Vrijeme, lokacija, vrijednost (TimeLocationValueTriple) Skup trojke: vrijeme, lokacija, vrijednost (mjerenje). Na primjer, u tački duž putanje.
Skup trojke vrijeme, lokacija, vrijednost je podtip tipa TimeValuePair.
Atributi tipa podataka TimeLocationValueTriple
Atribut
Definicija
Tip
Voidability
location
Geografska lokacija na kojoj je vrijednost ispravna.
GM_Position
7.5. Zahtjevi za posmatranje Ako se za raspoloživost podataka koristi tip OM_Observation ili bilo koji podtip, primjenjuju se sljedeći zahtjevi:
(1) Tip Process mora se koristiti za označavanje postupka upotrijebljenog u OM_Observation.
(2) Ako se iz OM_Observation upućuje na EnvironmentalMonitoringFacility, mora se navesti atribut parametra čiji naziv je
"relatedMonitoringFeature" a vrijednost je tipa AbstractMonitoringFeature.
(3) Za sva kodiranja koja su upotrijebljena u cijelom ili dijelu OM_Observation rezultata mora biti dostupan javni interfejs za programiranje
aplikacija (API) zbog čitanja kodirane datoteke. API mora imati mogućnost izlaganja potrebnih informacija za dobijanje prostornih
objekata.
(4) Ako u svojstvu postupka OM_Observation objekta postoji atribut processParameter, njegova vrijednost (naziv) mora biti obuhvaćena
atributom parametra OM_Observation.
8. MODEL KOMPLEKSA AKTIVNOSTI Kompleks aktivnosti infrastrukture prostornih podataka sadrži paket Kompleks aktivnosti (Activity Complex).
8.1. Kompleks aktivnosti
8.1.1. Tipovi prostornih objekata Paket Kompleks aktivnosti sadrži tip prostornih objekata Kompleks aktivnosti.
8.1.1.1. Kompleks aktivnosti (ActivityComplex) Jedna jedinica koja je tehnički i ekonomski pod kontrolom menadžmenta pravnog subjekta (operater) i obuhvata aktivnosti poput onih navedenih u klasifikaciji Eurostat NACE. Kompleks aktivnosti mora predstavljati cijelo područje na istoj ili različitim geografskim lokacijama kojim upravlja isti rukovodilac, uključujući cijelu infrastrukturu, opremu i materijale.
Atributi prostornog objekta tipa ActivityComplex
Atribut
Definicija
Tip
Voidability
inspireId
Identifikator spoljnog prostornog objekta.
Identifier
thematicId
Tematski identifikator kompleksa aktivnosti.
ThematicIdentifier geometry
Geometrija upotrijebljena za definisanje opsega ili položaja kompleksa aktivnosti.
GM_Object
function
Aktivnosti koje sprovodi kompleks aktivnosti. Funkcija je opisana prema
aktivnostima i može biti dopunjena informacijama o ulazima i izlazima koji su njen
rezultat.
Function
name
Opisni naziv kompleksa aktivnosti.
CharacterString
voidable
validFrom
Vrijeme od kojeg je kompleks aktivnosti počeo postojati u stvarnom svijetu.
DateTime
voidable
validTo
Vrijeme od kojeg kompleks aktivnosti više ne postoji u stvarnom svijetu.
DateTime
voidable
beginLifespanVersion Datum i vrijeme postavljana ili promjene ove verzije prostornog objekta u skupu
prostornih podataka.
DateTime
voidable
endLifespanVersion
Datum i vrijeme zamjene ili povlačenja ove verzije prostornog objekta iz skupa
prostornih podataka.
DateTime
voidable
8.1.2. Tipovi podataka
8.1.2.1. Funkcija (Function) Funkcija izražena kao aktivnost i opcijski izlaz i/ili izlaz.
Atributi tipa podataka Function
Atribut
Definicija
Tip
Voidability
activity
Kategorizovani opis pojedinačnog ili organizovanog skupa tehnički povezanih postupaka
koje sprovodi ekonomska jedinica, privatnog ili javnog, profitnog ili neprofitnog
karaktera.
EconomicActivityValue
input
Svaki klasifikovani ili registrovani materijal koji ulazi u tehničku i ekonomsku jedinicu u
skladu sa svojom funkcijom.
InputOutputValue
voidable
output
Svaki klasifikovani ili registrovani materijal koji izlazi iz tehničke i ekonomske jedinice u
skladu sa svojom funkcijom.
InputOutputValue
voidable
description Opis funkcije s više pojedinosti.
PT_FreeText
voidable
8.1.2.2. Kapacitet (Capacity) Kvantifikacija stvarne ili potencijalne sposobnosti sprovođenja neke aktivnosti koja se generalno ne mijenja, ne mijenja se često ili se ne mijenja do značajnog stepena.
Atributi tipa podataka Capacity
Atribut
Definicija
Tip
Voidability
activity
Kategorizovani opis pojedinačnog ili organizovanog skupa tehnički povezanih postupaka
koje sprovodi ekonomska jedinica, privatnog ili javnog, profitnog ili neprofitnog
karaktera.
EconomicActivityValue
input
Svaka mjerljiva informacija o bilo kojem klasifikovanom ili registovanom materijalu koji
ulazi u tehničku i ekonomsku jedinicu u skladu sa svojom funkcijom.
InputOutputAmount output
Mjerljiva informacija o bilo kojem klasifikovanom ili registrovanom materijalu koji
napušta tehničku i ekonomsku jedinicu u skladu sa svojom funkcijom.
InputOutputAmount
time
Vremensko trajanje na koje se odnosi navedeni kapacitet poput 1 godine za godišnji
kapacitet.
TM_Duration
description Opis kapaciteta.
PT_FreeText
voidable
8.1.2.3. Količina ulaza ili izlaza (InputOutputAmount) Tip, a gdje je dostupno, mjerljiva količina klasifikovanog ili registrovanog materijala koji ulazi u ili napušta tehničku i ekonomsku jedinicu.
Atributi tipa podataka InputOutputAmount
Atribut
Definicija
Tip
Voidability
inputOutput Klasifikovani ili registrovani materijal koji ulazi ili napušta tehničku i ekonomsku jedinicu u
skladu sa svojom funkcijom.
InputOutputValue
amount
Količina (poput zapremine ili mase) klasifikovanog ili registrovanog materijala koji ulazi u ili
napušta tehničku i ekonomsku jedinicu.
Measure
voidable
8.1.2.4. Dozvola (Permission) Odluka nadležnog organa (dozvola) koja garantuje rad cijelog ili dijela Kompleksa aktivnosti podložna određenim uslovima garancije da su instalacije ili dijelovi instalacija na lokaciji kojima upravlja isti operater u skladu sa zahtjevima koje je odredilo kompetentan nadležni organ. Dozvola može obuhvatati jednu ili više funkcija i određivati parametre kapaciteta. Taj uslov može se, zavisno od opsega, proširiti na drugu tip sertifikata ili dokumenata posebne važnosti (npr. ISO, EMAS, Međunarodni standardi kvaliteta itd.).
Atributi tipa podataka Permission
Atribut
Definicija
Tip
Voidability
id
Identifikujuća referenca za dozvolu.
ThematicIdentifier relatedParty
Strane povezane s dozvolom kojom se garantuje kompleksu aktivnosti koje su
otvorene za brojne različite uloge poput, između ostalih, kompetentnog nadležnog
organa ili kompanije.
RelatedParty
voidable
decisionDate
Privremena referenca koja upotpunjuje definiciju dozvole.
DateTime
voidable
dateFrom
Početni datum od kojeg se dozvola počinje primjenjivati i od kojeg je ona važeća.
DateTime
voidable
dateTo
Datum do kojeg se dozvola primjenjuje i do kojeg je ona važeća.
DateTime
voidable
description
Opis dozvole.
PT_FreeText
voidable
permittedFunction Funkcija ili funkcije kojima je dozvola zagarantovana.
Function
voidable
permittedCapacity Maksimalne količine ulaza i/ili izlaza aktivnosti u skladu s dozvolom.
Capacity
voidable
8.1.2.5. Opis kompleksa aktivnosti (ActivityComplexDescription) Dodatne informacije o kompleksu aktivnosti, uključujući njegov opis, adresu, pojedinosti o kontaktu i povezane strane.
Atributi prostornog objekta tipa ActivityComplexDescription
Uloga
pridruživanja
Definicija
Tip
Voidability
description
Dopunska definicija "Kompleksa aktivnosti" i njegovih karakteristika.
PT_FreeText
voidable
address
Adresa kompleksa aktivnosti, tj, adresa na kojoj se aktivnost odvija.
AddressRepresentation voidable
contact
Podaci o kontaktu za za kompleks aktivnosti.
Contact
voidable
relatedParty
Informacije o stranama povezanim s kompleksom aktivnosti. Otvorene su brojnim
različitim ulogama poput vlasnika, rukovodioca ili nadležnih organa.
RelatedParty
voidable
8.1.3. Popisi kodova
8.1.3.1. Ekonomska aktivnost (EconomicActivityValue) Klasifikacija ekonomskih aktivnosti.
Dopuštene vrijednosti za ovaj popis kodova sastoje se od vrijednosti sljedećih popisa kodova ili drugih popisa kodova koje su odredili provajderi servisa:
-
Klasifikacija ekonomske aktivnosti u skladu s vrijednostima Eurostat NACE (EconomicActivityNACEValue).
-
Klasifikacija statističkih podataka o otpadu iz ekonomske aktivnosti (EconomicActivityWasteStatisticsValue).
-
Klasifikacija obnove odloženog otpada (WasteRecoveryDisposalValue).
8.1.3.2. Ulaz ili izlaz (InputOutputValue) Klasifikacija ulaza ili izlaza.
Dopuštene vrijednosti za ovaj popis kodova sastoje se od vrijednosti sljedećih popisa kodova ili drugih popisa kodova koje su odredili provajderi usluga.
- Klasifikacija proizvoda prema ekonomskoj aktivnosti (ProductCPAValue).
- Klasifikacija otpada (WasteValue).
8.2. Zahtjevi za komplekse aktivnosti Ako provajder podataka koristi podtip ActivityComplex kako bi informacije o statusu, fizičkom kapacitetu i/ili dodatne informacije učinio dostupnima, moraju se koristiti relevantni Popisi kodova i tipovi podataka (ConditionOfFacilityValue, Capacity, Permission, ActivityComplexDescription) uključeni u paket Kompleks aktivnosti."
PRILOG 2
ZAHTJEVI ZA OBLASTI PROSTORNIH PODATAKA
1. KOORDINATNI REFERENTNI SISOBLASTI
1.1. Definicije
- "podatak" je parametar ili niz parametara koji u skladu s normom MEST ISO 19111 određuju položaj porijekla, mjerilo i orijentaciju
koordinatnog sistema, - "geodetski podatak" je podatak koji u skladu s normom MEST ISO 19111 opisuje odnos koordinatnog sistema i Zemlje, - "koordinatni sistem" je niz matematičkih pravila koji u skladu s normom MEST ISO 19111 određuju kako se koordinate pripisuju tačkama, - "koordinatni referentni sistem" je koordinatni sistem koji je u skladu s normom MEST ISO 19111 sa stvarnim svijetom povezan preko
podatka (datuma). Ta definicija uključuje koordinatne sisteme utemeljene na geodetskim ili kartezijanskim koordinatama i koordinatne
sisteme utemeljene na kartografskim projekcijama.
- "kartografska projekcija" je mijenjanje koordinata u skladu s normom MEST ISO 19111, na osnovu odnosa jedan prema jedan, iz
geodetskog koordinatnog sistema u ravni na osnovu istog podatka (datuma), - "složeni koordinatni referentni sistem" je koordinatni referentni sistem koji za opis položaja u skladu s normom MEST ISO 19111
upotrebljava dva različita nezavisna koordinatna referentna sistema, jedan za horizontalnu i jedan za vertikalnu komponentu, - "geodetski koordinatni sistem" je koordinatni sistem u kojem se položaj u skladu s normom MEST ISO 19111 određuje geodetskom
širinom, geodetskom dužinom i (u slučaju trodimenzionalnog koordinatnog sistema) elipsoidnom visinom,
-
- "srednji nivo mora" (mean sea level) -MSL odnosi se na prosječnu visinu površine mora na plimnoj stanici za sve faze plime tokom
19-godišnjeg perioda koja se često određuje iz očitavanja mjerenja svakog sata od fiksnog i unaprijed definisanog referentnog nivoa
(osnovna linija dijagrama).
- "najniža astronomska plima" (lowest astronomical tide) -LAT odnosi se na najniži nivo plime čije se pojavljivanje može predvidjeti u
prosječnim meteorološkim uslovima i u bilo kojoj kombinaciji astronomskih uslova.
1.2. Datum za trodimenzionalne i dvodimenzionalne koordinatne referentne sisteme Za trodimenzionalne i dvodimenzionalne koordinatne referentne sisteme i horizontalnu komponentu složenog koordinatnog referentnog sistema koji se upotrebljavaju da se skupovi prostornih podataka učine dostupnim, na području njihove geografske pokrivenosti upotrebljava se datum evropskog terestrijalnog referentnog sistema 1989 (ETRS89), na području izvan geografske pokrivenosti ETRS89 upotrebljava se datum međunarodnog terestrijalnog referentnog sistema (ITRS) ili nekog drugog geodetskog koordinatnog referentnog sistema koji je usklađen s ITRS-om. Usklađenost s ITRS-om znači da je sistem definicija utemeljen na definiciji ITRS-a i da je u skladu s normom MEST ISO 19111 odnos između oba sistema dobro dokumentovan.
1.3. Koordinatni referentni sisoblasti Skupovi prostornih podataka dostupni su najmanje u jednom koordinatnom referentnom sistemu koji je naveden u dijelovima 1.3.1., 1.3.2. i 1.3.3., osim ako važi jedan od uslova naveden u dijelu 1.3.4. ovog Priloga.
1.3.1. Trodimenzionalni koordinatni referentni sisoblasti - Trodimenzionalne kartezijanske koordinate utemeljene na podatku (datumu) iz dijela 1.2. ovog Priloga i koje upotrebljavaju parametre
elipsoida geodetskog referentnog sistema 1980 (GRS80).
- Trodimenzionalne geodetske koordinate (širina, dužina i elipsoidna visina) utemeljene na podatku (datumu) iz dijela 1.2. ovog Priloga i
koje upotrebljavaju parametre elipsoida GRS80.
1.3.2. Dvodimenzionalni koordinatni referentni sisoblasti
- Dvodimenzionalne geodetske koordinate (širina i dužina) utemeljene na podatku (datumu) iz dijela 1.2. ovog Priloga i koje upotrebljavaju
parametre elipsoida GRS80.
- Površinske koordinate koje upotrebljavaju koordinatni referentni sistem ETRS89 u Lambertovoj azimutnoj ekvivalentnoj projekciji
(Lambert Azimuthal Equal Area).
- Površinske koordinate koje upotrebljavaju koordinatni referentni sistem ETRS89 u Lambertovoj konformnoj konusnoj projekciji (Lambert
Conformal Conic).
- Površinske koordinate koje upotrebljavaju koordinatni referentni sistem ETRS89 u transverzalnoj Mercatorovoj projekciji (Transverse
Mercator).
1.3.3. Složeni koordinatni referentni sisoblasti
1. Za horizontalnu komponentu složenog koordinatnog referentnog sistema, upotrebljava se jedan od koordinatnih referentnih sistema iz
dijela 1.3.2. ovog Priloga.
2. Za vertikalnu komponentu upotrebljava se jedan od sljedećih koordinatnih referentnih sistema:
- Za vertikalnu komponentu u slobodnoj atmosferi mora se koristiti barometarski pritisak pretvoren u visinu u skladu s MEST ISO
2533:1975 standardna atmosfere ili drugih linearnih ili parametarskih referentnih sistema. Ako se koriste drugi parametarski
referentni sisoblasti, oni moraju biti opisani u dostupnoj referenci u skladu s MEST ISO 19111-2:2012.
- Za vertikalnu komponentu u slobodnoj atmosferi upotrebljava se barometarski pritisak, pretvoren u visinu pomoću standardne
atmosfere u skladu s MEST ISO 2533:1975.
- Za vertikalnu komponentu u morskim područjima u kojima postoji mjerljiv raspon plime (plimni tokovi) kao referentna površina
mora se koristiti najniža astronomska plima (LAT).
- Za vertikalnu komponentu u morskim područjima bez mjerljivog raspona plime, u otvorenim okeanima i u vodama čija je dubina veća od 200 metara, kao referentna površina mora se koristiti srednji nivo mora (MSL) ili dobro definisani
referentni nivo blizu MSL-a
1.3.4. Drugi koordinatni referentni sisoblasti U sljedećim slučajevima mogu se upotrebljavati drugi koordinatni referentni sisoblasti uz one iz dijela 1.3.1., 1.3.2. ili 1.3.3. ovog Priloga. 1. Za pojedine oblasti prostornih podataka u ovome Prilogu mogu se odrediti drugi koordinatni referentni sisoblasti.
2. Za regije izvan kontinentalne Evrope, države mogu odrediti odgovarajuće koordinatne referentne sistema.
Geodetske oznake i parametri, nužni za opis tih koordinatnih referentnih sistema kao i omogućavanje postupaka pretvaranja i preoblikovanja, dokumentuju se u skladu s MEST ISO 19111 i MEST ISO 19127 i stvara se identifikator.
1.4. Koordinatni referentni sisoblasti koji se upotrebljavaju za mrežni servis pregleda Za prikazivanje skupa prostornih podataka preko mrežnog servisa pregleda, moraju biti dostupni najmanje koordinatni referentni sisoblasti za dvodimenzionalne geodetske koordinate (širinu, dužinu).
1.5. Identifikatori koordinatnog referentnog sistema
1. Parametri koordinatnog referentnog sistema i identifikatori vode se u jednom ili u više zajedničkih registara za koordinatne referentne
sisteme.
2. Za upućivanje na koordinatne referentne sisteme upotrebljavaju se samo identifikatori iz zajedničkog registra.
2. GEOGRAFSKI SISOBLASTI MREŽA 2.1. Definicije - "mreža" znači mreža sastavljena od dva ili više niza krivulja u kojima se članovi svakog niza algoritamski presijecaju s članovima drugih
nizova, - "mrežno polje" znači polje koje razgraničavaju mrežne krive, - "mrežna tačka" znači tačka koja je na presjeku dvije ili više krivih na mreži.
2.2. Mreže Bilo koja mreža s fiksnim i jasno definisanim lokacijama definisana u djelovima 2.2.1. i 2.2.2. ovog Priloga mora se koristiti kao radni okvir za geo-referenciranje kako bi podaci iz mreže bili dostupni, osim u slučaju postojanja jednog od sljedećih uslova:
(1) Za specifične oblasti prostornih podataka u Prilogu 2. mogu biti određene druge mreže. U tom slučaju razmijenjeni podaci koji koriste
takvu tematski specifičnu mrežu moraju koristiti standarde u kojima je definicija mreže uključena u podatke ili je referencom povezana. (2) Za referenciranje na mrežu područja van kontinentalnih evropskih država mogu definisati sopstvenu mrežu na osnovu geodetskog
koordinatnog referentnog sistema usklađenog s ITRS-om i Lambertovom azimutalnom ekvivalentnom projekcijom prema istim
načelima određenim u dijelu 2.1.1. ovog Priloga. U tom slučaju mora se stvoriti referentni koordinatni sistem.
2.2.1. Mreža jednake površine Mreža jednake površine je utemeljena na koordinatnom referentnom sistemu ETRS89 u Lambertovoj azimutnoj ekvivalentnoj projekciji (ETRS89-LAEA) sa središtem projekcije u tački 52° N, 10° E te prividnim pomakom prema istoku: x0 = 4 321 000 m, i prividnim pomakom prema sjeveru: y0 = 3 210 000 m.
Izvor mreže podudara se s redukovanim izvorom koordinatnog referentnog sistema ETRS89-LAEA (x = 0, y = 0).
Mrežne tačke mreža koje se baziraju na ETRS89-LAEA podudaraju se s mrežnim tačkama mreže.
Mreža je hijerarhijska s rezolucijama 1 m, 10 m, 100 m, 1 000 m, 10 000 m i 100 000 m.
Usmjerenost mreže je jug-sjever i zapad-istok.
Mreža je označena kao Grid_ETRS89-LAEA. Za označavanje pojedinih rezolucija dodaje se veličina ćelije izražena u metrima.
Za nedvosmisleno referenciranje i označavanje mrežne ćelije upotrebljava se oznaka ćelije koja je sastavljena od veličine ćelije i koordinata donjeg lijevog ugla ćelije u ETRS89-LAEA. Veličina ćelije izražava se u metrima ("m") za veličinu ćelije do 100 m ili u kilometrima ("km") za ćelije do 1 000 m ili veće. Vrijednosti za pomjeranje prema sjeveru ili istoku dijeli se sa 10n, gdje je n broj sljedećih nula u vrijednosti veličine polja.
2.2.2. Geografska mreža podijeljena na zone 1.
Ako se podaci mreže isporučuju pomoću geodetskih koordinata određenih u dijelu 1.3. ovog Priloga, kao radni okvir za geo-
referenciranje može se koristiti mreža višestruke rezolucije definisana u ovom dijelu.
2.
Nivoi rezolucije definisani su u Tabeli 1.
3. Mreža se mora temeljiti na geodetskom referentnom koordinatnom sistemu ETRS89-GRS80.
4. Polazna tačka mreže mora se poklapati s tačkom presijeka Ekvatora i meridijana Greenwich (GRS80 geografska širina φ=0; GRS80
geografska dužina λ=0).
5. Orijentacija mreže mora biti jug-sjever i zapad-istok u skladu s mrežom definisanom meridijanima i paralelama elipsoida GRS80. 6. Za referenciranje na mrežu područja izvan kontinentalne Evrope provajderi podataka mogu definisati vlastitu mrežu na temelju
geodetskog koordinatnog referentnog sistema usklađenog s ITRS-om prema istim načelima određenim za Paneuropski Grid_ETRS89-
GRS80zn. U tom slučaju mora se stvoriti identifikator za referentni koordinatni sistem i odgovarajući identifikator mreže.
7. Mreža mora biti podijeljena na zone. Rezolucija mreže u smjeru jug-sjever mora imati isti ugao razmaka. Rezolucija mreže u smjeru
zapad-istok mora se odrediti kao proizvod ugaonog rastojanja i faktora zone kako je definisano u Tabeli 1.
8 . Mreža se mora označiti kao Grid_ETRS89-GRS80zn_res, gdje n predstavlja broj zona, a res veličinu ćelije u ugaonim jedinicama kako je
određeno u Tabeli 1.
Tabela 1.
Zajednička mreža Grid_ETRS89-GRS80: Razmak Geografske širine (nivo rezolucije) i dužine za svaku zonu
Nivoi
rezolucije
RAZMAK
GEOGRAFSKE
ŠIRINE
(Sekunde kružnog
luka)
RAZMAK GEOGRAFSKE DUŽINE (Sekunde kružnog luka)
Veličina
ćelije
Zona 1
(Geografska
širina 0°-50°)
Zona 2
(Geografska
širina 50°-70°)
Zona 3
(Geografska
širina 70°-75°)
Zona 4
(Geografska
širina 75°-80°)
Zona 5
(Geografska
širina 80°-90°)
NIVO 0
3 600
3 600
7 200
10 800
14 400
21 600
1 D
NIVO 1
3 000
3 000
6 000
9 000
12 000
18 000
50 M
NIVO 2
1 800
1 800
3 600
5 400
7 200
10 800
30 M
NIVO 3
1 200
1 200
2 400
3 600
4 800
7 200
20 M
NIVO 4
600
600
1 200
1 800
2 400
3 600
10 M
NIVO 5
300
300
600
900
1 200
1 800
5 M
NIVO 6
120
120
240
360
480
720
2 M
NIVO 7
60
60
120
180
240
360
1 M
NIVO 8
30
30
60
90
120
180
30 S
NIVO 9
15
15
30
45
60
90
15 S
NIVO 10
5
5
10
15
20
30
5 S
NIVO 11
3
3
6
9
12
18
3 S
NIVO 12
1,5
1,5
3
4,5
6
9
1 500 MS
NIVO 13
1
1
2
3
4
6
1 000 MS
NIVO 14
0,75
0,75
1,5
2,25
3
4,5
750 MS
NIVO 15
0,5
0,5
1
1,5
2
3
500 MS
NIVO 16
0,3
0,3
0,6
0,9
1,2
1,8
300 MS
NIVO 17
0,15
0,15
0,3
0,45
0,6
0,9
150 MS
NIVO 18
0,1
0,1
0,2
0,3
0,4
0,6
100 MS
NIVO 19
0,075
0,075
0,15
0,225
0,3
0,45
75 MS
NIVO 20
0,03
0,03
0,06
0,09
0,12
0,18
30 MS
NIVO 21
0,015
0,015
0,03
0,045
0,06
0,09
15 MS
NIVO 22
0,01
0,01
0,02
0,03
0,04
0,06
10 MS
NIVO 23
0,0075
0,0075
0,015
0,0225
0,03
0,045 7 500 MMS
NIVO 24
0,003
0,003
0,006
0,009
0,012
0,018 3 000 MMS
FAKTOR
-
1
2
3
4
6 - "
3. GEOGRAFSKI NAZIVI
3.1. Tipa prostornog objekta Sljedeće tipa prostornih objekata upotrebljavaju se za razmjenu i klasifikaciju prostornih objekata iz skupa podataka koji se odnose na oblast prostornog podatka Geografska imena:
-
Imenovano mjesto.
3.1.1. Imenovano mjesto (NamedPlace) Bilo koji entitet iz stvarnog svijeta koji ima jedno ili više vlastitih imena.
Atributi tipa prostornog objekta NamedPlace
Atribut
Definicija
Tip podatka
Voidability
beginLifespanVersion
Datum i vrijeme kad je ova verzija prostornog objekta unijeta u
skup prostornih podataka ili u njemu izmijenjena.
DateTime
voidable
endLifespanVersion
Datum i vrijeme kad je ta verzija prostornog objekta u skupu
prostornih podataka izmijenjena ili iz njega izbrisana.
DateTime
voidable
geometry
Geometrija
imenovanog
mjesta.
Specifikacija
podatka
ne
ograničava tipa geometrije.
GM_Object
inspireId
Spoljni identifikator objekta prostornog objekta.
Identifier
leastDetailedViewingResolution Rezolucija izražena indeksom mjerila ili razdaljinom na zemljištu,
iznad koje se imenovano mjesto i njegovo srodno ime (imena) ne
treba više prikazivati u osnovnoj usluzi pregleda.
MD_Resolution
voidable
localType
Karakteristike entiteta imenovanog geografskim imenom (-ima),
kako ih definiše provajder (izvor) podataka, najmanje na jednom
službenom jeziku.
LocalisedCharacterString voidable
mostDetailedViewingResolution Rezolucija izražena indeksom mjerila ili razdaljinom na zemljištu,
ispod koje se imenovano mjesto i njegovo srodno ime (imena) ne
treba više prikazivati u osnovnoj usluzi pregleda.
MD_Resolution
voidable
name
Imenovano mjesto.
GeographicalName
relatedSpatialObject
Identifikator prostornog objekta koji prikazuje isti entitet, ali se može pojaviti i u drugim oblastima prostornih podataka, ako
Identifier
voidable
postoje.
type
Karakterizacija entiteta označenoga geografskim imenom (-ima).
NamedPlaceTypeValue
voidable
3.2. Tipa podataka
3.2.1. Geografsko ime (GeographicalName) Vlastita imenica koja se upotrebljava za entitet u stvarnom svijetu.
Atributi tipa podataka GeographicalName
Atribut
Definicija
Tip podatka
Voidability
grammaticalGender Tip imenice u skladu s gramatičkim rodom.
GrammaticalGenderValue voidable
grammaticalNumber Gramatička kategorija imenica koje izražavaju razliku u broju.
GrammaticalNumberValue voidable
language
Jezik koji je u skladu s normom MEST ISO 639-3 ili MEST ISO 639-5 izražen
troslovnom oznakom.
CharacterString
voidable
nameStatus
Kvalitativne informacije koje omogućava razlikovanje vrijednosti imena
obzirom na stepen njegove standardizacije i/ili važnosti.
NameStatusValue
voidable
nativeness
Informacija koja omogućava da se utvrdi je li ime ono koje se upotrebljava/ili
se upotrebljavalo na području na kojem je prostorni objekt lociran u
trenutku kad se ime upotrebljava ili se upotrebljavalo.
NativenessValue
voidable
pronunciation
Odgovarajući, ispravan ili standardan (standardan u predmetnoj jezičkoj
zajednici) izgovor geografskog imena.
PronunciationOfName
voidable
sourceOfName
Prvobitni izvor podataka iz kojeg je uzeto geografsko ime i dodato u zbirku
podataka u kojoj se vodi/objavljuje. Za neke imenovane prostorne objekte
može se ponovno uputiti na skup podataka, ako druge informacije nisu
dostupne.
CharacterString
voidable
spelling
Ispravan način pisanja (ortografija) geografskog imena.
SpellingOfName
3.2.2. Izgovor imena (PronunciationOfName) Odgovarajući, ispravan ili standardan (standardan u predmetnoj jezičkoj zajednici) izgovor imena.
Atributi tipa podataka PronunciationOfName
Atribut
Definicija
Tip podatka
Voidability
pronunciationIPA
Odgovarajući, ispravan ili standardan (standardan u predmetnoj jezičkoj zajednici)
izgovor imena, izražen u međunarodnoj fonetskoj abecedi (IPA).
CharacterString voidable
pronunciationSoundLink Odgovarajući, ispravan ili standardan (standardan u predmetnoj jezičnoj zajednici)
izgovor imena, izražen vezom sa zvučnom datotekom.
URI
voidable
Ograničenja tipa podatka PronunciationOfName Najmanje jedan od dva atributa pronunciationSoundLink i pronunciationIPA ne smije biti void (prazan).
3.2.3. Pravopis imena (SpellingOfName) Ispravan način pisanja imena.
Atributi tipa podatka SpellingOfName
Atribut
Definicija
Tip podatka
Voidability
script
Niz grafičkih znakova (npr. abeceda) koji se koristi u pisanju imena, prema potrebi
izražen četveroslovnom oznakom u skladu s normom MEST ISO 15924.
CharacterString voidable
text
Način pisanja imena.
CharacterString transliterationScheme Način za prevođenje imena iz jednog pisma u drugo (transliteracija).
CharacterString voidable
3.3. Popisi kodova
3.3.1. Gramatički rod (GrammaticalGenderValue) Gramatički rod geografskog imena.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova GrammaticalGenderValue
Vrijednost
Definicija
common
"Zajednički" gramatički rod (spajanje "muškog" i "ženskog").
feminine
Gramatički rod - ženski.
masculine
Gramatički rod - muški.
neuter
Gramatički rod - srednji.
3.3.2. Gramatički broj (GrammaticalNumberValue) Gramatički broj geografskog imena.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova GrammaticalNumberValue
Vrijednost
Definicija
dual
Gramatički broj - dual
plural
Gramatički broj - množina.
singular
Gramatički broj - jednina.
3.3.3. Status imena (NameStatusValue) Status geografskog imena je informacija koja omogućava razlikovanje vrijednosti imena obzirom na stepen njegovog normiranja i/ili važnosti.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova NameStatusValue
Vrijednost
Definicija
historical
Istorijsko ime koje se trenutno ne koristi.
official
Ime koje se trenutno koristi i službeno je odobreno ili je utvrđeno zakonom.
other
Ime koje se trenutno koristi, ali nije službeno ni odobreno.
standardised Ime koje se trenutno koristi i koje je prihvatio ili ga preporučio organ kojem je dodijeljena savjetodavna funkcija i/ili o vlasti
za odlučivanje o pitanjima vezanima za toponimiju.
3.3.4. Tip imenovanog mjesta (NamedPlaceTypeValue) Tip imenovanog mjesta.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova NamedPlaceTypeValue
Vrijednost
Definicija
administrativeUnit Administrativne jedinice za lokalnu, regionalnu i nacionalnu upravu koje dijele područja gdje države imaju i/ili
ostvaruju nadležnost, i koje su odvojene administrativnim granicama.
building
Geografski položaj građevine.
hydrography
Hidrografski elementi, uključujući morska područja i sva druga vodna tijela i s njima povezane djelove, uključujući
riječne slivove i ušća.
landcover
Fizička i biološka prekrivenost zemljine površine, uključujući vještačke površine, poljoprivredne površine, šume, (polu)
prirodna područja, močvarna područja.
landform
Geomorfološki značaj terena.
other
Prostorni objekat koji nije uključen u druge tipa popisa kodova.
populatedPlace
Naseljeno mjesto.
protectedSite
Područje koje je u okviru međunarodnog zakonodavstva ili zakonodavstva države određeno ili se upravlja u svrhu
postizanja posebnih ciljeva očuvanja.
transportNetwork Drumska, željeznička, vazdušna, vodena saobraćajna mreža, saobraćajna mreža žičara te pripadajuća infrastruktura.
Uključuje veze između različitih mreža.
3.3.5. Izvor (NativenessValue) Izvor geografskog imena.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
3.4. Slojevi
Sloj za temu prostornih podataka Geografska imena
Ime sloja
Naslov sloja
Tip prostornog objekta
GN.GeographicalNames
Geografska imena
NamedPlace
4. ADMINISTRATIVNE JEDINICE
4.1. Struktura administrativnih jedinica oblasti prostornih podataka Tipovi određeni za administrativne jedinice oblasti prostornih podataka strukturisani su u sljedećim paketima:
-
Administrativne jedinice (Administrative Units); i -
Pomorske jedinice (Maritime Units)
4.2. Administrativne jedinice
4.2.1. Tipovi prostornih objekata Paket Administrativne jedinice sadrži sljedeće tipove prostornih objekata:
-
Administrativna granica;
-
Administrativna jedinica; i
-
Kondominijum.
4.2.1.1. Administrativna granica (AdministrativeBoundary) Linija razgraničenja između dvije administrativne jedinice.
Atributi prostornog objekta tipa AdministrativeBoundary
Atribut
Definicija
Tip
Voidability
beginLifespanVersion Datum i vrijeme postavljanja ili promjene ove verzije prostornog
objekta u skupu prostornih podataka.
DateTime
voidable
country
Kod države s dva znaka u skladu s Međuinstitucionalnim vodičem za
stilove.
CountryCode
endLifespanVersion
Datum i vrijeme zamjene ili povlačenja ove verzije prostornog objekta iz
skupa prostornih podataka.
DateTime
voidable
geometry
Geometrija koja predstavlja liniju granice.
GM_Curve
inspireId
Identifikator spoljnog prostornog objekta.
Identifier
legalStatus
Pravni status te administrativne granice.
LegalStatusValue
voidable
nationalLevel
Hijerarhijski nivo svih susjednih administrativnih jedinica čiji je dio ova
granica.
AdministrativeHierarchyLevel
technicalStatus
Tehnički status administrativne granice.
TechnicalStatusValue
voidable
Uloga pridruživanja prostornog objekta tipa AdministrativeBoundary
Uloga pridruživanja
Definicija
Tip
Voidability admUnit
Administrativne jedinice odvojene ovom administrativnom granicom.
AdministrativeUnit
voidable
4.2.1.2. Administrativna jedinica (AdministrativeUnit) Administrativna jedinica u kojoj je država sprovodila i/ili sprovodi prava nadležnosti za lokalno, regionalno i nacionalno upravljanje.
Atributi prostornog objekta tipa AdministrativeUnit
Atribut
Definicija
Tip
Voidability
beginLifespanVersion Datum i vrijeme postavljanja ili promjene ove verzije prostornog
objekta u skupu prostornih podataka.
DateTime
voidable
country
Kod države s dva znaka u skladu Međuinstitucionalnim vodičem za
stilove.
CountryCode
endLifespanVersion
Datum i vrijeme zamjene ili povlačenja ove verzije prostornog objekta iz
skupa prostornih podataka.
DateTime
voidable
geometry
Geometrijski
prikaz
prostornog
područja
pokrivenog
tom
administrativnom jedinicom.
GM_MultiSurface
inspireId
Identifikator spoljnog prostornog objekta.
Identifier
name
Službeni nacionalni geografski naziv administrativne jedinice koji je
prema potrebi naveden na nekoliko jezika.
GeographicalName
nationalCode
Tematski identifikator koji odgovara nacionalnim administrativnim
kodovima definisanim u svakoj državi.
CharacterString
nationalLevel
Nivo u hijerarhiji administracije na kojoj je administrativna jedinica
zasnovana.
AdministrativeHierarchyLevel
nationalLevelName
Naziv nivoa u hijerarhiji administracije na kojoj je administrativna
jedinica utemeljena.
LocalisedCharacterString
voidable
residenceOfAuthority Sjedište nacionalne ili lokalne administracije.
ResidenceOfAuthority
voidable
Uloge pridruživanja prostornog objekta tipa AdministrativeUnit
Uloga
pridruživanja
Definicija
Tip
Voidability
administeredBy
Administrativna jedinica zasnovana na istom nivou administrativne hijerarhije
koja upravlja tom administrativnom jedinicom.
AdministrativeUnit
voidable
boundary
Administrativne granice između te administrativne jedinice i svih ostalih
susjednih jedinica.
AdministrativeBoundary voidable
coAdminister
Administrativna jedinica zasnovana na istom nivou administrativne hijerarhije
kojom su-upravlja ta administrativna jedinica.
AdministrativeUnit
voidable
condominium
Kondominijum kojim upravlja ta administrativna jedinica.
Condominium
voidable
lowerLevelUnit
Jedinice utemeljene na nižem nivou administrativne hijerarhije kojima upravlja
ta administrativna jedinica.
AdministrativeUnit
voidable
upperLevelUnit
Administrativna jedinica utemeljena na višem nivou administrativne hijerarhije
kojom upravlja ta administrativna jedinica
AdministrativeUnit
voidable
Ograničenja prostornog objekta tipa AdministrativeUnit Uloga pridruživanja kondominijuma primjenjuje se samo na administrativne jedinice čiji nationalLevel = "1. red" (na nivou države).
Nijedna jedinica na najnižem nivou ne smije pridruživati jedinice na nižem nivou.
Nijedna jedinica na najvišem nivou ne smije pridruživati jedinice na višem nivou 4.2.1.3. Kondominijum (Condominium) Administrativno područje zasnovano nezavisno od bilo koje administrativne podjele teritorije kojim upravljaju dvije ili više država.
Atributi prostornog objekta tipa Condominium
Atribut
Definicija
Tip
Voidability beginLifespanVersion Datum i vrijeme ubacivanja ili promjene ove verzije prostornog objekta u skupu
prostornih podataka.
DateTime
voidable
endLifespanVersion
Datum i vrijeme zamjene ili povlačenja ove verzije prostornog objekta iz skupa
prostornih podataka.
DateTime
voidable
geometry
Geometrijski prikaz prostornog područja pokrivenog kondominijem.
GM_MultiSurface
inspireId
Identifikator spoljnog prostornog objekta.
Identifier
name
Službeni geografski naziv tog kondominijuma koji je prema potrebi naveden na
nekoliko jezika.
GeographicalName voidable
Uloga pridruživanja prostornog objekta tip Condominium
Uloga pridruživanja
Definicija
Tip
Voidability
admUnit
Administrativna jedinica koja upravlja kondominijumom.
AdministrativeUnit
voidable
4.2.2. Tipovi podataka
4.2.2.1. Sjedište nadležnog organa (ResidenceOfAuthority) Tip podataka koji predstavlja naziv i položaj sjedišta nadležnog organa.
Atributi tipa podataka ResidenceOfAuthority
Atribut
Definicija
Tip
Voidability
geometry
Položaj sjedišta nadležnog organa.
GM_Point
voidable
name
Naziv sjedišta nadležnog organa.
GeographicalName
4.2.3. Nabrajanja 4.2.3.1. Pravni status (LegalStatusValue) Opis pravnog statusa administrativnih granica.
Dopuštene vrijednosti za nabrajanje LegalStatusValue
Vrijednost
Definicija
agreed
Granica koja se podudara s ivicom dogovorena između susjednih administrativnih jedinica i sada je stabilna.
notAgreed
Granica koja se podudara s ivicom ali još nije dogovorena između susjednih administrativnih jedinica i može se mijenjati.
4.2.3.2. Tehnički status (TechnicalStatusValue) Opis tehničkog statusa administrativnih granica.
Dopuštene vrijednosti za nabrajanje TechnicalStatusValue
Vrijednost
Definicija
edgeMatched
Granice susjednih administrativnih jedinica koje imaju isti skup koordinata.
notEdgeMatched
Granice susjednih administrativnih jedinica koje nemaju isti skup koordinata.
4.2.4. Popisi kodova
4.2.4.1. Nivo administrativne hijerarhije (AdministrativeHierarchyLevel) Nivo upravljanja u nacionalnoj administrativnoj hijerarhiji. Ovaj popis kodova odražava nivo u hijerarhijskoj piramidi administrativnih struktura koji se temelji na geometrijskoj agregaciji teritorija i obavezno ne opisuje podređenost između odnosnih administrativnih nadležnih organa.
Ovim popisom kodova potrebno je upravljati iz registra zajedničkog popisa kodova.
4.3. Pomorske jedinice
4.3.1. Tipovi prostornih objekata Paket Pomorske jedinice sadrži sljedeće tipove prostornih objekata:
-
Osnovna linija;
-
Pomorska granica; i -
Pomorska zona.
4.3.1.1. Osnovna linija (Baseline) Linija od koje se mjere spoljne granice teritorijalnog mora i određene unutrašnje granice.
Atributi prostornog objekta tipa Baseline
Atribut
Definicija
Tip
Voidability
inspireId
Identifikator spoljnog prostornog objekta.
Identifier beginLifespanVersion Datum i vrijeme postavljanja ili promjene verzije prostornog objekta u skupu prostornih
podataka.
DateTime voidable
endLifespanVersion
Datum i vrijeme zamjene ili povlačenja ove verzije prostornog objekta iz skupa prostornih
podataka.
DateTime voidable
Uloge pridruživanja prostornog objekta tipa Baseline
Uloga pridruživanja
Definicija
Tip
Voidability
segment
Segment osnovne linije.
BaselineSegment
4.3.1.2. Pomorska granica (MaritimeBoundary) Linija koja označava razdvajanje bilo kog tipa pomorske nadležnosti.
Atributi prostornog objekta tipa MaritimeBoundary
Atribut
Definicija
Tip
Voidability
inspireId
Identifikator spoljnjeg prostornog objekta.
Identifier
geometry
Geometrijski prikaz pomorske granice.
GM_Curve
country
Država kojoj pripada pomorska zona ove granice.
CountryCode
legalStatus
Pravni status pomorske granice.
LegalStatusValue
voidable
technicalStatus
Tehnički status pomorske granice.
TechnicalStatusValue voidable
beginLifespanVersion Datum i vrijeme postavljanja ili promjene ove verzije prostornog objekta u skupu
prostornih podataka.
DateTime
voidable
endLifespanVersion
Datum i vrijeme zamjene ili povlačenja ove verzije prostornog objekta iz skupa
prostornih podataka.
DateTime
voidable
4.3.1.3. Pomorska zona (MaritimeZone) Morski pojas definisan međunarodnim ugovorima i sporazumima.
Atributi prostornog objekta tipa MaritimeZone
Atribut
Definicija
Tip
Voidability
inspireId
Identifikator spoljnjeg prostornog objekta.
Identifier
geometry
Geometrijski prikaz prostornog područja pokrivenog tom pomorskom zonom. GM_MultiSurface
zoneType
Tip pomorske zone.
MaritimeZoneTypeValue country
Država kojoj pripada ova pomorska zona.
CountryCode
name
Nazivi pomorske zone.
GeographicalName
voidable
beginLifeSpanVersion Datum i vrijeme postavljanja ili promjene ove verzije prostornog objekta u
skupu prostornih podataka.
DateTime
voidable
endLifepanVersion
Datum i vrijeme zamjene ili povlačenja ove verzije prostornog objekta iz
skupa prostornih podataka.
DateTime
voidable
Uloga pridruživanja prostornog objekta tipa MaritimeZone
Uloga pridruživanja
Definicija
Tip
Voidability
baseline
Osnovna linija ili linije upotrijebljene za opisivanje pomorske zone.
Baseline
voidable
boundary
Granica ili granice pomorske zone.
MaritimeBoundary
voidable
4.3.2. Tipovi podataka
4.3.2.1. Segment osnovne linije (BaselineSegment) Segment linije od kojeg se mjere spoljne granice teritorijalnog mora i određene unutrašnje granice.
Atributi tipa podataka BaselineSegment
Atribut
Definicija
Tip
Voidability
geometry
Geometrijski prikaz segmenta osnovne linije.
GM_Curve
segmentType
Tip osnovne linije upotrijebljen za ovaj segment.
BaselineSegmentTypeValue
4.3.3. Popisi kodova
4.3.3.1. Tip segmenta osnovne linije (BaselineSegmentTypeValue) Tipovi osnovnih linija upotrijebljenih za mjerenje širine teritorijalnog mora.
Dopuštene vrijednosti za ovaj popis kodova sastoje se samo od vrijednosti određenih u tabeli u nastavku.
Vrijednosti za popis kodova BaselineSegmentTypeValue
Vrijednost
Naziv
Definicija
normal
normalna
Normalna osnovna linija za mjerenje širine teritorijalnog mora je linija najnižeg nivoa vode na obali kako je
označeno na kartama velikog razmjera koje je službeno prihvatila obalna država.
straight
ravna
Osnovna linija za mjerenje širine teritorijalnog mora ravna je osnovna linija određena povezivanjem
odgovarajućih tačaka.
archipelagic arhipelaška Osnovna linija za mjerenje širine teritorijalnog mora ravna je osnovna linija koja povezuje krajnje spoljašnje tačke
krajnih spoljašnjih ostrva i grebena izloženih osjekama u arhipelagu.
4.3.3.2. Tip pomorske zone (MaritimeZoneTypeValue) Tip pomorske zone.
Dopuštene vrijednosti za popis kodova sastoje se samo od vrijednosti određenih u tabeli u nastavku.
Vrijednosti za popis kodova MaritimeZoneTypeValue
Vrijednost
Naziv
Definicija
internalWaters
Unutrašnje vode
Vode na kopnenoj strani osnovnih linija teritorijalnog mora obalne države.
territorialSea
Teritorijalno more Morski pojas definisan širinoma ne većom od 12 nautičkih milja izmjerenom od osnovnih linija
koje su određene u skladu s Konvencijom Ujedinjenih nacija o pravu mora.
contiguousZone
Pogranična zona
Zona koja se graniči s teritorijalnim morem obalne države koja se ne smije širiti više od 24
nautičke milje od osnovne linije od koje se mjeri širina teritorijalnog mora.
exclusiveEconomicZone Ekskluzivna
ekonomska zona
Površina koja je van i uz teritorijalno more obalne države podložna je posebnom zakonskom
režimu u kojem pravima i pravnom nadležnošću obalne države kao i pravima i slobodama
ostalih država upravljaju relevantne odredbe Konvencije Ujedinjenih nacija o pravu mora.
continentalShelf
Kontinentalni
sprud
Pomorska zona koja je van i uz teritorijalno more obalne države čija je spoljna granica
određena u skladu s članom 76. Konvencije Ujedinjenih nacija o pravu mora.
4.4. Specifični tematski zahtjevi
1.
Svaka pojava prostornog objekta tipa AdministrativeUnit, osim jedinice na nivou države i jedinice kojima se upravlja moraju upućivati
tačno na jednu jedinicu na višem nivo u administrativnoj hijerarhiji. Ovaj sporazum mora se izraziti ulogom pridruživanja
upperLevelUnit prostornog objekta tipa AdministrativeUnit.
2.
Svaka pojava prostornog objekta tipa AdministrativeUnit, osim onih na najnižem nivou, mora upućivati na svoje odnosne jedinice nižeg
nivoa. Ovaj sporazum mora se izraziti ulogom pridruživanja lowerLevelUnit prostornog objekta tipa AdministrativeUnit.
3.
Ako nekom administrativnom jedinicom upravljaju dvije ili više administrativnih jedinica, mora se upotrijebiti uloga pridruživanja
administeredBy. Jedinice koje zajednički upravljaju moraju primjenjivati inverznu ulogu coAdminister.
4.
Administrativne jedinice na istom nivou administrativne hijerarhije konceptualno ne smiju dijeliti zajednička područja.
5.
Pojavljivanja prostornog objekta tipa AdministrativeBoundary moraju odgovarati ivicama topološke strukture cijelog dijagrama
granice (uključujući sve nivoe).
6.
Prostorna granica kondominijuma ne smije biti dio geometrije koja predstavlja prostornu granicu administrativne jedinice.
7.
Kondominijuma smiju upravljati samo administrativne jedinice na nivou države.
4.5. Slojevi
Slojevi oblasti prostornih podataka administrativnih jedinica
Naziv sloja
Naslov sloja
Tip prostornog objekta
AU.AdministrativeUnit
Administrativna jedinica
AdministrativeUnit
AU.AdministrativeBoundary
Administrativna granica
AdministrativeBoundary
AU.Condominium
Kondominijum
Condominium
AU.Baseline
Osnovna linija
Baseline
AU.<CodeListValue> (1) Primjer: AU.ContiguousZone
<naziv koji može pročitati čovjek>
Primjer: Pogranična zona
MaritimeZone (zoneType: MaritimeZoneTypeValue)
AU.MaritimeBoundary
Pomorska granica
MaritimeBoundary
5. ADRESE LOKACIJA NEPOKRETNOSTI 5.1. Definicije
- "adresabilan predmet" znači prostorni predmet kojem ima smisla dodijeliti adresu.
5.2. Tipa prostornog objekta Sljedeće tipa prostornog objekta upotrebljavaju se za razmjenu i klasifikaciju prostornih objekata iz skupa podataka koji se odnose na temu Adrese:
-
adresa;
-
ime naslovljenog područja, -
sastavni dio adrese;
-
Naziv administrativne jedinice;
-
poštanski deskriptor; i -
naziv glavne saobraćajnice.
5.2.1. Adresa (Address) Oznaka nepromjenjive lokacije nekretnine pomoću strukturisanog sastava geografskih imena i identifikatora.
Atributi tipa prostornog objekta Address
Atribut
Definicija
Tip podatka
Voidability
alternativeIdentifier
Spoljni tematski identifikator prostornog objekta Address, koji omogućava
međuoperativnost s postojećim sisoblastima nasleđivanja ili aplikacijama.
CharacterString
voidable
beginLifespanVersion Datum i vrijeme kad je ova verzija prostornog objekta unešena u skup prostornih
podataka ili u njemu izmijenjena.
DateTime
voidable
endLifespanVersion
Datum i vrijeme kad je ova verzija prostornog objekta u skupu prostornih podataka
izmijenjena ili iz njega izbrisana.
DateTime
voidable
inspireId
Spoljni identifikator objekta prostornog objekta.
Identifier
locator
Jasno čitljivi dezignator ili naziv.
AddressLocator
position
Položaj karakteristične tačke koja prikazuje lokaciju adrese u skladu s određenom
specifikacijom, uključujući informacije o izvoru položaja.
GeographicPosition
status
Validnost adrese u životnom ciklusu (varijanta) prostornog objekta Address.
StatusValue
voidable
validFrom
Datum i vrijeme kad je ova verzija adrese u stvarnom svijetu važila ili će važiti.
DateTime
voidable
validTo
Datum i vrijeme kad je ova verzija adrese u stvarnom svijetu prestala važiti ili će
prestati važiti.
DateTime
voidable
Asocijacijske uloge tipa prostornog objekta Address
Asocijacijska
uloga
Definicija
Tip podatka
Voidability
building
Građevina kojoj je adresa dodijeljena ili sa kojom je
povezana.
Tip koja se navodi u oblasti prostornih podataka
Buildings
voidable
component
Označava da je komponenta adrese dio adrese.
AddressComponent
parcel
Katastarska parcela kojoj je adresa dodijeljena ili s
kojom je povezana.
CadastralParcel
voidable
parentAddress
Glavna (matična) adresa s kojom je ta (pod)adresa usko
povezana.
Address
voidable
Ograničenja tipa prostornog objekta Address Adresu ima prostorni objekt sa sastavnim dijelom adrese administrativne jedinice koja je na nivou 1. (zemlja).
Adresu ima tačno jedan zadati geografski položaj (atribut "default" prostornog objekta GeographicPosition mora imati vrijednost "true").
5.2.2. Ime područja adrese (AddressAreaName) Sastavni dio adrese koja prikazuje ime geografskog područja ili lokacije koja zbog dodjeljivanja adrese objedinjuje više naslovljivih objekata i nije administrativna jedinica.
Ime područja adrese je podtip tipa AddressComponent.
Atributi tipa prostornog objekta AddressAreaName
Atribut
Definicija
Tip podatka
Voidability
name
Vlastita imenica koje se upotrebljava za područje adrese.
GeographicalName
Asocijacijske uloge tipa prostornog objekta AddressAreaName
Asocijacijska uloga
Definicija
Tip podatka
Voidability
namedPlace
Naziv mjesta koje to područje adrese prikazuje.
NamedPlace
voidable
5.2.3. Sastavni dio adrese (AddressComponent) Identifikator ili geografsko ime određenog geografskog područja, lokacije ili drugog prostornog objekta koji određuje područje primjene adrese.
Riječ je o apstraktnom tipu.
Atributi tipa prostornog objekta AddressComponent
Atribut
Definicija
Tip podatka
Voidability
alternativeIdentifier
Spoljni tematski identifikator prostornog objekta Address Component, koji omogućava
međuoperativnost s postojećim nasleđenim sisoblastima ili aplikacijama.
CharacterString voidable
beginLifespanVersion Datum i vrijeme kad je ova verzija prostornog objekta unešena u skup prostornih
podataka ili u njemu izmijenjena.
DateTime
voidable
endLifespanVersion
Datum i vrijeme kad je ova verzija prostornog objekta u skupu prostornih podataka
izmijenjena ili iz njega izbrisana.
DateTime
voidable
inspireId
Spoljni identifikator prostornog objekta.
Identifier
status
Validnostsastavnog dijela adrese u životnom ciklusu (varijanta) prostornog objekta
Address Component.
StatusValue
voidable
validFrom
Datum i vrijeme kad je ova verzija sastavnog dijela adrese u stvarnom svijetu važila ili
će važiti.
DateTime
voidable
validTo
Datum i vrijeme kad je ova verzija sastavnog dijela adrese u stvarnom svijetu prestala
važiti ili će prestati važiti.
DateTime
voidable
Asocijacijske uloge tipa prostornog objekta AddressComponent
Asocijacijska
uloga
Definicija
Tip podatka
Voidabiity
situatedWithin
Drugi sastavni dio adrese u kojoj je prostorni objekakt koji prikazuje ovaj sastavni dio
adrese.
AddressComponent voidable
5.2.4. Naziv administrativne jedinice (AdminUnitName) Sastavni dio adrese koji prikazuje naziv administrativne jedinice za lokalnu, regionalnu i nacionalnu upravu gdje država ima i/ili ostvaruje jurisdikcijska prava.
Naziv administrativne jedinice je podtip tipa AddressComponent.
Atributi tipa prostornog objekta AdminUnitName
Atribut
Definicija
Tip podatka
Voidabiity
level
Administrativni nivo u nacionalnoj administrativnoj hijerarhiji.
AdministrativeHierarchyLevel
name
Službeno geografsko ime administrativne jedinice, prema potrebi na više jezika.
GeographicalName
Asocijacijske uloge tipa prostornog objekta AdminUnitName
Asocijacijska uloga
Definicija
Tip podatka
Voidability
adminUnit
Administrativna jedinica koja je izvor sadržaja imena administrativne jedinice.
AdministrativeUnit voidable
5.2.5. Poštanski deskriptor (PostalDescriptor) Sastavni dio adrese koji za poštanske svrhe prikazuje identifikaciju potpodjele adresa i poštanskih dostavnih tačaka u državi, regiji ili gradu. Poštanski deskriptor je podtip tipa AddressComponent.
Atributi tipa prostornog objekta PostalDescriptor
Atribut
Definicija
Tip podatka
Voidability
postCode Kod (broj) koji se stvara i koji se vodi u poštanske svrhe za identifikaciju podpodjele adresa i
poštanskih dostavnih tačaka.
CharacterString
postName Jedan ili više naziva koji su stvoreni i koji se vode u poštanske svrhe za identifikaciju
podpodjele adresa i poštanskih dostavnih tačaka.
GeographicalName
Ograničenja tipa prostornog objekta PostalDescriptor Ako nema poštanskog broja, traži se naziv pošte.
Ako nema naziva pošte, traži se poštanski broj.
5.2.6. Naziv saobraćajnice (ThoroughfareName) Sastavni dio adrese koja prikazuje naziv prolaza ili puta od jedne do druge lokacije.
Naziv saobraćajnice je podtip tipa AddressComponent.
Atributi tipa prostornog objekta ThoroughfareName
Atribut
Definicija
Tip podatka
Voidability
name
Naziv saobraćajnice.
ThoroughfareNameValue
Asocijacijske uloge tipa prostornog objekta ThoroughfareName
Asocijacijska
uloga
Definicija
Tip podatka Voidability
transportLink
Jedna ili više dionica saobraćajne mreže kojima je dodijeljen prostorni objekt
Thoroughfare Name.
TransportLink voidable
5.3. Tipa podataka
5.3.1. Lokator adrese (AddressLocator) Jasno čitljiv dezignator ili naziv koji korisniku ili aplikaciji omogućava da se u području upotrebe naziva saobraćajnice, naziva adrese područja, naziva administrativne jedinice ili poštanskog deskriptora u kojem je adresa locirana, upućuje na adresu ili da se adresa razlikuje od susjednih adresa.
Atributi tipa podataka AddressLocator
Atribut
Definicija
Tip podatka
Voidability
designator Broj ili niz znakova koji jedinstveno označavaju lokator u odgovarajućem (-im) području (-
ima) primjene.
LocatorDesignator
level
Nivo na koju lokator upućuje.
LocatorLevel
Value
name
Geografsko ime ili opisni tekst koji se odnosi na nekretninu određenu lokatorom.
LocatorName
Asocijacijske uloge tipa podatka AddressLocator
Asocijacijska
uloga
Definicija
Tip podatka
Voidability
withinScopeOf
Sastavni dio adrese koji određuje područje primjene u kojem se dodjeljuje lokator
adrese u skladu s pravilima koja osiguravaju nedvosmislenost.
AddressComponent voidable
Ograničenja tipa podataka AddressLocator Ako nema dezignatora, zahtijeva se naziv.
Ako nema naziva, zahtijeva se dezignator.
5.3.2. Prikaz adrese (AddressRepresentation) Prikaz prostornog objekta Address za poređenje sa spoljnim aplikacijskim šemama, koje moraju sadržati čitljive osnovne informacije i informacije o adresi.
Atributi tipa podataka AddressRepresentation
Atribut
Definicija
Tip podatka
Voidability
addressArea
Naziv ili nazivi geografskog područja ili lokaliteta koje objedinjuje više naslovljivih
objekata radi dodjeljivanja adrese, ali da pritom nije administrativna jedinica.
GeographicalName voidable
adminUnit
Naziv ili nazivi administrativne jedinice na području koje država ima i/ili ostvaruje
jurisdikcijsu na lokalnom, regionalnoj i nacionalnom nivou.
GeographicalName
locatorDesignator Broj ili niz znakova koji korisniku ili aplikaciji omogućava da lokatora u odgovarajućem
području primjene tumače, analiziraju i oblikuju. Lokator može sadržati više lokacijskih
dezignatora.
CharacterString
locatorName
Vlastita imenica (-e) koja (-e) se upotrebljava (-aju) za entitet u stvarnom svijetu
određeno lokatorom.
GeographicalName postCode
Kod (broj) koji se stvara i koji se vodi u poštanske svrhe za identifikaciju podpodjele
adresa i poštanskih dostavnih tačaka.
CharacterString
voidable
postName
Jedan ili više naziva koji su stvoreni i koji se vode u poštanske svrhe za identifikaciju
podpodjele adresa i poštanskih dostavnih tačaka.
GeographicalName voidable
thoroughfare
Naziv ili nazivi prolaza ili puta od jedne lokacije do druge, npr. puta ili unutrašnjeg
plovnog puta.
GeographicalName voidable
Asocijacijske uloge tipa podatka AddressRepresentation
Asocijacijska uloga
Definicija
Tip podatka
Voidability
addressFeature
Upućivanje na prostorni objekt Address.
Address
voidable
5.3.3. Geografski položaj (GeographicPosition) Položaj karakteristične tačke koja predstavlja lokaciju adrese prema određenoj specifikaciji, uključujući informacije o izvoru položaja.
Atributi tipa podataka GeographicPosition
Atribut
Definicija
Tip podatka
Voidability
default
Određuje treba li taj položaj primijenjivati kao zadat.
Boolean
geometry
Položaj tačke izražen koordinatama izabranog prostornog referentnog sistema.
GM_Point
method
Opis kako i ko je stvorio ili izveo geografski položaj adrese.
GeometryMethodValue
voidable
specification Informacija o specifikaciji koja se upotrebljava da se stvori ili izvede taj geografski
položaj adrese.
GeometrySpecificationValue voidable
5.3.4. Lokacijski dezignator (LocatorDesignator) Broj ili slijed znakova koji na jedinstven način određuju lokator u odgovarajućem području (-ima) primjene. Za puno označavanje lokatora može biti potreban jedan ili više lokacijskih dezignatora.
Atributi tipa podataka LocatorDesignator
Atribut
Definicija
Tip podatka
Voidability
designator Identifikacijski dio lokacijskog dezignatora sastoji se od jednog ili više brojeva ili
drugih znakova.
CharacterString
type
Tip vrijednosti lokatora koja aplikaciji omogućava da tumači, razlaže ili oblikuje u
skladu s određenim pravilima.
LocatorDesignatorTypeValue
5.3.5. Naziv lokatora (LocatorName) Vlastita imenica, koja se upotrebljava za entitet u stvarnom svijetu, određeno lokatorom.
Atributi tipa podataka LocatorName
Atribut
Definicija
Tip podatka
Voidability
name
Identifikacijski dio naziva lokatora.
GeographicalName
type
Tip vrijednosti lokatora koja aplikaciji omogućava da tumači, razlaže ili oblikuje u skladu s
određenim pravilima.
LocatorNameTypeValue
5.3.6. Dio naziva (PartOfName) Dio punog naziva nastao iz raščlanjivanja naziva saobraćajnice u odvojene, semantičke dijelove, upotrebom istog jezika i pisma na kojem je napisan puni naziv saobraćajnice.
Atributi tipa podatka PartOfName
Atribut
Definicija
Tip podatka
Voidability
part
Niz znakova koji izražava pojedinačni dio naziva upotrebom istog jezika i pisma na kojem je napisan
pun naziv saobraćajnice.
CharacterString
type
Klasifikacija dijela naziva prema njegovu semantičkom značenju u punom nazivu sobraćajnice.
PartTypeValue 5.3.7. Vrijednost naziva saobraćajnice (ThoroughfareNameValue) Vlastita imenica koja se može upotrijebiti za saobraćajnicu, uključujući i raščlanjivanje naziva na dijelove.
Atributi tipa podataka ThoroughfareNameValue
Atribut
Definicija
Tip podatka
Voidability
name
Vlastita imenica koja se upotrebljava za saobraćajnicu.
GeographicalName
nameParts
Jedan ili više dijelova na koje se može raščlaniti naziv saobraćajnice.
PartOfName
voidable
5.4. Popisi kodova (šifrarnici)
5.4.1. Geometrijska metoda (GeometryMethodValue) Opis kako i ko je stvorio ili izveo taj geografski položaj adrese.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova GeometryMethodValue
Vrijednost
Definicija
byAdministrator Odlučeno i ručno zabilježio službeni organ odgovoran za dodjeljivanje adrese ili provajder skupa podataka.
byOtherParty
Odlučeno i ručno zabilježila druga strana.
fromFeature
Automatski izvedeno iz drugog prostornog objekta infrastrukture prostornih podataka koji je povezan s adresom ili
sastavnim dijelom adrese.
5.4.2. Specifikacija geometrije (GeometrySpecificationValue) Informacija o specifikaciji koja se upotrebljava za stvaranje ili izvođenje tog geografskog položaja adrese.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova GeometrySpecificationValue
Vrijednost
Definicija
addressArea
Položaj izveden iz povezanih područja adrese.
adminUnit1stOrder
Položaj izveden iz povezane administrativne jedinice najvišeg nivoa.
adminUnit2ndOrder
Položaj izveden iz povezane administrativne jedinice drugog nivoa.
adminUnit3rdOrder
Položaj izveden iz povezane administrativne jedinice trećeg nivoa.
adminUnit4thOrder
Položaj izveden iz povezane administrativne jedinice četvrtog nivoa.
adminUnit5thOrder
Položaj izveden iz povezane administrativne jedinice petog nivoa.
adminUnit6thOrder
Položaj izveden iz povezane administrativne jedinice šestog nivoa.
building
Položaj koji služi za identifikaciju povezane građevine.
entrance
Položaj koji služi za identifikaciju ulaznih vrata ili ulaza.
parcel
Položaj koji služi za identifikaciju povezane zemljišne parcele.
postalDelivery
Položaj koji služi za identifikaciju poštanske dostavne tačke.
postalDescriptor
Položaj izveden iz povezanog područja poštanskog broja.
segment
Položaj izveden iz povezanog segmenta saobraćajnice.
thoroughfareAccess
Položaj koji služi za identifikaciju pristupne tačke sa saobraćajnicama.
utilityService
Položaj koji služi za identifikaciju tačke komunalne usluge.
5.4.3. Tip dezignatora lokacije (LocatorDesignatorTypeValue) Opis semantičkog značenja dezignatora lokacije.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova LocatorDesignatorTypeValue
Vrijednost
Definicija
addressIdentifierGeneral
Identifikator adrese koji se sastoji od brojeva i/ili znakova.
addressNumber
Identifikator adrese koji se sastoji samo od brojeva.
addressNumber2ndExtension
Drugo proširenje broja adrese.
addressNumberExtension
Proširenje broja adrese.
buildingIdentifier
Identifikator građevine koji se sastoji od brojeva i/ili znakova.
buildingIdentifierPrefix
Prefiks broja građevine.
cornerAddress1stIdentifier
Identifikator adrese povezan s nazivom primarne saobraćajnice u uglu adrese.
cornerAddress2ndIdentifier
Identifikator adrese povezan s nazivom sekundarne saobraćajnice u uglu adrese.
entranceDoorIdentifier
Identifikator za ulazna vrata, ulaz ili natkriveni prilaz.
floorIdentifier
Identifikator za sprat ili nivo unutar građevine.
kilometrePoint
Oznaka na putu na kojoj se nalazi broj koji duž puta označava njenu udaljenost od početne tačke puta.
postalDeliveryIdentifier
Identifikator poštanske dostavne tačke.
staircaseIdentifier
Identifikator za stepenište, obično unutar građevine.
unitIdentifier
Identifikator vrata, stana, apartmana ili sobe unutar građevine.
5.4.4. Nivo lokacije (LocatorLevelValue) Nivo na koju lokacija upućuje.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova LocatorLevelValue
Vrijednost
Definicija
accessLevel
Lokator identifikuje poseban pristup zemljišnoj parceli, građevini ili sličnom pomoću ulaznog broja ili sličnog
identifikatora.
postalDeliveryPoint Lokator identifikuje poštansku dostavnu tačku.
siteLevel
Lokator identifikuje posebnu zemljišnu parcelu, građevinu ili sličnu nekretninu pomoću broja adrese, broja građevine,
imena građevine ili nekretnine.
unitLevel
Lokator identifikatora poseban dio građevine.
5.4.5. Tip naziva lokacije (LocatorNameTypeValue) Opis semantičkog značenja naziva lokatora.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova LocatorNameTypeValue
Vrijednost
Definicija
buildingName
Ime građevine ili dijela građevine.
descriptiveLocator
Tekstualni opis lokacije ili predmeta koji se može adresirati.
roomName
Identifikator stana, apartmana ili sobe unutar građevine.
siteName
Ime nekretnine, stambenog kompleksa ili lokacije.
5.4.6. Tip dijela (PartTypeValue) Klasifikacija dijela imena u skladu sa semantičkim značenjem u punom nazivu saobraćajnice.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova PartTypeValue
Vrijednost
Definicija
name
Dio imena čini jezgro ili korijen imena saobraćajnice.
namePrefix Dio imena koristi se za odvajanje povezujućih riječi koje nisu relevantne za razvrstavanje od jezgra imena saobraćajnice.
qualifier
Dio imena koji određuje ime saobraćajnice.
type
Dio imena koji označava kategoriju ili tip saobraćajnice.
5.4.7. Status (StatusValue) Trenutna važnost adrese ili sastavnog dijela adrese u stvarnom svijetu.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova StatusValue
Vrijednost
Definicija
alternative Adresa ili sastavni dio adrese u opštoj upotrebi, koji se razlikuje od glavne adrese ili sastavnog dijela adrese koju je utvrdio
nadležniorgan za dodjeljivanje adrese ili staratelj-vlasnik skupa podataka.
current
Trenutna i važeća adresa ili sastavni dio adrese koja se prema mišljenju nadležnog organa odgovornog za dodjeljivanje adrese
ili staratelj skupa podataka smatra najprikladnom adresom u opštoj upotrebi.
proposed
Adresa ili sastavni dio adrese za koju se očekuje odobrenje provajdera skupa podataka ili nadležnog organa odgovornog za
dodjeljivanje adrese.
reserved
Adresa ili sastavni dio adrese koju je odobrio nadležni organ odgovoran za dodjeljivanje adrese ili provajdera skupa podataka,
ali koju je još je potrebno sprovesti.
retired
Adresa ili sastavni dio adrese koja više nije u svakodnevnoj upotrebi ili ju je ukinuo nadležni organ odgovoran za dodjeljivanje
adrese ili skrbnik skupa podataka.
5.5. Zahtjevi za oblasti
5.5.1. Položaj adrese
1. U skupu podataka položaj adrese prikazuje se koordinatama stvarne lokacije najboljom dostupnom tačnošću. Pritom se koriste
najpreciznije neposredno prikupljene koordinate ili, ako ih nema, tada koordinate izvedene iz jedne od sastavnih dijelova adrese, pri
čemu se prioritet daje sastavnom dijelu koji omogućava najtačnije određivanje položaja.
2. Ako adresa sadrži više od jednog položaja, atributu "specification" dodjeljuju se različite vrijednosti za svaki položaj.
5.5.2. Asocijacijske uloge
1. Asocijacijska uloga withinScopeOf mora sadržati vrijednosti svih lokatora koji su dodijeljeni u skladu s pravilima kojima se nastoji
osigurati nedvosmislenost u pojedinom sastavnom dijelu adrese (tj. nazivu saobraćajnice, nazivu područja adrese, poštanskom
deskriptoru ili nazivu u administrativne jedinice).
2. Asocijacijska uloga parentAddress mora postojati za sve adrese koje su povezane s matičnom (ili glavnom) adresom.
3. Adresa ima asocijaciju na naziv zemlje u kojoj je locirana. Osim toga, adresa mora imati asocijacije i na dodatne sastavne dijelove adrese
potrebne za nedvosmisleno označavanje i lokaciju primjera adrese.
5.6. Slojevi
Sloj za temu prostornih podataka Addresses
Naziv sloja
Naslov sloja
Tip prostornog objekta
AD.Address
Adrese
Address
6. KATASTARSKE PARCELE
6.1. Tipa prostornog objekta Sljedeće tipa prostornog objekta upotrebljavaju se za razmjenu i klasifikaciju prostornih objekata iz skupa podataka koji se odnose na oblast prostornih podataka Cadastral Parcels:
-
osnovna zemljišna jedinica nekretnine;
-
katastarska međa;
-
katastarska parcela; i -
podjela na katastarske jedinice.
Katastarske parcele moraju uvijek biti dostupne.
Osnovne zemljišne jedinice nekretnina osiguravaju države, pri čemu se jedinstveni katastarski identifikatori daju samo za osnovne zemljišne jedinice nekretnina, a ne za parcele.
Katastarske međe osiguravaju države, pri čemu se za katastarsku granicu evidentiraju informacije o apsolutnoj tačnosti položaja.
6.1.1. Osnovna zemljišna jedinica nekretnine (BasicPropertyUnit) Osnovna jedinica vlasništva koja je evidentirana u zemljišnim knjigama, katastru nekretnina i ekvivalentnim registrima. Definisana je jedinstvenim vlasničkim pravima i homogenim stvarnim pravima na nekretnine i sastoji se od jedne ili više susjednih ili geografski razdvojenih parcela.
Atributi tipa prostornog objekta BasicPropertyUnit
Atribut
Definicija
Tip podatka
Voidability
areaValue
Vrijednost evidentiranog područja koja kvantifikuje područje projektovano na horizontalnu ravnu katastarskih parcela od kojih se sastoji osnovna zemljišna
jedinica nekretnine.
Area
voidable
beginLifespanVersion
Datum i vrijeme kad je ova verzija prostornog objekta unešena u skup prostornih
podataka ili u njemu izmijenjena.
DateTime
voidable
endLifespanVersion
Datum i vrijeme kad je ova verzija prostornog objekta u skupu prostornih
podataka izmijenjena ili iz njega izbrisana.
DateTime
voidable
inspireId
Spoljni identifikator objekta prostornog objekta.
Identifier
nationalCadastralReference Tematski identifikator na nacionalnom nivou, obično potpun nacionalni kod
osnovne zemljišne jedinice nekretnine. Mora osigurati vezu s nacionalnim
zemljišnim katastrom ili ekvivalentnim registrom.
CharacterString
validFrom
Službeni datum i vrijeme kad je osnovna zemljišna jedinica nekretnine službeno
evidentirana ili će biti evidentirana.
DateTime
voidable
validTo
Datum i vrijeme kad se osnovna zemljišna jedinica nekretnine prestala službeno
koristiti ili će se prestati koristiti.
DateTime
voidable
Asocijacijske uloge tipa prostornog objekta BasicPropertyUnit
Asocijacijska
uloga
Definicija
Tip podatka
Voidability
administrativeUnit Administrativna jedinica najnižeg administrativnog nivoa u kojoj se ta osnovna
zemljišna jedinica nekretnine nalazi.
AdministrativeUnit voidable
Ograničenja tipa prostornog objekta BasicPropertyUnit Vrijednost atributa areaValue izražava se u kvadratnim metrima.
6.1.2. Katastarska međa (CadastralBoundary) Dio prikaza katastarske parcele. Jednu katastarsku među mogu dijeliti dvije susjedne katastarske parcele.
Atributi tipa prostornog objekta CadastralBoundary
Atribut
Definicija
Tip
podatka
Voidability
beginLifespan Version
Datum i vrijeme kad je ova verzija prostornog objekta unešena u skup prostornih podataka ili
u njemu izmijenjena.
DateTime voidable
endLifespan Version
Datum i vrijeme kad je ova verzija prostornog objekta u skupu prostornih podataka
izmijenjena ili iz njega izbrisana.
DateTime voidable
estimatedAccuracy Procijenjena apsolutna tačnost položaja katastarske međe u korišćenoj infrastrukturi
prostornih podataka koordinatnom referentnom sistemu. Apsolutna tačnost položaja je
Length
voidable
srednja vrijednost položajnih odstupanja za niz položaja, pri čemu su položajna odstupanja udaljenost između izmjerenog položaja i položaja koji se smatra pravim odgovarajućim
položajem.
geometry
Geometrija katastarske granice.
GM_Curve inspireId
Spoljni identifikator objekta prostornog objekta.
Identifier
validFrom
Službeni datum i vrijeme kad je katastarska međa pravno uspostavljena ili će biti pravno
uspostavljena.
DateTime voidable
validTo
Datum i vrijeme kad se katastarska međa prestala pravno koristiti ili će se prestati pravno
koristiti.
DateTime voidable
Asocijacijske uloge tipa prostornog objekta CadastralBoundary
Asocijacijska
uloga
Definicija
Tip podatka
Voidability
parcel
Katastarska parcela (-e) ocrtana(-e) tom katastarskom međom. Katastarska međa može
prikazati jednu ili više katastarskih parcela.
CadastralParcel voidable
Ograničenja tipa prostornog objekta CadastralBoundary Vrijednost atributa estimatedAccuracy izražena je u metrima.
6.1.3. Katastarska parcela (CadastralParcel) Područja koja definiše zemljišni katastar ili ekvivalentni registri.
Atributi tipa prostornog objekta CadastralParcel
Atribut
Definicija
Tip podatka
Voidability
areaValue
Veličina - površina evidentiranog područja koja kvantifikuje područje
projektovano na horizontalnu ravnu katastarske parcele.
Area
voidable
beginLifespan Version
Datum i vrijeme kad je ova verzija prostornog objekta unešena u skup prostornih
podataka ili u njemu izmijenjena.
DateTime
voidable
endLifespanVersion
Datum i vrijeme kad je ova verzija prostornog objekta u skupu prostornih
podataka izmijenjena ili iz njega izbrisana.
DateTime
voidable
geometry
Geometrija katastarske parcele.
GM_Object
inspireId
Spoljni identifikator objekta prostornog objekta.
Identifier
label
Tekst koji se upotrebljava za identifikaciju katastarske parcele.
CharacterString nationalCadastralReference Tematski identifikator na nacionalnom nivou, obično potpun nacionalni kod
katastarske parcele. Mora osigurati vezu s zemljišnim katastrom ili
ekvivalentnim registrom.
CharacterString
referencePoint
Tačka na katastarskoj parceli.
GM_Point
voidable
validFrom
Službeni datum i vrijeme kad je katastarska parcela pravno uspostavljena ili će
biti pravno uspostavljena.
DateTime
voidable
validTo
Datum i vrijeme kad se katastarska parcela pravno prestala koristiti ili će se
pravno prestati koristiti.
DateTime
voidable
Asocijacijske uloge tipa prostornog objekta CadastralParcel
Asocijacijska
uloga
Definicija
Tip podatka
Voidability
administrativeUnit
Administrativna jedinica najnižeg administrativnog nivoa u kojoj se ta katastarska
parcela nalazi.
AdministrativeUnit voidable
basicPropertyUnit
Osnovna zemljišna jedinica (-e) nekretnine u kojoj se ta katastarska parcela nalazi.
BasicPropertyUnit voidable
zoning
Podjela na katastarske jedinice najnižeg nivoa na kojoj se ta katastarska parcela
nalazi.
CadastralZoning
voidable Ograničenja tipa prostornog objekta CadastralParcel Vrijednost atributa areaValue izražena je u kvadratnim metrima.
Tip geometrije je GM_Surface ili GM_MultiSurface.
6.1.4. Podjela na katastarske jedinice (CadastralZoning) Posredna područja koja se upotrebljavaju za podjelu teritorije države u katastarske parcele.
Atributi tipa prostornog objekta CadastralZoning
Atribut
Definicija
Tip podatka
Voidability
beginLifespanVersion
Datum i vrijeme kad je ova verzija prostornog objekta unesena u
skup prostornih podataka ili u njemu izmijenjena.
DateTime
voidable
endLifespan Version
Datum i vrijeme kad je ova verzija prostornog objekta u skupu
prostornih podataka izmijenjena ili iz njega izbrisana.
DateTime
voidable
estimatedAccuracy
Procijenjena apsolutna tačnost položaja katastarskih parcela u
podjeli
na
katastarske
jedinice u
korišćenom
INSPIRE
koordinatnom referentnom sistemu. Apsolutna tačnost položaja je srednja vrijednost položajnih odstupanja za niz položaja, pri čemu su položajna odstupanja udaljenost između izmjerenog položaja i položaja koji se smatra pravim odgovarajućim
položajem.
Length
voidable
geometry
Geometrija podjele na katastarske parcele.
GM_MultiSurface
inspireId
Vanjski identifikator objekta prostornog objekta.
Identifier
label
Tekst koji se koristi za identifikaciju podjele na katastarske
jedinice.
CharacterString
level
Stepen podjele na katastarske jedinice u katastarskoj hijerarhiji.
CadastralZoningLevel
Value
voidable
levelName
Naziv nivoa podjele na katastarske jedinice u katastarskoj
hijerarhiji, najmanje na jednom službenom jeziku.
LocalisedCharacterString voidable
name
Naziv podjele na katastarske jedinice.
GeographicalName
voidable
nationalCadastalZoningReference Tematski identifikator na nacionalnom nivou, potpun nacionalni
kod podjele na katastarske jedinice.
CharacterString
originalMapScaleDenominator
Imenilac razmjere izvorne analogne mape (ako postoji) na koji se
podjele na katastarske jedinice odnosi.
Integer
voidable
referencePoint
Tačka u podjeli na katastarske jedinice.
GM_Point
voidable
validFrom
Službeni datum i vrijeme kad je podjela na katastarske jedinice
pravno uspostavljena ili će biti pravno uspostavljena.
DateTime
voidable
validTo
Datum i vrijeme kad se podjela na katastarske parcele pravno
prestala koristiti ili će se pravno prestati koristiti.
DateTime
voidable
Asocijacijske uloge tipa prostornog objekta CadastralZoning
Asocijacijska
uloga
Definicija
Tip podatka
Voidability
upperLevelUnit
Sljedeći viši nivo podjele na katastarske jedinice pod koju pripada ta podjela na
katastarske jedinice.
CadastralZoning voidable
Ograničenja tipa prostornog objekta CadastralZoning Vrijednost atributa estimatedAccuracy izražava se u metrima.
Podjela na katastarske jedinice na nižem nivou dio je podjele na višem nivou.
6.2. Popisi kodova
6.2.1. Nivo podjele na katastarske jedinice (CadastralZoningLevelValue) Hijerarhijski nivo podjele na katastarske jedinice.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova CadastralZoningLevelValue
Vrijednost
Definicija
1stOrder
Najviši hijerarhijski nivo(najveća područja) podjele na katastarske jedinice, koja je jednaka ili identična opštinama.
2ndOrder
Drugi hijerarhijski nivo podjele na katastarske jedinice.
3rdOrder
Treći hijerarhijski nivopodjele na katastarske jedinice.
6.3 Zahtjevi za oblasti
6.3.1. Prikaz geometrije
1. Domen vrijednosti prostornih svojstava koja su definisana u ovom dijelu nije ograničena na šemu prostornih podataka Simple Feature
prema normi EN ISO 19125-1.
2. Ako su osigurane katastarske međe, katastarske međe koje odgovaraju obrisu katastarske parcele moraju oblikovati zatvoreni (-e) krug (-
e).
6.3.2. Modeliranje referenci objekta Za sve primjere tipa prostornog objekta CadastralParcel upotrebljava se atribut nationalCadastralReference kao tematski identifikator. Taj atribut mora korisnicima omogućiti da ostvare vezu do pravnog propisa, vlasnika i drugih katastarskih informacija koje su u nacionalnim zemljišnim katastrima ili ekvivalentnim registrima.
6.3.3. Koordinatni referentni sisoblasti Ako su podaci koji se odnose na temu prostornog podatka Cadastral Parcels dostupni u ravnim koordinatama upotrebom Lambertove konformne konusne projekcije, oni moraju biti dostupni i u najmanje jednom dodatnom koordinatnom referentnom sistemu iz dijela 1.3.1., 1.3.2. i 1.3.3.
6.4. Pravila za prikazivanje
6.4.1. Slojevi
Sloj za temu prostornih podataka Cadastral Parcels
Ime sloja
Naslov sloja
Tip prostornog objekta
CP.CadastralParcel
Katastarska parcela
CadastralParcel
CP.CadastralZoning
Podjela na katastarske jedinice
CadastralZoning
CP.CadastralBoundary
Katastarska međa
CadastralBoundary
7. SAOBRAĆAJNE MREŽE KOJE OBUHVATAJU SAOBRAĆAJNE, ŽELJEZNIČKE, VAZDUŠNE I VODENE SAOBRAĆAJNE MREŽE, ELEKTRONSKE KOMUNIKACIONE MREŽE I PRATEĆU INFRASTRUKTURU
7.1. Definicije
- "referentna tačka aerodroma" je određeni geografski položaj aerodroma, koji je blizu početnog ili planiranoga geometrijskog središta
aerodroma i obično ostaje tamo gdje je izvorno određen;
- "vazdušna luka/heliodrom" je tačno određeno područje na kopnu ili vodi (uključujući sve građevine, instalacije i opremu) koje je
djelomično ili u potpunosti namijenjeno dolasku i odlasku aviona/helikoptera i njihovom kretanju po tlu;
- "dubokomorski put" je put na tačno određenom području unutar određenih granica gdje je morsko dno tačno izmjereno i koje osigurava
da potopljene prepreke ne prelaze najmanje dopuštene dubine;
- "intermodalna veza" je veza između dva elemenata u različitim saobraćajnim mrežama koje upotrebljavaju različite načine prevoza i tako
omogućavaju promjenu transportovanog medija (ljudi, roba itd.) s jednog oblika prevoza na drugi;
- "linijski element" je jednodimenzionalni objekat koji služi kao osa za linearno referenciranje, - "linearno referenciranje"je specifikacija lokacije u odnosu na jednodimenzionalni objekat kao mjere duž (i neobavezno odmaknute od)
tog elementa, - "oprema za pomoć pri navigaciji" je fizička oprema za pomoć pri navigaciji koja je na površini Zemlje, npr. Very High Frequency
Omnidirectional Radio Range (VOR), Distance Measuring Equipment (DME), lokalizator i Tactical Air Navigation Beacon (TACAN) itd., koji
omogućavaju sigurno vođenje vazdušnog saobraćaja po postojećim vazdušnim rutama, - "objektno referenciranje" je osiguranje prostornog opsega objekta upućivanjem na postojeći prostorni objekat ili skup prostornih
objekata, - "ranžirne željezničke stanice" su područja koje presijecaju brojni paralelni međusobno povezani kolosijeci (obično više od dva), koji se
upotrebljavaju za zaustavljanje vozova zbog ukrcavanja/iskrcavanja tereta bez prekidanja saobraćaja glavne željezničke pruge,
- "važna tačka" je određena geografska lokacija koja se upotrebljava za definisanje rute službe vazdušnog saobraćaja (ATS), puta leta
zrakoplova ili u druge navigacijske/ATS svrhe.
- "Area Navigation (RNAV)" je metoda navigacije koja avionu omogućava let na bilo kom željenom putu leta u okviru pokrivenosti zemaljskim referentnim navigacijskim uređajima ili u granicama mogućnosti opreme aviona, ili njihovom
kombinacijom,
- "TACAN Navigation" je metoda navigacije koja avionu omogućava let na bilo kom željenom putu leta u okviru pokrivenosti
zemaljskim referenciranim navigacijskim uređajima Tactical Air Navigation Beacon (TACAN)."
7.2. Struktura oblasti prostornih podataka "Saobraćajna mreža" Tipa određene za temu prostornih podataka saobraćajne mreže strukturisani su u sljedeće pakete:
-
zajednički elementi saobraćaja;
-
vazdušna saobraćajna mreža;
-
saobraćajna mreža žičara;
-
željeznička saobraćajna mreža;
-
saobraćajna putna mreža; i -
vodena saobraćajna mreža.
7.3. Zajednički elementi saobraćaja
7.3.1. Tipa prostornog objekta Sljedeće tipa prostornog objekta upotrebljavaju se za razmjenu i klasifikaciju prostornih objekata koji se odnose na zajedničke elemente saobraćaja:
-
ograničenje prilaza;
-
stanje objekta;
-
organ nadležan za održavanje;
-
stub za označavanje (stub međaš);
-
vlasnički organ;
-
ograničenje za vozila;
-
smjer saobraćajnog toka;
-
područje saobraćaja;
-
saobraćajna dionica;
-
niz saobraćajnih dionica;
-
skup saobraćajnih dionica;
-
saobraćajna mreža;
-
saobraćajni čvor;
-
saobraćajn objekt;
-
saobraćajna tačka;
-
svojstvo saobraćaja; i -
vertikalan položaj.
7.3.1.1. Ograničenje prilaza (AccessRestriction) Ograničenje na prilaz elementu saobraćaja.
Ograničenje prilaza je podtip tipa TransportProperty.
Atributi tipa prostornog objekta AccessRestriction
Atribut
Definicija
Tip podatka
Voidability
restriction
Tip ograničenja prilaza.
AccessRestrictionValue 7.3.1.2. Stanje objekta (ConditionOfFacility) Stanje elementa saobraćajne mreže u smislu njegove dovršenosti i upotrebe.
Stanje objekta je podtip tipa TransportProperty.
Atributi tipa prostornog objekta ConditionOfFacility
Atribut
Definicija
Tip podatka
Voidability
currentStatus Trenutna vrijednost stanja elementa saobraćajne mreže u smislu njegove dovršenosti
i upotrebe.
ConditionOfFacilityValue
7.3.1.3. Organ nadležan za održavanje (MaintenanceAuthority) Organ nadležan za održavanje elementa saobraćaja.
Organ nadležan je podtip tipa TransportProperty.
Atributi tipa prostornog objekta MaintenanceAuthority
Atribut
Definicija
Tip podatka
Voidability
authority
Naziv organa nadležnog za održavanje.
CI_Citation
7.3.1.4. Stub za označavanje (MarkerPost) Stub za označavanje udaljenosti je postavljen duž rute saobraćajne mreže, uglavnom u jednakim razmacima, koji označava udaljenost od početka rute, ili neke druge referentne tačke, do tačke gdje je postavljen stub za označavanje.
Stub za označavanje je podtip tipa TransportPoint.
Atributi tipa prostornog objekta MarkerPost
Atribut
Definicija
Tip
podatka
Voidability
location Udaljenost od početka rute, ili neke druge referentne tačke, do tačke gdje je postavljen stub za
označavanje.
Distance
Asocijacijske uloge tipa prostornog objekta MarkerPost
Asocijacijska uloga
Definicija
Tip podatka
Voidability
route
Ruta na saobraćajnoj mreži uzduž koje je postavljen stub za označavanje.
TransportLinkSet
voidable
7.3.1.5. Vlasnički organ (OwnerAuthority) Organ koji je vlasnik elementa saobraćaja.
Vlasnički organ je podtip tipa TransportProperty.
Atributi tipa prostornog objekta OwnerAuthority
Atribut
Definicija
Tip podatka
Voidability
authority
Naziv vlasničkog organa.
CI_Citation
7.3.1.6. Ograničenje za vozila (RestrictionForVehicles) Ograničenje za vozila na elementu saobraćaja.
Ova je Tip podtip tipa TransportProperty.
Atributi tipa prostornog objekta RestrictionForVehicles
Atribut
Definicija
Tip podatka
Voidability
measure
Mjera ograničenja.
Measure
restrictionType
Tip ograničenja.
RestrictionTypeValue
7.3.1.7. Smjer saobraćajnog toka (TrafficFlowDirection) Pokazuje smjer protoka saobraćaja u odnosu na smjer vektora saobraćajne veze.
Smjer saobraćajnog toka je podtip tipa TransportProperty.
Atributi tipa prostornog objekta TrafficFlowDirection
Atribut
Definicija
Tip podatka
Voidability
direction
Pokazuje smjer protoka saobraćaja.
LinkDirectionValue
Ograničenja tipa prostornog objekta TrafficFlowDirection Ovo se svojstvo može povezati samo s vrstom prostornog objekta Link ili LinkSequence.
7.3.1.8. Područje saobraćaja (TransportArea) Površina koja pokazuje prostorni opseg elementa saobraćajne mreže.
Područje saobraćaja je podtip tipa NetworkArea i Područje saobraćaja je podtip tipa TransportObject.
Riječ je o apstraktnom tipu .
Atributi tipa prostornog objekta TransportArea
Atribut
Definicija
Tip podatka
Voidability
validFrom
Trenutak kad je područje saobraćaja u stvarnom svijetu počelo postojati.
DateTime
voidable
validTo
Trenutak kad je područje saobraćaja u stvarnom svijetu prestalo postojati.
DateTime
voidable
Ograničenja tipa prostornog objekta TransportArea Sva područja saobraćaja imaju spoljni identifikator objekta.
7.3.1.9. Saobraćajna dionica (TransportLink) Linijski prostorni objekat koji opisuje geometriju i povezivost saobraćajne mreže između dvije tačake na mreži.
Saobraćajna dionica je podtip tipa Link i Saobraćajna dionica je podtip tipa TransportObject.
Riječ je o apstraktnom tipu.
Atributi tipa prostornog objekta TransportLink
Atribut
Definicija
Tip podatka
Voidability
validFrom
Trenutak kad je saobraćajna dionica u stvarnom svijetu počela postojati.
DateTime
voidable
validTo
Trenutak kad je saobraćajna dionica u stvarnom svijetu prestala postojati.
DateTime
voidable
Ograničenja tipa prostornog objekta TransportLink Sve saobraćajne dionice imaju spoljni identifikator objekta.
7.3.1.10. Niz saobraćajnih dionica (TransportLinkSequence) Linijski prostorni objekt, sastavljen od uređene zbirke saobraćajnih dionica, koji prikazuje neprekidni nerazgranati put u saobraćajnoj mreži. Element ima određeni početak i završetak i svaki se položaj na nizu saobraćajnih dionica može odrediti samo jednim parametrom, npr. dužinom. Opisuje element saobraćajne mreže za koji je karakterističan jedan ili više tematskih identifikatora i/ili svojstava.
Niz saobraćajnih dionica je podtip tipa LinkSequence i Niz saobraćajnih dionica je podtip tipa TransportObject.
Riječ je o apstraktnom tipu.
Atributi tipa prostornog objekta TransportLinkSequence
Atribut
Definicija
Tip podatka
Voidability
validFrom
Trenutak kad je niz saobraćajnih dionica u stvarnom svijetu počeo postojati.
DateTime
voidable
validTo
Trenutak kad je niz saobraćajnih dionica u stvarnom svijetu prestao postojati.
DateTime
voidable
Ograničenja tipa prostornog objekta TransportLinkSequence Niz saobraćajnih dionica mora se sastojati od saobraćajnih dionica koje pripadaju istoj saobraćajnoj mreži.
Svi nizovi saobraćajnih dionica imaju spoljni identifikator objekta.
7.3.1.11. Skup saobraćajnih dionica (TransportLinkSet) Zbirka skupova saobraćajnih dionica i/ili pojedinih saobraćajnih dionica koja ima posebnu funkciju ili važnost u saobraćajnoj mreži.
Skup saobraćajnih dionica je podtip tipa LinkSet.
Skup saobraćajnih dionica je podtip tipa TransportObject.
Riječ je o apstraktnom tipu.
Atributi tipa prostornog objekta TransportLinkSet
Atribut
Definicija
Tip podatka
Voidability
validFrom
Trenutak kad je skup saobraćajnih dionica u stvarnom svijetu počeo postojati.
DateTime
voidable
validTo
Trenutak kad je skup saobraćajnih dionica u stvarnom svijetu prestao postojati.
DateTime
voidable
Asocijacijske uloge tipa prostornog objekta TransportLinkSet
Asocijacijska uloga
Definicija
Tip podatka
Voidability
post
Kolona za označavanje duž rute na saobraćajnoj mreži.
MarkerPost
voidable
Ograničenja tipa prostornog objekta TransportLinkSet Skup saobraćajnih dionica mora se sastojati od saobraćajnih dionica ili niza saobraćajnih dionica koje pripadaju istoj saobraćajnoj mreži. Svi skupovi saobraćajnih dionica imaju spoljni identifikator objekta.
7.3.1.12. Saobraćajna mreža (TransportNetwork) Zbirka elemenata mreže koji pripadaju jednom obliku prevoza.
Saobraćajna mreža je podtip tipa Network.
Atributi tipa prostornog objekta TransportNetwork
Atribut
Definicija
Tip podatka
Voidability
inspireId
Spoljni identifikator objekta prostornog objekta.
Identifier
typeOfTransport
Tip saobraćajne mreže utemeljena na vrsti infrastrukture koju mreža koristi.
TransportTypeValue
7.3.1.13. Saobraćajni čvor (TransportNode) Tačkasti prostorni objekat koji se koristi za povezivanje.
Saobraćajni čvor je podtip tipa Node i Saobraćajni čvor je podtip tipa TransportObject.
Riječ je o apstraktnom tipu.
Atributi tipa prostornog objekta TransportNode
Atribut
Definicija
Tip podatka
Voidability
validFrom
Trenutak kad je saobraćajni čvor u stvarnom svijetu počeo postojati.
DateTime
voidable
validTo
Trenutak kad je saobraćajni čvor u stvarnom svijetu prestao postojati.
DateTime
voidable
Ograničenja tipa prostornog objekta TransportNode Svi saobraćajni čvorovi imaju spoljni identifikator objekta.
7.3.1.14. Saobraćajni objekt (TransportObject) Osnova identiteta objekata saobraćajne mreže u stvarnom svijetu.
Riječ je o apstraktnom tipu.
Atributi tipa prostornog objekta TransportObject
Atribut
Definicija
Tip podatka
Voidability
geographicalName Geografsko ime koje se upotrebljava za identifikaciju objekta saobraćajne mreže u
stvarnom svijetu. Osigurava "ključ" za implicitno povezivanje različitih prikaza objekta.
GeographicalName voidable
7.3.1.15. Saobraćajna tačka (TransportPoint) Tačkasti prostorni objekt, koji nije čvor, koji prikazuje položaj elementa saobraćajne mreže.
Saobraćajna tačka je podtip tipa NetworkElement i Saobraćajna tačka je podtip tipa TransportObject.
Riječ je o apstraktnom tipu.
Atributi tipa prostornog objekta TransportPoint
Atribut
Definicija
Tip podatka
Voidability
geometry
Lokacija saobraćajne tačke.
GM_Point
validFrom
Trenutak kad je saobraćajna tačka u stvarnom svijetu počela postojati.
DateTime
voidable
validTo
Trenutak kad je saobraćajna tačka u stvarnom svijetu prestala postojati.
DateTime
voidable
Ograničenja tipa prostornog objekta TransportPoint Sve saobraćajne tačke imaju spoljni identifikator objekta.
7.3.1.16. Svojstvo saobraćaja (TransportProperty) Identifikacija svojstva koje se odnosi na mrežu. Svojstvo može važiti za cjelokupan element mreže na koju se odnosi; kod linijskih prostornih objekata može se opisati linearnim referenciranjem.
Svojstvo saobraćaja je podtip tipa NetworkProperty.
Riječ je o apstraktnom tipu.
Atributi tipa prostornog objekta TransportProperty
Atribut
Definicija
Tip podatka
Voidability
validFrom
Trenutak kad je svojstvo saobraćaja u stvarnom svijetu počelo postojati.
DateTime
voidable
validTo
Trenutak kad je svojstvo saobraćaja u stvarnom svijetu prestalo postojati.
DateTime
voidable
Ograničenja tipa prostornog objekta TransportProperty Sva svojstva saobraćaja imaju spoljni identifikator objekta.
7.3.1.17. Vertikalan položaj (VerticalPosition) Vertikalan položaj u odnosu na druge elemente saobraćajne mreže.
Vertikalan položaj je podtip tipa TransportProperty.
Atributi tipa prostornog objekta VerticalPosition
Atribut
Definicija
Tip podatka
Voidability
verticalPosition
Relativni vertikalni položaj elementa saobraćaja.
VerticalPositionValue
7.3.2. Enumeracije
7.3.2.1. Tip saobraćaja (TransportTypeValue) Moguće tipa saobraćaja mreže.
Dopuštene vrijednosti za enumeraciju TransportTypeValue
Vrijednost
Definicija
air
Riječ je o mreži u vazdušnom saobraćaju.
cable
Riječ je o mreži u saobraćaju žičarama.
rail
Riječ je o mreži u željezničkom saobraćaju.
road
Riječ je o mreži u putnom saobraćaju.
water
Riječ je o saobraćajanoj mreži vodenim putevima.
7.3.3. Popisi kodova
7.3.3.1. Ograničenje prilaza (AccessRestrictionValue) Tipa ograničenja prilaza za element saobraćaja.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova AccessRestrictionValue
Vrijednost
Definicija
forbiddenLegally
Prilaz elementu saobraćaja zabranjen je u skladu sa zakonom.
physicallyImpossible
Prilaz elementu saobraćaja fizički je nemoguć zbog prisutnosti barijera ili drugih materijalnih prepreka.
private
Prilaz elementu saobraćaja ograničen je zbog toga što je on u privatnom vlasništvu.
publicAccess
Element saobraćaja javno je dostupan.
seasonal
Prilaz elementu saobraćaja zavisi od godišnjeg doba.
toll
Za prilaz elementu saobraćaja plaća se putarina.
7.3.3.2. Tip ograničenja (RestrictionTypeValue) Moguća ograničenja za vozila koja imaju pristup do elementa saobraćaja.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova RestrictionTypeValue
Vrijednost
Definicija
maximumDoubleAxleWeight
Najveća dopuštena težina po dvostrukoj osovini vozila na elementu saobraćaja.
maximumDraught
Najveći dopušteni gaz vozila na elementu saobraćaja.
maximumFlightLevel
Najviši dopušteni nivo leta za vozilo na elementu saobraćaja.
maximumHeight
Najveća dopuštena visina vozila koje može proći ispod drugog objekta.
maximumLength
Najveća dopuštena dužina vozila na elementu saobraćaja.
maximumSingleAxleWeight
Najveća dopuštena težina po jednostrukoj osovini vozila na elementu saobraćaja.
maximumTotalWeight
Najveća dopuštena ukupna masa vozila na elementu saobraćaja.
maximumTripleAxleWeight
Najveća dopuštena težina po trostrukoj osovini vozila na elementu saobraćaja.
maximumWidth
Najveća dopuštena širina vozila na elementu saobraćaja.
minimumFlightLevel
Najmanje dopušten nivo leta za vozilo na elementu saobraćaja.
7.4. Mreža zračnog saobraćaja
7.4.1. Tipa prostornog objekta Sljedeće se tipa prostornog objekta upotrebljavaju za razmjenu i klasifikaciju prostornih objekata koji se odnose na mrežu vazdušnog saobraćaja:
područje aerodroma;
kategorija aerodroma;
čvor aerodroma;
tip aerodroma;
vazdušna dionica;
niz vazdušnih dionica;
vazdušni čvor;
vazdušna ruta;
dionica vazdušne rute;
područje vazdušnog prostora;
područje ćelije;
stanje vazdušnog objekta;
određena tačka;
element dužine;
element širine;
(nadmorska) visina uzletišta;
postupak instrumentalnog prilaza;
donja granica (nadmorske) visine;
pomoć pri navigaciji;
dionica postupanja;
područje uzletno-sletne staze;
tačka središnje linije uzletno-sletne staze;
standardni instrumentalni dolazak;
standardni instrumentalni odlazak;
sastav površine;
površina vozne (rulne) staze;
površina slijetanja i uzlijetanja;
gornja granica nadmorske visine; i ograničenje upotrebe.
7.4.1.1. Područje aerodroma (AerodromeArea) Određeno područje na kopnu ili vodi (uključujući sve građevine, instalacije i opremu) koje je djelomično ili u cijelosti namijenjeno dolasku i odlasku aviona/helikoptera i njihovo kretanju po tlu.
Područje aerodroma je podtip tipa TransportArea.
7.4.1.2. Kategorija aerodroma (AerodromeCategory) Kategorija aerodroma koja se odnosi na opseg i važnost usluga vazdušnog saobraćaja koje se pružaju od aerodroma i do aerodroma. Kategorija aerodroma je podtip tipa TransportProperty.
Atributi tipa prostornog objekta AerodromeCategory
Atribut
Definicija
Tip podatka
Voidability
aerodromeCategory
Vrijednost koja pokazuje kategoriju aerodroma.
AerodromeCategoryValue
Ograničenja tipa prostornog objekta AerodromeCategory Ovo se svojstvo odnosi samo na prostorni objekat koji je čvor aerodroma ili područje aerodroma.
7.4.1.3. Čvor aerodroma (AerodromeNode) Čvor na referentnoj tački aerodroma vazdušne luke/heliodroma koji se koristi za njegov pojednostavljen prikaz.
Čvor aerodroma je podtip tipa AirNode.
Atributi tipa prostornog objekta AerodromeNode
Atribut
Definicija
Tip podatka
Voidability
designatorIATA
Troslovni dezignator IATA za aerodrom (vazdušnu luku/heliodrom).
CharacterString voidable
locationIndicatorICAO
Četvoroslovna oznaka lokacije za aerodrom (vazdušnu luku/heliodrom) - ICAO.
CharacterString voidable
Asocijacijske uloge tipa prostornog objekta AerodromeNode
Asocijacijska
uloga
Definicija
Tip podatka
Voidability
controlTowers
Niz kontrolnih tornjeva koji pripadaju aerodromu
(vazdušnoj luci/heliodromu).
Tip koja se definiše u oblasti prostornih
podataka Buildings.
voidable
7.4.1.4. Tip aerodroma (AerodromeType) Oznaka za tip aerodroma.
Tip aerodroma je podtip tipa TransportProperty.
Atributi tipa prostornog objekta AerodromeType
Atribut
Definicija
Tip podatka
Voidability
aerodromeType
Tip aerodroma.
AerodromeTypeValue
Ograničenja tipa prostornog objekta AerodromeType Ovo se svojstvo odnosi samo na prostorni objekat koji je čvor aerodroma ili područje aerodroma.
7.4.1.5. Vazdušna dionica (Vazdušni saobraćajni pravac) (AirLink) Linijski prostorni objekat koji opisuje geometriju i povezanost vazdušne mreže između dvije tačke na mreži.
Vazdušna dionica je podtip tipa TransportLink.
Riječ je o apstraktnom tipu .
7.4.1.6. Niz vazdušnih dionica (vazdušnih saobraćajnih pravaca) (AirLinkSequence) Linijski prostorni objekt, koji se sastoji od uređene zbirke vazdušnih dionica (vazdušnih saobraćajnih pravaca), koji prikazuje neprekidni nerazgranati put na vazdušnoj mreži.
Niz vazdušnih dionica je podtip tipa TransportLinkSequence.
7.4.1.7. Vazdušni čvor (AirNode) Čvor koje se pojavljuje u vazdušnoj mreži.
Vazdušni čvor je podtip tipa TransportNode.
Riječ je o apstraktnom tipu.
Atributi tipa prostornog objekta AirNode
Atribut
Definicija
Tip podatka
Voidability
significantPoint
Atribut koji pokazuje je li vazdušni čvor važna tačka ili nije.
Boolean
7.4.1.8. Vazdušna ruta (AirRoute) Određena maršuta od završetka uzlijetanja i faze početnog polijetanja do početka faze približavanja i slijetanja namijenjena usmjeravanju saobraćaja koje je potrebno zbog osiguranja službe vazdušnog saobraćaja.
Vazdušna ruta je podtip tipa TransportLinkSet.
Atributi tipa prostornog objekta AirRoute
Atribut
Definicija
Tip podatka
Voidability
airRouteType
Klasifikacija ruta.
AirRouteTypeValue
voidable
designator
Kod ili dezignator vazdušne rute.
CharacterString
voidable
7.4.1.9. Dionica vazdušne rute (AirRouteLink) Dio rute koji se obično leti bez međuslijetanja, koji određuju dvije uzastopne važne tačke.
Dionica vazdušne rute je podtip tipa AirLink.
Atributi tipa prostornog objekta AirRouteLink
Atribut
Definicija
Tip podatka
Voidability
airRouteLinkClass
Razred ili Tip dionice vazdušne rute.
AirRouteLinkClassValue
voidable
7.4.1.10. Područje vazdušnog prostora (AirspaceArea) Definisani opseg vazdušnog prostora koji je opisan kao horizontalna projekcija s vertikalnim granicama.
Područje vazdušnog prostora je podtip tipa TransportArea.
Atributi tipa prostornog objekta AirspaceArea
Atribut
Definicija
Tip podatka
Voidability
AirspaceAreaType Kod koji pokazuje opštu strukturu karakteristika pojedinog vazdušnog prostora.
AirspaceAreaTypeValue
7.4.1.11. Područje stanice (ApronArea) Tačno određeno područje kopnenog aerodroma/heliodroma koje je namijenjeno ukrcavanju i iskrcavanju putnika, utovaru i istovaru pošte ili tereta, punjenju goriva, parkiranju ili održavanju.
Područje stanice je podtip tipa TransportArea.
7.4.1.12. Stanje vazdušnog objekta (ConditionOfAirFacility) Stanje vazdušnog elementa saobraćajne mreže obzirom na njegovu dovršenost i upotrebu.
Stanje vazdušnog objekta je podtip tipa ConditionOfFacility.
Ograničenja tipa prostornog objekta ConditionOfAirFacility Ovo se svojstvo može odnositi samo na prostorni objekat koji je čvor aerodroma, područje aerodroma ili područje poletno-sletne staze.
7.4.1.13. Određena tačka (DesignatedPoint) Geografska lokacija koja nije označena mjestom radionavigacionog uređaja i koja se upotrebljava za određivanje rute ATS, putanje leta aviona ili u druge navigacijske svrhe ili svrhe ATS-a.
Ova je Tip podtip tipa AirNode.
Atributi tipa prostornog objekta DesignatedPoint
Atribut
Definicija
Tip podatka
Voidability
designator
Kodirani dezignator tačke.
CharacterString
voidable
7.4.1.14. Element dužine (ElementLength) Fizička dužina elementa.
Element dužine je podtip tipa TransportProperty.
Atributi tipa prostornog objekta ElementLength
Atribut
Definicija
Tip podatka
Voidability
length
Fizička dužina elementa.
Measure
Ograničenja tipa prostornog objekta ElementLength Ovo se svojstvo može odnositi samo na prostorni objekat koji je područje uzletno-sletne staze, područje vozne staze ili područje slijetanja i uzlijetanja.
7.4.1.15. Element širine (ElementWidth) Fizička širina elementa.
Element širine je podtip tipa TransportProperty.
Atributi tipa prostornog objekta ElementWidth
Atribut
Definicija
Tip podatka
Voidability
width
Fizička širina elementa.
Measure
Ograničenja tipa prostornog objekta ElementWidth Ovo se svojstvo može odnositi samo na prostorni objekat koji je područje uzletno-sletne staze, područje vozne staze ili područje slijetanja i uzlijetanja.
7.4.1.16. Nadmorska visina aerodroma (FieldElevation) Nadmorska visina aerodroma kao vertikalna udaljenost između najviše tačke pristanišnog područja aerodroma i srednje visine morskog nivoa.
Nadmorska visina aerodroma je podtip tipa TransportProperty.
Atributi tipa prostornog objekta FieldElevation
Atribut
Definicija
Tip podatka
Voidability
altitude
Vrijednost nadmorske visine aerodroma.
Measure
Ograničenja tipa prostornog objekta FieldElevation Ovo se svojstvo može odnositi samo na prostorni objekat koji je čvor aerodroma ili područje aerodroma.
7.4.1.17. Postupak instrumentalnog prilaza (InstrumentApproachProcedure) Niz unaprijed određenih manevara obzirom na vazduhoplovne instrumente s posebnom zaštitom pred preprekama od početnog položaja prilaza ili, kad je primjenjivo, od početka definisane rute dolaska do tačke iz koje je moguće izvršiti slijetanje, pa ako slijetanje nije dovršeno do položaja gdje važe kriterijumi za čekanje ili kriterijumi za visinu barijera na putu slijetanja.
Postupak instrumentalnog prilaza je podtip tipa ProcedureLink.
7.4.1.18. Donja granica (nadmorske) visine (LowerAltitudeLimit) Nadmorska visina koja određuje donju granicu objekta u mreži vazdušnog saobraćaja.
Donja granica je podtip tipa TransportProperty.
Atributi tipa prostornog objekta LowerAltitudeLimit
Atribut
Definicija
Tip podatka
Voidability
altitude
Vrijednost granice nadmorske visine.
Measure
Ograničenja tipa prostornog objekta LowerAltitudeLimit Ovo se svojstvo može odnositi samo na prostorni objekat koji je dionica vazdušne rute ili područje vazdušnog prostora.
7.4.1.19. Pomoć pri navigaciji (Navaid) Jedan ili više sistema za pomoć pri navigaciji koji osiguravaju usluge navigacione službe.
Pomoć pri navigaciji je podtip tipa AirNode.
Atributi tipa prostornog objekta Navaid
Atribut
Definicija
Tip podatka
Voidability
designator
Identifikator sistema za pomoć pri navigaciji.
CharacterString
voidable
navaidType
Tip pomoći pri navigaciji.
NavaidTypeValue
voidable
7.4.1.20. Dionica postupanja (ProcedureLink) Niz unaprijed određenih manevara s određenom zaštitom protiv barijera.
Dionica postupanja je podtip tipa AirLink.
7.4.1.21. Područje poletno sletne staze (RunwayArea) Tačno određeno pravougaono područje na kopnenom aerodromu/heliodromu pripremljeno za slijetanje i uzlijetanje aviona.
Područje poletno sletne staze je podtip tipa TransportArea.
Atributi tipa prostornog objekta RunwayArea
Atribut
Definicija
Tip podatka
Voidability
designator
Puni tekstualni dezignator uzletno-sletne staze, koja se upotrebljava za njeno jedinstveno
označavanje na aerodromu/heliodromu koji ima više od jedne uzletno-sletne staze.
CharacterString
voidable
runwayType Tip uzletno sletne staze, tj. uzletno-sletna staza za avione ili područje konačnog pristupa i
uzlijetanja (FATO) za helikoptere.
RunwayTypeValue voidable
7.4.1.22. Tačka središnje linije uzletno-sletne staze (RunwayCentrelinePoint) Operativno važan položaj na središnjoj liniji u smjeru uzletno-sletne staze.
Tačka središnje linije uzletno-sletne staze je podtip tipa AirNode.
Atributi tipa prostornog objekta RunwayCentrelinePoint
Atribut
Definicija
Tip podatka
Voidability
pointRole
Uloga tačke duž središnje linije u smjeru uzletno-sletne staze.
PointRoleValue
7.4.1.23. Standardni instrumentalni dolazak (StandardInstrumentArrival) Tačno određena ruta dolaska u skladu s pravilom instrumentalnog letenja (instrument flight rule, IFR) koji važnu tačku, obično rutu ATS, povezuje s tačkom od koje može započeti objavljeni postupak instrumentalnog prilaza.
Ova je Tip podtip tipa ProcedureLink.
Atributi tipa prostornog objekta StandardInstrumentArrival
Atribut
Definicija
Tip podatka
Voidability
designator
Tekstualni dezignator standardnog instrumentalnog dolaska.
CharacterString
voidable
7.4.1.24. Standardni instrumentalni odlazak (StandardInstrumentDeparture) Tačno određena ruta odlaska prema pravilima instrumentalnog letenja (IFR) koja povezuje aerodrome ili pojedinačnu uzletno sletnu stazu aerodroma s važnom tačkom koja je obično na tačno određenoj ruti ATS gdje počinje en-route faza leta.
Standardni instrumentalni odlazak je podtip tipa ProcedureLink.
Atributi tipa prostornog objekta StandardInstrumentDeparture
Atribut
Definicija
Tip podatka
Voidability
designator
Puni tekstualni dezignator standardnog instrumentalnog odlaska.
CharacterString
voidable
7.4.1.25. Sastav površine (SurfaceComposition) Sastav površine na aerodromu/heliodromu.
Sastav površine je podtip tipa TransportProperty.
Atributi tipa prostornog objekta SurfaceComposition
Atribut
Definicija
Tip podatka
Voidability
surfaceComposition
Oznaka za sastav površine na aerodromu/heliodromu.
SurfaceCompositionValue
Ograničenja tipa prostornog objekta SurfaceComposition Ovo se svojstvo može odnositi samo na prostorni objekat koji je područje uzletno sletne staze, područje vozne staze, područje stajališta ili područje slijetanja i uzlijetanja.
7.4.1.26. Područje vozne (rulne) staze (TaxiwayArea) Tačno određeni put na aerodromu/heliodromu namijenjen vožnji avionom/helikopterom i povezivanju jednog dijela aerodroma s drugim. Područje vozne (rulne) staze je podtip tipa TransportArea.
Atributi tipa prostornog objekta TaxiwayArea
Atribut
Definicija
Tip podatka
Voidability
designator
Tekstualni dezignator vozne (rulne) staze.
CharacterString
voidable
7.4.1.27. Područje slijetanja i uzlijetanja (TouchDownLiftOff) Učvršćeno područje na koje helikopter može sletjeti ili s kojeg može uzletjeti.
Područje slijetanja i uzlijetanja je podtip tipa AirNode.
Atributi tipa prostornog objekta TouchDownLiftOff
Atribut
Definicija
Tip podatka
Voidability
designator
Tekstualni dezignator područja slijetanja i uzlijetanja.
CharacterString
voidable 7.4.1.28. Gornja granica nadmorske visine (UpperAltitudeLimit) Nadmorska visina koja definiše gornju granicu objekta na mreži vazdušnog saobraćaja.
Gornja granica nadmorske visine je podtip tipa TransportProperty.
Atributi tipa prostornog objekta UpperAltitudeLimit
Atribut
Definicija
Tip podatka
Voidability
altitude
Vrijednost granice nadmorske visine.
Measure
Ograničenja tipa prostornog objekta UpperAltitudeLimit Ovo se svojstvo može odnositi samo na prostorni objekat koji je dionica vazdušne rute ili područje vazdušnog prostora.
7.4.1.29. Ograničenje upotrebe (UseRestriction) Ograničenja uporabe objekta vazdušne mreže.
Ograničenje upotrebe je podtip tipa TransportProperty.
Atributi tipa prostornog objekta UseRestriction
Atribut
Definicija
Tip podatka
Voidability
restriction
Tip ograničenja upotrebe objekta vazdušne mreže.
AirUseRestrictionValue
Ograničenja tipa prostornog objekta UseRestriction Ovo se svojstvo može odnositi samo na prostorni objekat koji je vazdušna ruta, vazdušna dionica (ili posebna vazdušna dionica), vazdušni čvor (ili posebni vazdušn čvor) ili područje aerodroma.
7.4.2. Popisi kodova (šifrarnici)
7.4.2.1. Kategorija aerodroma (AerodromeCategoryValue) Moguće kategorije aerodroma koje se odnose na područje primjene i važnost usluga vazdušnog saobraćaja koje nudi aerodrom ili koje se nude aerodromu.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova AerodromeCategoryValue
Vrijednost
Definicija
domesticNational
Aerodrom koji pruža usluge domaćeg nacionalnog vazdušnog saobraćaja.
domesticRegional
Aerodrom koji pruža usluge domaćeg regionalnog vazdušnog saobraćaja.
international
Aerodrom koji pruža usluge međunarodnog vazdušnog saobraćaja.
7.4.2.2. Tip aerodroma (AerodromeTypeValue) Oznaka koja određuje li pojava određenog entiteta aerodrom ili heliodrom.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova AerodromeTypeValue
Vrijednost
Definicija
aerodromeHeliport
Aerodrom sa pristanišnim područjem helidroma.
aerodromeOnly
Samo aerodrom.
heliportOnly
Samo helidrom.
landingSite
Mjesto za slijetanje.
7.4.2.3. Klasa dionice vazdušne rute (AirRouteLinkClassValue) Tip ruta s navigacionog gledišta.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova AirRouteLinkClassValue
Vrijednost
Definicija
conventional Konvencionalni vodni put: Vazdušna ruta koja za usluge vazdušnog saobraćaja ne koristi ni Area Navigation ni navigaciju
TACAN.
RNAV
Area Navigation Route: Vazdušna ruta koja za usluge vazdušnog saobraćaja koristi Area Navigation (RNAV).
TACAN
TACAN Route: Vazdušna ruta koja za usluge vazdušnog saobraćaja koristi TACAN Navigation.
7.4.2.4. Tip vazdušne rute (AirRouteTypeValue) Klasifikacija ruta kao ATS rute ili sjevernoatlantske rute (North Atlantic Tracks).
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova AirRouteTypeValue
Vrijednost
Definicija
ATS
Ruta ATS kako je opisana u Prilogu 11. ICAO-u.
NAT
Sjevernoatlantska ruta (dio sistema Organized Track System).
7.4.2.5. Ograničenje vazdušne upotrebe (AirUseRestrictionValue) Ograničenje upotrebe za objekat vazdušne mreže.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova AirUseRestrictionValue
Vrijednost
Definicija
reservedForMilitary
Objekat vazdušne mreže namijenjen je isključivo za vojnu upotrebu.
temporalRestrictions
Vremenska ograničenja primjenjuju se na upotrebu objekta vazdušne mreže.
7.4.2.6. Tip područja vazdušnog prostora (AirspaceAreaTypeValue) Odobrene tipa vazdušnog prostora.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova AirspaceAreaTypeValue
Vrijednost
Definicija
ATZ
Zona saobraćaja vazdušne luke (Airport Traffic Zone). Vazdušni prostor određenih dimenzija koji je uspostavljen oko vazdušne
luke u svrhu zaštite saobraćaja u vazdušnoj luci.
CTA
Kontrolisano područje (Control area). Kontrolisani vazdušni prostor koji se prostire uvis od utvrđene granice iznad površine
zemlje.
CTR
Kontrolisana zona (Control zone). Kontrolisani vazdušni prostor koji se prostire uvis od zemljine površine do određene gornje
granice.
D
Opasno područje (Danger area). Vazdušni prostor određenih dimenzija unutar kojeg se u određenom vremenu mogu odvijati
aktivnosti opasne za letenje aviona.
FIR
Područje informacija o letenju (Flight information region). Vazdušni prostor određenih dimenzija u kome se pružaju usluge
informacija o letenju i obavlja alarmiranje. Može se, primjera radi, koristiti ako više od jedne jedinice pruža usluge.
P
Zabranjeno područje (Prohibited area). Vazdušni prostor određenih dimenzija smješten iznad kopnenih područja ili
teritorijalnih voda države unutar kojeg je letenje avionaa zabranjeno.
R
Uslovno zabranjeno područje (Restricted area). Vazdušni prostor određenih dimenzija koji je smješten iznad kopnenih područja
ili teritorijalnih voda države unutar koga je letenje aviona ograničeno u skladu s određenim posebnim uslovima.
TMA
Finalno kontrolisano područje (Terminal control area). Kontrolisano područje koje se u načelu utvrđuje oko mjesta slijevanja
ruta ATS u okolini jednog ili više većih aerodroma. Uglavnom se koristi u Evropi u okviru koncepta fleksibilne upotrebe
vazdušnog prostora.
UIR
Područje informacija o letenju u gornjem vazdušnom prostoru, UIR (Upper flight information region (UIR)). Gornji vazdušni
prostor određenih dimenzija u kojem se pružaju usluge informacija o letenju i obavlja alarmiranje. Svaka država daje svoju
definiciju gornjeg vazdušnog prostora.
7.4.2.7. Tip pomoći pri navigaciji (NavaidTypeValue) Tipa pomoći pri navigaciji.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova NavaidTypeValue
Vrijednost
Definicija
DME
Oprema za mjerenje udaljenosti.
ILS
Sistem za slijetanje pomoću instrumenata.
ILS-DME
ILS s DME-om.
LOC
Lokalizator.
LOC-DME
LOC s DME-om.
MKR
Marker-radiofar.
MLS
Mikrotalasni sistem za slijetanje.
MLS-DME
MLS s DME-om.
NDB
Neusmjereni radiofar.
NDB-DME
NDB s DME-om.
NDB-MKR
Neusmjereni radiofar i marker-radiofar.
TACAN
Taktička vazdušna navigacija.
TLS
Transponderski sistem za slijetanje.
VOR
VHF svesmjerni radiofar.
VOR-DME
VOR s DME-om.
VORTAC
VOR s TACAN-om.
7.4.2.8. Uloga tačke (PointRoleValue) Uloga tačke središnje linije uzletno-sletne staze.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova PointRoleValue
Vrijednost
Definicija
end
Fizički završetak uzletno-sletne staze.
mid
Srednja tačka uzletno-sletne staze.
start
Fizički početak uzletno-sletne staze.
threshold
Početak dijela uzletno-sletne staze koji se koristi za slijetanje.
7.4.2.9. Tip uzletno-sletne staze (RunwayTypeValue) Oznaka kojom se razlikuju uzletno-sletne staze za avione i FATO za helikoptere.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova RunwayTypeValue
Vrijednost
Definicija
FATO
Područje konačnog prilaza i uzlijetanja za helikoptere.
runway
Uzletno-sletna staza za avionee.
7.4.2.10. Sastav površine (SurfaceCompositionValue) Oznaka za sastav površine.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova SurfaceCompositionValue
Vrijednost
Definicija
asphalt
Površina je asfaltna.
concrete
Površina je betonska.
grass
Površina je travnata.
7.5. Mreža saobraćaja žičara
7.5.1. Tipa prostornog objekta Sljedeće tipa prostornog objekta upotrebljavaju se za razmjenu i klasifikaciju prostornih objekata koji se odnose na mrežu saobraćaja žičara: - dionica žičara;
- niz dionica žičara;
- skup dionica žičara; i - čvor žičara.
7.5.1.1. Dionica žičara (CablewayLink) Linijski prostorni objekat koji opisuje geometriju i povezanost mreže žičara između dvije tačke na saobraćajnoj mreži žičara.
Dionica žičara je Tip podtip tipa TransportLink.
Atributi tipa prostornog objekta CablewayLink
Atribut
Definicija
Tip podatka
Voidability
cablewayType
Tip prevoza žičarom.
CablewayTypeValue
voidable
7.5.1.2. Niz dionica žičara (CablewayLinkSequence) Uređena zbirka niza dionica žičara koju obilježava jedan ili više tematskih identifikatora i/ili svojstava.
Niz dionica žičara je podtip tipa TransportLinkSequence.
7.5.1.3. Skup dionica žičara (CablewayLinkSet) Uređena zbirka skupa dionica žičara i/ili pojedinačnih dionica žičara koja ima posebnu funkciju ili važnost na saobraćajnoj mreži žičara. Ova je Tip podtip tipa TransportLinkSet.
7.5.1.4. Čvor žičare (CablewayNode) Tačkasti prostorni objekat koji se upotrebljava za prikazivanje povezanosti između dvije uzastopne dionice žičara.
Čvor žičare je podtip tipa TransportNode.
7.5.2. Popisi kodova
7.5.2.1. Tip žičare (CablewayTypeValue) Moguće tipa prevoza žičarom (cableway transport).
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova CablewayTypeValue
Vrijednost
Definicija
cabinCableCar Prevoz žičarom čija se vozila sastoje od viseće kabine za prevoz grupe ljudi i/ili robe s jednog mjesta na drugo.
chairLift
Prevoz žičarom čija se vozila sastoje od visećih sjedišta za prevoz pojedinaca ili grupe ljudi s jednog mjesta na drugo preko
čeličnog kabla koji je rastegnut između dvije tačke.
skiTow
Prevoz žičarom za povlačenje skijaša i surfera na snijegu uzbrdo.
7.6. Željeznička saobraćajna mreža
7.6.1. Tipa prostornog objekta Sljedeće tipa prostornog objekta upotrebljavaju se za razmjenu i klasifikaciju prostornih objekata koji se odnose na željezničku saobraćajnu mrežu:
7.6.1.1. Projektovana brzina (DesignSpeed) - projektovana brzina;
- nominalna širina;
- broj kolosijeka;
- područje željeznice;
- elektrifikacija željeznice;
- željeznička pruga;
- željeznička dionica;
- niz željezničkih dionica;
- željeznički čvor;
- područje željezničke stanice;
- oznaka željezničke stanice;
- čvor željezničke stanice;
- Tip željeznice;
- upotreba željeznice;
- područje ranžirne stanice; i - čvor ranžirne stanice.
Specifikacija najveće brzine za koju je željeznička pruga projektovana.
Projektovana brzina je podtip tipa TransportProperty.
Atributi tipa prostornog objekta DesignSpeed
Atribut
Definicija
Tip podatka
Voidability
speed
Specifikacija najveće brzine za koju je željeznička pruga projektovana.
Velocity
Ograničenja tipa prostornog objekta DesignSpeed Ovo se svojstvo može odnositi samo na prostorni objekat koji je dio željezničke saobraćajne mreže.
7.6.1.2. Nominalna širina kolosijeka (NominalTrackGauge) Nominalna udaljenost između dvije spoljne šine željezničkog kolosijeka.
Nominalna širina kolosijeka je podtip tipa TransportProperty.
Atributi tipa prostornog objekta NominalTrackGauge
Atribut
Definicija
Tip podatka
Voidability
nominalGauge
Jedinstvena vrijednost koja označava širinu kolosijeka.
Measure
voidable
nominalGaugeCategory Širina kolosijeka izražena kao nejasna kategorija s obzirom na standardnu
evropsku širinu kolosijeka.
TrackGaugeCategoryValue voidable
Ograničenja tipa prostornog objekta NominalTrackGauge Ovo se svojstvo može odnositi samo na prostorni objekat koji je dio željezničke saobraćaje mreže.
7.6.1.3. Broj kolosijeka (NumberOfTracks) Broj kolosijeka za željezničkom odsjeku(stretch).
Broj kolosijeka je podtip tipa TransportProperty.
Atributi tipa prostornog objekta NumberOfTracks
Atribut
Definicija
Tip podatka
Voidability
minMaxNumberOfTracks
Pokazuje predstavlja li broj kolosijeka najmanju ili najveću vrijednost.
MinMaxTrackValue
voidable
numberOfTracks
Broj postojećih kolosijeka.
Integer
Ograničenja tipa prostornog objekta NumberOfTracks To se svojstvo može odnositi samo na prostorni objekat koji je dio željezničke saobraćajne mreže.
7.6.1.4. Područje željeznice (RailwayArea) Površina koju zauzima željeznički kolosijek uključujući teret (ballast).
Područje željeznice je podtip tipa TransportArea.
7.6.1.5. Elektrifikacija željeznice (RailwayElectrification) Pokazatelj ima li željeznica električni sistem za napajanje vozila koja se po njoj kreću.
Elektrifikacija željeznice je podtip tipa TransportProperty.
Atributi tipa prostornog objekta RailwayElectrification
Atribut
Definicija
Tip podatka
Voidability
electrified
Pokazuje ima li željeznica električni sistem za napajanje vozila koja se po njoj kreću.
Boolean
Ograničenja tipa prostornog objekta RailwayElectrification To se svojstvo može odnositi samo na prostorni objekat koji je dio željezničke saobraćajne mreže.
7.6.1.6. Željeznička pruga (RailwayLine) Skup niza željezničkih dionica i/ili pojedinačnih željezničkih dionica koje obilježava jedan ili više tematskih identifikatora i/ili svojstava. Željeznička pruga je podtip tipa TransportLinkSet.
Atributi tipa prostornog objekta RailwayLine
Atribut
Definicija
Tip podatka
Voidability
railwayLineCode
Specifična oznaka koja se dodjeljuje željezničkoj pruzi u državi.
CharacterString
voidable
7.6.1.7. Željeznička dionica (RailwayLink) Linijski prostorni objekt koji opisuje geometriju i povezanost željezničke mreže između dvije tačke na mreži.
Željeznička dionica je podtip tipa TransportLink.
Atributi tipa prostornog objekta RailwayLink
Atribut
Definicija
Tip podatka Voidability
fictitious Željeznička dionica ne prikazuje stvarni i postojeći željeznički kolosijek nego njegovu fiktivnu putanju. Boolean
voidable
7.6.1.8. Niz željezničkih dionica (RailwayLinkSequence) Linijski prostorni objekat, sastavljen od uređene zbirke željezničkih dionica, koji prikazuje neprekidnu nerazgranatu trasu na željezničkoj mreži. Element ima određeni početak i kraj i svaki se položaj na nizu željezničkih dionica može odrediti samo jednim parametrom, npr. dužinom. Opisuje element željezničke mreže, koji obilježava jedan ili više tematskih identifikatora i/ili svojstava.
Niz željezničkih dionica je podtip tipa TransportLinkSequence.
7.6.1.9. Željeznički čvor (RailwayNode) Tačkasti prostorni objekat koji prikazuje važnu tačku duž željezničke mreže ili određuje presjek željezničkih kolosijeka koji se upotrebljavaju za opis njegove povezivosti.
Željeznički čvor je podtip tipa TransportNode.
Atributi tipa prostornog objekta RailwayNode
Atribut
Definicija
Tip podatka
Voidability
formOfNode
Funkcija željezničkog čvora na željezničkoj mreži.
FormOfRailwayNodeValue
voidable
7.6.1.10. Područje željezničke stanice (RailwayStationArea) Površinski prostorni objekat koji se upotrebljava za prikaz topoloških granica objekata na željezničkim stanicama (zgrade, željezničke stanice, instalacije i oprema) namijenjen djelatnostima željezničke stanice.
Područje željezničke stanice je podtip tipa TransportArea.
7.6.1.11. Oznaka željezničke stanice (RailwayStationCode) Jedinstvena oznaka koja se dodjeljuje željezničkoj stanici Oznaka željezničke stanice je podtip tipa TransportProperty.
Atributi tipa prostornog objekta RailwayStationCode
Atribut
Definicija
Tip podatka
Voidability
stationCode
Jedinstvena oznaka koja se dodjeljuje željezničkoj stanici.
CharacterString
Ograničenja tipa prostornog objekta RailwayStationCode To se svojstvo može odnositi samo na prostorni objekat koji je dio željezničke saobraćajne mreže.
7.6.1.12. Čvor željezničke stanice (RailwayStationNode) Željeznički čvor koji prikazuje lokaciju željezničke stanice duž željezničke mreže.
Čvor željezničke stanice je podtip tipa RailwayNode.
Atributi tipa prostornog objekta RailwayStationNode
Atribut
Definicija
Tip podatka
Voidability
numberOfPlatforms
Vrijednost koja prikazuje broj raspoloživih perona na željezničkoj stanici.
Integer
voidable
Ograničenja tipa prostornog objekta RailwayStationNode Za čvor željezničke stanice vrijednost atributa "formOfNode" mora uvijek biti "RailwayStop".
7.6.1.13. Tip željeznice (RailwayType) Tip željezničkog prevoza za koji je pruga projektovana.
Tip željeznice je podtip tipa TransportProperty.
Atributi tipa prostornog objekta RailwayType
Atribut
Definicija
Tip podatka
Voidability
type
Tip željezničkog prevoza za koji je pruga projektovana.
RailwayTypeValue
Ograničenja tipa prostornog objekta RailwayType To se svojstvo može odnositi samo na prostorni objekat koji je dio željezničke saobraćajne mreže.
7.6.1.14. Upotreba željeznice (RailwayUse) Trenutna upotreba željeznice.
Upotreba željeznice je podtip tipa TransportProperty.
Atributi tipa prostornog objekta RailwayUse
Atribut
Definicija
Tip podatka
Voidability
use
Trenutna upotreba željeznice.
RailwayUseValue
Ograničenja tipa prostornog objekta RailwayUse To se svojstvo može odnositi samo na prostorni objekat koji je dio željezničke saobraćajne mreže.
7.6.1.15. Područje ranžirne stanice (RailwayYardArea) Površinski prostorni objekat koji se upotrebljava za prikaz topoloških granica ranžirnog kolodvora.
Područje ranžirne stanice je podtip tipa TransportArea.
7.6.1.16. Čvor ranžirne stanice (RailwayYardNode) Željeznički čvor koji je na području ranžirnog kolodvora.
Ova je Tip podtip tipa RailwayNode.
Ograničenja tipa prostornog objekta RailwayYardNode Za čvor ranžirne stanice vrijednost atributa "formOfNode" mora uvijek biti "RailwayStop".
7.6.2. Enumeracije
7.6.2.1. Najmanji ili najveći broj kolosijeka (MinMaxTrackValue) Vrijednosti za označavanje predstavlja broj kolosijeka najveću, najmanju ili srednju vrijednost.
Vrijednosti dopuštene za enumeraciju MinMaxTrackValue
Vrijednost
Definicija
average
Broj kolosijeka srednja je vrijednost za određeni dio željezničke mreže.
maximum
Broj kolosijeka najveća je vrijednost za određeni dio željezničke mreže.
minimum
Broj kolosijeka najmanja je vrijednost za određeni dio željezničke mreže.
7.6.2.2. Kategorija širine kolosijeka (TrackGaugeCategoryValue) Moguće kategorije željeznica s obzirom na njihovu nominalnu širinu kolosijeka.
Vrijednosti dopuštene za enumeraciju TrackGaugeCategoryValue
Vrijednost
Definicija
broad
Nominalna širina kolosijeka veća je od standardne.
standard
Nominalna širina kolosijeka jednaka je evropskomu standardu (1 435 mm).
narrow
Nominalna širina kolosijeka manja je od standardne.
notApplicable
Definicija nominalne širine kolosijeka ne primjenjuje se za tu tip željezničkog prevoza.
7.6.3. Popisi kodova
7.6.3.1. Oblik željezničkog čvora (FormOfRailwayNodeValue) Moguće funkcije željezničkog čvora na željezničkoj mreži.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova FormOfRailwayNodeValue
Vrijednost
Definicija
junction
Željeznički čvor na kojem željeznička mreža ima mehanizam koji se sastoji od željezničkog kolosijeka s dvije pokretne šine i
obaveznom povezanošću koje vozilu omogućavaju prelaz s jednog kolosijeka na drugi.
levelCrossing Željeznički čvor na kojem željezničku mrežu presijeca put u istoj ravni.
pseudoNode Željeznički čvor koji predstavlja tačku gdje jedan ili više atributa željezničkih dionica povezanih s njom mijenjaju svoju
vrijednost, ili tačku koja je nužna za opis geometrije mreže.
railwayEnd
Samo jedna željeznička dionica povezana je sa željezničkim čvorom. Predstavlja kraj željezničke pruge.
railwayStop
Mjesto u željezničkoj mreži gdje vozovi staju zbog utovara/istovara tereta ili ukrcaja i iskrcaja putnika.
7.6.3.2. Tip željeznice (RailwayTypeValue) Moguće tipa željezničkog prevoza.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova RailwayTypeValue
Vrijednost
Definicija
cogRailway
Željeznički saobraćaj koji vozilima omogućava vožnju strmim padinama i koji se sastoji od željeznice koja ima prugu sa
zupčanim šinama(obično između šina), vozila su opremljena jednim ili više gonjenih ili pogonskih zupčanika koji
zahvataju te zupčane šine.
funicular
Željeznički saobraćaj koji se sastoji od kabla pričvršćenog za vozilo na šinama koje se kreće uz i niz vrlo strmu padinu.
Ako je moguće, vozila koja se penju i spuštaju međusobno djeluju kao protivteža.
magneticLevitation Željeznički saobraćaj koji se bazira na jednoj šini koja služi kao šina za vozilo i njime upravlja pomoću mehanizma
magnetne levitacije.
metro
Sistem gradskog željezničkog saobraćaja koji se koristi u velikim urbanim područjima, ima posebnu šinu koju ne dijeli s
drugim saobraćajnim sisoblastima, obično je na električni pogon, a u nekim slučajevima vozi ispod površine zemlje.
monorail
Željeznički saobraćaj koji se temelji na jednoj šini koja služi i kao jedini nosač i kao šina.
suspendedRail
Željeznički saobraćaj koji se bazira na jednoj šini koja služi i kao jedini nosač i kao šina duž koje se kreće zakačeno
vozilo.
train
Željeznički saobraćaj koji se obično sastoji od dvije uporedne šine po kojima vučno ili pogonsko vozilo vuče niz
međusobno povezanih vozila u svrhu prevoza tereta i putnika iz jednog odredišta na drugo.
tramway
Sistem željezničkog saobraćaja koji se koristi u urbanim područjima koji se često odvija na površinama puteva i dijeli
putni prostor s motornim vozilima i pješacima. Tramvaji su obično na električni pogon.
7.6.3.3. Upotreba željeznice (RailwayUseValue) Moguće upotrebe željeznice.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova RailwayUseValue
Vrijednost
Definicija
cargo
Željeznica se koristi isključivo za prevoz tereta.
carShuttle
Željeznica se koristi isključivo za prevoz automobila.
mixed
Željeznica se koristi za kombinovane namjene. Koristi se za prevoz putnika i tereta.
passengers
Željeznica se koristi isključivo za prevoz putnika.
7.7. Mreža drumslog saobraćaja
7.7.1. Tipa prostornog objekta Sljedeće tipa prostornog objekta upotrebljavaju se za razmjenu i klasifikaciju prostornih objekata koji se odnose na mrežu drumskog saobraćaja:
- evropski put;
- oblik puta;
- funkcionalni razred puta;
- broj saobraćajnih traka;
- put;
- drumsko područje;
- putna dionica;
- niz putnih dionica;
- naziv puta;
- putni čvor;
- odmorište uz put;
- tip odmorišta na putu;
- kategorija putne površine;
- širina puta;
- ograničenje brzine; i - kolovozna traka.
7.7.1.1. Evropski put (cesta) (ERoad) Zbirka niza putnih dionica i pojedinih putnih dionica koja prikazuje rutu koja je dio međunarodne mreže evropskog puta koju obilježava njen broj evropske rute.
Ova je Tip podtip tipa TransportLinkSet.
Atributi tipa prostornog objekta ERoad
Atribut
Definicija
Tip podatka
Voidability
europeanRouteNumber Oznaka rute u međunarodnoj mreži evropskog puta. Oznaka uvijek započinje slovom
"E" nakon čega slijedi jednocifreni, dvocifreni ili trocifreni broj.
CharacterString voidable 7.7.1.2. Oblik puta (FormOfWay) Klasifikacija na osnovu fizičkih svojstava putne dionice.
Oblik puta je podtip tipa TransportProperty.
Atributi tipa prostornog objekta FormOfWay
Atribut
Definicija
Tip podatka
Voidability
formOfWay
Fizički oblik puta.
FormOfWayValue
Ograničenja tipa prostornog objekta FormOfWay To se svojstvo može odnositi samo na prostorni objekat koji je dio drumske saobraćajne mreže.
7.7.1.3. Funkcionalni razred ceste (FunctionalRoadClass) Klasifikacija na temelju važnosti uloge koju put ima u putnoj mreži.
Ova je Tip podtip tipa TransportProperty.
Atributi tipa prostornog objekta FunctionalRoadClass
Atribut
Definicija
Tip podatka
Voidability
functionalClass
Funkcionalni položaj putne dionice u putnoj mreži.
FunctionalRoadClassValue
Ograničenja tipa prostornog objekta FunctionalRoadClass To se svojstvo može odnositi samo na prostorni objekat koji je dio putne prometne mreže.
7.7.1.4. Broj prometnih traka (NumberOfLanes) Broj saobraćajnih traka putnog elementa.
Broj prometnih traka je podtip tipa TransportProperty.
Atributi tipa prostornog objekta NumberOfLanes
Atribut
Definicija
Tip podatka
Voidability
direction
Pokazuje na koji se smjer vožnje odnosi broj saobraćajnih traka.
LinkDirectionValue
voidable
minMaxNumberOfLanes
Pokazuje predstavlja li broj traka najmanju ili najveću vrijednost.
MinMaxLaneValue
voidable
numberOfLanes
Broj saobraćajnih traka.
Integer
Ograničenja tipa prostornog objekta NumberOfLanes To se svojstvo može odnositi samo na prostorni objekat koji je dio putne saobraćajne mreže.
7.7.1.5. Put (Road) Zbirka niza putnih dionica i/ili pojedinih putnih dionica za koje je karakterističan jedan ili više tematskih identifikatora i/ili svojstava. Put je podtip tipa TransportLinkSet.
Atributi tipa prostornog objekta Road
Atribut
Definicija
Tip podatka
Voidability
localRoadCode
Identifikaciona oznaka koju lokalni organ nadležan za puteve dodjeljuje putu.
CharacterString
voidable
nationalRoadCode
Državni broj puta.
CharacterString
voidable
7.7.1.6. Putno područje (RoadArea) Površina koja se proteže do granica puta, uključujući saobraćajne površine i druge dijelove puta.
Putno područje je podtip tipa TransportArea.
7.7.1.7. Putna dionica (RoadLink) Linijski prostorni objekat koji opisuje geometriju i povezivost putne mreže između dvije tačke na mreži. Putne dionice mogu biti staze, biciklističke staze, putevi s jednim kolovoznom trakom, putevi s više kolovoznih traka i fiktivnim putevima (prečicima) preko trgova preko kojih se odvija promet.
Putna dionica je podtip tipa TransportLink.
7.7.1.8. Niz putnih dionica (RoadLinkSequence) Linijski prostorni objekat sastavljen od uređene zbirke putnih dionica koji prikazuje neprekidnu i nerazgranatu trasu na putnoj mreži. Element ima određen početak i kraj i svaki položaj u nizu putnih dionica može se odrediti sa samo jednim parametrom, npr. dužinom. Opisuje element putne mreže, koji obilježava jedan ili više tematskih identifikatora i/ili svojstava.
Niz putnih dionica je podtip tipa TransportLinkSequence.
7.7.1.9. Naziv puta (RoadName) Naziv puta koji mu je dodijelio nadležni organ.
Naziv puta je podtip tipa TransportProperty.
Atributi tipa prostornog objekta RoadName
Atribut
Definicija
Tip podatka
Voidability
name
Naziv puta.
GeographicalName
Ograničenja tipa prostornog objekta RoadName To se svojstvo može odnositi samo na prostorni objekat koji je dio drumske saobraćajne mreže.
7.7.1.10. Putni čvor (RoadNode) Tačkasti prostorni objekat koji se upotrebljava za prikaz povezanosti između dvije putne dionice ili važan prostorni objekat, npr. benzinska pumpa ili kružni tok.
Putni čvor je podtip tipa TransportNode.
Atributi tipa prostornog objekta RoadNode
Atribut
Definicija
Tip podatka
Voidability
formOfRoadNode
Opis funkcije putnog čvora na putnoj saobraćajnoj mreži.
FormOfRoadNode Value
voidable
7.7.1.11. Odmorište uz put (RoadServiceArea) Površina priključena na put i namijenjena pružanju različitih usluga na putu.
Odmorište uz put je podtip tipa TransportArea.
7.7.1.12. Tip usluge uz put (RoadServiceType) Opis tipa odmorišta na putu i raspoloživih usluga.
Tip usluge uz put je podtip tipa TransportProperty.
Atributi tipa prostornog objekta RoadServiceType
Atribut
Definicija
Tip podatka
Voidability
availableFacility
Usluga dostupna na određenom odmorištu uz put.
ServiceFacility Value
type
Tip odmorišta uz put.
RoadServiceType Value
Ograničenja tipa prostornog objekta RoadServiceType Ovo se svojstvo može odnositi samo na prostorni objekat tipa RoadServiceArea ili RoadNode (ako je atribut formOfRoadNode jednak atributu roadServiceArea).
7.7.1.13. Kategorija putne površine (RoadSurfaceCategory) Specifikacija stanja površine priključenog putnog elementa. Pokazuje je li put asfaltiran ili nije.
Kategorija putne površine je podtip tipa TransportProperty.
Atributi tipa prostornog objekta RoadSurfaceCategory
Atribut
Definicija
Tip podatka
Voidability
surfaceCategory
Tip putne površine.
RoadSurfaceCategoryValue
Ograničenja tipa prostornog objekta RoadSurfaceCategory To se svojstvo može odnositi samo na prostorni objekat koji je dio putne saobraćajne mreže.
7.7.1.14. Širina puta (RoadWidth) Širina puta mjerena kao srednja vrijednost.
Širina puta je podtip tipa TransportProperty.
Atributi tipa prostornog objekta RoadWidth
Atribut
Definicija
Tip podatka
Voidability
measuredRoadPart
Pokazuje za koji dio puta važi atribut "width".
RoadPartValue
voidable
width
Vrijednost širine puta.
Measure
Ograničenja tipa prostornog objekta RoadWidth To se svojstvo može odnositi samo na prostorni objekat koji je dio putne saobraćajne mreže.
7.7.1.15. Ograničenje brzine (SpeedLimit) Ograničenje brzine za vozila na putu.
Ograničenje brzine je podtip tipa TransportProperty.
Atributi tipa prostornog objekta SpeedLimit
Atribut
Definicija
Tip podatka
Voidability
areaCondition
Ograničenje brzine zavisi od uslova sredine.
AreaConditionValue
voidable
direction
Pokazuje za koji smjer vožnje važi ograničenje brzine.
LinkDirectionValue
voidable
laneExtension
Broj saobraćajnih traka (uključujući start liniju) za koje važi ograničenje
brzine.
Integer
voidable
speedLimitMinMaxType Pokazuje je li ograničenje brzine najviše ili najmanje i je li preporučeno.
SpeedLimitMinMaxValue speedLimitSource
Izvor ograničenja brzine.
SpeedLimitSourceValue
voidable
speedLimitValue
Vrijednost ograničenja brzine.
Velocity
startLane
Indeks prve trake za koji važi ograničenje brzine. Za države kod kojih se
saobraćaj odvija po desnoj strani, indeks 1 odnosi se na krajnju desnu liniju
i povećava se prema lijevoj liniji; za države kod kojih se saobraćaj odvija po
lijevoj strani, indeks 1 odnosi se na krajnju lijevu liniju i povećava se prema
desnoj liniji
Integer
voidable
validityPeriod
Razdoblje ograničenja brzine.
TM_Period
voidable
vehicleType
Tip vozila za koje važi ograničenje brzine.
VehicleTypeValue
voidable
weatherCondition
Vremenski uslovi od kojih zavisi ograničenje brzine.
WeatherConditionValue voidable
Ograničenja tipa prostornog objekta SpeedLimit To se svojstvo može odnositi samo na prostorni objekat koji je dio drumske saobraćajne mreže.
7.7.1.16. Kolovozne trake (VehicleTrafficArea) Površina koja pokazuje dio puta koji se upotrebljava za uobičajeni saobraćaj vozila.
Kolovozne trake je podtip tipa TransportArea.
7.7.2. Enumeracije
7.7.2.1. Funkcionalni razred puta (FunctionalRoadClassValue) Vrijednosti za funkcionalni razred puta. Klasifikacija se bazira na važnosti uloge koju put ima u putnoj mreži.
Vrijednosti dopuštene za enumeraciju FunctionalRoadClassValue
Vrijednost
Definicija
mainRoad
Najvažniji putevi u određenoj mreži.
firstClass
Drugi najvažniji putevi u određenoj mreži.
secondClass
Treći najvažniji putevi u određenoj mreži.
thirdClass
Četvrti najvažniji putevi u određenoj mreži.
fourthClass
Peti najvažniji putevi u određenoj mreži.
fifthClass
Šesti najvažniji putevi u određenoj mreži.
sixthClass
Sedmi najvažniji putevi u određenoj mreži.
seventhClass
Osmi najvažniji putevi u određenoj mreži.
eighthClass
Deveti najvažniji putevi u određenoj mreži.
ninthClass
Najmanje važni putevi u određenoj mreži.
7.7.2.2. Najmanji ili najveći broj traka (MinMaxLaneValue) Vrijednosti koja pokazuje predstavlja li broj traka najveću, najmanju ili srednju vrijednost.
Vrijednosti dopuštene za enumeraciju MinMaxLaneValue
Vrijednost
Definicija
maximum
Broj traka najveća je vrijednost za određeni dio putne mreže.
minimum
Broj traka najmanja je vrijednost za određeni dio putne mreže.
average
Broj traka srednja je vrijednost za određeni dio putne mreže.
7.7.2.3. Tip ograničenja brzine (SpeedLimitMinMaxValue) Moguće vrijednosti za prikaz tipa ograničenja brzine.
Vrijednosti dopuštene za enumeraciju SpeedLimitMinMaxValue
Vrijednost
Definicija
maximum
Ograničenje brzine najveća je vrijednost.
minimum
Ograničenje brzine najmanja je vrijednost.
recommendedMaximum
Ograničenje brzine preporučena je najveća vrijednost.
recommendedMinimum
Ograničenje brzine preporučena je najmanja vrijednost.
7.7.3. Popisi kodova
7.7.3.1. Lokalni uslovi (AreaConditionValue) Ograničavanje brzine zavisi od područja.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova AreaConditionValue
Vrijednost
Definicija
inNationalPark
Ograničenje brzine u nacionalnom parku.
insideCities
Ograničenje brzine u naseljenim mjestima.
nearRailroadCrossing
Ograničenje brzine u blizini željezničkih prelaza.
nearSchool
Ograničenje brzine u blizini škole.
outsideCities
Ograničenje brzine izvan naseljenih mjesta.
trafficCalmingArea
Ograničenje brzine u području mirnog saobraćaja.
7.7.3.2. Oblik putnog čvora (FormOfRoadNodeValue) Funkcije putnih čvorova.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova FormOfRoadNodeValue
Vrijednost
Definicija
enclosedTrafficArea Putni čvor nalazi se unutar zatvorenog područja saobraćaja i/ili ga predstavlja. Područje saobraćaja je područje koje
nema unutrašnju strukturu pravno definisanih smjerova vožnje. Najmanje dva puta povezana su sa tim područjem.
junction
Putnii čvor gdje se sijeku tri ili više putnih dionica.
levelCrossing
Putni čvor gdje putna mrežu presijeca put u istom nivou.
pseudoNode
Tačno dvije putne dionice povezane su s putnim čvorom.
roadEnd
Samo jedna putna dionica povezana je sa putnim čvorom. Predstavlja završetak puta.
roadServiceArea
Površina priključena na put i namijenjena pružanju različitih usluga na putu.
roundabout
Putni čvor predstavlja ili je dio kružnog toka. Kružni tok je put u obliku prstena gdje je dopušten saobraćaj samo u
jednom smjeru.
trafficSquare
Putni čvor nalazi se unutar trga preko kojeg se odvija saobraćaj i/ili ga predstavlja. Saobraćajni Trg preko kojeg se
odvija saobraćaj je područje (djelomično) okruženo putevima koje se ne koristi za saobraćaj i koje nije kružni tok.
7.7.3.3. Oblik puta (FormOfWayValue) Klasifikacija na temelju fizičkih svojstava putne dionice.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova FormOfWayValue
Vrijednost
Definicija
bicycleRoad
Put namijenjen isključivo biciklima.
dualCarriageway
Put s fizički odvojenom kolovoznom trakom bez obzira na broj saobraćajnih traka, koja nije brzi put niti autoput.
enclosedTrafficArea
Područje koje nema unutrašnju strukturu pravno definisanih smjerova vožnje. Najmanje dva puta povezana su s tim
područjem.
entranceOrExitCarPark Put koji je posebno napravljen za ulaz na parkiralište ili izlaz s parkirališta.
entranceOrExitService Pu koji se koristi samo za ulaz na odmorište ili izlaz s odmorišta.
freeway
Put koji nema ukrštanja s drugim putevima u istom nivou.
motorway
Put na koji se uobičajeno primjenjuju propisi koji se odnose na prilaz i upotrebu. Ima dvije ili više uglavnom fizički
odvojenih kolovoznih traka i nema ukrštanja na istom nivou.
pedestrianZone
Područje s putnom mrežom koje je posebno namijenjeno pješacima.
roundabout
Put u obliku prstena gdje je dopušten saobraćaj samo u jednom smjeru.
serviceRoad
Put koji se proteže uporedo sa putem s relativno visokom funkcijom povezanosti i koja je namijenjena povezivanju
s putevima sa slabom funkcijom povezanosti.
singleCarriageway
Put na kojoj saobraćaj nije odvojen fizičkim objektom.
slipRoad
Put koji je posebno projektovan za ulazak na ili izlazak s drugog puta.
tractorRoad
Uređen put samo za traktorska (poljoprivredno vozilo ili šumska mehanizacija) ili terenska vozila (veće vozilo na
velikim točkovima i pogonom na sva 4 točka).
trafficSquare
Područje (djelomično) okruženo putevima koje se ne koristi za saobraćaj i koje nije kružni tok.
walkway
Put rezervisan za pješake i fizičkom preprekom zatvoren za saobraćaj vozilima.
7.7.3.4. Dio puta (RoadPartValue) Pokazuje za koji dio puta važi vrijednost mjerenja.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova RoadPartValue
Vrijednost
Definicija
carriageway
Dio puta koji je rezervisan za saobraćaj.
pavedSurface
Dio puta koji je asfaltiran.
7.7.3.5. Tip odmorišta uz put (RoadServiceTypeValue) Tipa odmorišta uz put.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova RoadServiceTypeValue
Vrijednost
Definicija
busStation Odmorište uz put je autobusko stajalište.
parking
Odmorište uz put je parkiralište.
restArea
Odmorište uz put je odmorište.
toll
Područje koje pruža usluge naplate putarine kao što su automati za izdavanje kartica za naplatu putarine ili automati za
plaćanje putarine.
7.7.3.6. Kategorija putne površine (RoadSurfaceCategoryValue) Vrijednosti koje pokazuju je li put asfaltiran ili nije.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova RoadSurfaceCategoryValue
Vrijednost
Definicija
paved
Put je asfaltiran.
unpaved
Put nije asfaltiran.
7.7.3.7. Usluge na odmorištu (ServiceFacilityValue) Moguće usluge dostupne na odmorištu uz put.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova ServiceFacilityValue
Vrijednost
Definicija
drinks
Piće je dostupno.
food
Hrana je dostupna.
fuel
Gorivo je dostupno.
picnicArea
Postoji prostor za piknik.
playground
Postoji igralište.
shop
Postoji prodavnica.
toilets
Postoje toaleti.
7.7.3.8. Izvor ograničenja brzine (SpeedLimitSourceValue) Mogući izvori ograničenja brzine.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova SpeedLimitSourceValue
Vrijednost
Definicija
fixedTrafficSign
Izvor je fiksni saobraćajni znak (posebni saobraćajni propis koji važi za područje, eksplicitno ograničenje brzine).
regulation
Izvor je propis (nacionalno zakonodavstvo, pravilo ili "implicitno ograničenje brzine").
variableTrafficSign Izvor je promjenjivi saobraćajni znak.
7.7.3.9. Tip vozila (VehicleTypeValue) Moguće tipa vozila.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova VehicleTypeValue
Vrijednost
Definicija
allVehicle
Svako vozilo, pješaci su isključeni.
bicycle
Vozilo na dva točka s pogonom na pedale.
carWithTrailer
Lični automobil sa prikolicom.
deliveryTruck
Relativno malo teretno vozilo namijenjeno dostavi robe i materijala.
emergencyVehicle
Vozilo za djelovanje u hitnim slučajevima, uključujući (ali ne i ograničavajući se samo na) policijska vozila,
vozila hitne pomoći i vatrogasna vozila.
employeeVehicle
Vozilo kojim upravlja zaposleni organizacije i koje se koristi u skladu s postupcima navedene
organizacije.
facilityVehicle
Vozilo namijenjeno za korišćenje na lokalnom području na privatnom posjedu ili na posjedu s
ograničenim pristupom.
farmVehicle
Vozilo za obavljanje poljoprivrednih djelatnosti.
highOccupancyVehicle
Vozilo s brojem putnika koji je jednak (ili veći od) najmanjeg propisanog broja putnika.
lightRail
Prevozno sredstvo slično vozu koje se koristi u željezničkoj mreži u okviru ograničenog područja.
mailVehicle
Vozilo koje se koristi za prikupljanje, prevoz i dostavu poštanskih pošiljki.
militaryVehicle
Vozilo koje je ovlastilo vojni organ.
moped
Vozilo na dva ili tri točka opremljeno motorom s unutrašnjim sagorijevanjem, koje je manje od 50 cc i
postiže brzinu do 45 km/h (28 mph)
motorcycle
Vozilo na dva ili tri točka opremljeno motorom s unutrašnjim sagorijevanjem, koje je veće od 50 cc i
postiže brzinu veću od 45 km/h (28 mph).
passengerCar
Malo vozilo za privatni prevoz osoba.
pedestrian
Pješak.
privateBus
Vozilo za prevoz većih grupa ljudi, u privatnom vlasništvu ili iznajmljeno.
publicBus
Vozilo za prevoz većih grupa ljudi za koje su karakteristične objavljene rute i redovi vožnje.
residentialVehicle
Vozilo čiji je vlasnik stanovnik (ili posjetilac) određene ulice ili kvarta.
schoolBus
Vozilo koje za potrebe škole prevozi učenike.
snowChainEquippedVehicle
Svako vozilo opremljeno lancima za snijeg.
tanker
Teretno vozilo s više od dvije osovine za prevoz rasutih tečnosti i plinova.
taxi
Vozilo koje se unajmljuje i obično je opremljeno taksimetrom.
transportTruck
Teretno vozilo za prevoz robe na velike udaljenosti.
trolleyBus
Električno prevozno sredstvo slično autobusu.
vehicleForDisabledPerson
Vozilo s vidljivom oznakom da je namijenjeno prevozu invalidnih osoba.
vehicleWithExplosiveLoad
Vozilo za prevoz eksplozivnih materija.
vehicleWithOtherDangerousLoad Vozilo za prevoz opasnih materija, osim eksplozivnih materija ili materija koje mogu zagaditi vodu.
vehicleWithWaterPollutingLoad
Vozilo za prevoz materija koje mogu zagaditi vodu.
7.7.3.10. Vremenski uslovi (WeatherConditionValue) Vrijednosti za prikaz vremenskih uslova koji utiču na ograničenje brzine.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova WeatherConditionValue
Vrijednost
Definicija
fog
Ograničenje brzine važi kad je magla.
ice
Ograničenje brzine važi kad je led.
rain
Ograničenje brzine važi kad pada kiša.
smog
Ograničenje brzine važi kad količina smoga dostigne određenu vrijednost.
snow
Ograničenje brzine važi kad pada snijeg.
7.8. Mreža vodenog saobraćaja
7.8.1. Tipa prostornog objekta Sljedeće tipa prostornog objekta upotrebljavaju se za razmjenu i klasifikaciju prostornih objekata koji se odnose na mrežu vodenog saobraćaja:
- svetionik;
- bova;
- razred CEMT;
- stanje vodenog objekta;
- područje plovnog puta;
- trajektna veza;
- upotreba trajekta;
- unutrašnji plovni put;
- pomorski plovni put;
- pristanišno područje;
- pristanišni čvor;
- ograničenje za plovila;
- šema odvojene plovidbe;
- područje šeme odvojene plovidbe;
- prelaz šeme odvojene plovidbe;
- put šeme odvojene plovidbe;
- kružni tok šeme odvojene plovidbe;
- separator šeme odvojene plovidbe;
- niz vodenih dionica;
- vodeni čvor;
- smjer toka vodenog saobraćaja;
- vodeni put;
- dionica vodenog (plovnog) puta; i - čvor vodenog (plovnog) puta.
7.8.1.1. Svetionik (Beacon) Istaknut posebno izgrađen objekat koji je jasno vidljiv znak na fiksnoj lokaciji kao pomoć pri navigaciji ili za hidrografska mjerenja.
Svetionik je podtip tipa TransportPoint.
7.8.1.2. Bova (Buoy) Plutajući objekat pričvršćen za dno na posebnom mjestu (označenom na mapi) kao pomoć pri navigaciji ili u druge posebne svrhe.
Bova je podtip tipa TransportPoint.
7.8.1.3. Razred CEMT (CEMTClass) Klasifikacija unutrašnjeg plovnog puta prema sistemu Evropske konferencije ministara saobraćaja - CEMT.
Razred CEMT je podtip tipa TransportProperty.
Atributi tipa prostornog objekta CEMTClass
Atribut
Definicija
Vrta podatka
Voidability
CEMTClass Vrijednost koja označava klasifikaciju unutrašjeg plovnog puta prema sistemu Evropske
konferencije ministara saobraćaja - CEMT.
CEMTClassValue
Ograničenja tipa prostornog objekta CEMTClass To se svojstvo može odnositi samo na prostorni objekat koji je dio mreže vodenog saobraćaja
7.8.1.4. Stanje vodenog objekta (ConditionOfWaterFacility) Stanje elementa mreže vodenog saobraćaja u smislu njegove dovršenosti i upotrebe.
Stanje vodenog objekta je podtip tipa ConditionOfFacility.
Ograničenja tipa prostornog objekta ConditionOfWaterFacility To se svojstvo može odnositi samo na prostorni objekat koji je dio mreže vodenog saobraćaja.
7.8.1.5. Područje plovnog puta (FairwayArea) Glavni dio plovnog puta po kojem se najviše putuje.
Područje plovnog puta je podtip tipa TransportArea.
7.8.1.6. Trajektna veza (FerryCrossing) Poseban vodeni put namijenjen lakšem prevozu putnika, vozila i drugog tereta preko vodenog tijela i koje se obično koristi za povezivanje dva ili više čvorova kopnene saobraćajne mreže.
Trajektna veza je podtip tipa Waterway.
7.8.1.7. Uporaba trajekta (FerryUse) Tip prijevoza koja se obavlja trajektnom vezom.
Uporaba trajekta je podtip tipa TransportProperty.
Atributi tipa prostornog objekta FerryUse
Atribut
Definicija
Vrta podatka
Voidability
ferryUse
Vrijednost koja pokazuje tip prevoza koji se obavlja trajektnom vezom.
FerryUseValue
Ograničenja tipa prostornog objekta FerryUse To se svojstvo može odnositi samo na prostorni objekat koji je dio mreže vodenog saobraćaja.
7.8.1.8. Unutrašnji vodni put (InlandWaterway) Vodni put koji je definisan u unutrašnjim kontinentalnim vodama.
Unutrašnji vodni put je podtip tipa Waterway.
7.8.1.9. Pomorski vodeni put (MarineWaterway) Vodni put koji je definisan u morskim vodama.
Pomorski vodeni put je podtip tipa Waterway.
Atributi tipa prostornog objekta MarineWaterway
Atribut
Definicija
Vrta podatka
Voidability
deepWaterRoute
Atribut koji označava je li pomorski vodeni put dubokomorski put.
Boolean
voidable
7.8.1.10. Pristanišno područje (PortArea) Površinski prostorni objekat koji se upotrebljava za prikaz fizičkih granica svih objekata koji su dio kopnene zone morskog ili kontinentalnog pristaništa.
Pristanišno područje je podtip tipa TransportArea.
7.8.1.11. Pristanišni čvor (PortNode) Tačkasti prostorni objekat koji pojednostavljeno prikazuje morsko ili kopneno pristanište, koje se nalazi blizu obale vodenog tijela gdje je pristanište.
Pristanišni čvor je podtip tipa WaterNode.
7.8.1.12. Ograničenje za plovila (RestrictionForWaterVehicles) Ograničenje za plovila na elementu vodenog saobraćaja.
Ograničenje za plovila je podtip tipa RestrictionForVehicles.
Ograničenja tipa prostornog objekta RestrictionForWaterVehicles To se svojstvo može odnositi samo na prostorni objekt koji je dio mreže vodenog saobraćaja.
7.8.1.13. Šema odvojene plovidbe (TrafficSeparationScheme) Šema koja da bi smanjila opasnost od sudara na zakrčenim područjima i/ili područjima koja se spajaju, odvaja saobraćaj koji se kreće u suprotnim smjerovima ili u skoro suprotnim smjerovima.
Riječ je o apstraktnom tipu.
Asocijacijske uloge tipa prostornog objekta TrafficSeparationScheme
Asocijacijska uloga
Definicija
Tip podatka
Voidability
component
Sastavni dio šeme odvojene plovidbe.
TrafficSeparationSchemeArea marineWaterRoute
Zbirka pomorskih plovnih puteva povezanih sa šemom odvojene plovidbe. MarineWaterway
markerBeacon
Označivač koji je dio šeme odvojene plovidbe.
Beacon
markerBuouy
Označivač koji je dio šeme odvojene plovidbe.
Buouy
7.8.1.14. Područje šeme odvojene plovidbe (TrafficSeparationSchemeArea) Površinski prostorni objekat koji je dio šeme odvojene plovidbe.
Područje šeme odvojene plovidbe je podtip tipa TransportArea.
Riječ je o apstraktnom tipu .
7.8.1.15. Prelaz šeme odvojene plovidbe (TrafficSeparationSchemeCrossing) Tačno određeno područje u kojem se plovni putevi ukrštaju.
Prelaz šeme odvojene plovidbe je podtip tipa TrafficSeparationSchemeArea.
7.8.1.16. Put šeme odvojene plovidbe (TrafficSeparationSchemeLane) Područje sa tačno određenim granicama na kojem je uspostavljen jednosmjerni saobraćaj.
Put šeme odvojene plovidbe je podtip tipa TrafficSeparationSchemeArea.
7.8.1.17. Kružni tok šeme odvojene plovidbe (TrafficSeparationSchemeRoundabout) Šema odvojene plovidbe u kojoj se saobraćaj odvija u suprotnomu smjeru od kazaljke na satu oko određene tačke ili zone.
Kružni tok šeme odvojene plovidbe je podtip tipa TrafficSeparationSchemeArea.
7.8.1.18. Separator šeme odvojene plovidbe (TrafficSeparationSchemeSeparator) Zona koja odvaja plovne puteve po kojima brodovi plove u suprotnim smjerovima ili skoro u suprotnim smjerovima; ili odvaja plovne puteve namijenjene posebnim razredima brodova koji plove u istom smjeru.
Separator šeme odvojene plovidbe je podtip tipa TrafficSeparationSchemeArea.
7.8.1.19. Niz vodenih dionica (WaterLinkSequence) Linijski prostorni objekat sastavljen od uređene zbirke vodenih puteva i/ili vodotokova (ako je to potrebno), koji prikazuje neprekidni nerazgranati put u vodenoj mreži.
Niz vodenih dionica je podtip tipa TransportLinkSequence.
7.8.1.20. Vodeni čvor (WaterNode) Tačkasti prostorni objekat koji se upotrebljava za prikaz povezanosti između dvije različite dionice vodenog (plovnog) puta ili između dionice vodenog (plovnog) puta i dionice vodotoka u mreži vodenog saobraćaja.
Vodeni čvor je podtip tipa TransportNode.
Riječ je o apstraktnom tipu .
7.8.1.21. Smjer toka vodenog saobraćaja (WaterTrafficFlowDirection) Pokazuje smjer toka vodnog saobraćaja u odnosu na smjer vektora dionice vodenog saobraćaja.
Smjer toka vodenog saobraćaja je podtip tipa TrafficFlowDirection.
Ograničenja tipa prostornog objekta WaterTrafficFlowDirection To se svojstvo može odnositi samo na prostorni objekat koji je dio mreže vodenog saobraćaja.
7.8.1.22. Plovni put (Waterway) Zbirka redosleda vodenih dionica i/ili pojedinačnih dionica vodotokova (ako je to potrebno) za koje je karakterističan jedan ili više tematskih identifikatora i/ili svojstava, koji formiraju plovne rute na vodenom tijelu (okeani, mora, rijeke, jezera, kanali ili prokopi).
Plovni put je podtip tipa TransportLinkSet.
Riječ je o apstraktnom tipu .
7.8.1.23. Dionica plovnog puta (WaterwayLink) Linijski prostorni objekat koji opisuje geometriju ili povezanost mreže vodenog saobraćaja između dva uzastopna čvora plovnog puta i vodotoka. Pokazuje linijsku dionicu na vodnom tijelu koja se upotrebljava za brodski prijevoz.
Dionica plovnog puta je podtip tipa TransportLink.
7.8.1.24. Čvor plovnog puta (WaterwayNode) Tačkasti prostorni objekat koji se upotrebljava za prikaz povezanosti između dvije različite dionice plovnog puta ili između dionice plovnog puta i dionice vodotoka u mreži vodenog saobraćaja.
Čvor plovnog puta je podtip tipa WaterNode.
Atributi tipa prostornog objekta WaterwayNode
Atribut
Definicija
Tip podatka
Voidability
formOfWaterwayNode
Opis funkcije čvora plovnog puta u mreži vodenog saobraćaja.
FormOfWaterwayNodeValue
voidable
7.8.2. Enumeracije
7.8.2.1. Razred CEMT (CEMTClassValue) Klasifikacija unutrašnjeg plovnog puta u skladu sa CEMT-om.
Vrijednosti dopuštene za enumeraciju CEMTClassValue
Vrijednost
Definicija
I.
Unutrašnji plovni put koji pripada CEMT-razredu I.
II.
Unutrašnji plovni put koji pripada CEMT-razredu II.
III.
Unutrašnji plovni put koji pripada CEMT-razredu III.
IV.
Unutrašnji plovni put koji pripada CEMT-razredu IV.
V.a
Unutrašnji plovni put koji pripada CEMT-razredu V.a
V.b
Unutrašnji plovni put koji pripada CEMT-razredu V.b
VI.a
Unutrašnji plovni put koji pripada CEMT-razredu VI.a
VI.b
Unutrašnji plovni put koji pripada CEMT-razredu VI.b
VI.c
Unutrašnji plovni put koji pripada CEMT-razredu VI.c.
VII.
Unutrašnji plovni put koji pripada CEMT-razredu VII.
7.8.3. Popisi kodova
7.8.3.1. Upotreba trajekta (FerryUseValue) Tip prevoza koji se obavlja trajektom.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova FerryUseValue
Vrijednost
Definicija
cars
Trajekt prevozi automobile.
other
Trajekt prevozi ostala prevozna sredstva, osim putnika, automobila, teretnih vozila ili vozova.
passengers
Trajekt prevozi putnike.
train
Trajekt prevozi voz.
trucks
Trajekt prevozi teretna vozila.
7.8.3.2. Oblik čvora plovnog puta (FormOfWaterwayNodeValue) Funkcija čvora plovnog puta u mreži vodenog saobraćaja.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova FormOfWaterwayNodeValue
Vrijednost
Definicija
junctionFork
Infrastrukturni elementi pri kojima saobraćajni tok jednog plovila presijeca saobraćajni tok drugog plovila ili tačke u kojima
se saobraćajni tokovi plovila dijele ili spajaju.
lockComplex
Brana (Ustav) ili skup ustava namijenjena za podizanje i spuštanje brodova između vodenih pojaseva pri različitim
vodostajima na plovnim putevima rijeka i kanala.
movableBridge Most koji se može podignuti ili rotirati kako bi se omogućio prolazak brodova.
shipLift
Uređaj za prevoz brodova između vodnih tijela na dvije različite nadmorske visine, koji se koristi umjesto ustava na kanalu.
waterTerminal Mjesto gdje se roba pretovaruje.
turningBasin
Mjesto gdje se kanal ili uski plovni put širi kako bi se brodovi mogli okrenuti.
7.9. Zahtjevi vezani za oblast "Saobraćaj"
7.9.1. Usklađenost skupova prostornih podataka
1. Prikaz središnjih linija i čvorova u saobraćajnim mrežama uvijek je u okviru područja prikaza istog objekta.
2. Povezivost saobraćajnih mreža preko državnih granica i, kad je to potrebno, i preko regionalnih granica (i skupova podataka) u
državama uspostavljaju i održavaju odgovarajući nadležni organi, pri čemu upotrebljavaju mehanizme za prekograničnu povezanost koju
osigurava Tip NetworkConnection.
7.9.2. Modeliranje referenca objekta
1. Kad se u podacima saobraćajnih mreža upotrebljava linearno referenciranje, položaj referenciranih svojstava na dionicama i nizu dionica
izražava se kao udaljenost mjerena duž osigurane geometrije osnovnih dionica.
2. Međumodalna veza uvijek se odnosi na dva elementa koji pripadaju različitim mrežama.
7.9.3. Prikaz geometrije
1. Krajevi saobraćajnih dionica povezuju se uvijek kad postoji presjek između pojava u stvarnom svijetu koje prikazuju. Povezivanja se ne
stvaraju na ukrštaju mrežnih elemenata kod kojih nije moguć prelaz od jednog elementa do drugog.
2. U skupu podataka o saobraćajnim mrežama koji sadrži čvorove, ti su čvorovi prisutni samo kad se saobraćajne dionice dodiruju ili
završavaju.
7.9.4. Modeliranje reference objekta Kod vodenih saobraćajnih mreža ponovo se upotrebljava geometrija središnje linije vodene mreže oblasti Hidrografija, ako postoji i ako je to izvodivo. Stoga se objektno referenciranje upotrebljava za povezivanje puta vodenog saobraćaja s postojećom geometrijom vodene mreže u oblasti Hidrografija.
7.9.5. Središnje linije Središnje linije putnih i željezničkih objekata dio su opsega fizičkog objekta stvarnog svijeta koji prikazuju, ako navedena dionica nije označena kao "fictitious".
7.9.6. Osiguranje povezanosti mreže
1. Kad god u saobraćajnoj mreži postoji veza, svi povezani krajevi dionica i neobavezujući čvor koji su dio te veze moraju biti pozicionirani
na udaljenosti koja je manja od tolerancije povezanosti između njih.
2. Krajevi dionice i čvorovi koji nijesu povezani uvijek su odvojeni udaljenošću koja je veća od tolerancije povezivosti.
3. U skupovima podataka koji sadrže saobraćajne dionice i čvorove, relativan položaj čvorova i krajeva dionica mora, obzirom na navedenu
toleranciju povezivosti, odgovarati asocijacijama koje među njima postoje u skupu podataka.
7.10. Slojevi
Slojevi za temu prostornih podataka saobraćajne mreže
Tip sloja
Naziv sloja
Prostorni objekt(i) type(s)
TN.CommonTransportElements.TransportNode
Generički saobraćajni čvor.
TransportNode
TN.CommonTransportElements.TransportLink
Generička saobraćajna dionica.
TransportLink
TN.CommonTransportElements.TransportArea
Generičko područje saobraćaja.
TransportArea
TN.RoadTransportNetwork.RoadLink
Putna link.
RoadLink
TN.RoadTransportNetwork.VehicleTrafficArea
Kolovozna traka.
VehicleTrafficArea
TN.RoadTransportNetwork.RoadServiceArea
Odmorište uz put.
RoadServiceArea
TN.RoadTransportNetwork.RoadArea
Putna površina.
RoadArea
TN.RailTransportNetwork.RailwayLink
Željeznička dionica.
RailwayLink
TN.RailTransportNetwork.RailwayStationArea
Područje željezničke stanice.
RailwayStationArea
TN.RailTransportNetwork.RailwayYardArea
Područje ranžirne želejeznice.
RailwayYardArea
TN.RailTransportNetwork.RailwayArea
Područje željeznice.
RailwayArea
TN.WaterTransportNetwork.WaterwayLink
Dionica plovnog puta
WaterwayLink
TN.WaterTransportNetwork.FairwayArea
Područje plovnog objekta.
FairwayArea
TN.WaterTransportNetwork.PortArea
Pristanišno područje
PortArea
TN.AirTransportNetwork.AirLink
Vazdušna dionica.
AirLink
TN.AirTransportNetwork.AerodromeArea
Područje aerodroma.
AerodromeArea
TN.AirTransportNetwork.RunwayArea
Područje uzletno-sletne staze.
RunwayArea
TN.AirTransportNetwork.AirspaceArea
Područje vazdušnog prostora.
AirspaceArea
TN.AirTransportNetwork.ApronArea
Područje stajališta.
ApronArea
TN.AirTransportNetwork.TaxiwayArea
Područje vozne (rulne) staze.
TaxiwayArea
TN.CableTransportNetwork.CablewayLink
Dionica žičare.
CablewayLink
8. HIDROGRAFIJA
8.1. Definicije
- "vodonosnik" znači podpovršinski sloj ili stjenovite slojeve ili druge geološke slojeve koji su dovoljno porozni ili propusni da omogućavaju
značajan tok podzemnih voda ili oduzimanje značajnih količina podzemnih voda, - "podzemna voda" znači sva voda koja je ispod površine zemlje u zasićenom području i u neposrednom dodiru sa zemljištem ili zdravcem
(sloj ispod površinskog sloja), - "sliv" znači područje kopna sa kojeg sva površinska atmosferska voda otiče kroz niz potoka, rijeka a moguće i jezera do određene tačke
vodotoka.
8.2. Struktura teme prostornih podataka "Hidrografija" Tipa određene za oblast prostornih podataka Hidrografija strukturisane su u sljedeće grupe:
-
hidrografija - baza;
-
hidrografija - mreža; i -
hidrografija - fizičke vode.
8.3. Hidrografija - baza
8.3.1. Tipa prostornog objekta Sljedeće tipa prostornog objekta upotrebljavaju se za razmjenu i klasifikaciju prostornih objekata koji se odnose na skup hidrografija - baza: -
hidrografski objekat.
8.3.1.1. Hidrografski objekat (HydroObject) Baza identiteta hidrografskih objekata (uključujući vještačke) u stvarnom svijetu.
Riječ je o apstraktnom tipu.
Atributi tipa prostornog objekta HydroObject
Atribut
Definicija
Tip podatka
Voidability
geographicalName Geografsko ime koje se upotrebljava za identifikaciju hidrografskog objekta u
stvarnom svijetu. Osigurava "ključ" za implicitno povezivanje različitih prikaza objekta.
GeographicalName voidable
hydroId
Identifikator koji se upotrebljava za identifikaciju hidrografskog objekta u stvarnom
svijetu. Osigurava "ključ" za implicitno povezivanje različitih prikaza objekta.
HydroIdentifier
Asocijacijske uloge tipa prostornog objekta HydroObject
Asocijacijska uloga
Definicija
Tip podatka
Voidability
relatedHydroObject
Povezani hidrografski objekat koji prikazuje isti entitet u stvarnom svijetu.
HydroObject
voidable
8.3.2. Tipa podataka
8.3.2.1. Hidrografski identifikator (HydroIdentifier) Hidrografski tematski identifikator.
Atributi tipa podataka HydroIdentifier
Atribut
Definicija
Tip podatka
Voidability
classificationScheme
Opis identifikacijske šeme (nacionalna, vitd.) koja se upotrebljava.
CharacterString
localId
Lokalni identifikator koji dodjeljuje određeni nadležni organ.
CharacterString
Namespace
Pokazatelj područja primjene lokalnog identifikatora.
CharacterString
8.4. Hidrografija - mreža
8.4.1. Tipa prostornog objekta Sljedeće tipa prostornog objekta upotrebljavaju se za razmjenu i klasifikaciju prostornih objekata koji se odnose na skup hidrografija - mreža:
-
hidrografski čvor;
-
dionica vodotoka;
-
niz dionica vodotoka; i -
odvojeno ukrštanje vodotoka.
8.4.1.1. Hidrografski čvor (HydroNode) Čvor u hidrografskoj mreži.
Hidrografski čvor je podtip tipa Node i tipa HydroObject.
Atributi tipa prostornog objekta HydroNode
Atribut
Definicija
Tip podatka
Voidability
hydroNodeCategory
Tip hidrografskog čvora.
HydroNodeCategoryValue
voidable
8.4.1.2. Dionica vodotoka (WatercourseLink) Segment vodotoka u hidrografskoj mreži.
Dionica vodotoka je podtip tipa Dionica i tipa HydroObject.
Atributi tipa prostornog objekta WatercourseLink
Atribut
Definicija
Tip podatka
Voidability
flowDirection
Smjer vodenog toka na segmentu u odnosu na digitalizaciju geometrije segmenta.
LinkDirectionValue
voidable
length
Dužina segmenta mreže.
Length
voidable
8.4.1.3. Niz dionica vodotoka (WatercourseLinkSequence) Niz dionica vodotoka koji prikazuje nerazgranati put kroz hidrografsku mrežu.
Niz dionica vodotoka je podtip tipa LinkSequence i Niz dionica vodotoka je podtip tipa HydroObject.
8.4.1.4. Prelaz vodotoka na odvojenim nivoima (WatercourseSeparatedCrossing) Element u hidrografskoj mreži koji se upotrebljava u prelazu dionica vodotoka koje se ne dodiruju na odvojenim nivoima.
Prelaz vodotoka na odvojenim nivoima je podtip tipa GradeSeparatedCrossing i tipa HydroObject.
8.4.2. Popisi kodova
8.4.2.1. Kategorija hidrografskog čvora (HydroNodeCategoryValue) Definiše kategorije različitih Tip čvorova hidrografske mreže.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova HydroNodeCategoryValue
Vrijednost
Definicija
boundary
Čvor koji se koristi za povezivanje različitih mreža.
flowConstriction Čvor mreže koji sam po sebi nema veze s topologijom mreže, nego se odnosi na važnu hidrografsku tačku ili objekat, ili
vještački objekat, koji utiče na protok mreže.
flowRegulation
Čvor mreže koji sam po sebi nema veze s topologijom mreže, nego se odnosi na važnu hidrografsku tačku ili objekat, ili
vještački objekat, koji reguliše protok mreže.
junction
Čvor gdje se povezuju tri ili više dionica.
outlet
Završni čvor niza međusobno povezanih dionica.
source
Početni čvor niza međusobno povezanih dionica.
8.5. Hidrografija - fizičke vode
8.5.1. Tipa prostornog objekta Sljedeće tipa prostornog objekta upotrebljavaju se za razmjenu i klasifikaciju prostornih objekata koji se odnose na grupu hidrografija - fizičke vode:
-
prelaz;
-
brana;
-
slivni bazen;
-
nasip (uz rijeku);
-
slap;
-
tačka vodenog toka;
-
gas (plićak);
-
hidrografska važna tačka;
-
poplavljeno područje;
-
granica kopno-voda;
-
ustava;
-
vještački objekat;
-
brzice;
-
riječni sliv;
-
obala;
-
obalna konstrukcija;
-
regulacioni kanal;
-
stajaća voda;
-
površinska voda, i -
vodotok.
8.5.1.1. Prelaz (Crossing) Vještački objekat koji omogućava prolaz vode ispod i iznad prepreke.
Prelaz je podtip tipa ManMadeObject.
Atributi tipa prostornog objekta Crossing
Atribut
Definicija
Tip podatka
Voidability
type
Tip fizičkog prelaza.
CrossingTypeValue
voidable
8.5.1.2. Brana (DamOrWeir) Stalna prepreka preko vodotoka koja se upotrebljava za zahvatanje vode ili nadzor nad njenim tokom.
Brana je podtip tipa ManMadeObject.
8.5.1.3. Slivni bazen (DrainageBasin) Područje sa zajedničkim izlivom (odvodom) površinskih voda.
Slivni bazen je podtip tipa HydroObject.
Atributi tipa prostornog objekta DrainageBasin
Atribut
Definicija
Tip podatka
Voidability
area
Veličina slivnog bazena.
Area
voidable
basinOrder
Broj (oznaka) koja pokazuje stepen grananja/podjele u sistem slivnog bazena.
HydroOrderCode voidable
beginLifespan Version
Datum i vrijeme kad je ova verzija prostornog objekta unešena u skup prostornih
podataka ili u njemu izmijenjena.
DateTime
voidable
endLifespan Version
Datum i vrijeme kad je ova verzija prostornog objekta u skupu prostornih podataka
izmijenjena ili iz njega izbrisana.
DateTime
voidable
geometry
Geometrija slivnog bazena u obliku površine.
GM_Surface
inspireId
Spoljni identifikator objekta prostornog objekta.
Identifier
origin
Izvor slivnog bazena.
OriginValue
voidable
Asocijacijske uloge tipa prostornog objekta DrainageBasin
Asocijacijska uloga
Definicija
Tip podatka
Voidability
outlet
Izliv(i) površinskih voda u slivnom bazenu.
SurfaceWater
voidable
containsBasin
Porječje koje je dio većeg slivnog bazena.
DrainageBasin
voidable Ograničenja tipa prostornog objekta DrainageBasin Riječni sliv ne smije biti dio drugog slivnog bazena.
8.5.1.4. Obala (Embankment) Vještački duguljasti objekat od zemlje ili drugog materijala.
Obala je podtip tipa ManMadeObject.
8.5.1.5. Slap (Falls) Dio vodotoka koji vertikalno pada s visine.
Slap je podtip tipa FluvialPoint.
Atributi tipa prostornog objekta Falls
Atribut
Definicija
Tip
podatka
Voidability
height
Udaljenost mjerena od najniže tačke podnožja ili nivoa vode (nizbrdne/nizvodne strane) do najviše
tačke prostornog objekta.
Length
voidable
8.5.1.6. Tačka vodnog toka (FluvialPoint) Hidrografska važna tačka koja utiče na tok vode.
Tačka vodnog toka je podtip tipa HydroPointOfInterest.
Riječ je o apstraktnom tipu .
8.5.1.7. Plićak (Ford) Plitki dio vodotoka koji se može preći saobraćajnim sredstvima.
Plićak je podtip tipa ManMadeObject.
8.5.1.8. Hidrografska važna tačka (HydroPointOfInterest) Mjesto u prirodi gdje se voda pojavi, nestane ili promijeni svoj tok.
Hidrografska važna tačka je podtip tipa HydroObject.
Riječ je o apstraktnom tipu.
Atributi tipa prostornog objekta HydroPointOfInterest
Atribut
Definicija
Tip podatka Voidability
beginLifespanVersion Datum i vrijeme kad je ova verzija prostornog objekta unešena u skup prostornih
podataka ili u njemu izmijenjena.
DateTime
voidable
endLifespanVersion
Datum i vrijeme kad je ova verzija prostornog objekta u skupu prostornih podataka
izmijenjena ili iz njega izbrisana.
DateTime
voidable
geometry
Geometrija hidrografske važne tačke u obliku tačke, krive ili površine.
GM_Primitive
voidable
inspireId
Spoljni identifikator objekta prostornog objekta.
Identifier
levelOfDetail
Rezolucija izražena indeksom mjerila ili udaljenošću na tlu.
MD_Resolution
8.5.1.11. Granica kopno-voda (LandWaterBoundary) Crta na kojoj kopno dodiruje vodno tijelo.
Atributi tipa prostornog objekta LandWaterBoundary
Atribut
Definicija
Tip podatka
Voidability
beginLifespanVersion Datum i vrijeme kad je ova verzija prostornog objekta unešena u skup prostornih
podataka ili u njemu izmijenjena.
DateTime
voidable
endLifespanVersion
Datum i vrijeme kad je ova verzija prostornog objekta u skupu prostornih podataka
izmijenjena ili iz njega izbrisana.
DateTime
voidable
geometry
Geometrija granice kopna u obliku krive.
GM_Curve
inspireId
Spoljni identifikator objekta prostornog objekta.
Identifier origin
Tip granice kopna.
OriginValue
voidable
waterLevelCategory
Nivo vode koji određuje granicu kopno-voda.
WaterLevelValue voidable
8.5.1.12. Ustav (brana) (Lock) Ograđeni prostor s dvije ili više brana koji se upotrebljava za dizanje ili spuštanje brodova kad prelaze s jednog nivoa vode na drugu. Ustava je podtip tipa ManMadeObject.
8.5.1.13. Vještački objekat (ManMadeObject) Vještački objekat koji leži u vodnom tijelu ili ma jednu od sljedećih funkcija: zadržava vodu, - reguliše količinu vode, mijenja smjer vode, omogućava ukrštanje vodotokova.
Vještački objekat je podtip tipa HydroObject.
Riječ je o apstraktnom tipu .
Atributi tipa prostornog objekta ManMadeObject
Atribut
Definicija
Tip podatka
Voidability
beginLifespanVersion Datum i vrijeme kad je ova verzija prostornog objekta unešena u skup
prostornih podataka ili u njemu izmijenjena.
DateTime
voidable
condition
Stanje objekta kao cjeline na određenoj lokaciji s obzirom na planiranje,
izgradnju, popravak i/ili održavanje struktura i/ili opreme od kojih se objekat
sastoji.
ConditionOfFacilityValue voidable
endLifespanVersion
Datum i vrijeme kad je ova verzija prostornog objekta u skupu prostornih
podataka izmijenjena ili iz njega izbrisana.
DateTime
voidable
geometry
Geometrija vještačkog objekta u obliku tačke, krive ili površine.
GM_Primitive
voidable
inspireId
Spoljni identifikator objekta prostornog objekta.
Identifier
levelOfDetail
Rezolucija izražena indeksom mjerila ili udaljenošću na zemlji.
MD_Resolution
8.5.1.14. Brzaci (Rapids) Dio vodotoka s ubrzanim protokom, ali bez preloma na dnu nagiba koji bi omogućio nastanak slapa.
Brzaci je podtip tipa FluvialPoint.
8.5.1.15. Riječni sliv (RiverBasin) Područje kopna s kojega se sva površinska voda kroz potoke, rijeke, pa i jezera, slijeva u more kroz samo jedno riječno ušće, estuarij ili deltu. Riječni sliv je podtip tipa DrainageBasin.
8.5.1.16. Obala (Shore) Uzak pojas zemlje u neposrednom dodiru s vodom uključujući površinu između gornjeg i donjeg nivoa vode.
Obala je podtip tipa HydroObject.
Atributi tipa prostornog objekta Shore
Atribut
Definicija
Tip podatka
Voidability
beginLifespanVersion Datum i vrijeme kad je ova verzija prostornog objekta unesena u skup prostornih
podataka ili u njemu izmijenjena.
DateTime
voidable
composition
Primarna Tip materijala od kojega je prostorni objekt sastavljen, osim površine.
ShoreTypeValue voidable
delineationKnown
Pokazatelj da je razgraničenje (npr. granice i informacije) prostornog objekta
poznato.
Boolean
voidable
endLifespanVersion
Datum i vrijeme kad je ova verzija prostornog objekta u skupu prostornih podataka
izmijenjena ili iz njega izbrisana.
DateTime
voidable
geometry
Geometrija obale.
GM_MultiSurface inspireId
Spoljni identifikator objekta prostornog objekta.
Identifier 8.5.1.20. Obalna konstrukcija (ShorelineConstruction) Izgrađena struktura koja ne mijenja položaj na granici s vodnim tijelom.
Obalna konstrukcija je podtip tipa ManMadeObject.
8.5.1.21. Regulacioni kanal (Sluice) Otvoren nagnut kanal opremljen vratima za regulaciju protoka vode.
Regulacioni kanal je podtip tipa ManMadeObject.
8.5.1.22. Stajaća voda (StandingWater) Vodno tijelo u cijelosti okruženo kopnom.
Stajaća voda je podtip tipa SurfaceWater.
Atributi tipa prostornog objekta StandingWater
Atribut
Definicija
Tip podatka
Voidability
elevation
Nadmorska visina.
Length
voidable
meanDepth
Prosječna dubina vodnog tijela.
Length
voidable
surfaceArea
Površina vodnog tijela.
Area
voidable
Ograničenja tipa prostornog objekta StandingWater Geometrija stajaće vode može biti površina ili tačka.
8.5.1.23. Površinska voda (SurfaceWater) Svako poznato tijelo kopnenog plovnog puta.
Površinska voda podtip tipa HydroObject.
Riječ je o apstraktnom tipu.
Atributi tipa prostornog objekta SurfaceWater
Atribut
Definicija
Tip podatka
Voidability
beginLifespanVersion Datum i vrijeme kad je ova verzija prostornog objekta unešena u skup
prostornih podataka ili u njemu izmijenjena.
DateTime
voidable
endLifespanVersion
Datum i vrijeme kad je ova verzija prostornog objekta u skupu
prostornih podataka izmijenjena ili iz njega izbrisana.
DateTime
voidable
geometry
Geometrija površinske vode: - krivulja ili površina za vodotok, - tačka ili
površina za stajaću vodu.
GM_Primitive
inspireId
Spoljni identifikator objekta prostornog objekta.
Identifier
levelOfDetail
Rezolucija izražena indeksom mjerila ili udaljenošću na zemljištu.
MD_Resolution
localType
Određuje "lokalni" naziv za tip površinske vode.
LocalisedCharacterString
voidable
origin
Izvor površinske vode.
OriginValue
voidable
persistence
Stepen postojanosti vode.
HydrologicalPersistenceValue voidable
tidal
Pokazuje utiče li na površinsku vodu voda morskih mijena.
Boolean
voidable
Asocijacijske uloge tipa prostornog objekta SurfaceWater
Asocijacijska
uloga
Definicija
Tip podatka Voidability
bank
Obala (-e) s površinskom vodom.
Shore
voidable
drainsBasin
Slivni bazen(i) dreniran(i) površinskom vodom.
DrainageBasin voidable
neighbour
Asocijacija na drugi primjer iste površinske vode u stvarnom svijetu u drugom skupu
podataka.
SurfaceWater voidable 8.5.1.24. Vodotok (Watercourse) Prirodni ili vještački tok vode.
Vodotok je podtip tipa SurfaceWater.
Atributi tipa prostornog objekta Watercourse
Atribut
Definicija
Tip podatka
Voidability
condition
Stanje vodotoka u smislu njegovog planiranja, izgradnje, popravke i/ili
održavanja.
ConditionOfFacilityValue voidable
delineationKnown Pokazatelj da je razgraničenje (npr.: granice i informacije) prostornog objekta
poznato.
Boolean
voidable
length
Dužina vodotoka.
Length
voidable
level
Vertikalni položaj vodotoka u odnosu na zemljište.
VerticalPositionValue
voidable
streamOrder
Broj (oznaka) koji izražava stepen grananja u sistemu vodotoka.
HydroOrderCode
voidable
width
Širina vodotoka (kao raspon) duž njegove dužine.
WidthRange
voidable
Ograničenja tipa prostornog objekta Watercourse Obale na obje strane vodenog toka moraju se navesti (pomoću svojstva bank) kao dva zasebna objekta ShoreGeometrija vodotoka može biti krivulja ili površina.
Atribut "condition" može se navesti samo za vještački vodotok.
8.5.1.25. Močvarno zemljište (Wetland) Slabo drenirano ili povremeno poplavljeno područje u kojem je zemlja zasićena vodom i u kojem uspijeva vegetacija.
Močvarno zemljište je podtip tipa HydroObject.
Atributi tipa prostornog objekta Wetland
Atribut
Definicija
Tip podatka
Voidability
beginLifespanVersion Datum i vrijeme kad je ova verzija prostornog objekta unešena u skup
prostornih podataka ili u njemu izmijenjena.
DateTime
voidable
endLifespanVersion
Datum i vrijeme kad je ova verzija prostornog objekta u skupu prostornih
podataka izmijenjena ili iz njega izbrisana.
DateTime
voidable
geometry
Geometrija močvarnog zemljišta u obliku površine.
GM_Surface
inspireId
Spoljni identifikator objekta prostornog objekta.
Identifier
localType
Određuje "lokalni" naziv za tip močvarnog zemljišta.
LocalisedCharacterString voidable
Tidal
Pokazuje utiče li na močvarno zemljište voda morskih mijena.
Boolean
voidable
8.5.2. Tipa podataka
8.5.2.1. Hidrografska oznaka nivoa (HydroOrderCode) Hidrološki značajna "oznaka nivoa" koja se koristi za razvrstavanje vodotoka i slivnih bazena u smislu hijerarhije.
Atributi tipa podataka HydroOrderCode
Atribut
Definicija
Tip podatka
Voidability
order
Broj (oznaka) koji pokazuje stepen grananja ili dijeljenja u sistemu vodotoka ili u sistemu
slivnog bazena.
CharacterString
orderScheme Opis pojma na kojem se temelji razvrstavanje.
CharacterString scope
Pokazatelj područja primjene ili izvora oznake nivoa (uključujući nacionalni, nadnacionalni ili
evropski nivo).
CharacterString
8.5.2.2. Raspon širine (WidthRange) Raspon horizontalne širine vodotoka duž njegove dužine.
Atributi tipa podataka WidthRange
Atribut
Definicija
Tip podatka
Voidability
lower
Donja granica raspona širine.
Length
upper
Gornja granica raspona širine.
Length
8.5.3. Enumeracije
8.5.3.1. Izvor (OriginValue) Tip numeracije koja određuje hidrografske kategorije "izvora" (prirodni, vještački) za različite hidrografske objekte.
Vrijednosti dopuštene za numeraciju OriginValue
Vrijednost
Definicija
natural
Pokazatelj da je prostorni objekt prirodan.
manMade
Pokazatelj da je prostorni objekt vještački.
8.5.4. Popisi kodova
8.5.4.1. Tip prelaza (CrossingTypeValue) Tipa prelaza fizičkih vodotokova koje je stvorio čovjek.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova CrossingTypeValue
Vrijednost
Definicija
aqueduct
Cijev ili vještački kanal za prinos vode iz udaljenog izvora, obično pomoću gravitacije, za snadbijevanje vodom, te za
poljoprivredne i/ili industrijske namjene.
bridge
Struktura koja povezuje dvije lokacije i omogućava prelaz transportnog puta preko prepreke na terenu.
culvert
Zatvoreni kanal koji vodotok vodi ispod puta, željeznice, kanala ili drugih objekata.
siphon
Cijev za prelivanje tečnosti s višeg nivoa na niži pri čemu se koriste razlike u pritiscima kako bi se vodeni pritisak podigao na
viši nivo prije nego što se tečnost izlije.
8.5.4.2. Hidrološka postojanost (HydrologicalPersistenceValue) Kategorije hidrološke postojanosti vodnog tijela.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova HydrologicalPersistenceValue
Vrijednost
Definicija
dry
Rijetko puno i/ili tečne, uopšteno samo tokom i/ili neposredno nakon obilnih padavina.
ephemeral
Puno i/ili tečne tokom i/ili neposredno nakon padavina.
intermittent
Puno i/ili tečne jedan dio godine.
perennial
Neprekidno puno i/ili tečne tokom cijele godine.
8.5.4.3. Poplava (InundationValue) Tip zemljišta koje je podložno poplavama.
Ovaj tip je kandidat za tip koji treba uzeti u obzir u oblasti prostornih podataka Područja sa rizikom od prirodnih katastrofa.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova InundationValue
Vrijednost
Definicija
controlled
Područje koje je povremeno poplavljeno zbog regulacije vodostaja akumulirane vode.
natural
Područje koje je povremeno poplavljeno, ali ne zbog plimnih voda.
8.5.4.4. Tip obale (ShoreTypeValue) Kategorije sastava obalnog područja.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova ShoreTypeValue
Vrijednost
Definicija
boulders
Velike stijene koje su erodirale zbog djelovanja vode i vremenskih uslova.
clay
Čtipa i guste čestice zemljišta sitno zrnaste strukture koje se uglavnom sastoje od aluminijskih hidrosilikata, koje dodavanjem
vode postaju plastičnije i mogu se oblikovati i sušiti.
gravel
Manje kamene strukture izmijenjene zbog djelovanja vode ili usitnjavanja.
mud
Meko, vlažno zemljište, pijesak, prašina i/ili druge čestice zemljišta.
rock
Stijene svih veličina.
sand
Zrnasti materijal koji se sastoji od malih erodiranih fragmenata (uglavnom silicijumski) stijena, manji od šljunka a veći od
grudvice blata.
shingle
Mali, rastresiti, kamenčići zaobljeni djelovanjem vode, posebno dospjeli na morskoj obali.
stone
Dijelovi stijena ili mineralnih materija(osim kovina) određenog oblika i veličine, najčešće vještački oblikovani, koji se koriste za
neku posebnu namjenu.
8.5.4.5. Nivo vode (WaterLevelValue) Nivo reference morskih mijena/nivoa vode na osnovu kojih se označuju dubine i visine.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova WaterLevelValue
Vrijednost
Definicija
equinoctialSpringLowWater
Nizak nivo vode morskih mijena oko ravnodnevice.
higherHighWater
Najviše visoke vode (ili plima) određenog lunarnog dana nastala zbog djelovanja deklinacije A1 Mjeseca i
Sunca.
higherHighWaterLargeTide
Prosjek najviše visokih voda, po jedna vrijednost za svaku od 19 godina posmatranja.
highestAstronomicalTide
Najviši nivo morskih mijena koja se može predvidjeti na temelju prosječnih meteoroloških uslova i za bilo
koju kombinaciju astronomskih uslova.
highestHighWater
Najviši nivo vode zabilježen na nekoj lokaciji.
highWater
Najviši nivo površine vode postignut u jednom plimnom ciklusu.
highWaterSprings
Proizvoljni nivo vode koji je približno jednak nivou srednje visoke vode za vrijeme mladog i punog mjeseca.
indianSpringHighWater
Visina plime koja je približno jednaka nivou srednje više visoke vode tokom najjačih morskih mijena.
indianSpringLowWater
Visina plime koja je približno jednaka nivou srednje niže niske vode tokom najjačih morskih mijena.
localDatum
Proizvoljan datum koji je definisala lokalna lučka uprava od kojeg navedena uprava mjeri vodostaj i visinu
plime i oseke.
lowerLowWater
Najniža niska voda (ili oseka) određenog lunarnog dana nastala zbog djelovanja deklinacije A1 Mjeseca i
Sunca.
lowerLowWaterLargeTide
Prosjek najnižih niskih voda, po jedna vrijednost za svaku od 19 godina posmatranja.
lowestAstronomicalTide
Najniži nivo morskih mijena koja se može predvidjeti na temelju prosječnih meteoroloških uslova i za bilo
koju kombinaciju astronomskih uslova.
lowestLowWater
Proizvoljni nivo vode koja odgovara najnižem nivou morskih mijena koja je zabilježena na nekoj lokaciji ili je
ta vrijednost nešto niža.
lowestLowWaterSprings
Proizvoljni nivo vode koji odgovara najnižem nivou vode koja je zabilježena na nekoj lokaciji tokom najjačih
morskih mijena u razdoblju kraćem od 19 godina.
lowWater
Približna vrijednost srednje niske vode usvojena kao referentni nivo za ograničeno područje, bez obzira na
kasnija detaljna mjerenja.
lowWaterDatum
Približna vrijednost srednje niske vode koja je usvojena kao standardna referentna vrijednost za ograničeno
područje.
lowWaterSprings
Proizvoljni nivo vode kojaije približno jednak nivou srednje niske vode za mlađaka i uštapa.
meanHigherHighWater
Prosječna visina više visoke vode na nekoj lokaciji tokom razdoblja od 19 godina.
meanHigherHighWaterSprings Prosječna visina više visoke vode na nekoj lokaciji tokom najjačih morskih mijena.
meanHigherLowWater
Prosječna visina više niske vode svakog lunarnog dana zabilježena u razdoblju od 19 godina koje je odredila
država (National Tidal Datum Epoch).
meanHighWater
Prosječna visina svih visokih voda na nekoj lokaciji tokom razdoblja od 19 godina.
meanHighWaterNeaps
Prosječna visina visokih voda kod najslabijih morskih mijena.
meanHighWaterSprings
Prosječna visina visokih voda kod najjačih morskih mijena.
meanLowerHighWater
Prosječna visina niže visoke vode svakog lunarnog dana zabilježena u razdoblju od 19 godina koje je
odredila država (National Tidal Datum Epoch).
meanLowerLowWater
Prosječna visina nižih niskih voda na nekoj lokaciji tokom razdoblja od 19 godina.
meanLowerLowWaterSprings Prosječna visina nižih niskih voda na nekoj lokaciji tokom najjačih morskih mijena.
meanLowWater
Prosječna visina svih niskih voda na nekoj lokaciji tokom razdoblja od 19 godina.
meanLowWaterNeaps
Prosječna visina niskih voda pri najslabijim morskim mijenama.
meanLowWaterSprings
Prosječna visina niskih voda pri najjačim morskim mijenama.
meanSeaLevel
Prosječna visina nivoa mora na mareografskoj stanici mjerena unaprijed utvrđenim referentnim nivoom
meanTideLevel
Aritmetička sredina srednje visoke vode i srednje niske vode.
meanWaterLevel
Prosječna visina vodostaja mjerena svaki sat tokom dostupnog razdoblja evidencije.
nearlyHighestHighWater
Prosječan nivo koji je približno jednak nivou najviše vode koja je zabilježena na nekoj lokaciji, obično je
jednaka nivou visoke vode za vrijeme mladog i punog mjeseca.
nearlyLowestLowWater
Nivo koji je približno jednak najnižem nivou vode koja je zabilježena na nekoj lokaciji obično je jednak nivou
niske vode tokom najjačih morskih mijena.
tropicHigherHighWater
Najviše visoke vode (ili plima) koje nastaju svakih pola mjeseca kad je djelovanje maksimalne deklinacije
Mjeseca najveće.
tropicLowerLowWater
Najniže niske vode (ili oseka) koje nastaju svakih pola mjeseca kad je djelovanje maksimalne deklinacije
Mjeseca najveće.
8.6. Hidrografija - izvještavanje
8.6.1. Tip prostornog objekta Sljedeći tipovi prostornog objekta upotrebljavaju se za razmjenu i razvrstavanje prostornih objekata koji se odnose na kategoriju hidrografija - izvještavanje:
-
obalna voda;
-
tijelo podzemne vode;
-
jezero;
-
rijeka;
-
rijeka ili jezero;
-
tijelo površinske vode;
-
prelazna voda; i -
vodno tijelo.
8.6.1.1. Obalna voda (u skladu sa propisom kojim se uređuje pitanje voda) (WFDCoastalWater) Površinska voda na kopnenoj strani crte, koja je u svakoj svojoj tački udaljena jednu nautičku milju na morsku stranu od najbliže temeljne tačke od koje se mjeri širina teritorijalnih voda, i kad je to primjenjivo, proteže se do spoljne granice prelaznih voda.
Obalna voda u je podtip tipa WFDSurfaceWaterBody.
Obalna voda je kandidat za tip koji treba uzeti u obzir u oblasti prostornih podataka Područja koja su proglašena zonama zaštite ili kojima se upravlja.
Ograničenja tipa prostornog objekta WFDCoastalWater Geometrija obalne vode mora biti površina.
8.6.1.2. Tijelo podzemne vode (propisom kojim se uređuje pitanje voda) - (WFDGroundWaterBody) Izrazit volumen podzemne vode u vodonosniku ili vodonosnicima.
Tijelo podzemne vode je podtip tipa WFDWaterBody.
Tijelo podzemne vode je kandidat za tip koji treba uzeti u obzir u oblasti prostornih podataka Područja koja su proglašena zonama zaštite ili kojima se upravlja u skladu sa posebnim propisima Zakona o infrastrukturi prostornih podataka.
Atributi tipa prostornog objekta WFDGroundWaterBody
Atribut
Definicija
Tip podatka
Voidability
geometry
Geometrija tijela podzemne vode WFD.
GM_Primitive
voidable
8.6.1.3. Jezero u skladu s WFD-om (WFDLake) Vodno tijelo na unutrašnjim vodama dugotrajne površine.
Jezero je podtip tipa WFDRiverOrLake.
Jezero je kandidat za tip koji treba uzeti u obzir u oblasti prostornih podataka Područja koja su proglašena zonama zaštite ili kojima se upravlja.
Ograničenja tipa prostornog objekta WFDLake Geometrija jezera mora biti površina.
8.6.1.4. Rijeka (u skladu s propisom kojim se uređuje pitanje voda) (WFDRiver) Vodno tijelo na unutrašnjim vodama koje većim dijelom teče po površini, ali jednim dijelom toka može teći i ispod površine.
Rijeka je podtip tipa WFDRiverOrLake.
Rijeka je kandidat za tip koji treba uzeti u obzir u oblasti prostornih podataka Područja koja su proglašena zonama zaštite ili kojima se upravlja.
Ograničenja tipa prostornog objekta WFDRiver Geometrija rijeke mora biti krivulja.
Atributi "main" i "large" ne smiju se navoditi za kanale.
8.6.1.5. Rijeka ili jezero u skladu s WFD-om (WFDRiverOrLake) Apstraktni razred koji sadržava zajedničke atribute za rijeku ili jezero u skladu s WFD-om.
Rijeka ili jezero je podtip tipa WFDSurfaceWaterBody.
Riječ je o apstraktnom tipu.
Rijeka ili jezero je kandidat za tip koju treba uzeti u obzir u oblasti prostornih podataka Područja koja su proglašena zonama zaštite ili kojima se upravlja u skladu sa posebnim propisima Zakona o infrastrukturi prostornih podataka.
Atributi tipa prostornog objekta WFDRiverOrLake
Atribut
Definicija
Tip
podatka
Voidability
large
Rijeke s porječjem > 50 000 km2; ili rijeke i glavni pritoci s porječjem između 5 000 km2 i 50 000 km2.
Jezera površine > 500 km2.
Boolean
voidable
main
Rijeke s porječjem > 500 km2. Jezera površine > 10 km2.
Boolean
voidable
8.6.1.6. Tijelo površinske vode u skladu s WFD-om (WFDSurfaceWaterBody) Izrazit i važan element površinske vode.
Tijelo površinske vode je podtip tipa WFDWaterBody.
Riječ je o apstraktnom tipu.
Ovaj tip je kandidat za tip koju treba uzeti u obzir u oblasti prostornih podataka Područja koja su proglašena zonama zaštite ili kojima se upravlja.
Atributi tipa prostornog objekta WFDSurfaceWaterBody
Atribut
Definicija
Tip podatka Voidability
artificial
"Vještačko vodno tijelo"znači tijelo površinske vode koje je stvorio čovjek.
Boolean
geometry
Geometrija tijela površinske vode; - površina u slučaju obalnih voda, - površina u slučaju
prelaznih voda, - kriva u slučaju m, - površina u slučaju jezera.
GM_Primitive
heavilyModified
"Bitno modifikovano vodno tijelo" znači tijelo površinske vode koje je zbog fizičkih
promjena djelovanjem čovjeka bitno izmijenilo svoja svojstva.
Boolean
representativePoint Reprezentativna tačka vodnog tijela.
GM_Point
voidable
Ograničenja tipa prostornog objekta WFDSurfaceWaterBody Atribut "heavilyModified" dopušten je samo ako nije riječ o vještačkom vodnom tijelu.
8.6.1.7. Prelazna voda u skladu s WFD-om (WFDTransitionalWater) Tijela površinske vode u blizini riječnih ušća koja su djelomično slana zbog blizine obalnih voda, međutim na njih znatno utiču tokovi slatke vode.
Prelazna voda je podtip tipa WFDSurfaceWaterBody.
Prelazna voda je tip kandidat za tip koju treba uzeti u obzir u oblasti prostornih podataka Područja koja su proglašena zonama zaštite ili kojima se upravlja.
Ograničenja tipa prostornog objekta WFDTransitionalWater Geometrija prijelazne vode mora biti površina.
8.6.1.8. Vodno tijelo u skladu s WFD-om (WFDWaterBody) Apstraktni razred koji prikazuje tijelo površinske vode ili tijelo podzemne vode WFD.
Vodno tijelo je podtip tipa HydroObject.
Riječ je o apstraktnom tipu.
Vodno tijelo je kandidat za tip koju treba uzeti u obzir u oblasti prostornih podataka Područja koja su proglašena zonama zaštite ili kojima se upravlja.
Atributi tipa prostornog objekta WFDWaterBody
Atribut
Definicija
Tip
podatka
Voidability
beginLifespanVersion Datum i vrijeme kad je ova verzija prostornog objekta unešena u skup prostornih
podataka ili u njemu izmijenjena.
DateTime
voidable
endLifespanVersion
Datum i vrijeme kad je ova verzija prostornog objekta u skupu prostornih podataka
izmijenjena ili iz njega izbrisana.
DateTime
voidable
inspireId
Spoljni identifikator objekta prostornog objekta.
Identifier
8.7. Zahtjevi specifični za temu "Hidrografija"
8.7.1. Usklađenost skupova prostornih podataka
1. Hidrografske dionice, središnje linije i čvorovi uvijek su unutar prikaza područja istog objekta.
2. Povezivost hidrografskih mreža preko državnih granica i, kad je to potrebno, i preko regionalnih granica (i skupova podataka) u
državama uspostavljaju i održavaju odgovarajuća tijela, pri čemu upotrebljavaju mehanizme za prekograničnu povezanost koju osigurava
Tip NetworkConnection type.
3. Sve vrijednosti atributa objekata u toj šemi jednake su odgovarajućem svojstvu tog objekta koji se upotrebljava za obavezu izvještavanja.
8.7.2. Upravljanje identifikatorom
1. Ako se geografsko ime koristi kao jedinstveni hidrološki identifikator za objekat u toj specifikaciji, tad se ime (toponim) preuzima, ako je
to moguće, iz panevropskog (geografskog) imenika ili kojega drugog priznatog panevropskog izvora.
2. Atribut localId spoljnog identifikatora objekta prostornog objekta jednak je identifikatoru koji se upotrebljava za obavezu izvještavanja. 8.7.3. Modeliranje referenca objekta
1. Ako se isti objekat iz stvarnog svijeta u skupu podataka mijenja upotrebom prostornih objekata iz više od jedne hidrografske aplikacijske
šeme, tad ti prostorni objekti imaju isto jedinstveno geografsko ime ili isti hidrografski tematski identifikator.
2. Kad se u podacima hidrografske mreže upotrebljava linearno referenciranje, položaj referentnih svojstava na dionicama i nizu dionica
izražava se kao udaljenost mjerena duž osigurane geometrije temeljnih dionica objekta.
8.7.4. Prikaz geometrije
1. Ako se prostorni objekti osiguravaju na različitim prostornim rezolucijama, za svaki prostorni objekat, kad je to moguće, mora biti
navedena prostorna rezolucija upotrebom atributa levelOfDetail.
2. Dionice vodotokova uvijek se sijeku kad postoji veza među pojavama stvarnog svijeta koji prikazuju. Presjeci se ne stvaraju na prelazu
elemenata mreže, ako nije moguć prelaz vode iz jednog elementa u drugi.
3. U skupu podataka o hidrografskoj mreži koja sadrži čvorove, ti su čvorovi prisutni samo kad se dionice vodotokova dodiruju ili
završavaju.
4. Geometrija je jednaka geometriji koja se upotrebljava za obaveze izvještavanja.
8.7.5. Upotreba atributa DelineationKnown
1. Atribut delineationKnown ne upotrebljava se da pokaže da je tačnost/preciznost određene geometrije slaba; to treba iskazati
odgovarajućim elementima o kvalitetu podataka.
2. Atribut delineationKnown ne upotrebljava se da pokaže promjenu geometrije tokom vremena, kad je promjena geometrije poznata.
8.7.6. Središnje linije Središnje linije vodenih tokova dio su opsega fizičkog objekta stvarnog svijeta koji predstavljaju, ako dionica vodotoka nije označena kao "fictitious".
8.7.7. Osiguranje povezivosti hidrografske mreže
1. Kad god u hidrografskoj mreži postoji povezanost, svi povezani završeci dionica i neobavezni čvorovi koji su dio te povezanosti moraju
biti pozicionirani na udaljenosti koja je manja od tolerancije povezanosti među njima.
2. Završeci dionica i čvorovi koji nisu povezani uvijek su odvojeni udaljenošću koja je veća od tolerancije povezivosti.
3. U skupovima podataka koji sadrže saobraćajne dionice i čvorove, relativni položaj čvorova i završetaka dionica u odnosu na navedenu
toleranciju povezanosti odgovaraju asocijacijama koje među njima postoje u skupovima podataka.
8.8. Slojevi
"Tip sloja"
Naslov sloja
Tipovi prostornih objekata
HY.Network
Hidrografska mreža.
HydroNode, WatercourseLink
HY.PhysicalWaters.Waterbodies
Vodeni resursi.
Watercourse, StandingWater
HY.PhysicalWaters.LandWaterBoundary Vodene
granice
na
kopnu.
LandWaterBoundary
HY.PhysicalWaters.Catchments
Razvođa.
DrainageBasin, RiverBasin
HY.PhysicalWaters.HydroPointOfInterest Vodene
tačke
od
interesa.
Rapids, Falls
HY.PhysicalWaters.ManMadeObject
Izgrađeni objekti
Crossing, DamOrWeir, Embankment, Lock, Ford, ShorelineConstruction,
Sluice
HY. PhysicalWaters.Wetland
Močvare
Wetland
HY. PhysicalWaters.Shore
Obale
Shore"
9. ZAŠTIĆENA PODRUČJA U SKLADU SA ZAKONOM I ZAŠTIĆENA NEPOKRETNA KULTURNA DOBRA
9.1. Tip prostornog objekta Sljedeći tipovi prostornog objekta upotrebljavaju se za razmjenu i klasifikaciju prostornih objekata iz skupa podataka koji se odnose na oblast prostornih podataka zaštićena područja:
-
zaštićena područja.
9.1.1. Zaštićena područja (ProtectedSite) Područje koje se određuje ili kojim se upravlja u okviru međunarodnog prava i prava država i Unije radi postizanja posebnih ciljeva očuvanja.
Atributi tipa prostornog objekta ProtectedSite
Atribut
Definicija
Tip podatka
Voidability
geometry
Geometrija koja određuje granicu zaštićenog područja.
GM_Object
inspireID
Spoljni identifikator objekta prostornog objekta.
Identifier
legalFoundationDate
Datum kad je zaštićeno područje postalo pravno valjano. To je
datum kad je stvoren objekat stvarnog svijeta, a ne datum kad je
ostvaren njegov prikaz u informacijskom sistemu.
DateTime
voidable
legalFoundationDocument URL ili pozivanje na pravni akt na temelju kojeg je zaštićeno
područje stvoreno.
CI_Citation
voidable
siteDesignation
Oznaka (Tip) zaštićenog područja.
DesignationType
voidable
siteName
Ime zaštićenog područja.
GeographicalName
voidable
siteProtectionClassification Klasifikacija zaštićenog područja s obzirom na svrhu zaštite.
ProtectionClassificationValue voidable
9.2. Tip podataka
9.2.1. Tip oznake (DesignationType) Tip podatka koji sadrži oznaku zaštićenog područja, uključujući oznaku upotrijebljene šeme i vrijednosti u navedenoj šemi.
Atributi tipa podataka DesignationType
Atribut
Definicija
Tip podatka
Voidability
designation
Stvarna oznaka područja.
DesignationValue
designationScheme
Šema iz koje je oznaka uzeta.
DesignationSchemeValue percentageUnderDesignation Dio područja koji pripada pod oznaku. Upotrebljava se ponajprije za
kategorizaciju IUCN-a. Ako se za taj atribut ne daju vrijednosti,
njegova je pretpostavljena vrijednost 100 %.
Percentage
Ograničenja tipa podataka DesignationType Za područja je potrebno upotrebljavati oznake iz odgovarajuće šeme oznaka, pri čemu se vrijednosti oznaka moraju podudarati sa šemom oznaka.
9.3. Enumeracije
9.3.1. Klasifikacija zaštite (ProtectionClassificationValue) Klasifikacija zaštićenog područja na temelju svrhe zaštite.
Vrijednosti dopuštene za enumeraciju ProtectionClassificationValue
Vrijednost
Definicija
natureConservation
Područje zaštićeno zbog očuvanja biološke raznolikosti.
archaeological
Područje zaštićeno zbog očuvanja arheološke baštine.
cultural
Područje zaštićeno zbog očuvanja kulturne baštine.
ecological
Područje zaštićeno zbog očuvanja ekološke stabilnosti.
landscape
Područje zaštićeno zbog očuvanja karakteristika predijela.
environment
Područje zaštićeno zbog očuvanja stabilnosti životne sredine.
Geological
Područje zaštićeno zbog očuvanja geoloških karakteristika.
9.4. Popisi kodova
9.4.1. Šema oznaka (DesignationSchemeValue) Šema koja se upotrebljava za dodjeljivanje oznake zaštićenim područjima.
Popis kodova koji države mogu proširiti.
Vrijednosti dopuštene za popis kodova DesignationSchemeValue
Vrijednost
Definicija
emeraldNetwork
Zaštićeno područje ima oznaku prema programu Smaragdne mreže (Emerald Network).
IUCN
Zaštićeno područje razvrstano je prema klasifikaciji šeme Međunarodne unije za očuvanje prirode.
nationalMonumentsRecord
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih
spomenika.
natura2000
Zaštićeno područje ima oznaku u skladu sa propisom kojim je uređena oblast prirode.
ramsar
Zaštićeno područje ima oznaku prema Ramsarskoj konvenciji.
UNESCOManAndBiosphereProgramme Zaštićeno područje ima oznaku prema programu UNESCO-a "Čovjek i biosfera".
UNESCOWorldHeritage
Zaštićeno područje ima oznaku prema Konvenciji UNESCO-a o svjetskoj baštini.
9.4.2. Oznaka (DesignationValue) Apstraktni osnovni tipza popise kodova koji sadrže tipa klasifikacija i oznake iz različitih šema.
Riječ je o apstraktnom tipu .
9.4.3. Oznaka IUCN (IUCNDesignationValue) Popis kodova za klasifikaciju šeme Međunarodne unije za očuvanje prirode (IUCN).
Oznaka IUCN je podtip tipa DesignationValue.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova IUCNDesignationValue
Vrijednost
Definicija
habitatSpeciesManagementArea Zaštićeno područje razvrstano je prema klasifikaciji šeme IUCN-a kao područje upravljanja staništem ili
vrstom.
managedResourceProtectedArea Zaštićeno područje razvrstano je prema klasifikaciji šeme IUCN-a kao zaštićeno područje upravljanja
resursima.
nationalPark
Zaštićeno područje razvrstano je prema klasifikaciji šeme IUCN-a kao nacionalni park.
naturalMonument
Zaštićeno područje razvrstano je prema klasifikaciji šeme IUCN-a kao prirodni spomenik.
ProtectedLandscapeOrSeascape Zaštićeno područje razvrstano je prema klasifikaciji šeme IUCN-a kao zaštićeni kopneni/morski predio.
strictNatureReserve
Zaštićeno područje razvrstano je prema klasifikaciji šeme IUCN-a kao strogi rezervat prirode.
wildernessArea
Zaštićeno područje razvrstano je prema klasifikaciji šeme IUCN-a kao područje divljine.
9.4.4. Oznaka područja na osnovu Registra nacionalnih zaštićenih spomenika (NationalMonumentsRecordDesignationValue) Popis kodova za klasifikaciju šeme Registra nacionalnih zaštićenih spomenika.
Oznaka područja na osnovu Registra nacionalnih zaštićenih spomenika je podtip tipa DesignationValue.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova NationalMonumentsRecordDesignationValue
Vrijednost
Definicija
agricultureAndSubsistence
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
poljoprivredni ili održivi spomenik (agricultural or subsistence monument).
civil
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
civilni spomenik (civil monument).
commemorative
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
komemorativni spomenik (commemorative monument).
commercial
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
komercijalni spomenik (commercial monument).
communications
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
spomenik iz područja komunikacija (communications monument).
defence
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
spomenik iz područja obrane (defence monument).
domestic
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
domaći spomenik (domestic monument).
education
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
vaspitno obrazovni spomenik (education monument).
gardensParksAndUrbanSpaces Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
vrt, park ili spomenik urbanog prostora (garden, park or urban space monument).
healthAndWelfare
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
spomenik iz područja zdravstva i socijalne zaštite (health and welfare monument).
industrial
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
industrijski spomenik (industrial monument).
maritime
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
pomorski spomenik (maritime monument).
monument
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
spomenik bez određene kategorije (monument with some unclassified form).
recreational
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
spomenik iz područja rekreacije (recreational monument).
religiousRitualAndFunerary
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
vjerski, obredni ili pogrebni spomenik (religious, ritual or funerary monument).
settlement
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
spomenik-naselje (settlement monument).
transport
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
spomenik iz područja saobraćaja (transport monument).
waterSupplyAndDrainage
Zaštićeno područje razvrstano je prema klasifikaciji šeme Registra nacionalnih zaštićenih spomenika kao
spomenik iz područja snadbijevanja vodom i komunalija (water supply and drainage monument).
9.4.5. Oznaka Natura2000 (Natura2000DesignationValue) Popis kodova za šemu oznake Natura2000 u skladu sa propisom kojim je uređena oblast prirode.
Oznaka Natura2000 je podtip tipa DesignationValue.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova Natura2000DesignationValue
Vrijednost
Definicija
proposedSiteOfCommunityImportance Zaštićeno područje predložno je prema programu Natura2000 za područje od važnosti za zajednicu
(Site of Community Importance, SCI).
proposedSpecialProtectionArea
Zaštićeno područje predložno je prema programu Natura2000 za područje posebne zaštite (Special
Protection Area, SPA).
siteOfCommunityImportance
Zaštićeno područje prema programu Natura2000 ima oznaku područja od značaja za zajednicu (Site
of Community Importance, SCI).
specialAreaOfConservation
Zaštićeno područje prema programu Natura2000 ima oznaku posebnog područja očuvanja (Special
Area of Conservation, SAC).
specialProtectionArea
Zaštićeno područje prema programu Natura2000 ima oznaku područja posebne zaštite (Special
Protection Area, SPA).
9.4.6. Oznaka Ramsar (RamsarDesignationValue) Popis kodova za šemu oznake prema Konvenciji o vlažnim područjima koja su od međunarodne važnosti (Ramsarska konvencija).
Oznaka Ramsar je podtip tipa DesignationValue.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova RamsarDesignationValue
Vrijednost
Definicija
ramsar
Zaštićeno područje ima oznaku prema Ramsarskoj konvenciji.
9.4.7. Oznaka prema programu UNESCA Čovjek i biosfera (UNESCOManAndBiosphereProgrammeDesignationValue) Popis kodova za klasifikacijsku šemu prema programu Čovjek i biosfera.
Oznaka prema programu UNESCA Čovjek i biosfera je podtip tipa DesignationValue.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova UNESCOManAndBiosphereProgrammeDesignationValue
Vrijednost
Definicija
biosphereReserve
Zaštićeno područje ima oznaku biosfernog rezervata prema programu "Čovjek i biosfera".
9.4.8. Oznaka prema programu UNESCO Svjetska baština (UNESCOWorldHeritageDesignationValue) Popis kodova za šemu oznake prema programu Svjetska baština.
Oznaka prema programu UNESCO Svjetska baština je podtip tipa DesignationValue.
Dopuštene vrijednosti za ovaj popis kodova sadrže samo vrijednosti iz tabele u nastavku.
Vrijednosti dopuštene za popis kodova UNESCOWorldHeritageDesignationValue
Vrijednost
Definicija
cultural
Zaštićeno područje ima oznaku područja svjetske kulturne baštine.
mixed
Zaštićeno područje ima oznaku područja svjetske kulturne i svjetske prirodne baštine.
natural
Zaštićeno područje ima oznaku područja svjetske prirodne baštine.
9.5. Slojevi
Slojevi za temu prostornih podataka Zaštićena područja
Tip sloja
Naziv sloja
Prostorni objekt(i)
PS.ProtectedSite
Zaštićena područja.
ProtectedSite
PRILOG 3
TEHNIČKA RJEŠENJA ZA USPOSTAVLJANJE I ODRŽAVANJE MREŽNIH SERVISA
Definicije
- »Osnovna operativna sposobnost« označava mogućnost Mrežnog servisa da pruža potpunu funkcionalnost, bez garantovanja kvaliteta servisa u skladu sa propisima koji su dati u Prilogu I. ovih Implementacionih pravila ili pristupa servisu za sve korisnike putem nacionalnog geoportala;
- »Izvođenje« označava najmanji postignut nivo kojim se smatra da je cilj postignut predstavljajući brzinu kojom se zahtjev može riješiti u sklopu Mrežnog servisa;
- »Kapacitet« označava maksimalan broj istovremenih zahtjeva za servisima koje su pruženi sa zagarantovanim učinkom;
- »Dostupnost« označava vjerovatnost da je Mrežni servis dostupan;
- »Vrijeme odziva« označava vrijeme mjereno na lokaciji servisa subjekta NIPP-a za koje je operativna funkcija servisa vratila prvi bajt rezultata;
- »Zahtjev za servisom« označava pojedinačni zahtjev prema jednoj operativnoj funkciji Mrežnog servisa;
- »INSPIRE element metapodatka« označava elemente metapodatka propisane Pravilnikom o sadržaju metapodataka Priloga B;
- »Objavi« označava operaciju za postavljanje, brisanje ili ažuriranje elemenata metapodataka o izvorima u Servisu pronalaženja;
- »Prirodni jezik« označava jezik kojim se govori, piše ili kojim ljudi simbolički označavaju u opštu svrhu komunikacije;
- »Prikupi« označava operaciju izvlačenja elemenata metapodataka o izvorima iz primarnog Servisa pronalaženja kao i dopuštanje stvaranja, brisanja ili ažuriranja metapodataka ovih izvora u ciljanom Servisu pronalaženja;
- »Sloj« označava osnovnu jedinicu geografskih informacija koja može biti zatražena kao mapa sa servera
-»Preuzimanje sa direktnim pristupom« znači servis preuzimanja koji na osnovu upita omogućava pristup prostornim objektima u skupovima prostornih podataka
KVALITET SERVISA
1. Mrežni servisi treće strane neće biti uzeti u obzir prilikom ocjene kvaliteta servisa kako bi se izbjeglo moguće pogoršanje zbog kaskadnog efekta.
2. Kriterijumi kvaliteta servisa koji se moraju osigurati su:
- izvođenje;
- kapacitet; i - dostupnost.
2.1. IZVOĐENJE
Normalna situacija podrazumijeva vremensko razdoblje bez vršnog opterećenja. Ona je postavljena na 90 % vremena.
Vrijeme odziva za slanje inicijalnog odziva na zahtjev usluge pronalaženja je najviše 3 sekunde u normalnoj situaciji.
Za sliku od 470 kilobajta (npr. 800 × 600 piksela s dubinom boje od 8 bita) odzivno vrijeme za slanje inicijalnog odziva na zahtjev "Očitaj mapu" prema usluzi pregleda u normalnoj situaciji je najviše 5 sekundi.
Za postupak "Očitaj metapodatke o uslugama preuzimanja" vrijeme za slanje inicijalnog odziva u normalnoj situaciji je najviše 10 sekundi. Za postupak "Očitaj skup prostornih podataka" i za postupak "Očitaj prostorni objekt" kao i za upit koji obuhvata isključivo granični pravougaonik, odzivno vrijeme za slanje inicijalnog odziva u normalnoj situaciji je najviše 30 sekundi, a takođe u normalnoj situaciji stalna brzina prenosa usluge preuzimanja iznosi više od 0,5 megabajta u sekundi ili više od 500 prostornih objekata u sekundi.
Za postupak "Opiši skup prostornih podataka" i za postupak "Opiši tip prostornog objekta" odzivno vrijeme za slanje inicijalnog odziva u normalnoj situaciji je najviše 10 sekundi, a takođe u normalnoj situaciji stalna brzina prenosa usluge preuzimanja iznosi više od 0,5 megabajta u sekundi ili više od 500 prostornih objekata u sekundi.
2.2. KAPACITET
Servis pronalaženja mora u skladu s kriterijumima kvaliteta usluge istovremeno obraditi najmanje 30 zahtjeva u sekundi.
Servis pregleda mora u skladu s kriterijumima kvaliteta usluge istovremeno obraditi najmanje 20 zahtjeva u sekundi.
Servis preuzimanja mora u skladu s kriterijumima kvaliteta usluge istovremeno obraditi najmanje 10 zahtjeva u sekundi. Broj zahtjeva koji se istovremeno obrađuju može se ograničiti na 50.
Servis transformacije mora u skladu s kriterijumima kvaliteta usluge istovremeno obraditi najmanje 5 zahtjeva u sekundi.
2.3. DOSTUPNOST
Vjerovatnost da mrežni servisi budu dostupni biće 99% vremena.
SERVIS PRONALAŽENJA
DIO A
Kriterijum pretrage
1. Servis pronalaženja će podržavati pretragu s elementima metapodataka navedenim u Tabeli 1 ovog dijela.
Tabela 1
Minimalni kriterijum pretrage
Elementi
metapodataka Ključne riječi
Ključna riječ.
Klasifikacija prostornih podataka i usluga (za skupove prostornih podataka i serije skupova prostornih podataka)
Tematska kategorija.
Klasifikacija prostornih podataka i servis (za usluge prostornih podataka)
Tip usluge prostornih podataka.
Kvalitet i ispravnost skupova prostornih podataka
Porijeklo.
Kvalitet i ispravnost skupova prostornih podataka
Prostorna rezolucija.
Stepen usklađenosti sa kriterijumima i normama
Specifikacija.
Stepen usklađenosti sa implementacionim pravilima
Stepen.
Geografska lokacija
Geografski granični pravougaonik.
Uslovi koji se primjenjuju za pristup i korišćenje skupova prostornih podataka i servisa
Uslovi koji se primjenjuju za pristup i
korišćenje.
Uslovi koji se primjenjuju na pristup i korišćenje skupova prostornih podataka i servisa
Ograničenja javnog pristupa.
Javna institucija nadležna za uspostavljanje, upravljanje, održavanje i distribuciju skupova prostornih podataka i servisa
Odgovorna strana.
Javna institucija nadležna za uspostavljanje, upravljanje, održavanje i distribuciju skupova prostornih podataka i servisa
Uloga odgovorne strane.
2. INSPIRE elementi metapodataka ili skup elemenata koji moraju biti dostupni kao kriterijum pretraživanja su i:
1. naziv izvora;
2. rezime izvora;
3. Tip izvora;
4. jedinstveni identifikator izvora; i 5. vremenska referenca.
Logički i uporedni operatori moraju biti podržani u svrhu pronalaženje izvora kroz kombinaciju kriterijuma pretrage.
Prostorni operator naveden u Tabeli 2 ovog dijela mora biti podržan u svrhu pronalaženje izvora na temelju geografske lokacije izvora.
Tabela 2
Ime operatora Svojstvo Presijek
(Intersects)
Zahtijeva da INSPIRE element metapodatka geografskog graničnog pravougaonika presijeca definisano područje interesa
DIO B
Operacije
1. LISTA OPERACIJA
1.1. Zahtjevi prema servisama pronalaženja 1.1.1. Javne institucije će uspostaviti i voditi mrežu sledećih servisa za skupove prostornih podataka i servisa za koje su metapodaci izrađeni u skladu s propisanim kriterijumima i normama:
1. Servis pronalaženja koji omogućava potragu za skupovima prostornih podataka i servisama na osnovu sadržaja odgovarajućih metapodataka kao i prikazivanje sadržaja metapodataka.
2. Servis pregleda koj omogućava, kao minimum, prikaz, navigaciju, povećanje/smanjenje, kretanje ili preklapanje za pregled dostupnih skupova prostornih podataka kao i prikaz informacija legende i bilo kojeg relevantnog sadržaja metapodataka.
3. Servis preuzimanja koji omogućava preuzimanje kopija skupova prostornih podataka ili djelova tih skupova i, gdje je prikladno,direktni pristup tim podacima.
4. Servis transformacije koji omogućava trasnformaciju skupova prostornih podataka s obzirom na postizanje interoperabilnosti.
5. Servisi koje omogućavaju pozivanje servisa prostornih podataka.
Ovi servisi moraju uzeti u obzir relevantne zahtjeve korisnika i moraju biti laki za upotrebu, raspoloživi javnosti i dostupni putem interneta ili putem bilo kojeg drugog telekomunikacionog sredstva.
1.1.2. Za potrebe servisa pronalaženja, kao minimum će se primijeniti sljedeća kombinacija kriterijuma pretrage:
1. Ključne riječi.
2. Klasifikacija prostornih podataka i servisa.
3. Kvalitet i ispravnost skupova prostornih podataka.
4. Stepen usklađenosti s kriterijumima i normama za interoperabilnost i usklađivanje skupova prostornih podataka i servisa.
5. Geografska lokacija.
6. Uslovi pristupa i korišćenja skupova prostornih podataka i servisa.
7. Javne institucije odgovorne za uspostavljanje, upravljanje, održavanje i distribuciju skupova prostornih podataka i servisa.
Servis pronalaženja pružiće operacije navedene u Tabeli 3 ovog dijela kako bi bio u skladu sa zahtjevima izraženima u tačkama 1.1.1. navedenih u Listi operacija.
Tabela 3
Operacija
Uloga Isporučuje metapodatke Usluge pronalaženja (Get Discovery Service Metadata)
Osigurava sve potrebne informacije o servisu i opisuje mogućnosti servisa
Pronađi metapodatke
(Discover Metadata)
Operacija Pronađi metapodatke omogućava traženje elemenata INSPIRE metapodataka
izvora, na osnovu izraza upita, koje treba povući iz ciljanog Servisa pronalaženja
Servis pronalaženja podržavaće operacije navedene u Tabeli 4 ovog Priloga.
Tabela 4
Operacija
Uloga Objavi metapodatke
(Publish Metadata)
Operacija Objavi metapodatke omogućava uređivanje elemenata INSPIRE metapodataka izvora u Servisu pronalaženja
(mehanizmi unošenja ili izvlačenja metapodataka - push or pull mechanisms). Uređivanje znači unošenje, ažuriranje i
brisanje.
Poveži Servis pronalaženja
(Link Discovery Service)
Funkcija Poveži servis pronalaženja omogućava izjavu o dostupnosti Servisa pronalaženja za pronalaženje izvora kroz
Servis pronalaženja zemlje dok se metapodaci izvora održavaju na lokaciji vlasnika.
Parametri zahtjeva i odaziva svake operacije dopunjavaju opis svake operacije i čine sastavni dio tehničke specifikacije Servisa pronalaženja.
2. OPERACIJA »OČITAJ METAPODATKE SERVISA PRONALAŽENJA«
2.1. Zahtjev »Očitaj metapodatke servisa pronalaženja« 2.1.1. Parametri zahtjeva »Očitaj metapodatke servisa pronalaženja« Parametri zahtjeva »Očitaj metapodatke servisa pronalaženja« navodi izvorni jezik sadržaja odziva na »Očitaj metapodatke servisa pronalaženja«.
2.2. Odziv na »Očitaj metapodatke servisa pronalaženja« Odziv na »Očitaj metapodatke servisa pronalaženja« sadržaće sledeće skupove parametara:
- metapodatke servisa pronalaženja, - metapodatke operacija, - jezike.
2.2.1. Parametri Metapodataka servisa pronalaženja Parametri Metapodataka servisa pronalaženja sadržaće barem elemente INSPIRE metapodataka Servisa pronalaženja.
2.2.2. Parametri Metapodataka operacija Parametar Metapodaci operacija pruža metapodatke o operacijama koje je sproveo Servis pronalaženja. Ti parametri metapodataka opisivaće svaku operaciju. Oni će osigurati najmanje sledeće:
1. Ukazati je li dostupan mehanizam izvlačenja ili unošenja za »Objavi metapodatke«, ili su dostupna oba mehanizma.
2. Opisati svaku operaciju, uključujući najmanje opis razmijenjenih podataka i mrežnu adresu.
2.2.3. Parametar jezika Predviđena su dva parametra jezika:
- parametar Jezik odziva koji označava prirodni jezik korišćen u parametrima odziva »Očitaj metapodatke Usluge pronalaženja«, - parametar Podržani jezici s popisom prirodnih jezika koje podržava Servis pronalaženja.
3. OPERACIJA »PRONAĐI METAPODATKE« 3.1. Zahtjev »Pronađi metapodatke« Ovaj zahtjev za pronalaženjem metapodataka sadrži sljedeće parametre:
- jezik, - upit.
3.1.1. Parametar jezika Parametar jezika ukazuje na prirodni jezik zahtijevan za sadržaj Odziva na »Pronađi metapodatke«.
3.1.2. Parametar upita Parametar upita sadržaće kombinaciju kriterijum pretrage kao što je specifikovano u dijelu A.
3.2. Odziv na »Pronađi metapodatke« 3.2.1. Parametar Odziv na »Pronađi metapodatke« Parametar Odziv na »Pronađi metapodatke« sadržaće barem elemente metapodataka svakog izvora koji odgovara upitu.
4. OPERACIJA »OBJAVI METAPODATKE« Funkcija »Objavi metapodatke« omogućava objavu elemenata metapodataka koji se odnose na izvore kroz Servis pronalaženja. Dvije su mogućnosti:
- mehanizam unošenja: omogućava uređivanje elemenata metapodataka izvora dostupnih iz Servisa pronalaženja, - mehanizam izvlačenja: omogućava Servisu pronalaženja zemlje da s udaljene lokacije izvuče elemente metapodataka izvora.
Podržaće se barem jedna od gore-navedenih mogućnosti.
4.1. Mehanizam unošenja 4.1.1. Zahtjev »Uredi metapodatke« 4.1.1.1. Parametar zahtjeva »Uredi metapodatke« Parametar zahtjeva »Uredi metapodatke« pruža sve potrebne informacije kako bi elementi INSPIRE metapodataka izvora bili unešeni, ažurirani ili izbrisani u Servisu pronalaženja.
4.2. Mehanizam izvlačenja 4.2.1. Zahtjev »Prikupi metapodatke« 4.2.1.1. Parametar zahtjeva »Prikupi metapodatke« Parametar zahtjeva »Prikupi metapodatke« pruža sve informacije o udaljenoj lokaciji potrebne kako bi se povukli dostupni metapodaci izvora. Uključuje barem elemente metapodataka dodijeljene servisu prostornih podataka.
5. OPERACIJA »POVEŽI SERVIS PRONALAŽENJA« Operacija »Poveži servis pronalaženja« omogućava izjavu o dostupnosti Servisa pronalaženja u skladu s ovim Implementacionim pravilima, za pronalaženje izvora kroz Servis pronalaženja zemlje, dok metapodaci izvora ostaju na lokaciji vlasnika.
5.1. Zahtjev »Poveži servis pronalaženja« 5.1.1. Parametar zahtjeva »Poveži servis pronalaženja« Parametar zahtjeva »Poveži servis pronalaženja« pružiće sve informacije o Servisu pronalaženja javnih organa ili treće strane u skladu sa ovim Implementacionim pravilima, omogućavaći Servisu pronalaženja zemlje da dobije metapodatke izvora, na osnovu kombinacije kriterijuma pretraživanja od Servisa pronalaženja tijela javne uprave ili treće strane, pa i da ih kombinuje s metapodatcima ostalih izvora.
SERVIS PREGLEDA
DIO A
Operacije
1. POPIS OPERACIJA
1.1. Servis pregleda pružaće operacije navedene u Tabeli 1 ovog dijela kako bi se osigurala usklađenost sa zahtjevima u tačkama 1.1.1. Priloga II, Dio B, Lista operacija.
Tabela 1
Operacija
Uloga Očitaj metapodatke Servisa pregleda
Pruža sve potrebne informacije o servisu i opisuje mogućnosti servisa
Očitaj mapu
Vraća mapu koja sadrži geografske i tematske informacije koje dolaze iz dostupnih prostornih skupova
podataka. Ova mapa je prostorno referencirana slika.
1.2. Servis pregleda će podržati operacije navedene u Tabeli 2 ovog dijela.
Tabela 2
Operacija
Uloga Poveži Servis pregleda
Omogućava javnoj instituciji ili trećoj strani objavu Servisa pregleda radi mogućnosti uvida u njene izvore kroz Servis
pregleda zemlje, dok mogućnost pregleda ostaje na lokaciji tijela javne uprave ili treće strane.
Parametri zahtjeva i odziva svake operacije dopunjuju opis svake operacije, pa čine sastavni dio tehničke specifikacije Servisa pregleda.
2. OPERACIJA »OČITAJ METAPODATKE USLUGE PREGLEDA«
2.1. Zahtjev »Očitaj metapodatke servisa pregleda«
2.1.1. Parametri zahtjeva »Očitaj metapodatke servisa pregleda«
Parametar zahtjeva »Očitaj metapodatke servisa pregleda« označava prirodni jezik zahtjevan za sadržaj Odziva na »Očitaj metapodatke servisa pregleda«.
2.2. Parametri odziva na »Očitaj metapodatke servisa pregleda«
Odziv na »Očitaj metapodatke usluge pregleda mora sadržati sledeći niz parametara:
- metapodatke servisa pregleda,
- metapodatke operacija,
- jezike,
- metapodatke slojeva.
2.2.1. Parametri metapodataka servisa pregleda Parametri metapodataka servisa pregleda moraju sadržati barem elemente metapodataka servisa pregleda.
2.2.2. Parametri metapodatatka operacija
Parametar metapodataka operacije opisuje operacije Servisa pregleda, a mora sadržati najmanje opis razmijenjenih podataka i mrežnu adresu svake operacije.
2.2.3. Parametri jezika
Moraju se osigurati dva parametra jezika:
- parametar »Jezik odziva« koji označava prirodni jezik koji se koristi u parametrima Odziva na »Očitaj metapodatke servisa pregleda«,
- parametar »Podržani jezici« koji sadrži popis prirodnih jezika koje podržava Servis pregleda.
2.2.4. Parametri metapodataka slojeva
Za svaki sloj osiguraće se elementi metapodataka navedeni u Tabeli 3 ovog dijela.
Tabela 3
Elementi metapodataka
Opis
Naziv izvora
Naziv sloja, koji se koristi za ljudsku komunikaciju, kako bi se predstavio sloj, npr. u meniju
Rezime izvora
Rezime sloja
Ključna riječ
Dodatne ključne riječi
Geografski granični pravougaonik
Najmanji granični pravouganik u svim podržanim Referentnim koordinatnim sisoblastima područja
pokrivenog slojem
Jedinstveni identifikator izvora
Jedinstveni identifikator izvora za izvor koji se koristi za stvaranje sloja
Za svaki sloj moraju se osigurati parametri specifični za sloj, navedeni u Tabeli 4 ovog dijela.
Tabela 4
Parametar
Opis Ime
Usklađeno ime sloja
Referentni koordinatni sistem
Popis Referentnih koordinatnih sistema u kojima je sloj dostupan
Stilovi
Popis stilova iscrtavanja dostupnih za sloj.
Stil se sastoji od naziva i jedinstvenog identifikatora
URL legende
Lokacija legende za svaki stil, jezik i parove dimenzija
Parovi dimenzija
Označava podržane dvodimenzionalne parove osi za višedimenzionalne skupove prostornih podataka i serije
skupova prostornih podataka
3. OPERACIJA »PRIKAŽI MAPU«
3.1. Zahtjev »Prikaži mapu«
3.1.1. Parametri zahtjeva »Prikaži mapu«
Moraju se osigurati parametri zahtjeva »Prikaži mapu« navedeni u Tabeli 5 ovog dijela.
Tabela 5
Parametar
Opis Slojevi
Popis imena slojeva koji će biti uključeni u mapi Stilovi
Popis stilova koji će se koristiti za svaki sloj Referentni koordinatni sistem
Referentni koordinatni sistem mape
Granični okvir
Četiri koordinate uglova dvodimenzionalne mape za odabrani Par dimenzija i u odabranom Referentnom
koordinatnom sistemu Širina slike
Širina mape u pikselima Visina slike
Visina mape u pikselima Format slike
Format proizvedene slike Jezik
Jezik koji će se koristiti za odziv Par dimenzija
Dvodimenzionalni sistem osa koji će se koristiti za mapu Na primjer: geografska dimenzija i vrijeme
4. OPERACIJA »POVEŽI SERVIS PREGLEDA«
4.1. Zahtjev »Poveži servis pregleda«
4.1.1. Parametar zahtjeva »Poveži servis pregleda«
Parametar zahtjeva »Poveži servis pregleda« osiguraće sve informacije o Servisu pregleda tijela javne uprave ili treće strane u skladu s ovom Odlukom, omogućavaći Servisu pregleda zemlje da preuzme mapu iz Servisa pregleda tijela javne uprave ili treće strane kao i da je kombinuje s ostalim mapama.
DIO B
Ostale karakteristike 1. Servis pregleda imaće sledeće karakteristike:
1.1. Referentni koordinatni sistem Slojevi će se moći istovremeno gledati korišćenjem jedinstvenog referentnog koordinatnog sistema, a Servis pregleda će najmanje podržavati koordinatne sisteme iz člana 6. Zakona o infrastrukturi prostornih podataka 1.2. Format slike Servis pregleda podržaće barem jedan od sledećih formata slike:
- Portable Network Graphics (PNG) format, - Graphics Interchange Format (GIF), bez kompresije.
SERVIS PREUZIMANJA
DIO A
Postupci preuzimanja
1. POPIS POSTUPAKA Tabela 1
Postupak
Uloga
Očitaj metapodatke o usluzi preuzimanja
Pruža sve potrebne informacije o usluzi, dostupne skupove prostornih podataka i opisuje mogućnosti usluge.
Očitaj skup prostornih podataka
Postupak "Očitaj skup prostornih podataka" omogućava preuzimanje skupa prostornih podataka.
Opiši skup prostornih podataka
Ovaj postupak vraća opis svih Tip prostornih objekata koji su sadržani u skupu prostornih objekata.
Poveži uslugu preuzimanja
Omogućava organu javne uprave ili trećoj strani da odredi dostupnost usluge preuzimanja za preuzimanje
prostornih podataka ili, ako je to moguće, prostornih objekata, putem usluge preuzimanja države, dok mogućnost
preuzimanja ostaje na lokaciji organa javne uprave ili treće strane.
Parametri zahtjeva i odziva svakog postupka dopunjuju opis svakog postupka i čine sastavni dio tehničke specifikacije usluge preuzimanja. 2. POSTUPAK "OČITAJ METAPODATKE O USLUZI PREUZIMANJA"
2.1. Zahtjev "Očitaj metapodatke o usluzi preuzimanja"
2.1.1. Parametar zahtjeva "Očitaj metapodatke o usluzi preuzimanja" Parametar zahtjeva "Očitaj metapodatke o usluzi preuzimanja" navodi prirodni jezik za sadržaj odziva "Očitaj metapodatke o usluzi preuzimanja".
2.2. Odziv "Očitaj metapodatke o usluzi preuzimanja" Odziv "Očitaj metapodatke o usluzi preuzimanja" sadrži sljedeće skupove parametara:
-
metapodaci o usluzi preuzimanja, -
metapodaci o postupcima, -
jezici, -
metapodaci o skupovima prostornih podataka.
2.2.1. Parametar "Metapodaci o usluzi preuzimanja" Parametar "Metapodaci o usluzi preuzimanja" sadrži barem INSPIRE elemente metapodataka o usluzi preuzimanja.
2.2.2. Parametar "Metapodaci o postupcima" Parametar "Metapodaci o postupcima" pruža metapodatke o postupcima koje sprovodi usluga preuzimanja. On sadrži barem opis svakog postupka, uključujući najmanje opis razmijenjenih podataka i mrežnu adresu.
2.2.3. Parametar "Jezici" Predviđena su dva parametra jezika:
- parametar "Jezik odziva" koji navodi prirodni jezik koji se koristi u parametrima odziva "Očitaj metapodatke o usluzi preuzimanja", - parametar "Podržani jezici" koji sadrži popis prirodnih jezika koje podržava usluga preuzimanja.
2.2.4. Parametri" Metapodaci o skupovima prostornih podataka" Osiguravaju se INSPIRE elementi metapodataka o dostupnim skupovima prostornih podataka. Osim toga, za svaki skup prostornih podataka takođe se navodi popis referentnih koordinatnih sitema iz Pravilnika o interoperabilnosti koji su na raspolaganju.
3. POSTUPAK" OČITAJ SKUP PROSTORNIH PODATAKA"
3.1. Zahtjev "Očitaj skup prostornih podataka" Zahtjev "Očitaj skup prostornih podataka" sadrži sljedeće parametre:
-
jezik, -
identifikator skupa prostornih podataka, -
referentni koordinatni sistem.
3.1.1. Parametar "Jezik" Parametar "Jezik" navodi prirodni jezik koji se traži za skup prostornih podataka.
3.1.2. Parametar "Identifikator skupa prostornih podataka" Parametar "Identifikator skupa prostornih podataka" sadrži jedinstveni identifikator izvora skupa prostornih podataka.
3.1.3. Parametar "Referentni koordinatni sistem" Parametar "Referentni koordinatni sistem" sadrži jedan od referentnih koordinatnih sistema uključenih u popis referentnih koordinatnih sistema koji su na raspolaganju na koje upućuje tačka 2.2.4.
3.2. Odziv "Očitaj skup prostornih podataka"
3.2.1. Parametar odziva "Očitaj skup prostornih podataka" Parametar odziva "Očitaj skup prostornih podataka" je traženi skup prostornih podataka na traženom jeziku i u traženom referentnom koordinatnom sistemu.
4. POSTUPAK "OPIŠI SKUP PROSTORNIH PODATAKA"
4.1. Zahtjev "Opiši skup prostornih podataka" Zahtjev "Opiši skup prostornih podataka" sadrži sljedeće parametre:
-
jezik, -
identifikator skupa prostornih podataka.
4.1.1. Parametar "Jezik" Parametar "Jezik" navodi prirodni jezik koji se traži za opis tipa prostornih objekata.
4.1.2. Parametar "Identifikator skupa prostornih podataka" Parametar "Identifikator skupa prostornih podataka" sadrži jedinstveni identifikator izvora skupa prostornih podataka.
4.2. Odziv "Opiši skup prostornih podataka"
4.2.1. Parametar odziva "Opiši skup prostornih podataka" Parametar odziva "Opiši skup prostornih podataka" je opis prostornih objekata u traženom skupu prostornih podataka i na traženom jeziku.
5. POSTUPAK "POVEŽI USLUGU PREUZIMANJA" Postupak "Poveži uslugu preuzimanja" omogućava da se utvrdi da je usluga preuzimanja na raspolaganju za preuzimanje izvora putem usluge preuzimanja države pri čemu izvor ostaje na lokaciji vlasnika.
5.1. Zahtjev "Poveži uslugu preuzimanja"
5.1.1. Parametar zahtjeva "Poveži uslugu preuzimanja" Parametar zahtjeva "Poveži uslugu preuzimanja"" pruža sve informacije o usluzi preuzimanja organa javne uprave ili treće strane, čime je usluzi preuzimanja države omogućen pristup skupovima prostornih podataka i, ako je to moguće, prostornim objektima usluge preuzimanja organa javne uprave ili treće strane.
DIO B
Postupci preuzimanja sa direktnim pristupom
6. POPIS POSTUPAKA Ako usluga preuzimanja omogućava direktan pristup skupovima prostornih podataka, on uz postupke iz Tabele 1 omogućavai postupke navedene u Tabeli 2 ovog dijela.
Tabela 2
Postupak
Uloga
Očitaj prostorni objekat
Ovaj postupak omogućava očitavanje prostornih objekata na osnovu upita.
Opiši tip prostornog objekta
Ovaj postupak daje opis navedenih tipova prostornih objekata.
Parametri zahtjeva i odziva svakog postupka dopunjavaju opis svakog postupka i čine sastavni dio tehničke specifikacije usluge preuzimanja.
7. POSTUPAK "OČITAJ PROSTORNI OBJEKAT"
7.1. Zahtjev "Očitaj prostorni objekat" Zahtjev "Očitaj prostorni objekt" podržava sljedeće parametre:
-
jezik, -
identifikator skupa prostornih podataka, -
referentni koordinatni sistem, -
upit.
7.1.1. Parametar "Jezik" Parametar "Jezik" navodi prirodni jezik koji se traži za prostorne objekte.
7.1.2. Parametar "Identifikator skupa prostornih podataka" Parametar "Identifikator skupa prostornih podataka" sadrži jedinstveni identifikator izvora traženog skupa prostornih podataka. Ako parametar nije naveden, pretpostavlja se da su odabrani svi raspoloživi skupovi prostornih podataka.
7.1.3. Parametar "Referentni koordinatni sistem" Parametar "Referentni koordinatni sistem" sadrži jedan od referentnih koordinatnih sistema uključenih u popis referentnih koordinatnih sistema iz Pravilnika o interoperabilnosti.
7.1.4. Parametar "Upit" Parametar "Upit" sastoji se od kriterijuma pretrage iz popisa navedenog u dijelu C.
7.2. Odziv "Očitaj prostorni objekat" Odziv "Očitaj prostorni objekat" sadrži sljedeće parametre:
-
skup prostornih objekata, -
metapodaci o skupu prostornih objekata.
7.2.1. Parmetar "Skup prostornih objekata" Parametar "Skup prostornih objekata" je skup prostornih objekata u skladu s Pravilnikom o interoperabilnosti na traženom jeziku i u referentnom koordinatnom sistemu koja ispunjava kriterijume pretrage iz upita.
7.2.2. Parametar "Metapodaci o skupu prostornih objekata" Parametar "Metapodaci o skupu prostornih objekata" sadrži barem INSPIRE elemente metapodataka o skupu prostornih objekata.
8. POSTUPAK "OPIŠI TIP PROSTORNOG OBJEKTA"
8.1. Zahtjev "Opiši tip prostornog objekta" Zahtjev "Opiši tip prostornog objekta" sadrži sljedeće parametre:
-
jezik, -
tip prostornog objekta.
8.1.1. Parametar "Jezik" Parametar "Jezik" navodi prirodni jezik koji se traži za opis tipa prostornog objekta.
8.1.2. Parametar "Tip prostornog objekta" Parametar "Tip prostornog objekta" sadrži jezičko neutralnu oznaku za tip prostornog objekta u skladu s Pravilnikom o interoreabilnosti. Ako parametar nije naveden, pretpostavlja se da su odabrane sve tipa prostornih objekata.
8.2. Odziv "Opiši tip prostornog objekta"
8.2.1. Parametar odziva "Opiši tip prostornog objekta" Parametar odziva "Opiši tip prostornog objekta" je opis tipa prostornog objekta u skladu s Implementacionim pravilima za interoperabilnost.
DIO C
Kriterijum pretrage za postupak "Očitaj prostorni objekat" Za potrebe postupka "Očitaj prostorni objekat" usluge preuzimanja primjenjuju se sljedeći kriterijumi pretrage:
- jedinstveni identifikator izvora skupa prostornih podataka, - svi relevantni ključni atributi i odnos između prostornih objekata iz Implementacionih pravila za interoperabilnost, a posebno jedinstveni
identifikator prostornog objekta i karakteristike vremenske dimenzije, uključujući i datum poslednjeg ažuriranja, - granični pravougaonik, izražen u bilo kojem od referentnih koordinatnih sistema iz Implementacionih pravila za interoperabilnost - tema prostornih podataka.
Kako bi se omogućilo pronalaženje prostornih objekata kombinacijom kriterijuma pretrage podržavaju se logički i uporedni operateri.
