![covid-19 banner](covid-banner.jpg)

# Données historiques de la COVID-19 dans la province de Québec / Historical Data about the COVID-19 in the province of Québec

[Lien vers les données en version web (HTML) / Link to datasets in web format (HTML)](https://pboardman.github.io/covid19-data-quebec/data.html)

[English version](#English)

## Francais

Le but de ce dépôt git est de rendre disponible facilement l'historique des cas de COVID-19 au Québec par région.

Les données proviennent principalement du [site du gouvernement du Québec](https://www.quebec.ca/sante/problemes-de-sante/a-z/coronavirus-2019/situation-coronavirus-quebec/) archivé sur la [Wayback Machine](https://web.archive.org/web/*/https://www.quebec.ca/sante/problemes-de-sante/a-z/coronavirus-2019/).
Les seuls chiffres qui ne proviennent pas du gouvernement sont les chiffres de nouveaux cas après le 18 mars parce qu'ils ne sont pas disponibles.

Si vous avez des informations historiques sur la COVID-19 au Québec que vous voudriez rendre disponible dans le dépôt; merci de créer un `Issue` avec l'information que vous voudriez ajouter. L'information doit être officielle.

Ce projet n'est **pas** affilié avec le gouvernement du Québec ou du Canada.

### Données disponibles

Les données sont disponibles sont:
- `region` Contient le nombre de nouveaux cas et le total des cas par région et par date.
- `total` Contient le nombre de cas total, mort total et guérison totale au Québec par date.
- `montreal` Contient le nombre de cas total par arrondissement de Montréal.

Les deux formats de données disponibles sont JSON et CSV, une version Web basique existe aussi pour consulter les informations en format graphique. Les informations sont toujours les mêmes, seulement le format change.

La version web se trouve ici:
- [region/total/montreal](https://pboardman.github.io/covid19-data-quebec/data.html)

Vous pouvez accéder aux API JSON ici:
- [region](https://pboardman.github.io/covid19-data-quebec/json/region.json)
- [total](https://pboardman.github.io/covid19-data-quebec/json/total.json)
- [montreal](https://pboardman.github.io/covid19-data-quebec/json/montreal.json)

Et en format CSV ici:
- [region](https://pboardman.github.io/covid19-data-quebec/csv/region.csv)
- [total](https://pboardman.github.io/covid19-data-quebec/csv/total.csv)
- [montreal](https://pboardman.github.io/covid19-data-quebec/csv/montreal.csv)


### Notes

- `2020-03-18` Avant le 18 mars les chiffres des nouveaux cas sont les chiffres du gouvernements du Québec, a partir du 18 mars les chiffres sont calculé comme suit parce qu'il n'y a plus d'information officiel: `total des cas aujourd'hui - total des cas hier`
- `2020-03-23` A partir du 23 mars, les "cas probables" ont été ajouté par le gouvernements du Québec. (auparavant seulement les cas confirmé étaient calculés)
- `2020-05-03` https://web.archive.org/web/20200504175646/https://www.ledevoir.com/societe/sante/578200/coronavirus-bilan-quebec-3-mai

### Sources
- [quebec.ca](https://www.quebec.ca/sante/problemes-de-sante/a-z/coronavirus-2019/?utm_source=print&utm_medium=print&utm_campaign=coronavirus_2020) (Toutes les données dans les données de `region` + total_case et total_death des données de `total`)
- [Institut national de santé publique](https://www.inspq.qc.ca/covid-19/donnees) (total_recovered, hospitalisations et ICU des données de `total`)
- [santemontreal](https://santemontreal.qc.ca/population/coronavirus-covid-19/#c36391) (Toutes les données dans les données de `montreal`)
- La photo de la bannière en haut de la page à été prise à Montréal près de la rue Notre-Dame et Dickson


## English

The point of this repository is to make easily available the historical data about COVID-19 Cases in Québec by region.

The Data in this repository comes almost entirely from the [Government of Québec website](https://www.quebec.ca/sante/problemes-de-sante/a-z/coronavirus-2019/situation-coronavirus-quebec/) archived in the [Wayback Machine](https://web.archive.org/web/*/https://www.quebec.ca/sante/problemes-de-sante/a-z/coronavirus-2019/). The only data that does not come from the governement is the number of case by day after March 23 since the information is not available.

If you have historic data converning the COVID-19 in Québec that you would like to make available in this repository just create an `Issue` with the data you want to add. The information must be official.

This project is **not** affiliated with the government of Québec or Canada.

### Available datasets

The available datasets are:
- `region` Contains the number of new case and total case, by region and by date.
- `total` Contains the number of total case, total death, and total recovery in all of Québec by date.
- `montreal` Contains the number of total case by boroughs of Montréal.

The datasets are available as either JSON or CSV format. There is also a web version meant for a quick look at the datasets. they all contains the same information, only the format changes.

The web version can be found here:
- [region/total](https://pboardman.github.io/covid19-data-quebec/data.html)

The JSON APIs are here:
- [region](https://pboardman.github.io/covid19-data-quebec/json/region.json)
- [total](https://pboardman.github.io/covid19-data-quebec/json/total.json)
- [montreal](https://pboardman.github.io/covid19-data-quebec/json/montreal.json)

And the CSV APIs are here:
- [region](https://pboardman.github.io/covid19-data-quebec/csv/region.csv)
- [total](https://pboardman.github.io/covid19-data-quebec/csv/total.csv)
- [montreal](https://pboardman.github.io/covid19-data-quebec/csv/montreal.csv)


### Notes

- `2020-03-18` Before march 18 the data about new cases come from the government of Québec, on march 18 and onward, the number are calculated like this since the information isn't available: `number of case today - number of case yesterday`
- `2020-03-23` Starting on march 23, the government switched between counting only confirmed case to counting confirmed + probable case
- `2020-05-03` https://web.archive.org/web/20200504175646/https://www.ledevoir.com/societe/sante/578200/coronavirus-bilan-quebec-3-mai


### Sources
- [quebec.ca](https://www.quebec.ca/sante/problemes-de-sante/a-z/coronavirus-2019/?utm_source=print&utm_medium=print&utm_campaign=coronavirus_2020) (all data in `region` dataset + total_case and total_death of `total` dataset)
- [Institut national de santé publique](https://www.inspq.qc.ca/covid-19/donnees) (total_recovered, hospitalisations and ICU in `total` dataset)
- [santemontreal](https://santemontreal.qc.ca/population/coronavirus-covid-19/#c36391) (all data in `montreal` dataset)
- covid-19 banner picture was taken in Montréal near Notre-Dame and Dickson streets