G = nx.Graph()
def noeud(T):
    for (k,v) in POPU.items():
        T.add_node((k),infection = v[0], protection = v[1], Tdesinfection = v[2] )
    return T
def affichage(T):
    figure = nx.draw(T)
    plt.savefig("simple_path.png") # save as png
    plt.show(figure) # display

    print("Nodes du graph: ")
    print(T.nodes())
    print("Edges du graph: ")
    print(T.edges())
    
    print(type(T.nodes()))
    print(type(T.edges()))
