#importation de bibliotheques 
from pylab import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random as rd


#Variables globales:
#Nombre d'individus:
global N 
N = 100
#Nombre de serveurs:
global NS
NS = 10
#virus:
global virus
virus = (0.5, 0.0, 0.0, 0.0)
#Reseau :
#global R
#R = reseau()
#seuilg : seuil pour qu'un serveur souche soit considéré global
#global sg
#sg = 50


#internet : ensemble des réseaux (locaux et globaux) : dict[str:list[set[int], str, bool]]
#global internet
#internet = type_serv()

#SG : serveurs globaux : dict[str : list[set(int), set(str)]]
SG = {"Google" : [set(), set()],
      "Jeux" : [set(), set()],
      "CIA" : [set(), set()],
      }

SG_adresses = ["Google", "Jeux", "CIA"]





def population():
    """ Crée un dictionnaire représentant l'ensemble des individus, de la forme : adresse : [infection, protection, Tdesinfection, serveurs]"""
    pop = dict()
    infection = False
    for i in range(1,N+1):
        protection = rd.uniform(0.0, 1.0)
    #Plus le taux de protection est haut moins le temps de desinfection est eleve.
        Tdesinfection = 1.0 - protection
        serveurs_locaux = ""
        serveurs_globaux = set()
        pop[i] = [infection, protection, Tdesinfection, serveurs_locaux, serveurs_globaux]
    return pop

#POPU : population totale : dict[int : list[bool, float, float, str, set[int]
global POPU
POPU = population()
#POPU_adresses : liste des adresses de POPU : list[int]
global POPU_adresses
POPU_adresses = list(POPU.keys())

"""def serv_locaux():
    Le dictionnaire représentant l'ensemble des serveurs, de la forme : adresse : [Nconnections]
    D_serv = dict()
    for i in range(1, NS+1):
        Nconnections = rd.randint(2, N/500)
        #!!!fonction gaussienne
        D_serv["s"+str(i)] = Nconnections
    return D_serv
"""
def s_locaux():
    """
    Attribue un ensemble de personnes connectées au serveur à chaque serveur local
    Nonetype -> dict[str:set[int]]
    """
    #DR : dictionaire des serveurs locaux : dict[str:list[set(int), set(str)]
    DR = dict()
    for i in range(1, NS+1):
        #Ea : ensemble d'adresses de personnes connectées au serveur : list[int]
        Ea = set()
        #Esg : ensemble d'adresses de serveurs globaux connectés au serveur : list[str]
        Esg = set()
        #n : nombre de personnes connectées au serveur : int
        n = rd.randint(2, N/10)
        while n > 0:
            flag = False
            while not flag :
                p = rd.choice(POPU_adresses)
                if POPU[p][3] == "":
                    flag = True
                    Ea.add(p)
                    POPU[p][3] = "s"+ str(i)
                    
            n -= 1
        
        #m : nombre de serveurs globaux connectés au serveur : int
        m = rd.randint(1,3)
        while m > 0:
            sg = rd.choice(SG_adresses)
            Esg.add(sg)
            SG[sg][1].add("s"+ str(i))
            m -= 1
        DR["s"+str(i)] = [Ea, Esg]
        Ea = set()
        Esg = set()
#!!!relier aussi des serv globaux aux serv locaux
        
    return DR



s_locaux()

def s_globaux():
    """
    Attribue un ensemble de personnes connectées au serveur à chaque serveur global
    Nonetype -> dict[str:set[int]]
    """
    for sg in SG:
        #Ea : ensemble d'adresses de personnes connectées au serveur : lis[int]
        Ea = set()
        #n : nombre de personnes connectées au serveur : int
        n = rd.randint(2, N/10)
        while n > 0:
            p = rd.choice(POPU_adresses)
            Ea.add(p)
            POPU[p]
            
            n -= 1
            
#!!!relier aussi les pop qu'on vient d'ajouter
        SG[sg][0] = Ea
#!!! finir de relier des trucs (pop et serv locaux aux serv globaux)
        

"""def type_serv():
    
    
    serv = connections()
    for a in serv:
        if len(serv[a])>= sg:
            serv[a]=[serv[a], 'serveur_global', False]
            
        if len(serv[a])<= sg:
            serv[a]=[serv[a], 'serveur_local', False]     
        
        return serv
"""

"""
def propagation():
    #i : internet : dict[str:list[set[int], str, bool]]
    i = internet
"""
    
    
    
    
    
#connexction de d_serv [dans des emseble]    
        
"""def differenciation():
    D_serv = serv_souche()
    E_servl = set()
    E_servg = set()
    for serv in D_serv:
        if D_serv[serv][0] > sg:
            E_servg.add(serv)
        else:
            E_servl.add(serv)
    return (E_servl, E_servg, D_serv)
    
def internet():
    internet = dict()
    E_servl, E_servg, D_serv = differenciation()
    for serv in D_serv:
        if serv in E_servl:
            D_serv[serv] = n
            E_connections = set()
            for e in range(n):
                personne = rd.choice(list(POPU.items()))
                adresse, liste = personne
                serv[adresse] = liste
                
    return null"""
       
    
#global R
#R = reseau()
#global M
#M = init_matrice()

"""def init_matrice():
    Initialise la matrice representant les connexions entre les individus sous la forme d'un booleen, False pour non connecte et True pour connecte.
    Null -> list[bool] 
    #Matrice (N+1, N+1), de bool initialises a False
    mat = np.full((N+1, N+1), False, dtype=bool)
    #Ligne et colonne 0 initialises a True pour representer le reseau 0
    for j in range(0,N+1):
        mat[0, j] = True
    for i in range(0,N+1):
        mat[i, 0] = True
    #Verification qu'un utilisateur ne peut pas se connecter a lui-meme    
    for i in range(N+1):
        j = i
        mat[i,j] = False     
    return mat
def contamination(individu_1, individu_2):
    Simule l'echange de donnee d'un individu 1 a un individu 2 dans un reseau 'reseau'
    #importation du virus
    infectiosite,_,_,_ = virus
    #Si l'individu 2 est moins protege que le virus n'est efficace, alors il devient infecte.
    if R[individu_1][0] == True and infectiosite > R[individu_2][1]:
        R[individu_2][0] = True
    return reseau"""



"""def propagation(individu_1):
    Simule la propagation intentionnelle du virus à partir d'un individu infecté
    #L_connecte : liste des individus connectés à individu_1 selon M : list[tuple(int, int)]
    L_connecte = []
    for i in range(N):
        for j in range(N):
            if j >= i:
                next
            if M[i,j] == True:
                L_connecte.append(i,j)
                print(L_connecte)"""
