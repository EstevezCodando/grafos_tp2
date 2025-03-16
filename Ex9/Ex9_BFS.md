# 📌 Implementação do Algoritmo Breadth-First Search (BFS)

## 📖 Descrição
O algoritmo **BFS (Busca em Largura)** é uma técnica de travessia de grafos que explora **todos os vértices vizinhos antes de avançar para os próximos níveis**. Diferente do **DFS (Busca em Profundidade)**, que usa uma **pilha**, a BFS utiliza uma **fila (FIFO - First In, First Out)** para garantir que os vértices sejam explorados em camadas.

Nesta implementação, representamos um **grafo não direcionado** usando **lista de adjacência**, e aplicamos o algoritmo **BFS iniciando pelo vértice `A`**.

## 🏗 Estrutura do Código

### **1️⃣ Classe `Grafo`**
A classe contém:
- **`lista_adjacencia`** → Dicionário que armazena os vértices e suas conexões.
- **`adicionar_aresta(origem, destino)`** → Adiciona uma aresta bidirecional entre dois vértices.
- **`bfs(inicio)`** → Executa a busca em largura a partir do vértice informado.

---

## 📜 Código de Implementação

```python
from collections import deque, defaultdict

class Grafo:
    def __init__(self):
        self.lista_adjacencia = defaultdict(list)
    
    def adicionar_aresta(self, origem: str, destino: str) -> None:
        """
        Adiciona uma aresta bidirecional ao grafo.
        """
        self.lista_adjacencia[origem].append(destino)
        self.lista_adjacencia[destino].append(origem)
    
    def bfs(self, inicio: str):
        """
        Implementa a Busca em Largura (BFS) para percorrer o grafo a partir de um vértice inicial.
        """
        visitados = set()
        fila = deque([inicio])
        ordem_visita = []
        
        while fila:
            vertice = fila.popleft()
            if vertice not in visitados:
                visitados.add(vertice)
                ordem_visita.append(vertice)
                
                for vizinho in self.lista_adjacencia[vertice]:
                    if vizinho not in visitados:
                        fila.append(vizinho)
        
        return ordem_visita

# Criando o grafo conforme a Questão 7
grafo = Grafo()
grafo.adicionar_aresta("A", "B")
grafo.adicionar_aresta("A", "C")
grafo.adicionar_aresta("B", "D")
grafo.adicionar_aresta("C", "E")
grafo.adicionar_aresta("D", "F")
grafo.adicionar_aresta("E", "F")

# Executando BFS a partir do vértice A
ordem_bfs = grafo.bfs("A")
print("Ordem dos vértices visitados pela BFS:", ordem_bfs)
```

## 📊 Saída Esperada
```plaintext
Ordem dos vértices visitados pela BFS: ['A', 'B', 'C', 'D', 'E', 'F']
```

## 🔍 **Como o BFS Funciona?**

1️⃣ **Inicialização:**
   - Criamos um **conjunto `visitados`** para armazenar os nós já percorridos.
   - Usamos uma **fila (`deque`)** para armazenar os vértices que precisam ser explorados.
   - Criamos uma **lista `ordem_visita`** para armazenar a ordem de visita dos vértices.

2️⃣ **Execução:**
   - Retiramos um vértice da **fila** (`popleft()`), marcamos como **visitado** e armazenamos na lista `ordem_visita`.
   - Adicionamos todos os **vizinhos não visitados** à **fila**, garantindo que sejam processados posteriormente.
   - O processo continua **até que todos os vértices sejam explorados**.

## 📌 **Diferença entre BFS e DFS**

| Característica | BFS (Busca em Largura) | DFS (Busca em Profundidade) |
|---------------|----------------------|--------------------------|
| Estrutura de dados | **Fila (FIFO)** | **Pilha (LIFO)** |
| Ordem de visita | Explora **camada por camada** | Explora **um ramo antes de voltar** |
| Melhor para | Encontrar caminhos mínimos em grafos não ponderados | Explorar todos os caminhos possíveis |
| Complexidade | O(V + E) | O(V + E) |


