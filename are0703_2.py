#importation de bibliotheques 
from pylab import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random as rd


#Variables globales:
#Nombre d'individus:
global N 
N = 1000
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
global sg
sg = 50
#POP : population totale : dict[int : list[bool, float, float, set[str], set[int]
global POP
POP = population()
#POP_adresses : liste des adresses de POP : list[int]
global POP_adresses
POP_adresses = list(POP.keys())
#internet : ensemble des réseaux (locaux et globaux) : dict[str:list[set[int], str, bool]]
global internet
internet = type_serv()


def population():
    """ Crée un dictionnaire représentant l'ensemble des individus, de la forme : adresse : [infection, protection, Tdesinfection, serveurs]"""
    pop = dict()
    infection = False
    serveurs = set()
    connections = set()
    for i in range(1,N+1):
        protection = rd.uniform(0.0, 1.0)
    #Plus le taux de protection est haut moins le temps de desinfection est eleve.
        Tdesinfection = 1.0 - protection
        pop[i] = [infection, protection, Tdesinfection, serveurs, connections]
    return pop


def serv_souche():
    """ Le dictionnaire représentant l'ensemble des serveurs, de la forme : adresse : [Nconnections]"""
    D_serv = dict()
    for i in range(1, NS+1):
        Nconnections = rd.randint(2, N/10)
        #!!!fonction gaussienne
        D_serv["s"+str(i)] = Nconnections
    return D_serv

def connections():
    """
    Attribue un ensemble de personnes connectées au serveur à chaque serveur
    Nonetype -> dict[str:set[int]]
    """
    DR = dict()
    #Dss : dictionaire des serveurs souche : dict[str:int]
    Dss = serv_souche()
    for serv in Dss:
        #Ea : ensemble d'adresses de personnes connectées au serveur : lis[int]
        Ea = set()
        #n : nombre de personnes connectées au serveur : int
        n = Dss[serv]
        while n > 0:
            Ea.add(rd.choice(POP_adresses))
            n -= 1
        DR[serv] = Ea
        
    return DR

def type_serv():
    
    
    serv = connections()
    for a in serv:
        if len(serv[a])>= sg:
            serv[a]=[serv[a], 'serveur_global', False]
        if len(serv[a])<= sg:
            serv[a]=[serv[a], 'serveur_local', False]          
    return serv


def propagation():
    #i : internet : dict[str:list[set[int], str, bool]]
    i = internet
    
    
    
    
    
    
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
                personne = rd.choice(list(POP.items()))
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



def propagation(individu_1):
    """Simule la propagation intentionnelle du virus à partir d'un individu infecté"""
    #L_connecte : liste des individus connectés à individu_1 selon M : list[tuple(int, int)]
    L_connecte = []
    for i in range(N):
        for j in range(N):
            if j >= i:
                next
            if M[i,j] == True:
                L_connecte.append(i,j)
                print(L_connecte)
        







