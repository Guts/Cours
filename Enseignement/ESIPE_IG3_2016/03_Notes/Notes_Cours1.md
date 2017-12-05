# Compte Rendu du cours 1 de GIS 2.0

Aux origines : OGC, Mapserver, GPS public, WMS 1.0, PostGIS, OSM, Google Maps, Cartoweb
CartoWeb 3 : Premier framework OpenSource pour faire des applications cartographiques sur le web.

## Rappel de la chronologie des SIG

### Les premiers frémissements : 
1994 : OGC (Organisme de standardisation privé)
1996 : Mapserver
2000 : Ouverture du GPS / WMS 1.0
2001 : PostGIS
2004 : Open Street Map
2005 : Google Maps

### L'essor :
2006 : OpenLayers
2006 : OSGeo Foundation (fondation qui oeuvre pour le developpement d'outils SIG OpenSource)
2006 : WMS 1.3.0 ( norme actuelle )
2007 : iPhone 1 => soulève les problématiques d'ergonomie et de vitesse 
2007 : Norme INSPIRE
2007 : Amazon EC2/ES3

### L'écosystème :
2008 : Esri à l'OGC
2009 : OpenGeo Suite
2010 : ArcGIS Online / GeOrchestra / HTML5 (1e version)
2011 : Leaflet

### Full web & cloud :
2014 : HTML5 (version finale)
Isogeo
Data Centric Strategy
Cloud Computing

La directive INSPIRE (Infrastructure for Spatial Informations in Europe) est une directive européenne Open Data friendly
Elle a pour objectif de standardiser les données géographiques à l'échelle de l'Europe afin d'en faciliter l'exploitation.
Les données sont collectées en une seule fois, et la mise à jour est effectuée là où elle est le plus efficace
L'idée est que les données soient facile à combiner, sans discontinuité aux niveau des frontières, et partageables entre différents niveaux de résolution et d'exploitation, afin de les rendre accessibles.

## La directive INSPIRE :
-> concerne les collectivités, communes, EPCI à fiscalité propre de + de 3500 habitants
-> impose une gratuité par défaut des données ouvertes
-> propose les données dans un format standard ouvert aisément réutilisable

Un certain nombre de lois ont affecté le développement de cette directive, à savoir :
-Loi Macron
-Loi Nôtre
-Loi Valter
-Loi Numérique

Ces lois sont basées sur les rapports suivants :
-Rapport Jutand
-Rapport Trojette

## Echéancier récent et à venir de l'application de la directive :

3 décembre 2013 : métadata disponibles pour les données et services relatifs aux annexes l à 3 (types de données par importance)
25 février 2013 : données nouvelles conformes aux règlements de l'annexe 1
30 décembre 2015 : données nouvelles conformes aux règlements des annexes 2 et 3
25 février 2018 : données autres conformes au règlements spécifiant les thèmes de l'annexe 1994
30 décembre 2020 : données autres conformes au règlement spécifiant les thèmes des annexes 2 et 3

Il existe deux types de licence OpenSource (permissive ou contaminante) :
### Licence ouverte
Permet de partager, copier, réutiliser, recréer, extraire, distribuer, modifier
Restrictions : mention de la paternité
Mention obligatoire : source et date de dernière mise à jour, interdiction de dénaturation et d'altération, utilisation commerciale, garantie des droits de propriété intellectuelle, gestions des droits des tiers

### Licence ODBL (Open Data Commons Open Database Licence), qui n'est pas toujours valide dans le droit français
Permet de partager (à l'identique), copier, réutiliser, recréer, extraire, distribuer, modifier
Mention obligatoire : source et date de dernière mise à jour, interdiction de dénaturation et altération
Il s'agit d'une licence contaminante, toute donnée basée sur des données ODBL prend la licence ODBL.

### Bonnes pratiques orietées usages :
-Utiliser des API de requétage des données
-Référencement des données sur différents portails
-Utiliser des données à jour
-Utiliser des données harmonisées

### Bonnes pratiques juridiques
-Identifier la nature des données
-Clarifier la potique et la stratégie open data
-Utiliser les licences standards

### Mesurer les risques (peu nombreux)
-Logique derogatoire
-Principe de jurisprudence : ne pas créer de précedent
-Le vrai risque : gaspillage de ressourcescen publiant la donnée sans penser aux usages
