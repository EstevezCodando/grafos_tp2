# 📌 Grafo de Logística - Lista de Adjacência

## 📖 Descrição
Este projeto implementa um **grafo não direcionado** utilizando **lista de adjacência** para modelar as rotas entre centros de distribuição de uma empresa de logística. Cada centro de distribuição é tratado como um **vértice**, enquanto cada **rota** entre centros representa uma **aresta** com um peso associado, indicando o tempo médio de transporte.

Esta abordagem é útil para planejamento logístico, otimização de rotas de entrega e análise de eficiência operacional.

## 🏗 Estrutura do Código

O código é organizado da seguinte forma:

- **Classe `GrafoLogistica`**: Representa a estrutura do grafo utilizando uma lista de adjacência.
- **Método `adicionar_rota(origem, destino, tempo_transporte)`**:
    - Adiciona conexões entre dois centros de distribuição com um peso associado ao tempo médio de transporte.
    - Se um centro ainda não existir no dicionário, ele é automaticamente criado.
    - Garante que a estrutura permaneça **não direcionada**.
- **Método `obter_vizinhos(centro)`**:
    - Retorna a lista de centros conectados a um determinado centro de distribuição.
    - Se o centro não existir no grafo, retorna uma lista vazia.
- **Método `bfs_rota_mais_curta(inicio, destino)`**:
    - Implementa o **algoritmo BFS (Busca em Largura)** para encontrar a rota mais curta entre dois centros de distribuição.
    - Retorna o caminho encontrado ou `None` se não houver conexão entre os centros.

## 📜 Exemplo de Uso

```python
from collections import deque

class GrafoLogistica:
    def __init__(self):
        self.lista_adjacencia = {}
    
    def adicionar_rota(self, origem: str, destino: str, tempo_transporte: int) -> None:
        if origem not in self.lista_adjacencia:
            self.lista_adjacencia[origem] = []
        if destino not in self.lista_adjacencia:
            self.lista_adjacencia[destino] = []
        
        self.lista_adjacencia[origem].append((destino, tempo_transporte))
        self.lista_adjacencia[destino].append((origem, tempo_transporte))
    
    def obter_vizinhos(self, centro: str) -> list:
        return self.lista_adjacencia.get(centro, [])
    
    def bfs_rota_mais_curta(self, inicio: str, destino: str) -> list:
        fila = deque([(inicio, [inicio])])
        visitados = set()
        
        while fila:
            atual, caminho = fila.popleft()
            if atual == destino:
                return caminho
            
            if atual not in visitados:
                visitados.add(atual)
                for vizinho, _ in self.lista_adjacencia.get(atual, []):
                    if vizinho not in visitados:
                        fila.append((vizinho, caminho + [vizinho]))
        
        return None  # Se não houver caminho

# Criando o grafo de logística
grafo = GrafoLogistica()

grafo.adicionar_rota("A", "B", 5)
grafo.adicionar_rota("A", "C", 10)
grafo.adicionar_rota("B", "D", 7)
grafo.adicionar_rota("C", "E", 8)
grafo.adicionar_rota("D", "E", 4)

# Exibir vizinhos de cada centro de distribuição
print("Lista de vizinhos de cada centro:")
for centro in ["A", "B", "C", "D", "E"]:
    print(f"{centro}: {grafo.obter_vizinhos(centro)}")

# Testando a rota mais curta
origem, destino = "A", "E"
caminho = grafo.bfs_rota_mais_curta(origem, destino)
print(f"Rota mais curta de {origem} para {destino}: {caminho}")
```

## 📊 Saída Esperada
```plaintext
Lista de vizinhos de cada centro:
A: [('B', 5), ('C', 10)]
B: [('A', 5), ('D', 7)]
C: [('A', 10), ('E', 8)]
D: [('B', 7), ('E', 4)]
E: [('C', 8), ('D', 4)]

Rota mais curta de A para E: ['A', 'C', 'E']
```

## 📌 Benefícios da Lista de Adjacência

✅ **Uso eficiente de memória**: A lista de adjacência armazena apenas conexões existentes, economizando espaço em comparação com uma matriz de adjacência.

✅ **Expansibilidade**: Fácil de adicionar novos centros de distribuição e conexões sem redimensionamento da estrutura.

✅ **Busca eficiente**: Encontrar vizinhos de um centro leva **tempo O(1)**, pois acessamos diretamente a chave do dicionário.

✅ **Facilidade de implementação**: Estrutura simples e intuitiva para manipular e consultar relações entre centros de distribuição.

