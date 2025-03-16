import numpy as np
from collections import defaultdict
import sys
import time

# Número de vértices e arestas
num_vertices = 1000
arestas = [(0, 10), (5, 20), (50, 200), (100, 150), (300, 400),
           (600, 700), (800, 900), (20, 450), (700, 50), (900, 300)]

# Implementação da Matriz de Adjacência
matriz_adjacencia = np.zeros((num_vertices, num_vertices), dtype=int)
for u, v in arestas:
    matriz_adjacencia[u][v] = 1
    matriz_adjacencia[v][u] = 1  # Grafo não direcionado

# Implementação da Lista de Adjacência
lista_adjacencia = defaultdict(list)
for u, v in arestas:
    lista_adjacencia[u].append(v)
    lista_adjacencia[v].append(u)

# Função para medir tempo de busca por vizinhos
def tempo_busca_vizinhos_matriz(vertice):
    inicio = time.time()
    vizinhos = [i for i in range(num_vertices) if matriz_adjacencia[vertice][i] == 1]
    return time.time() - inicio, vizinhos

def tempo_busca_vizinhos_lista(vertice):
    inicio = time.time()
    vizinhos = lista_adjacencia[vertice]
    return time.time() - inicio, vizinhos

# Testando tempo de busca para um vértice
vertice_teste = 50
matriz_tempo, matriz_vizinhos = tempo_busca_vizinhos_matriz(vertice_teste)
lista_tempo, lista_vizinhos = tempo_busca_vizinhos_lista(vertice_teste)

print(f"Vizinhos do vértice {vertice_teste} na Matriz: {matriz_vizinhos} (Tempo: {matriz_tempo:.6f}s)")
print(f"Vizinhos do vértice {vertice_teste} na Lista: {lista_vizinhos} (Tempo: {lista_tempo:.6f}s)")

# Comparação de uso de memória
memoria_matriz = sys.getsizeof(matriz_adjacencia)
memoria_lista = sys.getsizeof(lista_adjacencia) + sum(sys.getsizeof(v) for v in lista_adjacencia.values())

print(f"Uso de memória - Matriz de Adjacência: {memoria_matriz} bytes")
print(f"Uso de memória - Lista de Adjacência: {memoria_lista} bytes")
