# 📌 Representação do Grafo

Podemos interpretar esses relacionamentos de duas formas distintas:
1 - **Um grafo não direcionado**, considerando que a amizade é mútua  ou seja, se Alice é amiga de Bob, então Bob também é amigo de Alice.
2 - **Um grafo direcionado**, considerando que a amizade funciona de maneira similar a "seguidor" e "seguido".
Considerando o texto  e a noção de "amizade" vamos partir da premissa que é um grafo não direcionado e as amizades são mútuas.

O grafo pode ser descrito como **G = (V, E)**, onde:
- **V (Vértices)**: Representam os usuários da rede social.
- **E (Arestas)**: Representam as conexões de amizade entre os usuários.

---

## 1️⃣ Lista de Vértices e Arestas

### 📍 **Vértices (V)**
O conjunto de vértices representa os usuários da rede:
```text
V = {Alice, Bob, Carlos, Diana, Eduardo}
```

### 🔗 **Arestas (E)**
As conexões entre os usuários são representadas pelas arestas:
```text
E = {(Alice, Bob), (Alice, Carlos), (Bob, Diana), (Carlos, Diana), (Carlos, Eduardo)}
```
Cada aresta representa uma **conexão de amizade** e **não tem direção específica**.

---

## 2️⃣ Classificação: Grafo Direcionado ou Não Direcionado?

✔️ **O grafo é não direcionado.**

### 🔎 **Justificativa**:
- A **relação de amizade é simétrica**: se Alice é amiga de Bob, então Bob automaticamente é amigo de Alice.
- Como **não há um sentido único** (como seguir alguém no Twitter), as arestas **não possuem direção**, tornando o grafo **não direcionado**.

---
### 📷 Visualização do Grafo
![Representação do Grafo](Ex1_figure.png)

## 3️⃣ Desenho do Grafo

Para desenhar o grafo utilizamos networkx e matplotlib

```python
import networkx as nx
import matplotlib.pyplot as plt

def obter_conexoes():
    return {
        "Alice": ["Bob", "Carlos"],
        "Bob": ["Diana"],
        "Carlos": ["Diana", "Eduardo"]
    }

def construir_grafo(conexoes):
    grafo = nx.Graph()
    for usuario, amigos in conexoes.items():
        for amigo in amigos:
            grafo.add_edge(usuario, amigo)
    return grafo

def desenhar_grafo(grafo):
    plt.figure(figsize=(6, 4))
    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
    plt.title("Rede Social - Grafo de Amizades")
    plt.show()

# Execução
grafo = construir_grafo(obter_conexoes())
desenhar_grafo(grafo)
```

---

## 📊 **Conclusão**
- Representamos a rede social como um **grafo não direcionado**.
- Listamos os **vértices (usuários)** e **arestas (conexões de amizade)**.
- Justificamos que **não há direcionalidade** pois a relação de amizade é bidirecional.
- Utilizamos Python e `networkx` para gerar e visualizar o grafo.


