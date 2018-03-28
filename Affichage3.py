def noeud(T):
    for(k,v) in I.items():
        T.add_node((k), infection = v[0], genre = v[-1])
    return T
def liaison(T):
    """ relie les noeuds entre eux à partir de la BASE de donnée qui donne les Utilisateurs liés """
    for  (k,v) in SL.items():
        for e in v[3:5]:
            for f in e:
                T.add_edge(k,f, weight = 1)
    for  (k,v) in SG.items():
        for e in v[3:6]:
            for f in e:
                T.add_edge(k,f, weight = 1)
    return T

def affichage(T):
    indi = [] #individus infectés
    servli = [] #serveusr locaux infectés
    servgi = [] #serveurs globaux infectés
    inds = [] #individus sains
    servls = [] #serveurs locaux sains
    servgs = [] #serveurs globaux sains
    
    for i in I:   
        if G.node[i]['infection'] == True:
            if G.node[i]['genre'] == 'i':
                indi.append(i)         
            if G.node[i]['genre'] == 'sl':
                servli.append(i)
            if G.node[i]['genre'] == 'sg':
                servgi.append(i)
        else:
            if G.node[i]['genre'] == 'i':
                inds.append(i)         
            if G.node[i]['genre'] == 'sl':
                servls.append(i)
            if G.node[i]['genre'] == 'sg':
                servgs.append(i)            


            
    f = plt.figure(1)
    nx.draw_kamada_kawai(T,nodelist = indi, node_shape = 'o', node_color = 'red', node_size = 150, with_labels = True)
    nx.draw_kamada_kawai(T,nodelist = servli, node_shape = 'd', node_color = 'red', node_size = 300, with_labels = True)
    nx.draw_kamada_kawai(T,nodelist = servgi, node_shape = 's', node_color = 'red', node_size = 500, with_labels = True)
    nx.draw_kamada_kawai(T,nodelist = inds, node_shape = 'o', node_color = 'green', node_size = 150, with_labels = True)
    nx.draw_kamada_kawai(T,nodelist = servls, node_shape = 'd', node_color = 'green', node_size = 300, with_labels = True)
    nx.draw_kamada_kawai(T,nodelist = servgs, node_shape = 's', node_color = 'green', node_size = 500, with_labels = True)
    f.show() # display
    print("Nodes du graph: ")
    print(T.nodes())
    print("Edges du graph: ")
    print(T.edges())
    
    print(type(T.nodes()))
    print(type(T.edges()))
    return None
def Test(T):
    noeud(T)
    liaison(T)
    return affichage(T)
Test(G)   
