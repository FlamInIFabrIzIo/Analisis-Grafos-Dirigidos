from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt

####### Grafos de ejemplo representados como diccionarios #######

# Cada clave es un nodo, y su valor es un conjunto de nodos a los que apunta
GRAFO_EJEMPLO_0 = {
    0: set([1, 2]),
    1: set(),
    2: set(),
}

GRAFO_EJEMPLO_1 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3]),
    3: set([0]),
    4: set([1]),
    5: set([2]),
    6: set(),
}

GRAFO_EJEMPLO_2 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3, 7]),
    3: set([7]),
    4: set([1]),
    5: set([2]),
    6: set(),
    7: set([3]),
    8: set([1, 2]),
    9: set([0, 3, 4, 5, 6, 7]),
}


###### Función para crear un grafo completo no dirigido #######

def crear_grafo_completo(cantidad_nodos):
    """
    Crea un grafo completo donde cada nodo se conecta con todos los demás.
    No se permiten bucles (no se conecta consigo mismo).
    
    :param cantidad_nodos: cantidad de nodos en el grafo
    :return: diccionario representando el grafo
    """
    grafo = {}

    if cantidad_nodos < 1:
        return grafo

    for nodo in range(cantidad_nodos):
        conexiones = [i for i in range(cantidad_nodos) if i != nodo]
        grafo[nodo] = set(conexiones)

    return grafo


######## Función para calcular los in-degrees ##########

def calcular_grados_entrada(grafo_dirigido):
    """
    Calcula el número de aristas entrantes (grados de entrada) para cada nodo.
    
    :param grafo_dirigido: diccionario que representa un grafo dirigido
    :return: diccionario con el grado de entrada de cada nodo
    """
    grados = Counter()

    for nodo, conexiones in grafo_dirigido.items():
        if nodo not in grados:
            grados[nodo] = 0
        for destino in conexiones:
            grados[destino] += 1

    return grados


# ====== 📊 Función para obtener la distribución de in-degrees ======

def distribucion_grados_entrada(grafo_dirigido):
    """
    Calcula cuántos nodos tienen cierta cantidad de grados de entrada.
    
    :param grafo_dirigido: diccionario que representa un grafo dirigido
    :return: diccionario con la distribución de los grados de entrada
    """
    distribucion = Counter()
    grados = calcular_grados_entrada(grafo_dirigido)

    for cantidad in grados.values():
        distribucion[cantidad] += 1

    return distribucion


######### Función para visualizar un grafo dirigido ############

def dibujar_grafo(grafo_dirigido, titulo="Grafo dirigido"):
    """
    Visualiza un grafo dirigido con flechas usando networkx y matplotlib.

    :param grafo_dirigido: diccionario con el grafo
    :param titulo: título opcional del gráfico
    """
    G = nx.DiGraph()

    for nodo, destinos in grafo_dirigido.items():
        for destino in destinos:
            G.add_edge(nodo, destino)

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=1000,
            node_color="skyblue", edge_color="gray", arrows=True)
    plt.title(titulo)
    plt.show()


######## Pruebas #########

# Elegí qué grafo visualizar o analizar
grafo = GRAFO_EJEMPLO_2

# Visualización
dibujar_grafo(grafo, "Visualización del grafo de ejemplo 1")

# Cálculo de grados de entrada
print("Grados de entrada por nodo:", calcular_grados_entrada(grafo))

# Distribución de grados de entrada
print("Distribución de grados de entrada:", distribucion_grados_entrada(grafo))

