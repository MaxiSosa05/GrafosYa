import random

def generar_vertices():
    
    origenes = [
        "Plaza Central", "Hospital", "escuela", "UNO",
        "Municipalidad", "Biblioteca", "Museo",
        "Parque", "Centro Comercial", "Aeropuerto"
    ]

    estaciones = [f"E{i}" for i in range(1, 11)]  # E1 a E10

    vertices = []
    n = random.randint(6, 10)  # número de ubicaciones a usar

    for j in range(n):
        vertices.append(random.choice(origenes))
        vertices.append(estaciones[j])  # cada ubicación con su estación

    return vertices


def generar_aristas(vertices: list) -> list:

    aristas = []
    ubis = []
    est = []

    # separar ubicaciones y estaciones
    for v in vertices:
        if v.startswith("E"):
            est.append(v)
        else:
            ubis.append(v)

    # mínimo y máximo de aristas
    min_aristas = len(ubis) + (len(est) - 1)  # 1 arista por ubicación + cadena de estaciones
    max_aristas = len(ubis) * len(est) + (len(est) * (len(est) - 1)) // 2

    if max_aristas > 50:
        max_aristas = 28

    total_aristas = random.randint(min_aristas, max_aristas)

    # 1. Conectar cada ubicación con al menos una estación
    for ubi in ubis:
        aristas.append((ubi, random.choice(est), random.randint(2, 15)))

    # 2. Conectar estaciones entre sí formando una cadena (garantiza conexidad)
    for i in range(len(est) - 1):
        aristas.append((est[i], est[i+1], random.randint(2, 15)))

    # 3. Agregar aristas aleatorias hasta alcanzar total_aristas
    while len(aristas) < total_aristas:
        tipo = random.choice(["ubi-est", "est-est"])
        if tipo == "ubi-est":
            u = random.choice(ubis)
            e = random.choice(est)
        else:
            u, e = random.sample(est, 2)

        # evitar duplicados (sin importar el orden en est-est)
        if tipo == "ubi-est":
            if (u, e) not in aristas:
                aristas.append((u, e, random.randint(2, 15)))
        else:
            if (u, e) not in aristas and (e, u) not in aristas:
                aristas.append((u, e, random.randint(2, 15)))

    return aristas


if __name__ == "__main__":

    a = generar_vertices()

    b = generar_aristas(a)

    print(b)