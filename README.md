# virus-informatique- chachou edou avec un x à la fin belette flo
Modélisation de la propagation d'un virus informatique au sein d'un ensemble d'ordinateurs et de serveurs reliés en réseau interne et publique.
Les paramètres seront entre autres:

- la date de mise en ligne du virus
- le niveau de protection de chaque usager (anti-virus)
- le niveau de complexité du virus (donc plus ou moins détecté par les anti-virus)
- le type de transmission du virus (mail, fichier vérolé, cheval de troie etc)

Cahier des charges ARE DYNAMIC

                                                  Le virus informatique
                                                  
                                                  
BAILLY Antoine
GUILY Florian
MATHEU Edouard
OUERTATANI Mohamed Achref

Le virus peux toucher un ordinntateur comment? Le virus informatique affecte de la meme facon que un virus biologique affecte le corps. en effet il existe 3 type de virus . Virus classique qui se replique dans un environement informatique vise a endommager le systeme en se comportant comme des bout de code inutiles qui vient s'implanter dans programme pour l'endommager.
Le ver informatique par contre agit et se repand dans un reseaux de machines , il est moins offensif et il sert plutot a l'espionnage et le vol d'information. Finalement , le cheval de troie qui est plutôt une platefomre qui delivre un virus ou un verre; on donne l'exemple des jeux telechargeable en ligne , ces jeux peuvent comporter le virus et a chaque fois qu'on joue le virus se propage encore plus. 
Le virus informatique peux détruire des fichier ralentir les serveur et les réseaux ,donner un acces facile a l'espionneur grâce au backdoor.

Objectifs:
- Faire une modélisation graphique de la propagation d'un virus.
- Pouvoir faire varier la modélisation par la modification de certaines variables.
- Créer des graphiques pour pouvoir visualiser la modélisation.

Problématique:
- Comment la propagation d'un virus informatique évolue-t-elle en fonction de divers facteurs ?

Questions importantes autour du sujet: 
- Comment modéliser le comportement d'un virus dans un environnement informatique ?
- Quels sont les facteurs de propagation d'un virus informatique ? Comment influencent-ils sa propagation ?
- Comment se protéger des virus informatiques ?

Phénomène principal étudié:
Le phénomène principal étudié est la propagation d'un virus informatique un réseau.

Agents : 3 agents
Interaction : Aléatoire
Dynamique : Propagation
Variables : temps , anti-virus , type de virus , nombre d'agents , nombre de nœuds ( serveurs ) , manière de transmission , détectabilité du virus.

Méthode de validation :
Le parc informatique ainsi que le niveau de protection sont en constante augmentation. Les chiffres concernants le nombre d'infecté n'est donc pas le même en fonction des années. Nous allons donc nous appuyer sur les chiffres d'inféctions de chaque année et sur le nombre d'utilisateur par année afin de validerle modèle.

import random as rd

type : individu : contamination par le virus, niveau de sécurité

virus = (0.5, 0.0, 0.0, 0.0)

def contamination(individu_1, individu_2, reseau):
    """Simule l'échange de donnée d'un individu 1 à un individu 2 dans un réseau 'reseau'"""
    infectiosité,_,_,_ = virus
    if reseau[individu_1][0] == True and infectiosité > reseau[individu_2][1]:
        reseau[individu_2][0] = True
    return reseau
    
 contamination("i1", "i8", réseau)
    
 réseau = {'i1': [True, 0.5],
 'i10': [False, 0.9],
 'i2': [False, 0.6],
 'i3': [False, 0.4],
 'i4': [False, 0.9],
 'i5': [False, 0.7],
 'i6': [False, 0.5],
 'i7': [False, 0.1],
 'i8': [True, 0.2],
 'i9': [False, 0.6]}
 
 def journée(reseau):
    "simule une journée de travail dans une entreprise nommée 'reseau'"
    #i1 : indice de l'individu 1 : int
    i1 = 0
    #i2 : indice de l'individu 2 : int
    i2 = 0
    for j in range(50):
        i1 = rd.randint(1, 10)
        i2 = rd.randint(1, 10)
        if i2 == i1:
            i2 += 1
        contamination("i"+str(i1), "i"+str(i2), reseau)
    return reseau
    
    journée(réseau)
    
    {'i1': [True, 0.5],
 'i10': [False, 0.9],
 'i2': [False, 0.6],
 'i3': [True, 0.4],
 'i4': [False, 0.9],
 'i5': [False, 0.7],
 'i6': [False, 0.5],
 'i7': [False, 0.1],
 'i8': [True, 0.2],
 'i9': [False, 0.6]}
 
 famille_Bailly = {"Antoine": [True, 0.2],
                  "Lionel": [False, 0.6],
                  "Christelle": [False, 0.3],
                  "Corentin": [False, 0.7],
                 }

famille_Regimbaud = {"Hannah": [False, 0.5],
                     "Pascal": [False, 0.5]
                    }

famille_Provendier = {"Hannah": [False, 0.5],
                      "Florence": [True, 0.1]
                     }
famille_Matheu = {"Edouard": [False, 0.9],
                  "Valou": [False, 0.4],
                  "Vincent": [False, 0.6]
                 }
rectorat_académie_de_Versailles = {"Vincent": [False, 0.6],
                                   "i1": [True, 0.5],
                                   "i2": [False, 0.6],
                                   "i3": [False, 0.4],
                                   "i4": [False, 0.9],
                                   "i5": [False, 0.7],
                                   "i6": [False, 0.5],
                                   "i7": [False, 0.1],
                                   "i8": [False, 0.2],
                                   "i9": [False, 0.6],
                                   "i10": [False, 0.9]
                                  }
                                  

réseau = {"i1": [True, 0.5],
          "i2": [False, 0.6],
          "i3": [False, 0.4],
          "i4": [False, 0.9],
          "i5": [False, 0.7],
          "i6": [False, 0.5],
          "i7": [False, 0.1],
          "i8": [False, 0.2],
          "i9": [False, 0.6],
          "i10": [False, 0.9]
         }
type : virus = infectiosité, transmissibilité, discrétion, ...
[{'Antoine': [True, 0.2],
  'Christelle': [False, 0.3],
  'Corentin': [False, 0.7],
  'Lionel': [False, 0.6]},
 {'Hannah': [False, 0.5], 'Pascal': [False, 0.5]},
 {'Florence': [True, 0.1], 'Hannah': [False, 0.5]},
 {'Edouard': [False, 0.9], 'Valou': [True, 0.4], 'Vincent': [False, 0.6]},
 {'Vincent': [False, 0.6],
  'i1': [True, 0.5],
  'i10': [False, 0.9],
  'i2': [False, 0.6],
  'i3': [True, 0.4],
  'i4': [False, 0.9],
  'i5': [False, 0.7],
  'i6': [False, 0.5],
  'i7': [False, 0.1],
  'i8': [False, 0.2],
  'i9': [False, 0.6]}]





