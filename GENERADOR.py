import random

def generar_vertices():
    
    origenes = [
        "Plaza Central", "Hospital", "escuela", "UNO",
        "Municipalidad", "Biblioteca", "Museo",
        "Parque", "Centro Comercial", "Aeropuerto"
    ]

    estaciones = [f"E{i}" for i in range(1, 11)]  # E1 a E10

    vertices = []

    n = random.randint(6, 10)  # número de ubicaciones a usar , para variedad...

    for j in range(n):
        vertices.append(random.choice(origenes))
        vertices.append(estaciones[j])  # cada ubicación con su estación

        # subo a la lista la misma cantidad de ubis que de estaciones

    return vertices


def generar_aristas(vertices: list) -> list:

    aristas = [] # se guarda (ubi , est, peso)
    aristasExist = [] # se guarda (ubi, est) para validar repetidos
    ubis = []
    est = []

    # separar ubicaciones y estaciones
    for v in vertices:
        if v.startswith("E"): # o sea si empieza con "E" devuelve true , distinge mayusculas
            est.append(v)
        else:
            ubis.append(v)

    # mínimo y máximo de aristas
    min_aristas = len(ubis) + (len(est) - 1)  # 1 arista por ubicación + cadena de estaciones
    max_aristas = len(ubis) * len(est) + (len(est) * (len(est) - 1)) // 2
    # las dos barritas hacen qe el resultado de la divicion se 
    # quede con la parte entera


    # se limita a 25 por que el posible maximo seria 190 ,  
    # y no seria "comodamente visible"
     
    total_aristas = random.randint(min_aristas, 25)

    # primero me aseguro que todas las ubicaciones esten con una estacion
    for ubi in ubis:
        r = random.choice(est)
        aristas.append((ubi, r, random.randint(2, 15)))
        aristasExist.append((ubi, r))

    # segundo Conectar estaciones entre sí 
    for i in range(len(est) - 1):
        aristas.append((est[i], est[i+1], random.randint(2, 15)))
        aristasExist.append((est[i], est[i+1]))


    # tecero Agregar aristas aleatorias hasta alcanzar total_aristas
    while len(aristas) < total_aristas:
        tipo = random.choice(["ubi-est", "est-est"]) # posibles combinaciones
        if tipo == "ubi-est":
            u = random.choice(ubis) 
            e = random.choice(est)
        else:
            u, e = random.sample(est, 2)

        # evitar duplicados 
        if tipo == "ubi-est":
            if (u, e) not in aristasExist and (e, u) not in aristasExist:
                aristas.append((u, e, random.randint(2, 15)))
                aristasExist.append((u,e))
        else:
            if (u, e) not in aristasExist and (e, u) not in aristasExist:
                aristas.append((u, e, random.randint(2, 15)))
                aristasExist.append((u,e))

        # al ser no dirigido se verifica a -> b  y b -> a      

    return aristas