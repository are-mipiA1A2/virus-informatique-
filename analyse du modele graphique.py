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
global NSL
NSL = 5
#virus:
global virus
virus = (0.5, 0.0, 0.0, "vers")
#Reseau :
#global R
#R = reseau()
#seuilg : seuil pour qu'un serveur souche soit considéré global
#global sg
#sg = 50


#internet : ensemble des réseaux (locaux et globaux) : dict[str:list[set[int], str, bool]]
#global internet
#internet = type_serv()

#SG : serveurs globaux (Nom : [infection, personnes connectées, serveurs locaux connectés, servereurs globaux connectés] : dict[str : list[bool, set(int), set(str)]]
SG = {"Internet1" : [False, True, 0.9, 0.1, set(), set(), set()],
      "Internet2" : [False, True, 0.9, 0.1, set(), set(), set()],
      "Internet3" : [False, True, 0.9, 0.1, set(), set(), set()],
      }

SG_adresses = ["Internet1", "Internet2", "Internet3"]





def population():
    """ Crée un dictionnaire représentant l'ensemble des individus, de la forme : adresse : [infection, protection, Tdesinfection, serveurs]"""
    pop = dict()
    infection = False
    for i in range(1,N+1):
        protection = rd.uniform(0.0, 1.0)
    #Plus le taux de protection est haut moins le temps de desinfection est eleve.
        Tdesinfection = 1.0 - protection
        serveur_local = ""
        serveurs_globaux = set()
        pop[i] = [infection, True, protection, Tdesinfection, set(), serveur_local, serveurs_globaux]
    return pop

#POPU : population totale : dict[int : list[bool, float, float, str, set[int]
global POPU
POPU = population()
#POPU_adresses : liste des adresses de POPU : list[int]
global POPU_adresses
POPU_adresses = list(POPU.keys())

def s_locaux():
    """
    Attribue un ensemble de personnes connectées au serveur à chaque serveur local
    Nonetype -> dict[str:set[int]]
    """
#!!!  ???
    for e in POPU:
        POPU[e][5] = ""
#!!! ???
    #DR : dictionaire des serveurs locaux : dict[str:list[set(int), set(str)]
    DR = dict()
    for i in range(1, NSL+1):
        protection = rd.uniform(0.0, 1.0)
        #Plus le taux de protection est haut moins le temps de desinfection est eleve.
        Tdesinfection = 1.0 - protection
        #Ea : ensemble d'adresses de personnes connectées au serveur : list[int]
        Ea = set()
        #Esg : ensemble d'adresses de serveurs globaux connectés au serveur : list[str]
        Esg = set()
        #n : nombre de personnes connectées au serveur : int
        n = rd.randint(3, N/20)
        x = len(POPU_adresses)
        while n > 0 and x != 0:
            flag = False
            while not flag and x != 0:
                x -= 1
                p = rd.choice(POPU_adresses)
                if POPU[p][5] == "":
                    flag = True
                    Ea.add(p)
                    POPU[p][5] = "s"+ str(i)
            
            n -= 1
        
        #m : nombre de serveurs globaux connectés au serveur : int
        m = rd.randint(1,3)
        while m > 0:
            sg = rd.choice(SG_adresses)
            Esg.add(sg)
            SG[sg][5].add("s"+ str(i))
            m -= 1
        DR["s"+str(i)] = [False, True, protection, Tdesinfection, Ea, "", Esg]
        Ea = set()
        Esg = set()
#!!!relier aussi des serv globaux aux serv locaux
        
    return DR

SL = s_locaux()

def s_globaux():
    """
    Attribue un ensemble de personnes connectées au serveur à chaque serveur global
    Nonetype -> dict[str:set[int]]
    """
    #Epc : ensemble de personnes non connectées à un serveur local : set[int]
    Epnc = set()
    for e in POPU:
        if POPU[e][5] == "":
            Epnc.add(e)
    for p in Epnc:
        #sg : serveur global sélectionné aléatoirement : str
        sg = rd.choice(SG_adresses)
        POPU[p][6].add(sg)
        SG[sg][4].add(p)
    for sg1 in SG:
        for sg2 in SG:
            if sg1 != sg2:
                SG[sg1][6].add(sg2)
    return None

s_globaux()

def internet():
    """
    """
    internet = dict()
    for c,v in POPU.items():
        v.append("i")
        internet[c] = v
    for c,v in SL.items():
        v.append("sl")
        internet[c] = v
    for c,v in SG.items():
        v.append("sg")
        internet[c] = v
    return internet

J = internet()
I_adresses = list(J.keys())    

def non_proteges(I,p):
    for i in range(int((len(I)-3)*p)):
        flag = False
        while not flag:
            e = rd.choice(I_adresses)
            if I[e][7] != "sg" and I[e][1] == True:
                I[e][1] = False
                flag = True
            else:
                next
                
    return I
#non_proteges()

def I_connection():
    I_connections = dict()
    for e in I:
        v = []
        for i in range(4,7):
            if type(I[e][i]) == str and len(I[e][i]) != 0:
                v.append(I[e][i])
            elif len(I[e][i]) != 0:
                for f in I[e][i]:
                    v.append(f)
            else: next
        I_connections[e] = v
    return I_connections

#I_connections = I_connection()


