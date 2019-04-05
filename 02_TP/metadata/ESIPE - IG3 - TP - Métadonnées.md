
L'interopérabilité en géomatique - TP sur les métadonnées
------------------------------
Novembre 2016.

# Objectifs

 - comprendre le fonctionnement d'un serveur géographique
 - expérimenter le catalogage avec différents outils
 - s'essayer aux différentes façons d'administrer GeoServer

# Étapes

 1. Télécharger et "faire connaissance" avec des données de démonstration ;
 2. Renseigner cette connaissance dans des outils de catalogage ;
 3. Consommer les métadonnées.

![enter image description here](https://wiki.code4lib.org/images/1/1d/Metadata.jpg)
Source : [Code4lib](https://wiki.code4lib.org/).

______

# Faire connaissance avec les données

## Télécharger les données

 1. Télécharger plusieurs shapefiles depuis [data.gouv.fr](http://www.data.gouv.fr/fr/datasets/?q=&format=shp). Par exemple :
	- [Vidéosurveillance](http://www.data.gouv.fr/fr/datasets/videoprotection-implantation-des-cameras-551635/) ;
	- [Stations RATP](http://www.data.gouv.fr/fr/datasets/positions-geographiques-des-stations-du-reseau-ratp-ratp/)
	- [Stations Transilien](http://www.data.gouv.fr/fr/datasets/cartographie-openstreetmap-des-gares-transilien/)
	- [Vélib](http://www.data.gouv.fr/fr/datasets/velib-paris-et-communes-limitrophes-idf/)

 2. Extraire dans un dossier */sample_geodataset/*

## Explorer les données

 - lire leurs descriptions et les sites liés
 - les ouvrir et tenter de répondre aux questions que pourrait se poser potentiellement un utilisateur ayant besoin de chacune des données

# Cataloguer les données

Une fois la connaissance rassemblée, il est temps de l'intégrer dans un outil de catalogage.

## Documenter une donnée avec GéoSource (~GeoNetwork)

Utiliser [le site de démonstration du BRGM](http://www.geosource.fr/) pour créer une fiche de métadonnées sur chacun des jeux de données.

## Documenter avec CKAN

Utiliser [le site de démonstration](http://ckan.org/).

## Documenter une donnée avec Isogeo

### Scanner les données

En se basant sur [l'aide en ligne](http://help.isogeo.com/fr/features/scan_fme/scanFME_process.html).

### Documenter

En 3 grandes étapes :

 2. [Étiqueter ](http://help.isogeo.com/fr/features/documentation/md_classify.html) ;
 3. [Éditer par lot](http://help.isogeo.com/fr/features/documentation/md_edit_batch.html) ;
 4. [Édition unitaire](http://help.isogeo.com/fr/features/documentation/md_edit_single.html).

En bonus, inventorier un service OGC et lier l'une de ses couches aux métadonnées des données.

### Partager 

[Aux applications](http://help.int.hq.isogeo.fr/fr/features/admin/shares.html) :

 - CSW
 - OpenCatalog
 - API ESIPE

## Bonux : documenter avec d'autres outils

Au choix :

 - [l'éditeur INSPIRE officiel](http://inspire-geoportal.ec.europa.eu/editor/) ;
 - QGIS : propriétés projet, propriétés de chaque couche, QShpere
 - Esri : ArcCatalog
 - [CatMDEdit ](http://catmdedit.sourceforge.net/)
 - [Expire](https://sourceforge.net/projects/expire/)
 - [Metadator](https://github.com/Guts/Metadator) (PJ)
____

# Consommer les métadonnées

Les métadonnées sont un moyen d'accéder aux données. Leur finalité est donc de servir des usages précis :

 - effectuer des recherches filtrées ;
 - connaître les dernières données mises à jour depuis la dernière fois ;
 - ajouter la donnée à une carte ;
 - consulter les informations complètes ;

## Via CSW

Utiliser différents moyens :

 - le client CSW de QGIS ;
 - [utiliser GDAL](http://gdal.org/drv_csw.html) ;
 - [utiliser OWSLib](https://geopython.github.io/OWSLib/#csw)
 

## Utiliser l'API Isogeo

### Présentation rapide

API REST en lecture, authentifiée via oAuth2.

### Avec Python

 1. Créer un nouvel environnement virtuel, puis installer la bibliothèque Python :

	```python
	pip install isogeo_pysdk
	```

 2. Configurer un fichier settings.ini à partir du modèle et avec les clés d'API transmises.

En se basant sur les exemples disponibles dans le code source, réaliser les tâches suivantes :

 - exporter les métadonnées au format XML
 - ajouter un donnée à QGIS via la métadonnée, via le plugin et via un script


### En Java

[Exemple en JEE](https://github.com/TSIG15/CHIMN/tree/master/src).

----------


# Ressources

 - [site officiel de GeoNetwork](http://geonetwork-opensource.org/) ;
 - [documentation officielle de l'utilisation de GeoNetwork](http://geonetwork-opensource.org/manuals/trunk/fra/users/index.html) ;
 - [interface d'administration d'Isogeo](https://app.isogeo.com) ;
 - [documentation officielle d'Isogeo](http://help.isogeo.com/) ;
________

> Sources officielles du cours : https://github.com/Guts/ESIPE_IG3_2016

> Contenu rédigé avec [StackEdit](https://stackedit.io/).