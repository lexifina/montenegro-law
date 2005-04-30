# Član 18
Kod upotrebe računarske opreme moraju se koristiti API ( Application Program Interface) programska rješenja, kojima se obezbjeđuje korišćenje bilo koje vrste smart kartica, PCMCIA ( Personal Computer Memory Card International Association ) modula, tokena i drugih uređaja.
Oprema sa ugrađenim API programskim rješenjima mora obezbijediti:
1) izradu elektronskog potpisa;
2) provjeru elektronskog potpisa;
3) oblikovanje podataka;
4) komunikaciju uređaja i podataka.
API programska rješenja moraju se zasnivati na kriptografskim obrascima:
1) PKCS#11 (CRYPTOKI, RSA) za ugradnju u uređaje i programe;
2) IDUP-API ( Independent Data Unit Protection ) za ugradnju u uređaje;
3) GSS-API ( General Security Services ) za ugradnju u programe;
4) Microsoft CryptoAPI za ugradnju u programe.
Kod upotrebe kartica Fortezza obavezna je primjena RFC 2876 ( Use of the KEA and SKIPJACK Algorithms in CMS ) Obrasca povezivanja procesa kriptovanja i procesa potpisivanja.
