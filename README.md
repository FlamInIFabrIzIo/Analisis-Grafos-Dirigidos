# Análisis de Grafos Dirigidos

Este proyecto proporciona herramientas para la visualización y el análisis básico de redes dirigidas. Está diseñado para trabajar con grafos representados como diccionarios en Python, donde cada nodo apunta a un conjunto de nodos destino.

## Funcionalidades

- **Creación de grafos completos no dirigidos**: Genera grafos donde cada nodo está conectado con todos los demás.
- **Cálculo de grados de entrada**: Determina el número de aristas entrantes para cada nodo en un grafo dirigido.
- **Distribución de grados de entrada**: Analiza cuántos nodos tienen una cantidad específica de grados de entrada.
- **Visualización de grafos dirigidos**: Representa gráficamente los nodos y las conexiones utilizando `networkx` y `matplotlib`.

## Requisitos

Este proyecto utiliza las siguientes bibliotecas de Python:

- `networkx`: Para la representación y manipulación de grafos.
- `matplotlib`: Para la visualización gráfica de los grafos.

Asegúrate de instalarlas antes de ejecutar el código:

```bash
pip install networkx matplotlib
```

<p align="center">
  <img src="Analisis-Grafos-Dirigidos\image\grafo-proy.png" alt="Visualización del GRAFO_EJEMPLO_1" />
</p>


En la imagen se puede apreciar como cada nodo apunta a los nodos definidos en el diccionario original, visualizándose mediante flechas.Esto permite observar la estructura del grafo, la dirección de las conexiones y analizar visualmente los grados de entrada de cada nodo.