import os 
import matplotlib.pyplot as plt
import networkx as nx
from GENERADOR import*


class Grafo:

    def __init__(self):
        self.vertices = generar_vertices()
        self.aristas = generar_aristas(self.vertices)
        self.G = nx.Graph()

        self.construccion()


    def construccion(self):
        # agregar nodos
        for v in self.vertices:
            self.G.add_node(v)

        # agregar aristas
        for u, v, peso in self.aristas:
            self.G.add_edge(u, v, weight=peso)

    def dibujar(self):

        pos = nx.spring_layout(self.G , k = 10, scale= 0.9, iterations= 100)
        # k es distancia entre nodos 
        # scale define el tamaño de los nodos
        # iterations las veces que se ajustan las fuerzas
        # grafo se comporta como un sistema físico simulado. 
        # Cada nodo siente fuerzas y se mueve hasta que el sistema se estabiliza  

        # en pos se crea un diccionario donde a cada vertice le coresponde coordenadas

        # separar nodos por tipo
        estaciones = [n for n in self.G.nodes if n.startswith("E")]
        ubicaciones = [n for n in self.G.nodes if not n.startswith("E")]

        plt.figure(figsize=(10, 6))

        # nodos
        nx.draw_networkx_nodes(self.G, pos, nodelist=ubicaciones, node_color="skyblue", node_size=1000)
        nx.draw_networkx_nodes(self.G, pos, nodelist=estaciones, node_color="pink", node_size=800)
        # se separa por color y tamaño


        # aristas
        nx.draw_networkx_edges(self.G, pos, width=1) 
        # en este casos se modifica solo el grosor

        # etiquetas nodos
        nx.draw_networkx_labels(self.G, pos, font_size=10)
        # el tamaño de lso nombres 

        # etiquetas pesos
        labels = nx.get_edge_attributes(self.G, "weight")
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels, font_size=7)

        plt.title("POO2 - TP 2")
        #plt.axis("off") # saca el marco
        plt.show()


    def __str__(self):
        
        resultado = (
            f"\n--------------Detalle del grafo----------------\n\n"
            f"cantidad de vetices: {len(self.vertices)}\n"
            f"cantidad de aristas: {len(self.aristas)} \n\n"
            f"----------------------------------------------"
        )
    
        return resultado
 
    