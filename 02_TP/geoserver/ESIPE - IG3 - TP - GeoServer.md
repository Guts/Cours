

Les services web géographiques - TP sur GeoServer
------------------------------
Octobre 2017.

# Objectifs

## Globaux

 - comprendre la place d'un serveur géographique dans une infrastructure de données spatiales (IDS)
 - situer les enjeux autour des services dans l'écosystème

## Techniques 

 - prendre en main la configuration et l'administration d'un serveur géographique (GeoServer)
 - s'essayer aux différentes façons d'administrer GeoServer

# Étapes

 1. Installer et configurer GeoServer
 2. Connecter GeoServer à des sources de données existantes
 3. Manipuler les différents services sur les données ajoutées
 4. Configuration avancée : les styles
 5. Configuration avancée : l'authentification sur les services
 6. Manipuler GeoServer avec son API REST

![enter image description here](https://boundlessgeo.com/wp-content/uploads/2016/11/GeoServer-Graphic1-e1447277233800.png)
Source : [Boundless](https://boundlessgeo.com/geoserver/).

# Installer et configurer GeoServer

GeoServer est développé en Java et a donc besoin d'un serveur et d'un interpréteur compatible.

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

> Adapter le chemin sur la machine hôte pour le volume

```bash
docker run -d -p 8080:8080 -v /your/host/data/path:/geoserver_data/data camptocamp/geoserver:2.13
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

> Source : https://hub.docker.com/r/winsent/geoserver/

## Importance et structure du dossier de données _data_dir_

### Le *data_dir* au centre du fonctionnement de GeoServer

Comme son nom nom l'indique, il s'agit du dossier des données persistantes de GeoServer, y compris les paramètres de configuration.

Pour un usage en production, comme d'ailleurs pour toute architecture sur le [modèle client-serveur tripartite](https://fr.wikipedia.org/wiki/Architecture_trois_tiers), il est recommandé de bien séparer *le data_dir* du reste de l'installation l'application.

### Structure du *data_dir*

Si l'interface graphique d'administration et l'API REST de configuration ont diminué l'intérêt de la connaissance de la structure détaillée du *data_dir*, c'est important d'en connaître les grandes lignes pour mieux gérer les cas problématiques.

Pour en savoir plus, consulter [la page de la documentation officielle dédiée à la structure du data_dir](http://docs.geoserver.org/stable/en/user/datadirectory/structure.html).

Dans le *data_dir*, on retrouve l'ensemble des fichiers utilisés par GeoServer :

- les données stockées en fichiers évidemment
- configuration (accès, styles, projections personnalisées...)
- logs
- plugins
- les bibliothèques tierces utilisées pour les fonctionnalités de démonstration (OpenLayers notamment)


________

# Prise en main

Une fois installé, se rendre sur [l'interface d'administration](http://localhost:8080/geoserver).

## Renseigner les informations de base

Les serveurs géographiques ont, par définition, vocation à être publiés. Comme toute publication, il faut en indiquer les "mentions légales".
La première étape de la configuration consiste donc à renseigner les métadonnées sur le serveur et les services.

### Le point de contact

1. Renseigner [le point de contact du serveur géographique](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.admin.ContactPage).

=> Constater le changement dans les *GetCapabilities* dans le navigateur.

### Les métadonnées des services

Chaque service peut être décrit et documenté de façon à exposer ses capacités de la manière la plus précise possible.

#### Au niveau global

Documenter les métadonnées globales des différents services :

 - [CSW](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.csw.web.CSWAdminPage)
 - [WCS](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.wcs.web.WCSAdminPage)
 - [WFS](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.wfs.web.WFSAdminPage)
 - [WMS](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.wms.web.WMSAdminPage)
 - [WMTS](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.gwc.web.wmts.WMTSAdminPage)

Constater les impacts sur :

 - les *GetCapabilities*
 - le dossier *data_dir*.

#### Au niveau d'un espace de travail

 1. Activer le service WFS sur un espace de travail, [*cite*](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.workspace.WorkspaceEditPage?7&name=cite) par exemple (créé automatiquement à l'installation de GeoServer)
 2. Configurer et documenter spécifiquement [le service WFS de cet espace de travail](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.wfs.web.WFSAdminPage?9&workspace=cite).


Constater les impacts sur :

 - les *GetCapabilities* du [WFS global](http://localhost:8080/geoserver/ows?service=wfs&version=2.0.0&request=GetCapabilities) et du [WFS de l'espace de travail](http://localhost:8080/geoserver/cite/ows?service=wfs&version=2.0.0&request=GetCapabilities) ;
 - le dossier *data_dir* et les sous-dossiers correspondant à l'espace de travail.

## Principes généraux

### Organisation des données

Dans GeoServer, les données sont compartimentées selon une arborescence à 3 niveaux :

- **Espace de travail (*workspace*) :** équivalent d'un répertoire virtuel pouvant contenir un ou plusiuers entrepôts

- **Entrepôt (*datastore*) :** regroupement des couches de même type (vecteur ou ratser) et de même format de stockage (PostGIS, dossier de shapefiles, ) des données de même type (vecteur ou raster). Les entrepôts définissent une source de données et la décrivent (texte de description de la donnée et page de codes de la source de données, utiles pour les dbf des shapefiles par exemple).

- **Couche (*layer*) :** les couches sont un moyen de présenter les données des entrepôts, en précisant sa « bounding box » (son emprise), et en affectant un style d'affichage de ces données (en attribuant l'un des styles gérés par Geoserver par ailleurs). L'identifiant unique d'une couche est ainsi composé : "nom_workspace:nom_couche".

En plus de ces types liés à l'organisation des données, il est possible de créer des **groupes ou agrégats de couches** (*layerGroup*) : ils permettent de servir plusieurs couches ordonnées d'une seule requête WMS de façon indépendante aux espaces de travail et des entrepôts.

Schéma résumant les concepts (source: [Boundless](http://workshops.boundlessgeo.com/geoserver-intro/overview/concepts.html)) :

![enter image description here](http://workshops.boundlessgeo.com/geoserver-intro/_images/concepts.png)

### Aperçu et consommation des services

Pour avoir un aperçu du rendu des couches, GeoServer embarque un OpenLayers pour la [prévisualisation des couches](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.demo.MapPreviewPage).

# Connecter GeoServer à des sources de données existantes

## Créer un espace de travail

### Via l'interface graphique

 1. Créer le workspace ESIPE_IG3
 2. Cocher la valeur par défaut, définir l'espace de nommage (http://esipe.u-pem.fr/ par exemple) et activer tous les services.

=> Observer l'impact dans le dossier `data_dir/workspaces`.

### Directement dans le data_dir

 1. Créer un sous-dossier `data_dir/workspaces/manual_wks` ;
 2. Y créer un premier fichier workspace.xml contenant :

	```xml
	<workspace>
	  <id>WorkspaceInfoImpl--570ae188:124761b8d78:-7ffd</id>
	  <name>manual_workspace</name>
	</workspace>
	```
 3. Y créer un second fichier namespace.xml contenant :

	```xml
	<namespace>
	  <id>NamespaceInfoImpl--570ae188:124761b8d78:-7ffe</id>
	  <prefix>manual_workspace</prefix>
	  <uri>http://esipe.u-pem.fr/</uri>
	</namespace>
	```

 4. Redémarrer GeoServer.

=> Observer la liste des espaces de travail dans l'interface d'administration.

## Ajouter des données stockées en fichiers

### Dossier de shapefiles

 1. Télécharger plusieurs shapefiles depuis [data.gouv.fr](http://www.data.gouv.fr/fr/datasets/?q=&format=shp). Par exemple :
	 - [Vidéosurveillance](http://www.data.gouv.fr/fr/datasets/videoprotection-implantation-des-cameras-551635/) ;
	 - [Stations RATP](http://www.data.gouv.fr/fr/datasets/positions-geographiques-des-stations-du-reseau-ratp-ratp/)
	 - [Stations Transilien](http://www.data.gouv.fr/fr/datasets/cartographie-openstreetmap-des-gares-sncf-transilien-en-ile-de-france-1/)
	 - [Vélib](http://www.data.gouv.fr/fr/datasets/velib-paris-et-communes-limitrophes-idf/)
 2. Déposer les shapefiles dans un sous-dossier `datagouv_shapes` dans le *data_dir* ;
 3. Ajouter l'entrepôt correspondant ;
 4. Publier l'une des couches de données en :
	 - remplissant les métadonnées depuis la fiche source sur data.gouv (titre, résumé, mots-clés...)
	 - s'assurant que le SRS et l'emprise soient les bons

### Fichiers rasters

#### GeoTIFF

 1. Télécharger une [donnée raster de test](http://data.opengeo.org/bmreduced.tiff) ;
 2. La déposer dans le *data_dir*
 3. Publier la donnée

## Ajouter des données vectorielles stockées en SGBD

### PostGIS

 1. Créer un entrepôt de données de type PostGIS. Entrer les informations de connexion à la base locale. Si elle n'existe pas, se connecter à celle-ci :
	 - host : "postgresql-guts.alwaysdata.net"
	 - database : "guts_gis"
	 - user : "guts_player"
	 - password : à l'oral ;)
 3. Publier l'une des tables

## Ajouter des services externes (*cascading*)

### Service WMS

 1. Créer un entrepôt de données à partir du [WMS des données Corine Land Cover du MEDDE](http://clc.developpement-durable.gouv.fr/geoserver/wms?request=GetCapabilities&service=WMS).
 2. Publier l'une des couches issue de l'entrepôt clc.

### Service WFS

 1. Créer un entrepôt de données à partir du [WFS de la
    PPIGE](https://www.ppige-npdc.fr/geoserver/ows?service=wfs&version=2.0.0&request=GetCapabilities).
 2. Publier l'une des couches issue de l'entrepôt opendata.


----------

# Optimiser le cache des tuiles

## Gérer le Geowebcache intégré à GeoServer

// A VENIR //

## 



----------


# Manipuler les différents services sur les données ajoutées

Une fois les services publiés, il est temps de vérifier que leur bon fonctionnement.
 
## Dans QGIS

### Via l'interface

Référencer les différents services dans QGIS via l'interface graphique.

### Via la console Python

En s'appuyant sur [la documentation de PyQGIS](http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/loadlayer.html), charger un WMS et un WFS via la console Python intégrée.

Pour bien comprendre, il est recommandé de bien décomposer les paramètres de l'URI à passer.

### Via le plugin GeoServer Explorer

Boundless a développé un plugin pour gérer GeoServer directement depuis QGIS. L'installer, le configurer et explorer ses possibilités.

## Avec OWSLib

// A VENIR //

----------

# Styles

Les styles sont la définition de l'apparence d'affichage d'une couche, selon le format standard [SLD (Styled Layer Descriptor)](http://www.opengeospatial.org/standards/sld).

Un fichier SLD est un XML contenant la description des styles d’affichage des couches, en fonction du type de forme géométrique, des échelles de visualisation, d’une classification sur une valeur attributaire, etc. 

## Consulter les styles par défaut

Via l'interface d'administration, consulter [les styles préenregistrés](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.wms.web.data.StylePage).

## Créer un nouveau style dérivé

### Via l'interface d'administration

Créer un nouveau style à partir d'un existant et appliquer à un [symbole TTF](http://docs.geoserver.org/2.1.1/user/styling/sld-extensions/pointsymbols.html#the-ttf-marks) à la couche des caméras de surveillance.

### Via QGIS

Ouvrir une couche dans QGIS, définir un style assez avancé et l'exporter en SLD, avant de l'importer dans GeoServer.

=> Constater les limites de l'interopérabilité

### Via d'autres outils

Plusieurs outils permettent d'éditer les SLD à l'aide d'une interface graphique. [AtlasStyler](http://www.geopublishing.org/) a longtemps été une référence et encore aujourd'hui malgré l'arrêt de son développement.

----------

# L'authentification sur les services

GeoServer permet de gérer l'accès aux données et aux services selon une logique utilisateur/groupe/rôle. Il est également possible de le connecter à un service d'annuaire LDAP.

## Scénario classique d'une IDG

En se basant sur [la documentation](http://docs.geoserver.org/latest/en/user/security/index.html), mettre en place les règles suivantes :

 - 3 niveaux d'accès : administrateur, membre et anonyme
 - les administrateurs et les membres peuvent accéder en lecture à toutes les données, ainsi qu'à tous les services 
 - les membres ne peuvent pas écrire de données
 - les anonymes (non authentifiés) peuvent consulter les services de tous les espaces de travail sauf le GetFeature et le Transaction du WFS, ainsi que le GetCoverage du WCS.

Il faut donc créer :

 - Un rôle MEMBERS_ROLE ;
 - Un groupe d’utilisateur MEMBERS ;
 - Un utilisateur 'esipe' qui appartiendra au groupe MEMBERS_ROLE ayant un rôle MEMBERS ;
 - Un utilisateur 'noname_nogame' n’appartenant à aucun groupe et n’ayant aucun rôle.

Puis mettre en place les règles correspondantes sur les données et les services.

Tester le fonctionnement des services dans QGIS.

## Pour une gestion plus fine : GeoFence

Pour savoir comment aller plus loin dans la configuration de la sécurité de GeoServer, consulter [la documentation de GeoFence](http://docs.geoserver.org/latest/en/user/community/geofence-server/index.html).

----------

# Manipuler GeoServer avec son API REST

Utilisation du module existant en Python.

## Travailler dans un environnement virtuel

Créer :

```bash
virtualenv virtenv_gs
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

## Utiliser

En se basant sur la [documentation](http://boundlessgeo.github.io/gsconfig/), réaliser les opérations suivantes.

### Lecture : lister les couches publiées



### Écriture : publier un shapefile

[Exemple de shapefiles](http://www.data.gouv.fr/fr/datasets/emploi-exhaustif-statistiques-communales-idf/) à publier dans l'espace de travail ESIPE_IG3.



----------


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