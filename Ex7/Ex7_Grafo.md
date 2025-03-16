# 📌 Representação e Travessia de um Grafo

## 📖 Descrição
Este projeto implementa um **grafo não direcionado** utilizando **lista de adjacência** para representar conexões entre cidades. Cada **cidade** é um **vértice**, e cada **estrada direta** entre duas cidades é uma **aresta**.

Essa estrutura é útil para modelar redes de transporte, permitindo análises como a identificação de vizinhos e a busca por caminhos mais curtos.

## 🏗 Estrutura do Código

O código é organizado da seguinte forma:

- **Classe `Grafo`**: Representa a estrutura do grafo usando uma lista de adjacência.
- **Método `adicionar_estrada(cidade_origem, cidade_destino)`**:
    - Adiciona conexões bidirecionais entre cidades.
    - Se uma cidade ainda não existir no dicionário, ela é criada automaticamente.
- **Método `obter_vizinhos(cidade)`**:
    - Retorna a lista de cidades vizinhas.
    - Se a cidade não existir no grafo, retorna uma lista vazia.
- **Método `exibir_grafo()`**:
    - Exibe todas as conexões do grafo de forma legível.

## 📜 Código de Implementação

```python
from collections import defaultdict

class Grafo:
    def __init__(self):
        self.lista_adjacencia = defaultdict(list)
    
    def adicionar_estrada(self, cidade_origem: str, cidade_destino: str) -> None:
        """
        Adiciona uma estrada bidirecional (cidade_origem ↔ cidade_destino) na lista de adjacência.
        """
        self.lista_adjacencia[cidade_origem].append(cidade_destino)
        self.lista_adjacencia[cidade_destino].append(cidade_origem)
    
    def obter_vizinhos(self, cidade: str) -> list:
        """
        Retorna a lista de cidades vizinhas de uma determinada cidade.
        """
        return self.lista_adjacencia.get(cidade, [])
    
    def exibir_grafo(self) -> None:
        """
        Exibe todas as conexões do grafo.
        """
        for cidade, vizinhos in self.lista_adjacencia.items():
            print(f"{cidade} → {', '.join(vizinhos)}")

# Criando o grafo das cidades
grafo_cidades = Grafo()

# Adicionando as estradas conforme o enunciado
grafo_cidades.adicionar_estrada("A", "B")
grafo_cidades.adicionar_estrada("A", "C")
grafo_cidades.adicionar_estrada("B", "D")
grafo_cidades.adicionar_estrada("C", "E")
grafo_cidades.adicionar_estrada("D", "F")
grafo_cidades.adicionar_estrada("E", "F")

# Exibir o grafo
grafo_cidades.exibir_grafo()
```

## 📊 Saída Esperada

```plaintext
A → B, C
B → A, D
C → A, E
D → B, F
E → C, F
F → D, E
```

## 📌 Estrutura de Dados Mais Eficiente

### **Por que usar `defaultdict(list)`?**
A estrutura **`defaultdict(list)`** do Python é a melhor opção para armazenar a lista de adjacência porque:

✅ **Evita verificações manuais**: Ao adicionar uma estrada, não precisamos verificar se a cidade já existe no dicionário.
✅ **Facilita a adição de novas conexões**: Se a cidade ainda não existir, `defaultdict` cria automaticamente uma lista vazia para ela.
✅ **Acesso rápido e eficiente**: Como dicionários têm tempo de busca **O(1)** na média, acessar as conexões de uma cidade é muito rápido.

### **Comparação com outras estruturas**

| Estrutura de Dados | Vantagens | Desvantagens |
|-------------------|-----------|-------------|
| `defaultdict(list)` | Rápido para adicionar e buscar conexões. Memória eficiente para grafos esparsos. | Não é adequado para grafos densos com muitas conexões |
| Lista de listas | Simples de implementar. | Requer pesquisa linear para encontrar conexões, tornando-o ineficiente para grandes grafos. |
| Matriz de adjacência | Acesso a arestas é instantâneo **O(1)**. | Usa **O(n²)** de memória, tornando-o impraticável para grafos grandes e esparsos. |

