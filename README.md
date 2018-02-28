# virus-informatique-
Modélisation de la propagation d'un virus informatique au sein d'un ensemble d'ordinateurs et de serveurs reliés en réseau interne et publique.
Les paramètres seront entre autres:

- la date de mise en ligne du virus
- le niveau de protection de chaque usager (anti-virus)
- le niveau de complexité du virus (donc plus ou moins détecté par les anti-virus)
- le type de transmission du virus (mail, fichier vérolé, cheval de troie etc)

Cahier des charges ARE DYNAMIC

                                                  Le virus informatique
                                                  
                                                  
- BAILLY Antoine
- GUILY Florian
- MATHEU Edouard
- OUERTATANI Mohamed Achref

Comment le virus peut-il toucher un ordinateur? Le virus informatique affecte de la même facon qu'un virus biologique affecte un corps. En effet, il existe 3 types de virus:
- Le virus classique qui se réplique dans un environnement informatique vise a endommager le systeme en se comportant comme des bouts de code inutiles qui viennent s'implanter dans le programme pour l'endommager.
- Le ver informatique par contre agit et se répand dans un réseaux de machines , il est moins offensif et il sert plutôt à l'espionnage et le vol d'information.
- Le cheval de Troie qui est plutôt une plateforme qui délivre un virus ou un ver; on donne l'exemple des jeux telechargeables en ligne, ces jeux peuvent contenir le virus et à chaque fois qu'on joue, le virus se propage encore plus. 
Le virus informatique peux détruire des fichiers, ralentir les serveurs et les réseaux, donner un accès facile à l'espion grâce au backdoor.

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

- Agents : 3 types d'agents : PC , Serveurs , Virus
- Interaction : Aléatoire
- Dynamique : Propagation
- Variables : VARIABLES GLOBALES : temps, connexion inter-PC
              - PC ( Infection, Antivirus , (???)) 
              - Serveurs ( Nombre, Type de serveurs, Probabilité d'infection à partir de ce serveur ) 
              - Virus ( Type de virus, Manière de transmission, Détectabilité )


Méthode de validation:
Le parc informatique ainsi que le niveau de protection sont en constante augmentation. Les chiffres concernants le nombre d'infecté n'est donc pas le même en fonction des années. Nous allons donc nous appuyer sur les chiffres d'inféctions de chaque année et sur le nombre d'utilisateur par année afin de validerle modèle.

Premières idées de modélisation: 

# VOIR FICHIER ARE.IPYNB



