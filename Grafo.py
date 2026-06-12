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

        pos = nx.spring_layout(self.G, seed=42 , k = 5 )

        # separar nodos por tipo
        estaciones = [n for n in self.G.nodes if n.startswith("E")]
        ubicaciones = [n for n in self.G.nodes if not n.startswith("E")]

        plt.figure(figsize=(10, 6))

        # nodos
        nx.draw_networkx_nodes(self.G, pos, nodelist=ubicaciones, node_color="skyblue", node_size=800)
        nx.draw_networkx_nodes(self.G, pos, nodelist=estaciones, node_color="lightgreen", node_size=800)

        # aristas
        nx.draw_networkx_edges(self.G, pos, width=1)

        # etiquetas nodos
        nx.draw_networkx_labels(self.G, pos, font_size=8)

        # etiquetas pesos
        labels = nx.get_edge_attributes(self.G, "weight")
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels, font_size=7)

        plt.title("Grafo Ubicaciones - Estaciones")
        plt.axis("off")
        plt.show()



    def __str__(self):

         # Creamos un bloque de texto completo usando f-string
        resultado = (
            f"Detalle del grafo : \n\n"
            f"cantidad de vetices: {len(self.vertices)} \n\n"
            f"cantidad de aristas: {len(self.aristas)} \n\n"
        )
    
        return resultado
 
    