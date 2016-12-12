Python (2.7.9+)
=====

Novembre 2016.

# Introduction

Python est un **langage interprété, libre, gratuit** et surtout mature et intégré dans de nombreux logiciels et systèmes (multiplateformes). De haut niveau, ses performances n'ont pas vocation à égaler celles de langages plus bas mais son code source en C/C++ lui garantit un excellent rapport qualité/prix (d'apprentissage).

Concernant la géomatique, Python est **l'un des 3 langages les plus utilisés avec le Java et le JavaScript**. Au-delà de l'aspect "religieux" parfois liés au choix du langage de développement, ces 3 langages sont assez complémentaires pour répondre à l'éventail des besoins liés aux problématiques du secteur.
De nombreuses briques logicielles de base en géomatique sont développées en C/C++ (GDAL ou le moteur de QGIS par exemple) mais le profil de ses utilisateurs n'est alors plus celui d'un/e géomaticien/ne.

De part son orientation scripting, Python est présent dans plusieurs logiciels. Notamment :
 - QGIS
 - ArcGIS (via le module arcpy)
 - gvSIG
 - FME
 - MapProxy
 - // A COMPLETER //

A noter que lorsque l'on désigne Python on parle généralement de son interpréteur en C ("C Python") mais qu'il existe d'autres implémentations de l'interpréteur : en Java ("[Jython](http://www.jython.org/)" qui tourne dans une JVM) et en .NET ("[IronPython](http://ironpython.net/)") notamment. Elles sont rarement maintenues correctement.

Enfin, le nom du langage n'a rien à voir avec le serpent mais avec les [Monty Python](https://fr.wikipedia.org/wiki/Monty_Python) :

<iframe width=100% height="430" src="https://www.youtube.com/embed/3g-g2yYR6Jk?rel=0" frameborder="0" allowfullscreen></iframe>

## Choix de la version

La branche principale est la **3** mais la 2 continue d'être maintenue, compte-tenu du nombre important de ses implémentations. C'est pourtant bien la 3 qui est à privilégier, notamment pour ses améliorations sur des points cruciaux du langage : exécution aynchrone et gestion de l'encodage en particulier.

Tenant compte de la disponibilité de certaines bibliothèques, ce cours/TP utilise la version 2.x. Ce n'est que partie remise !

