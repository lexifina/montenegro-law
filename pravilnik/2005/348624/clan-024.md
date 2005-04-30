# Član 24
Postupak povezivanja sistema certifikovanja zasniva se na primjeni dogovorenih obrazaca za područja:
1) certifikata;
2) poruka;
3) razmjene certifikata i poruka;
4) prenosa certifikata i poruka.
Certifikat ima dogovorenu obaveznu formu utvrđenu putem Obrasca DŽ.509 v 3:1997.
Poruke uključuju:
1) zahtjev za izdavanje certifikata, koji se iskazuje putem Obrasca PKCS# 10;
2) nepotpisane/potpisane/kriptovane poruke, koje se iskazuju putem Obrasca PKCS#7;
3) podatke o potpisniku, koji se iskazuju putem Obrasca PKCS#12 ( Personal Information Edžchange Syntadž ).
Zahtjev za izdavanje certifikata zasniva se na potpisanoj PKCS#10 oblikovanoj poruci, a odgovor ( certifikat) na PKCS#7 nepotpisanoj poruci. Sistemi certifikovanja koji imaju mogućnost tehnološke podrške mogu koristiti i CMP ( Certificate Management Protocols ).
Prenos certifikata i poruka sprovodi se putem telekomunikacionih sistema, uz obaveznu upotrebu Obrasca S/MIME ( Secure Multipurpose Internet Mail Edžtensions ), odnosno SSL ( Secure Socket Layer ) protokola.
