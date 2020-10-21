'''
        Proyecto 3
    Aplicar los conceptos de autómatas, 
    expresiones regulares y gramáticas

Creado por:

    Juan Fernando De Leon Quezada       17822
    Diego Estrada                       18XXX
    Andree Toledo                       18XXX

'''

import networkx as nx

def generate_graph(p):

    G = nx.Graph()

    if type(p) == tuple:
        G.add_node(p[0])
        if type(p[1]) == tuple:
            G.add_node(p[1][0])
            G.add_edge(p[0], p[1][0])
            G_1 = generate_graph(p[1])
            G.add_nodes_from(G_1)
            G.add_edges_from(G_1.edges())
        else:
            G.add_node(p[1])
            G.add_edge(p[0], p[1])
        
        if (len(p) > 2):
            if type(p[2]) == tuple:
                G.add_node(p[2][0])
                G.add_edge(p[0], p[2][0])
                G_2 = generate_graph(p[2])
                G.add_nodes_from(G_2)
                G.add_edges_from(G_2.edges())
            else:
                G.add_node(p[2])
                G.add_edge(p[0], p[2])
    
    return G