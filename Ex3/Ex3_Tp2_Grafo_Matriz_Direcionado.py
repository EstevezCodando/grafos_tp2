import numpy as np

cidades = ["A", "B", "C", "D"]
indice = {cidade: i for i, cidade in enumerate(cidades)}


# Criando a Matriz de Adjacência (grafo direcionado)
matriz_adj_dir = np.zeros((len(cidades), len(cidades)), dtype=int)

# Definição das conexões entre cidades (AGORA DIRECIONADAS)
conexoes_direcionadas = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D")
]

# Preenchendo a matriz direcionada
for cidade1, cidade2 in conexoes_direcionadas:
    i, j = indice[cidade1], indice[cidade2]
    matriz_adj_dir[i][j] = 1  # Apenas direção única

# Exibindo a Matriz de Adjacência Direcionada
print("\nMatriz de Adjacência para o grafo direcionado:")
print(matriz_adj_dir)
