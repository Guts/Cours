

Les services web géographiques - TP sur GeoServer
------------------------------
Novembre 2016.

# Objectifs

 - comprendre le fonctionnement d'un serveur géographique
 - prendre en main la configuration et l'administration d'un serveur géographique (GeoServer)
 - s'essayer aux différentes façons d'administrer GeoServer

# Étapes

 1. Installer et configurer GeoServer
 2. Connecter GeoServer à des sources de données existantes
 3. Manipuler les différents services sur les données ajoutées
 4. Configuration avancée : les styles
 5. Configuration avancée : l'authentification sur les services
 6. Manipuler GeoServer avec son API REST

# Installer et configurer GeoServer

GeoServer est développé en Java et a donc besoin d'un serveur et d'un interpréteur compatible.

## Importance et structure du dossier de données _data_dir_

### Le data_dir au centre du fonctionnement de GeoServer

Comme son nom nom l'indique, il s'agit du dossier des données persistantes de GeoServer, y compris les paramètres de configuration.

Pour un usage en production, comme d'ailleurs pour toute architecture sur le [modèle client-serveur tripartite](https://fr.wikipedia.org/wiki/Architecture_trois_tiers), il est recommandé de bien séparer le data_dir du reste de l'installation l'application.

### Structure du data_dir

Si l'interface graphique d'administration et l'API REST de configuration ont diminué l'intérêt de la connaissance de la structure détaillée du data_dir, c'est important d'en connaître les grandes lignes pour mieux gérer les cas problématiques.

