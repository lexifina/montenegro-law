# Član 28
## Elektronski imenici
Svi potpisnici i subjekti sistema certifikovanja upisuju se u elektronske imenike.
Usluge elektronskih imenika zasnivaju se na primjeni Obrasca ITU- T DŽ.500:2001 (Directory Service) -ISO/IEC 9594:2001 ili LDAP v 3 ( RFC 2251 Lightnjeight Directory Access Protocol ) putem jedinstvene strukture ( DIT -Directory Information Tree ).
Nazivi subjekata u elektronskom imeniku (DN) kodiraju se po Obrascu ASN.l i moraju biti izraženi podskupom atributa koji obezbjeđuje jedinstvenost naziva subjekta (DN), sa liste atributa prema RFC 3739 LJualified Certificate Profile:
1) komponenta domena (domainComponent);
2) naziv države ( countryName; nazivi i oznake u skladu sa Obrascem ISO 3166- 1: 1997+Alpha 2 )
3) uobičajeno ime ( commonName );
4) prezime (surname);
5) ime po rođenju (givenName);
6) pseudonim ( pseudonym );
7) serijski broj ( serialNumber );
8) titula ( title );
9) naziv organizacije/pravnog lica (organizationName );
10) naziv organizacione jedinice (organizationalUnitName );
11) naziv Republike (stateOrProvinceName);
12) mjesto/adresa (localityName);
Sadržaj elektronskog imenika mora biti izrađen primjenom Obrasca kodiranja ISO/IEC 10646 -1 :2000 Universal Multiple Octet Coded Character Set ( UCS ) -Basic Multiple Plane ( BMP ), odnosno u skladu sa obrascem UTF-8.
