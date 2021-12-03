Prototyp webu pro organizaci https://www.lekaripomahajicesku.cz/

Mottem LPČ je "Naočkujme milion lidí posilující dávkou za týden a pomožme našim zdravotníkům."

Tohoto cíle chtějí dosáhnout mimo jiné i webovou aplikací, která:

* bude vizualizovat počet dobrovolníků v jednotlivých regionech
* umožní registraci ordinací
* umožní registraci dobrovolníkům, kteří chtějí pomoct v očkovacích centrech
* zprostředkuje nasbírané kontakty hejtmanům a centrálnímu řídícímu týmu

Aplikace Liška je prototyp webové aplikace, který vše zmíněné realizuje,
na produkci se ale neobjevil. Nakonec jsme se rozhodli pro jednodušší řešení
založené na technologiích Googlu (Forms a Sheets).

## Spuštění

Ke spuštění aplikace je nutný Docker.

Build image:

    docker-compose build

Spuštění:

    docker-compose run

Migrace (nutné spustit pouze jednou, po prvním spuštění):

    docker-compose exec app bash
    ./manage.py migrate

V prohlížeči pak navštívit http://localhost:8088/

## TODO

Jde o hrubý prototyp. Pokud by se v něm někdy pokračovalo, bude se muset doladit
spousta věcí:

* výstup pro mapovou vrstvu
* datové modely
* auth systém
* správu dat provozovateli ordinací
* kešování

Možná se budou hodit i datové podklady z https://nrpzs.uzis.cz/index.php?pg=home--download
