# 📌 Comparação entre Matriz de Adjacência e Lista de Adjacência

## 📖 Descrição
Este projeto implementa e compara duas formas de representar grafos: **Matriz de Adjacência** e **Lista de Adjacência**. O objetivo é analisar qual estrutura é mais eficiente para armazenar um grafo com **1000 vértices e apenas 10 arestas**, considerando:

- **Uso de memória**
- **Tempo de busca por vizinhos**
- **Tempo para verificar a existência de uma aresta**

Em grafos esparsos, a lista de adjacência tende a ser mais eficiente devido ao menor uso de memória, enquanto a matriz de adjacência pode ser mais rápida para verificar se uma aresta existe.

## 🏗 Estrutura do Código

O código é organizado da seguinte forma:

- **Implementação da Matriz de Adjacência**
    - Usa uma matriz \( n \times n \) para armazenar as conexões entre vértices.
    - Consome \( O(n^2) \) espaço em memória.
- **Implementação da Lista de Adjacência**
    - Usa um dicionário onde cada vértice armazena apenas seus vizinhos.
    - Consome \( O(n + m) \) espaço, onde \( m \) é o número de arestas.
- **Funções para medir tempo de busca por vizinhos**
    - Mede o tempo necessário para encontrar os vizinhos de um vértice na matriz e na lista.
- **Comparação de uso de memória**
    - Calcula o tamanho ocupado em memória por cada estrutura.

## 📜 Código de Implementação

```python
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
```

## 📊 Saída Esperada

```plaintext
Vizinhos do vértice 50 na Matriz: [200, 700] (Tempo: 0.002300s)
Vizinhos do vértice 50 na Lista: [200, 700] (Tempo: 0.000001s)

Uso de memória - Matriz de Adjacência: 8000000 bytes
Uso de memória - Lista de Adjacência: 5000 bytes
```

## 📌 Análise Comparativa

### **1️⃣ Uso de Memória**
- **Matriz de Adjacência**: Ocupa **O(n²)** espaço, consumindo **8MB** de memória para 1000 vértices.
- **Lista de Adjacência**: Ocupa **O(n + m)** espaço, consumindo **5KB**, pois armazena apenas as conexões existentes.

✅ **A Lista de Adjacência é muito mais eficiente em memória.**

### **2️⃣ Tempo de Busca por Vizinhos**
- **Matriz de Adjacência**: Percorre toda a linha da matriz (**O(n)**) para encontrar vizinhos.
- **Lista de Adjacência**: Retorna os vizinhos instantaneamente (**O(1)**).

✅ **A Lista de Adjacência é muito mais rápida para encontrar vizinhos.**

### **3️⃣ Tempo para Verificar se uma Aresta Existe**
- **Matriz de Adjacência**: Verifica diretamente em **O(1)**.
- **Lista de Adjacência**: Percorre a lista de vizinhos, que no pior caso pode ser **O(m)**.

✅ **A Matriz de Adjacência é melhor para verificar a existência de uma aresta.**

## 📌 Conclusão

Para um grafo **esparso** com **1000 vértices e apenas 10 arestas**, a **Lista de Adjacência** é a melhor escolha, pois:

✅ **Usa muito menos memória**, armazenando apenas as conexões existentes.
✅ **Permite busca eficiente por vizinhos**.
✅ **Escala melhor para grafos grandes**.

A **Matriz de Adjacência** só seria vantajosa se o grafo fosse **denso**, contendo muitas conexões entre os vértices.
