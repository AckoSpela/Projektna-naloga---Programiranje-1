# Projektna-naloga---Programiranje-1
Projektna naloga pri predmetu Programiranje 1 - analiza podatkov o študentski prehrani.
=======================================================================================

Analizirala bom restavracije s študentsko prehrano na strani
[Študentska prehrana](https://www.studentska-prehrana.si/sl/restaurant).

Za vsako restavracijo bom zajela:
* ime restavracije
* lokacijo
* doplačilo in ceno obroka
* lastnosti restavracije (dostopnost za invalide, ponuja vegetarijanske obroke, kosila, ima dostavo ...)

Delovne hipoteze:
* Več dodatnih lastnosti, kot ima restavracija, dražji je obrok.
* Restavracije, ki ponujajo vegetarianske ali celiakiji prijazne obroke, so v povprečju dražje od tistih, ki tega ne ponujajo.
* V Ljubljani restavracije v povprečju ponujajo več dodatnih lastnosti, kot drugje po Sloveniji.
* V turistično bolj obiskanih krajih je cena obroka v povprečju višja.


_____________________________________________________________

V repozitoriju so tri CSV datoteke. Datoteka 'restavracije.csv' vsebuje podatke o restavracijah na strani (id (po katerem so restavracije sortirane), ime, naslov, kraj, cena obroka in doplačilo), 'lastnosti.csv' pa vsebuje lastnosti restavracij (dostopnost za invalide, ponuja vegetarijanske obroke, kosila, ima dostavo ...) razvrčene po id-ju restavracij. Obe datoteki sem zajela sama. Datoteka 'turisticni_kraji.csv' je pridobljena s spletne strani [SiStat](https://pxweb.stat.si/SiStat) in vsebuje podatke o turistični obiskanosti slovenskih občin v letih 2018 in 2019.
Naloženi sta tudi dve python datoteki, ki sem ju uporabljala; 'orodja.py', ki je last profesoja Pretnarja, ter html datoteka spletne strani [Študentska prehrana](https://www.studentska-prehrana.si/sl/restaurant).
V repozitoriju je tudi datoteka z analizo zajetih podatkov in podatkov s strani [SiStat](https://pxweb.stat.si/SiStat).
