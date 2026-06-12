import os 
import random 
from Grafo import*



import os

def Menu():

    print("--- MENU ---\n")
    print("1 _ otro grafo")
    print("2 _ detalles del grafo")
    print("3 _ generar el camino mas corto de tres origen-destino")
    print("4 _ generar la ruta de menor costo para la camioneta")
    print("5 _ dibujar el grafo")
    print("6 _ salir...\n")

    op = -1

    while op < 1 or op > 6:
        try:
            op = int(input("indique la opcion: "))
            if op < 1 or op > 6:
                print("opcion incorrecta, elija nuevamente")
        except ValueError:
            print("Error: debe ingresar un número entre 1 y 6")
            op = -1

    return op


class Main:

    def __init__(self):
        self.nom = "hector"

    def Desplegar(self):


        k1 = 2
        k2 = 5

        op = Menu()

        grafo = Grafo()

        while op != 6:



            match(op):

                case 1:
                    grafo = Grafo()
                    print("se a genereado otro grafo \n")

                case 2: 
                    print(grafo)    

                case 3:

                    ubi = [n for n in grafo.vertices if not n.startswith("E")]

                    for i in range(0,3):

                        print("\n--- par numero " , i+1 , " ---")

                        ubi = [n for n in grafo.vertices if not n.startswith("E")]

                        origen = random.choice(ubi)
                        destino = random.choice([x for x in ubi if x != origen])
                        

 
                        camino = nx.shortest_path(grafo.G, source=origen, target=destino, weight="weight")
                        distancia = nx.shortest_path_length(grafo.G, source=origen, target=destino, weight="weight")
                        precio = (k1 * distancia) + (k2 * (len(camino) - 1) )

                        print(origen , " hasta " , destino, ":")
                        print("resultado de aplicar dijstra : ", camino)
                        print("distancia total" ,distancia)
                        print("PRECIO = " , precio , "\n")  

                        ubi.remove(origen)
                        ubi.remove(destino)    

                case 4:

                    estaciones = [x for x in grafo.vertices if x.startswith("E")]

                    subgrafo = grafo.G.subgraph(estaciones)
                    mst = nx.minimum_spanning_tree(subgrafo, algorithm="kruskal")

                    # ruta (DFS sobre el MST)
                    inicio = estaciones[0]
                    ruta = list(nx.dfs_preorder_nodes(mst, source=inicio))

                    print("Ruta de la camioneta:")
                    print(" -> ".join(ruta))

                case 5:

                    grafo.dibujar()

                case 6:
                    break

            i = input("para continuar presione enter...")
            os.system('cls')
            op = Menu()
              




if __name__ == "__main__":


    os.system('cls')

    main = Main()

    main.Desplegar()