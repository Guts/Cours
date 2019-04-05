Cartographier un flux Twitter
=====

Novembre 2016.

<iframe width=100% height="375" src="https://www.youtube.com/embed/UKftOH54iNU" frameborder="0" allowfullscreen></iframe>

# Objectifs

 - se connecter à un flux de données en ligne (Twitter) via une API
 - structurer et traiter les données récupérées
 - représenter les données

# Étapes

 1. Se connecter à l'API de Twitter via le module Python Tweepy
 2. Effectuer une recherche basée sur un mot-clé et un filtre spatial
 3. Récupérer et stocker les données localement dans une structure orientée pour l'usage voulu
 4. Représenter les données avec Follium

# Déroulé

## Connexion à l'API Twitter

### Identifier son programme

 1. Consulter les [conditions d'utilisation de l'API Twitter](https://dev.twitter.com/overview/terms/agreement-and-policy)
 2. [Créer son application](https://apps.twitter.com/) et récupérer :

 	- consumer_key
 	- consumer_secret
 	- token_key
 	- token_secret

Stocker les identifiants dans un fichier `settings.ini` dont la structure est la suivante :

```ini
[credentials]
ckey = 
csecret = 
tkey = 
tsecret = 

[app]
rule = @
account_screen_name = 
account_user_id = 
```

Faire en sorte que les paramètres soient chargés dans un dictionnaire (*dict*) nommé *settings* au début du script.

### Se connecter

Le module Tweepy sera utilisé pour les exemples mais de nombreux autres modules existent et peuvent être également utilisés.

Consulter [sa documentation](http://docs.tweepy.org/en/stable/).

```python
OAUTH_KEYS = {
	'consumer_key':settings.get(...,
	'consumer_secret':settings.get(...,
	'access_token_key':settings.get(...,
	'access_token_secret':settings.get(...,
	}

auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)
```

### Afficher les informations sur l'utilisateur et ses followers

En s'appuyant sur la documentation, afficher :

 - le nom de l'utilisateur affiché sur sa page de profil
 - son identifiant unique
 - son emplacement
 - le nombre de ses followers
 - le nombre de personnes qu'il suit

```python
tw_user = api.get_user('geojulien')
```

En bouclant sur la liste de ses followers, afficher :

 - le nom du follower
 - le nom de sa localisation déclarée dans son profil
 - son emplacement
 - le nombre de ses followers
 - le nombre de personnes qu'il suit
 - son fuseau horaire
 - s'il géolocalise ses tweets ou pas

### Rechercher

Pour chaque recherche, boucler sur les =< 20 premiers résultats et afficher :

 - la date de création du tweet, 
 - le texte,
 - l'identifiant de l'auteur,
 - les coordonnées géographiques du tweet, 
 - la langue du tweet

1. Effectuer une recherche vide ;
2. Effectuer une recherche vide aux alentours de l'ESIPE ;
3. Effectuer une recherche sur un mot-clé aux alentours de l'ESIPE ;
4. Effectuer une recherche vide aux alentours de l'ESIPE et étant identifiée comme positive par Twitter ;

## Stocker et structurer les données

A partir de la recherche filtrée géographiquement, générer un geojson.


Fonctionnement type :

```python
import geojson

li_objs = []

# stockage dans des objets en vue de la sérialisation
point = Point((longitude, latitude))
obj = Feature(geometry=point,
	      id=row[0].value,
              properties={"KEY": VALUE,
                              })
li_objs.append(obj)

# sérialisation en GeoJSON
featColl = FeatureCollection(li_objs)
with open("../ParisBeerWeek_participants.geojson", "w") as outfile:
    dump(featColl, outfile, sort_keys=True)

```

Vérifier le geojson sur http://geojson.io.

## Analyser l'information sémantique

La bibliothèque *[Natural Language Toolkit (NLTK)](http://www.nltk.org/)* est utilisée.

Une fois le module installée, télécharger les corpora *stopwords* et *twitter_samples*, ainsi que le modèle *punkt*.

```python
import nltk
nltk.download()
```

Ne pas oublier d'importer le module en début de script.

```python
import nltk
from nltk.corpus import stopwords
```

Une fois l'installation complète :

 - indiquer les 10 mots les plus représentés dans les tweets en français
 - supprimer les tweets contenant des références NSFW et -18 ans
 - filtrer sur les tweets positifs et négatifs en s'appuyant sur l'échantillon présent dans nltk (```from nltk.corpus import twitter_samples ```). Comparer avec les critères passés à l'API Twitter (`:)` et `:(`)
 - générer un GeoJSON dont un attribut indique s'il s'agit d'un tweet positif ou négatif

----------

# Ressources


 - [documentation sur l'API de recherche Twitter](https://dev.twitter.com/rest/public/search) ;
 -  

________

> Sources officielles du cours : https://github.com/Guts/ESIPE_IG3_2016

> Contenu rédigé avec [StackEdit](https://stackedit.io/).