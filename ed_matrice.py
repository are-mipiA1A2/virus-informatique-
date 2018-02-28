#importation de bibliotheques 
from pylab import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random as rd


#Variables globales:
#Nombre d'individus:
global N 
N = 5



def init_matrice():
    """ Initialise la matrice representant les connexions entre les individus sous la forme d'un booleen, False pour non connecte et True pour connecte.
    Null -> list[bool] """
    mat = np.full((N+1, N+1), False, dtype=bool)
    for j in range(0,N+1):
        mat[0, j] = True
    for i in range(0,N+1):
        mat[i, 0] = True
        
    for i in range(N+1):
        j = i
        mat[i,j] = False     
    
    return mat


