import numpy as np

cidades = ["A", "B", "C", "D"]
indice = {cidade: i for i, cidade in enumerate(cidades)}

# Criando a Matriz de Adjacência (grafo não direcionado)
matriz_adj = np.zeros((len(cidades), len(cidades)), dtype=int)

# Definição das conexões entre cidades
conexoes = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D")
]

# Preenchendo a matriz
for cidade1, cidade2 in conexoes:
    i, j = indice[cidade1], indice[cidade2]
    matriz_adj[i][j] = 1
    matriz_adj[j][i] = 1  # Como é um grafo não direcionado

# Exibindo a Matriz de Adjacência
print("Matriz de Adjacência para o grafo não direcionado:")
print(matriz_adj)
