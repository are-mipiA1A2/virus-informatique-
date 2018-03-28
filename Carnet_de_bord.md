# CARNET DE BORD

## Mercredi 28 Février 2018 

**Recherche documentaires sur le nombres d'internautes depuis 1995 ( et recherche non aboutie de la proportion 
d'internautes infectés par un virus )**

**Modèle de base, fonction de base ( création du réseau ) en 2 parties:**
 - créer les liaisons de chaque utilisateurs 
 - créer les caractères de chaque utilisateurs 

**1er programme : équation de base => prend 2 individus: 1 infecté, un non-infecté et "regarde" comment un individu devient 
infecté**

**Discussion du modèle sur papier: choix ( provisoire ? ) des variables, du moyen de propagation ( mode d'action ) :**
 - VARIABLE GLOBALE : temps ( date de mise en ligne )(int) , connexion inter-PC (bool ?), virus (tupl)
 - PC ( infection (bool (> float pour ajouter " vaccins " ?)) , Taux de protection ( float ) , Taux de désinfection ( float )
 - Serveurs ( nombre )

## Mercredi 7 Mars 2018

2 groupes de travail:

**Chercher une bibliothèque qui permet de modéliser un réseau, => Network X : entrainement sur la bibliothèque afin de comprendre son fonctionnement**

**Création d'une fonction qui permet de créer la population ( de base ), organisation en réseau, nombre de serveurs et nombre de personnes connectées au serveur. Differenciation serveurs locaux ou globaux en fonction de la taille ( tout est généré aléatoirement)**

## Mercredi 14 Mars 2018 

2 groupes de travail:

**Manipulation de la bibliothèque Network X et début de modélisation du réseau à partir du code du 1er groupe ( création des noeuds avec des valeurs d'infection , un taux de désinfection et de protection ) et affichage des noeuds**

**Nouvelle idée: créer manuellement les serveurs globaux pour simplifier la tache :** 
- créer un dict avec ( serveurs : Google , jeux ...   ) 
- associer la connexion ( ensemble ) à la population

## Mercredi 21 Mars 2018 

2 groupes de travail:

**Constitution des liaisons "edges" entre Utilisateurs et Serveurs  à partir de la base de donnée des utilisateurs et mise en forme visuelle, mise en place de la visualisation de la propagation de l'infection en établissant un code couleur sur les noeuds :**
- beige : sain
- rouge : infecté

**Reprise du programme sur les serveurs locaux : un utilisateur ne peut être connecté qu'à un seul serveur local
Fin du réseau  ( serveur global notament ), début du programme propagation,
Recherche documentaire**

## Mercredi 28 Mars 2018

2 tableaux :

nom       type      intervalle      valeur     initiale      fixe
_________________________________________________________________
Infectiosité