[Télécharger la version](https://docs.python.org) adaptée à ses besoins.

## Gestion des modules standards et tiers

A noter qu'en dépit de sa vocation multi-plateforme, quand Python est intégré dans un système ou un logiciel, c'est rarement dans sa version standard. Par exemple, les interpréteurs intégrés dans Ubuntu excluent certaines bibliothèques standard (liées au GUI notamment).

### Gestionnaire de paquets et de dépendances

Le packaging et la gestion des dépendances n'est pas vraiment la force de Python, notamment à cause de la gestion parfois complexe des dépendances en C/C++. Cela implique souvent par l'installation de prérequis en plus du simple interpréteur, chargés d'aider à compiler ces bibliothèques :

- Debian : python-software-properties python-virtualenv python-setuptools python-dev
- Windows : [Microsoft Visual C++ Compiler for Python 2.7](https://www.microsoft.com/en-us/download/details.aspx?id=44266)

Depuis la version 2.7.10 (ou 9 ?), la distribution standard de Python intègre pip qui facilite grandement l'installation et la mise à jour des bibliothèques tierces. D'autres gestionnaires de paquets existent, comme [conda](http://conda.pydata.org/docs/index.html) par exemple qui est multilanguage.

Pour connaître les bibliothèques déjà installées sur un système ou dans un environnement virtuel, une seule commande suffit :

```bash
# afficher directement dans la console
pip list
# stocker dans un fichier texte
pip freeze > installed_libs.txt
```

Utile pour la prise en main d'un environnement mais aussi pour documenter les dépendances nécessaires à son projet, stockées par convention dans un fichier *requirements.txt*.

### Packages ou modules

Formellement, tout fichier .py est un module. Un package est une collection de modules éventuellement organisés en sous-dossiers dans lesquels se trouve systématiquement un fichier `__init__.py`.

Retenir qu'un module n'est pas forcément un package ou une partie d'un package, mais qu'un package est aussi un module.

Généralement connaître ces principes n'est pas nécessaire pour travailler en Python mais cela aide à la compréhension de l'architecture du langage et s'avère utile dans certaines situations (imports absolus ou relatifs, etc.).

### Les indispensables de la librairie standard

 - os (notamment le module path)
 - sys
 - time
 - logging
 - collections

### Les modules tiers indispensables pour la vie de tous les jours

 - pip (quand il n'est pas déjà installé)
 - virtualenv
 - [six](https://pypi.python.org/pypi/six) pour arrondir les angles entre les versions 2 et 3 de Python
 - [python-dateutil](https://dateutil.readthedocs.io/), pytz et arrow pour une manipulation complète et sympa des dates
 - [pyttk](https://pypi.python.org/pypi/pyttk) pour des interfaces graphiques bureautiques minimalistes
 - [requests](http://docs.python-requests.org/en/master/) pour manipuler les API web
 - [django](https://www.djangoproject.com/) ou [flask](http://flask.pocoo.org/) pour les applications web

### Les modules tiers indispensables pour la vie de géomaticien/ne

 - geojson, shapefly, pyshape
 - GDAL et ses différentes surcouches (rasterio, fiona...)
 - OWSLib pour les standards OGC
 - [Pandas](http://pandas.pydata.org/) et sa déclinaison [GéoPandas](http://geopandas.org/) pour tout ce qui est traitement  de volumes de données structurées importants
 - [PySAL](http://pysal.readthedocs.io/en/latest)
 - numpy pour les calculs scientifiques et comme dépendance quasi-systématique
 - [pyproj](https://jswhit.github.io/pyproj/) pour les projections
 - [jinja2](http://jinja.pocoo.org/docs) pour tout ce qui est templating

## Environnements virtuels

Ce module permet de créer des environnements isolés virtuellement du reste du système et d'utiliser un interpréteur et des dépendances spécifiques pour chaque application. La création et la gestion des environnements virtuels en font l'un des atouts du langage.

```bash
# installer
pip install --user virtualenv
# Windows Debian
virtualenv virtenv --no-site-packages
# Ubuntu
python -m venv
```

## Les caractéristiques de base

### Structure des fichiers.py

L'encodage du fichier est indiqué en commentaire dès la première ligne :

```python
# -*- coding: utf-8 -*-
```

La gestion de l'encodage est un souci récurrent dans les opération i/O avec Python. La version 3 a amélioré les choses.

Les imports s'organisent juste après une documentation succincte:

```python
"""
    Documentation succincte
"""

# Standard library
import locale
import logging  # log files
from os import listdir, walk, path         # files and folder managing
from os import environ as env, access, R_OK
import platform  # about operating systems
from sys import exit, platform as opersys
import threading    # handling various subprocesses
from time import strftime
from webbrowser import open_new

# 3rd party libraries
try:
    from osgeo import gdal
    from osgeo import ogr  # handler for vector spatial files
    from osgeo import osr
except ImportError:
    import gdal
    import ogr  # handler for vector spatial files
    import osr

from isogeo_pysdk import Isogeo
from xlwt import easyxf, Formula, Workbook  # excel writer

# Custom modules
from modules import ReadRasters    # for rasters files
from modules import ReadSHP        # for shapefiles
```

L'indentation en 4 espaces est obligatoire :

```python
class MyClass(Object):
    # attributs
    object_version = "1.2.0-beta3"

    def __init__(self):
        """Paramètres de la méthode d'instanciation de MyClass """
        # start
        logging.info('Version: {0}'.format(self.object_version))

        # basics settings
        if opersys == 'win32':
            logging.info('Operating system: {0}'.format(platform.platform()))
            self.iconbitmap('Dallas.ico')    # windows icon
            self.uzer = env.get(u'USERNAME')
            # boucle sur la méthode
            for lettre in self.uzer:
                self.adallas(lettre)
        else:
            pass
     
    def adallas(self, parametre_methode):
        """Cette phrase décrit la méthode."""
        print(parametre_methode.lower())

###### Stand alone program ########

if __name__ == '__main__':
    """Standalone execution."""
    app = MyClass()
```

Pour les bonnes pratiques, consulter [la PEP 8](https://www.python.org/dev/peps/pep-0008/) et installer les modules liés (pep8 et pyflake).

### Typage dynamique

```python
# définir la variable youpi
youpi = "Youpi!"
print(youpi, type(youpi))
> ('Youpi!', <type 'str'>)

# changer le type de la variable
youpi = 2
print(youpi, type(youpi))
> (2, <type 'int'>)
```

### Manipulation de chaînes

Formater une chaîne  :

```python
m = "M"
print("{0}erci {1} fois {0}onsieur !".format(m, 1000))
```

Toute chaîne est indexée :

```python
test = "Python"

# Mémo
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

# Démo
test[2:-1]
> 'tho'

test[2] == test[-4]
> True
```

Une chaîne de caractères est un itérable : 

```python
# parcourir et afficher chaque lettre d'une chaîne en majuscule
for lettre in test:
    print(lettre.upper())
```


### Itérables

La compréhension de liste est un des paradigmes de la programmation fonctionnelle. Ses fonctions les plus classiques sont disponibles en Python. Par exemple, créer une liste des chiffres de 0 à 19 :

```python
# via une boucle
nums_for = []
for n in range(20):
  nums.append(str(n))
print ("".join(nums))
```


```python
# avec la compréhension en liste
nums_inl = [str(n) for n in range(20)]
print ("".join(nums))
```

Exemple de fonction intégrée :


```python
# passer chaque élément d'un itérable à une fonction
def double_ca(simple):
    """Double le chiffre simple."""
    return 2 * simple

print(map(double_ca, range(10)))
```

Il est possible d'aller bien plus loin via le module itertools.


### Exercices

#### Nombres premiers

Créer automatiquement une liste des nombres premiers compris entre 0 et 1000.

#### Rechercher / remplacer

Dans [le texte de présentation de l'ESIPE](http://esipe.u-pem.fr/esipe-mlv/presentation/), remplacer toutes les voyelles par leur index dans l'alphabet :

 - A = 1
 - E = 5 
 - etc.

----------

# Ressources

 - [site officiel de Python](https://www.python.org/) ;
 - [documentation officielle](https://docs.python.org) ;
 - [Sam & Max (NSFW)](http://sametmax.com/cours-et-tutos/) ;
 - les [articles de Martin Laloux sur Portail SIG](http://www.portailsig.org/user/gene/track) ;

________

> Sources officielles du cours : https://github.com/Guts/ESIPE_IG3_2016

> Contenu rédigé avec [StackEdit](https://stackedit.io/).