TP - Créer une API REST avec Django REST Framework
------------------------------
Novembre 2017.

## Objectifs

Comprendre le fonctionnement d'une API REST en expérimentant sa mise en place complète, par exemple dans le cadre d'un blog.

## Étapes

 1. Installer et configurer Django REST Framework
 2. Documenter l'API

# TP

Créer une simple API en lecture seulement afin de récupérer toutes les données disponibles sur un blog :

 - Articles
 - Catégories
 - Tags

## Installer

Dans un environnement virtuel (` python -m venv virtenv` sur Windows) :

```bash
pip install django
pip install djangorestframework django_rest_swagger markdown djangorestframework-filters
```

Sauvegarder les dépendances dans un fichier dédié :

`pip freeze > requirements.txt`

### Démarrer le projet et l'application Django

```
django-admin startproject placesapi
cd placesapi
python manage.py startapp blog_site
python manage.py startapp api
python manage.py makemigrations
python manage.py migrate
```


Éditer le fichier placesapi/settings.py pour ajouter les 2 applications :

```python
# ~lines 33
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party
    "cities_light",
    # project,
    "blog",
    "api"
]

# ~lines 126
\# CITIES LIGHT

CITIES_LIGHT_TRANSLATION_LANGUAGES = ['fr', 'en']
CITIES_LIGHT_INCLUDE_COUNTRIES = ['BEL', 'FR']
CITIES_LIGHT_INCLUDE_CITY_TYPES = ['PPL', 'PPLA', 'PPLA2', 'PPLA3',
                                   'PPLA4', 'PPLC', 'PPLF', 'PPLG', 'PPLL', 'PPLR', 'PPLS', 'STLMT', ]

```

Structurer la base de données :

```
python manage.py makemigrations
python manage.py migrate
```

Créer le super admin :

`python manage.py createsuperuser --email admin@example.com --username admin`


Arborescence attendue :

- dossier migrations,
- fichiers : 
	- models.py,
	- views.py,
	- apps.py,
	- tests.py,
	- admin.py

## Concepts généraux

### Les viewsets

Les viewsets vont jouer le rôle de vues (MVC). Elles vont permettre de requêter la base de données en fonction d'une requête donnée, on peut les comparer à des controllers dans le pattern MVC.

Dans ces viewsets vous aurez donc des méthodes telles que :

 - get
 - post
 - list
 - create

Plusieurs types existents : Generic, ModelViewSet, ReadOnlyModelViewset, etc.

Utiliser principalement ReadOnlyModelViewSet afin d'avoir un viewset spécifique à mon modèle et limitant les actions sur cette entrée de l'API à la lecture. 


### Les serializers

Les *serializers* permettent de... sérialiser les instances en JSON et transformer le JSON en instance Python, à l'instar des formulaires Django.

Créer puis éditer `api/serializers.py` :

```python
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
```

### Les vues


Éditer `api/views.py` :

```python
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer 
```

### Les URLs

from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


## Documentation API

Afin que tout développeur puisse consommer (aisément) notre API, il est important d'y apporter de la documentation.

Pour cela, nous allons installer swagger qui est un générateur automatique de documentation. Il va permettre de montrer les urls disponibles pour les requêtes HTTP, mais aussi le type de retour de chaque champs de notre JSON, etc, etc...

Pour cela, on va commencer par ajouter django_rest_swagger dans notre requirements.txt ou avec pip c'est comme vous voulez.

En suite on va ajouter 'rest_framework_swagger' à notre liste d'applications django dans le settings.py.

Et pour finir, nous allons inclure les urls swagger dans notre urls.py

#juanwolf_s_blog/urls.py
urlpatterns = [
    '',
    r'^api/docs/', include('rest_framework_swagger.urls')),
    r'^api/', include('api.urls'))
]

Et bim voilà le résultat ! https://blog.juanwolf.fr/api/docs/
The End

C'est terminé pour notre petit tour d'horizon du django rest framework, j'espère que ça vous a plu ! Si jamais vous voulez entrer plus en détail sur le sujet, je vous invite à vous rendre sur le site du django rest framework qui est très bien documenté ! Sur ce, Codez bien !

Merci d'avoir lu cet article ! N'hésitez pas à laisser votre avis dans les commentaires ci-dessous ou si vous vous sentez généreux et prêt à être gracieusement remercié de ma part, voici mon Flattr !

----------

# Ressources

 - [Site officiel de Django](http://geoserver.org/) ;
 - [Site officiel de Django REST Framework](http://www.django-rest-framework.org/) ;
 - [Tutoriels sur DRF par Makina Corpus](https://makina-corpus.com/blog/metier/2015/django-rest-framework-les-serializer-et-les-exceptions-partie-1) ;
 - [documentation du client Python pour l'API GeoServer](http://boundlessgeo.github.io/gsconfig/) ;
 - [bonnes pratiques d'une API](https://github.com/interagent/http-api-design) ;
 - [tutoriel complet sur la conception d'une API REST](http://www.restapitutorial.com/);
 
________

> Sources officielles du cours : https://github.com/Guts/ESIPE_IG3
> Rédigé avec [StackEdit](https://stackedit.io/).