L_infections = []
L_echecs = []
def N_infections():
    N = 0
    for e in I:
        if I[e][0] == True:
            N += 1
    return N

def I_adresses_ponderee():
    LR = []
    for i in range(len(I_adresses)):
        for j in range(len(I_connections[I_adresses[i]])):
            LR.append(I_adresses[i])
    return LR

#I_adresses_ponderees = I_adresses_ponderee()

I["Internet1"][0] = True

def antiviruss():
    E_proteges = set()
    for e in I:
        if I[e][1] == True:
            E_proteges.add(e)
    return [False, E_proteges]

#antivirus = antiviruss()

#I_infectes = {"Internet1" : 1}


def edd_vers_antivirus(i1,i2,eff):
    """Simule l'échange de donnée d'un individu 1 à un individu 2 dans un réseau 'reseau'"""
#!!! rechercher si un antivirus peut enregistrer un virus même si l'ordi devient pas infecté
    infectiosité,_,_,Type = virus
    if I[i2][0] == True:
        return None 
    if I[i1][0]:
        if I[i2][1]:
            x = rd.randint(0,eff)
            if x == eff-1 :
                antivirus[0] = True
            
    if infectiosité > I[i2][2]:
        I[i2][0] = True
        I_infectes[i2] = int(I[i2][3]*20)
        if I[i2][6] == "sl"and Type == "vers":
            for e in I_connections[i2]:
                I[e][0] = True
                I_infectes[e] = int(I[e][3]*20)
                    
def p2p(eff):
    flag = False
    while not flag:
        i1 = rd.choice(I_adresses)
        if type(i1) == int:
            flag = True
    flag = False
    while not flag:
        i2 = rd.choice(I_adresses)
        if type(i2) == int and i1 != i2:
            flag = True
    edd_vers_antivirus(i1,i2,eff)
    
    
    
def journee_ponderee_antivirus(eff):
#!!! _,_,_,vers
#échanges de donnée classiques
    for j in range(1000):
        i1 = rd.choice(I_adresses_ponderees)
        if len(I_connections[i1]) != 0:
            i2 = rd.choice(I_connections[i1])
            edd_vers_antivirus(i1,i2,eff)
        else:
            next
#pear to pear
    for k in range(100):
        p2p(eff)
#rôle de l'antivirus
    E_del = set()
#!!! voir si faut pas mettre le test pour l'antivirus dans la boucle
    if antivirus[0]:
        for e in antivirus[1]:
            I[e][0] = False
            I[e][2] = 1.0
            if e in I_infectes:
                E_del.add(e)
#désinfection manuelle 
    for e in I_infectes:
        if I_infectes[e] == 0:
            I[e][0] = False
            E_del.add(e)
        elif I_infectes[e] > 0:
            I_infectes[e] -= 1
        else:
            print("erreur, temps pour la désinfection négatif")
    for e in E_del:
        del I_infectes[e]
    E_del = set()
    #print(antivirus[0])
    #print(N_infections())
    
    return I_infectes

def test(eff):
    for i in range(20):
        journee_ponderee_antivirus(eff)
    return N_infections()

def simulation_infe(frame, Type_virus, patient0):
    L = []
    S = 0
    I_connections = dict()
    I_adresses_ponderees = []
    for m in range (1,9):
        for w in range (10):
            global virus
            virus = (m/10, 0.0, 0.0, Type_virus)
            I = J
            I_adresses = list(I.keys())
            I = non_proteges(I,m/10)
            I_adresses = list(I.keys())
            I_connections = I_connection()
            I_adresses_ponderees = I_adresses_ponderee()
            I[patient0][0] = True
            antivirus = antiviruss()
            I_infectes = {patient0 : 1}
            S = S + test(0)
            I_connections = dict()
            I_adresses_ponderees = []
        L.append(S//10)
    return L
"""
#z = y = simulation_infe(10,"vers","Internet1")
#y = simulation_infe(10,"virus","Internet1")
y = simulation_infe(10,"vers","Internet1")
#z = simulation_infe(10,"vers","s1")
#w = simulation_infe(10,"vers",44)
x = np.linspace(0, 1, 10)
figure()
#plot(x, w, 'r', color='black' )
plot(x, y, 'r',color='C0',  label='virus')
plot(x, z, 'r',  label='vers')
xlabel('infectiosités')
ylabel('nombre d infectes')
title('comparaison entre les patient0 ')
show()
List_eff = [5000 , 4000 , 3000 , 2000, 1000, 500, 200, 100, 50, 10]
def simulation_antivirus(liste):
    L = []
    S = 0
    I_connections = dict()
    I_adresses_ponderees = []
    for m in liste:
        for w in range (11):
            global virus
            virus = (0.5, 0.0, 0.0, "vers")
            I = J
            I_connections = I_connection()
            I_adresses_ponderees = I_adresses_ponderee()
            I["Internet1"][0] = True
            antivirus = antiviruss()
            I_infectes = {"Internet1" : 1}
            S = S + test(m)
            I_connections = dict()
            I_adresses_ponderees = []
        L.append(S//100)
    return L
x = List_eff
y = simulation_antivirus(List_eff)
figure()
plot(x, y, 'r')
xlabel('efficacite d antivirus')
ylabel('nombre d infectes')
title('nombre d infectes au bout de 20jours en fonction d efficacite d antivirus ')
show()"""



