G = nx.Graph()
def noeud(T):

    #L=[]2 [False, 0.5786481814287545, 0.4213518185712455, set(), set()]
    for (k,v) in POPU.items():
        T.add_node((k),infection = v[0], protection = v[1], Tdesinfection = v[2] )
    return T
        #L.append(e,POPU(e))
    #return 


def affichage(T):
    color_map= []
    for i in range (1, len(POPU)+1):
        if (G.node[i]['infection'] == True):
            color_map.append('red')
        else:
            color_map.append('green')
    f = plt.figure(1)
    nx.draw(T,node_color = color_map,with_labels = True)
    f.show() # display

#def liaison(L):
    """ relie les noeuds entre eux à partir de la BASE de donnée qui donne les Utilisateurs liés """
 #   for  (k,v) in POPU.items():
#        L.add_edge()
        
    print("Nodes du graph: ")
    print(T.nodes())
    print("Edges du graph: ")
    print(T.edges())
    
    print(type(T.nodes()))
    print(type(T.edges()))
