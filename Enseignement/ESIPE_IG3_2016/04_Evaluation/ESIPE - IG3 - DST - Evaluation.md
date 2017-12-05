GIS 2.0 - Évaluation (2h)
------------------------------
Janvier 2017.

# Évaluation

## Objectifs de l'évaluation

 - démontrer la compréhension de l'articulation des différentes technologies présentées dans le cadre d'une réponse à un besoin
 - utiliser des données géographiques de sources participatives
 - mettre en place des services géographiques
 - s'assurer des éléments de qualité et de diffusion des données géographiques

----------


# Énoncé

## Contexte

Le complexe des 2 parcs d'attractions Disneyland Paris, en situation notoire de fragilité financière (références presse [1](http://www.marianne.net/disneyland-paris-mickey-mouise-100249295.html) et [2](http://www.rtl.fr/actu/societe-faits-divers/disneyland-paris-plombe-par-les-royalties-versees-a-walt-disney-7786816558)), souhaite amorcer une nouvelle dynamique centrée sur le modèle participatif dans le but de renouveler son image et de prendre un virage sur les attractions numériques.

La société souhaite étudier la faisabilité d'une "météo" dynamique des attractions basées sur les réseaux sociaux.

![Vue aérienne du complexe Disneyland Paris](https://radiodisneyclub.fr/wp-content/uploads/2015/06/Disneyland-Paris_Plan-25-ans.png)

## Objectif global

Proposer une POC (*Proof of Concept*) d'une cartographie si possible interactive représentant dynamiquement le baromètre des impressions positives et négatives à l'échelle du complexe, de chacun des deux parcs, de chaque zone et de chaque attraction.

Dans le cadre de la POC, seul Twitter sera utilisé comme source.

## Objectifs fonctionnels

 - la cartographique web est interactive, ergonomique, responsive et facile à déployer
 - les tweets font l'objet d'une qualification par analyse sémantique (paramétrable) et d'une historisation
 - des services géographiques standardisés sont mis en place de façon à faciliter une utilisation par des partenaires
 - les données et les services sont documentés selon les exigences législatives
 - les données brutes et leurs métadonnées sont synchronisées sur http://data.gouv.fr
 - une API REST permet d'interroger les données sans accès direct à la base pour favoriser les réutilisations et le socle d'innovation

## Livrables attendus

 - établir les spécifications (fonctionnelles et techniques) de la réponse que vous envisageriez de proposer
 - réaliser tout ou partie de la POC
 - envisager la prise en compte d'autres réseaux sociaux en justifiant leur priorisation : Snapchat, Instagram, Facebook, etc.
 - envisager la prise en compte de sources autres que les réseaux sociaux (journaux...).
 - envisager les questions juridiques et les garde-fous techniques à mettre en place

## Conditions d'évaluation

 - La gestion du temps et la capacité à présenter une vision globale et claire de la réponse proposée sont pris en compte dans l'évaluation. "Choisir c'est renoncer", mais "mieux vaut renoncer que tenir un bol plein d'eau" (Lao Tseu).
 - Vous pouvez établir des binômes, l'évaluation est alors la même pour les deux personnes ;

## Ressources

 - données OpenStreetMap sur Disneyland Paris : http://overpass-turbo.eu/s/lut ou :
	
	```json
    (
	node(48.86361372526071,2.770485877990722,48.8760907210035,2.7811717987060547);
rel(bn)->.x;
way(48.86361372526071,2.770485877990722,48.8760907210035,2.7811717987060547);
  node(w)->.x;
  rel(bw);
);
out meta;

	```
________

> Sources officielles du cours : https://github.com/Guts/ESIPE_IG3_2016

> Contenu rédigé avec [StackEdit](https://stackedit.io/).
