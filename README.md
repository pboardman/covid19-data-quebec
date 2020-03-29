# Données historiques de la COVID-19 dans la province de Québec / Historical Data about the COVID-19 in the province of Québec

[English version](#English)

## Francais

Le but de ce dépôt git est de rendre disponible facilement l'historique des cas de COVID-19 au Québec par région.

Les données contenu dans le fichier `covid19-case-qc.csv` proviennent principalement du [site du gouvernement du Québec](https://www.quebec.ca/sante/problemes-de-sante/a-z/coronavirus-2019/situation-coronavirus-quebec/) archivé sur la [Wayback Machine](https://web.archive.org/web/*/https://www.quebec.ca/sante/problemes-de-sante/a-z/coronavirus-2019/).
Les seuls chiffres qui ne proviennent pas du gouvernement sont les chiffres de nouveaux cas après le 18 mars parce qu'ils ne sont pas disponibles.

Si vous avez des informations historiques sur la COVID-19 au Québec que vous voudriez rendre disponible dans le dépôt; merci de créer un `Issue` avec l'information que vous voudriez ajouter. L'information doit être officielle.

Ce projet n'est **pas** affilié avec le gouvernement du Québec ou du Canada.

### Information relié aux données

- `2020-03-18` Avant le 18 mars les chiffres des nouveaux cas sont les chiffres du gouvernements du Québec, a partir du 18 mars les chiffres sont calculé comme suit parce qu'il n'y a plus d'information officiel: `total des cas aujourd'hui - total des cas hier`
- `2020-03-23` A partir du 23 mars, les "cas probables" ont été ajouté par le gouvernements du Québec. (auparavant seulement les cas confirmé étaient calculés)

## English

The point of this repository is to make easily available the historical data about COVID-19 Cases in Québec by region.

The Data contained in the `covid19-case-qc.csv` comes almost entirely from the [Government of Québec website](https://www.quebec.ca/sante/problemes-de-sante/a-z/coronavirus-2019/situation-coronavirus-quebec/) archived in the [Wayback Machine](https://web.archive.org/web/*/https://www.quebec.ca/sante/problemes-de-sante/a-z/coronavirus-2019/). The only data that does not come from the governement is the number of case by day after March 23 since the information is not available.

If you have historic data converning the COVID-19 in Québec that you would like to make available in this repository just create an `Issue` with the data you want to add. The information must be official.

This project is **not** affiliated with the government of Québec or Canada.

### Information related to the data in this repository

- `2020-03-18` Before march 18 the data about new cases come from the government of Québec, on march 18 and onward, the number are calculated like this since the information isn't available: `number of case today - number of case yesterday`
- `2020-03-23` Starting on march 23, the government switched between counting only confirmed case to counting confirmed + probable case