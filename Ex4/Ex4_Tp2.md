# 📌 Grafo de Bairros - Lista de Adjacência

## 📖 Descrição
Este projeto implementa um **grafo não direcionado** utilizando **lista de adjacência** para representar a conexão entre bairros de uma cidade. A estrutura de dados escolhida permite representar a malha viária da cidade de forma eficiente, facilitando consultas sobre conexões diretas entre bairros.

Cada **bairro** é tratado como um **vértice**, enquanto cada **rua** conectando dois bairros é uma **aresta** do grafo. Esse modelo é útil para diversas aplicações, como planejamento de rotas de transporte, logística de entregas e análise de fluxo urbano.

## 🏗 Estrutura do Código

O código é organizado da seguinte forma:

- **Classe `Grafo`**: Responsável por armazenar e manipular a estrutura do grafo.
    - Utiliza um dicionário (`self.lista_adjacencia`) para representar os bairros e suas conexões.
- **Método `adicionar_aresta(bairro_origem, bairro_destino)`**:
    - Adiciona conexões entre dois bairros, garantindo que o grafo seja **não direcionado**.
    - Se um bairro ainda não existir no dicionário, ele é automaticamente criado.
    - Evita duplicatas para garantir consistência na estrutura.
- **Método `obter_vizinhos(bairro)`**:
    - Retorna uma lista de bairros vizinhos para um determinado bairro.
    - Se o bairro não existir no grafo, retorna uma lista vazia, evitando erros.
- **Método `exibir_grafo()`**:
    - Exibe todas as conexões do grafo em formato legível.
    - Permite visualizar facilmente a estrutura da malha viária representada.

## 📜 Exemplo de Uso

```python
from grafo import Grafo

# Criando o grafo
grafo_bairros = Grafo()

grafo_bairros.adicionar_aresta("Centro", "Bairro A")
grafo_bairros.adicionar_aresta("Centro", "Bairro B")
grafo_bairros.adicionar_aresta("Bairro A", "Bairro C")
grafo_bairros.adicionar_aresta("Bairro B", "Bairro C")
grafo_bairros.adicionar_aresta("Bairro C", "Bairro D")

# Exibir o grafo completo
grafo_bairros.exibir_grafo()

# Consultar vizinhos de um bairro
bairro_consulta = "Bairro C"
print(f"Vizinhos de {bairro_consulta}: {grafo_bairros.obter_vizinhos(bairro_consulta)}")
```

## 📊 Saída Esperada

```plaintext
Grafo de bairros:
Centro → Bairro A, Bairro B
Bairro A → Centro, Bairro C
Bairro B → Centro, Bairro C
Bairro C → Bairro A, Bairro B, Bairro D
Bairro D → Bairro C

Vizinhos de Bairro C: ['Bairro A', 'Bairro B', 'Bairro D']
```

## 📌 Benefícios da Lista de Adjacência

### 🛠 Como a Lista de Adjacência Otimiza o Armazenamento?
A lista de adjacência é uma estrutura eficiente para representar grafos esparsos (com poucas conexões) porque:

- **Uso eficiente de memória**: Em um grafo com muitos vértices e poucas arestas, a matriz de adjacência desperdiça muito espaço armazenando zeros desnecessários. A lista de adjacência armazena apenas conexões existentes, economizando memória significativamente.
- **Acesso rápido aos vizinhos**: Como os vizinhos de um vértice são armazenados diretamente em listas, encontrar os bairros conectados a um determinado bairro é uma operação rápida, geralmente \(O(1)\) no caso de dicionários.
- **Facilidade de expansão**: Adicionar um novo bairro ou uma nova rua ao grafo não requer redimensionamento da estrutura, diferentemente da matriz de adjacência que precisaria de uma nova linha e coluna.
- **Eficiência computacional**: Para um grafo com \(n\) vértices e \(m\) arestas, a lista de adjacência consome \(O(n + m)\) espaço, enquanto a matriz de adjacência ocupa \(O(n^2)\), tornando a lista muito mais escalável para grafos grandes.



✅ **Eficiência em memória**: A lista de adjacência armazena apenas conexões existentes, economizando espaço em comparação com uma matriz de adjacência, que desperdiçaria memória para bairros sem conexão.

✅ **Busca eficiente**: Encontrar vizinhos de um bairro leva **tempo O(1)**, pois acessamos diretamente a chave do dicionário.