Pour en savoir plus, consulter [la page de la documentation officielle dédiée à la structure du data_dir](http://docs.geoserver.org/stable/en/user/datadirectory/structure.html).

## Installation et démarrage rapide

### Debian

#### Binaire indépendant avec Jetty

 1. Télécharger et installer Java 8 JRE Oracle ;
 2. Télécharger le binaire stable ;
 3. Exécuter :

	```bash
	GEOSERVER_HOME=/usr/local/apps/geoserver/
	GEOSERVER_DATA_DIR=~/geoserver /usr/local/apps/geoserver
	/usr/local/apps/geoserver/bin/startup.sh
	du -sh geoserver/
	```

#### Application Web Java avec tomcat

```bash
# Installation de tomcat7
sudo apt-get install tomcat7

# Téléchargement et désarchivage de geoserver
cd /home/Téléchargements/
sudo wget http://downloads.sourceforge.net/geoserver/geoserver-2.10.0-war.zip
sudo unzip geoserver-2.10.0-war.zip

# Déplacement de geoserver.war
sudo mv ./geoserver.war /var/lib/tomcat/webapps

# Redémarrage de tomcat
sudo service tomcat7 restart
```

#### Personnaliser le data_dir

```bash
export GEOSERVER_DATA_DIR=/home/path_to_myCustomDataDir/
```

### Windows

Suivre [la documentation officielle](http://docs.geoserver.org/stable/en/user/installation/win_installer.html) :

1. Télécharger et installer Java 8 JRE Oracle ;
2. Télécharger l'installeur de GeoServer ;
3. Appliquer la Next Mania ;)

Une fois l'installation terminée :

1. Changer l'emplacement du data_dir dans les variables d'environnement
2. Télécharger et installer les plugins : [INSPIRE](http://docs.geoserver.org/stable/en/user/extensions/inspire/using.html#inspire-using), WPS, CSW
3. Démarrer GeoServer et ouvrir l'interface d'administration http://localhost:8080/geoserver

### Docker

Plusieurs recettes (images) de conteneurs Docker sont disponibles pour déployer facilement GeoServer. Voici une sélection.

#### Basique 

Permet de déployer :
 - Ubuntu 14.04
 - Tomcat 8
 - GeoServer 2.6.x

> Source :   https://github.com/eliotjordan/docker-geoserver

#### Avec le plugin WPS - Camptocamp

```bash
docker run -d -p 8080:8080 camptocamp/geoserver:2.9
```

> Source : https://hub.docker.com/r/camptocamp/geoserver/

#### Personnalisable - Kartoza

```bash
docker pull kartoza/geoserver
```

> Source : https://hub.docker.com/r/kartoza/geoserver/

#### Avec GDAL - OLOLO

Déploie :

 - JAI 1.1.3
 - ImageIO 1.1
 - GDAL 1.10.1

Plugins intégrés :

 - gdal
 - ogr
 - printing
 - importer


```bash
docker run -d winsent/geoserver
```

> Source : https://hub.docker.com/r/kartoza/geoserver/

________

## Prise en main

Une fois installé, se rendre sur [l'interface d'administration](http://localhost:8080/geoserver).

### Renseigner les informations de base

Les serveurs géographiques ont, par définition, vocation à être publiés. La première étape de la configuration consiste donc à renseigner les métadonnées sur le serveur et les services.

#### Le point de contact

1. Renseigner [le point de contact du serveur géographique](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.admin.ContactPage).

=> Constater le changement dans les *GetCapabilities* dans le navigateur.

#### Les métadonnées des services

Chaque service peut être décrit et documenté de façon à exposer ses capacités de la manière la plus précise possible.

Documenter les métadonnées globales des différents services :

 - [CSW](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.csw.web.CSWAdminPage)
 - [WCS](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.wcs.web.WCSAdminPage)
 - [WFS](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.wfs.web.WFSAdminPage)
 - [WMS](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.wms.web.WMSAdminPage)
 - [WMTS](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.gwc.web.wmts.WMTSAdminPage)

Constater les impacts sur :

 - les *GetCapabilities*
 - le dossier *data_dir*.

## Principes généraux

### Organisation des données

Dans GeoServer, les données sont compartimentées selon une arborescence à 3 niveaux :

- **Espace de travail (*workspace*) :** équivalent d'un répertoire virtuel pouvant contenir un ou plusiuers entrepôts

- **Entrepôt (*datastore*) :** regroupement des couches de même type (vecteur ou ratser) et de même format de stockage (PostGIS, dossier de shapefiles, ) des données de même type (vecteur ou raster). Les entrepôts définissent une source de données et la décrivent (texte de description de la donnée et page de codes de la source de données, utiles pour les dbf des shapefiles par exemple).

- **Couche (*layer*) :** les couches sont un moyen de présenter les informations des entrepôts, en précisant sa « bounding box » (son emprise), et en affectant un style d'affichage de ces données (en attribuant l'un des styles gérés par Geoserver par ailleurs)

En plus de ces types liés à l'organisation des données, il est possible de créer des **groupes de couches** (*layerGroup*) : ils permettent de servir plusieurs couches d'une seule requête WMS sans avoir à utiliser les 




### Valeurs par défaut

# Connecter GeoServer à des sources de données existantes

## Créer un espace de travail

 1. Créer le workspace ESIPE_IG3
 2. Cocher la valeur par défaut, définir l'espace de nommage (http://esipe.u-pem.fr/ par exemple) et activer tous les services.

=> Observer l'impact dans le dossier `data_dir/workspaces`.

## Ajouter des données vectorielles stockées en fichiers

### Dossier de shapefiles


### Fichiers rasters

 1. Télécharger la [donnée raster de test](http://data.opengeo.org/bmreduced.tiff) ;
 2. La déposer dans le bon dossier du data_dir

## Ajouter des données vectorielles stockées en SGBD

### PostGIS

 1. Créer
 2. un entrepôt de données de type PostGIS. Entrer les informations de connexion à la base locale. Si elle n'existe pas, se connecter à celle-ci :
	 - host : "postgresql-guts.alwaysdata.net"
	 - database : "guts_gis"
	 - user : "guts_player"
	 - paassword : à l'oral ;)

## Ajouter des services externes (*cascading*)

### Service WMS

 1. Créer un entrepôt de données à partir du [WMS des données Corine Land Cover du MEDDE](http://clc.developpement-durable.gouv.fr/geoserver/wms?request=GetCapabilities&service=WMS).
 2. Publier l'une des couches issue de l'entrepôt clc.

### Service WFS

 1. Créer un entrepôt de données à partir du [WFS de la
    PPIGE](https://www.ppige-npdc.fr/geoserver/ows?service=wfs&version=2.0.0&request=GetCapabilities).
 2. Publier l'une des couches issue de l'entrepôt opendata.


# Manipuler les différents services sur les données ajoutées
 

# Configuration avancée : l'authentification sur les services



# Manipuler GeoServer avec son API REST

## Travailler dans un environnement virtuel

Créer :

```bash
virtualenv virtenv_gs
```

Activer :

```bash
source virtenv/bin/activate
```

## Installer le module Python

Dépendances tierces :

 - httplib2 >=0.7.4
 - gisdata = 0.5.4

```bash
pip install gsconfig
```

## Ouvrir l'accès

Paramètres de la méthode :

- service_url=*str*,
- username=*str*,
- password=*str*,
- disable_ssl_certificate_validation=*bool*


```python
pip install gsconfig
```


## 



# Ressources

 - [site officiel de GeoServer](http://geoserver.org/) ;
 - [documentation officielle de l'utilisation de GeoServer](http://docs.geoserver.org/stable/en/user/) ;
 - [documentation du module Python](http://boundlessgeo.github.io/gsconfig/) sur l'API REST ;
 - [introduction à Geoserver par Boudless (en)](http://workshops.boundlessgeo.com/geoserver-intro/) ;
 - les [articles sur GeoTribu](http://geotribu.net/taxonomy/term/29) (un peu anciens) ;
 - le cours de Jean-Christophe  DESCONNETS (IRD, Montpellier) ;
 
________

> Sources officielles du cours : https://github.com/Guts/ESIPE_IG3_2016

> Contenu rédigé avec [StackEdit](https://stackedit.io/).