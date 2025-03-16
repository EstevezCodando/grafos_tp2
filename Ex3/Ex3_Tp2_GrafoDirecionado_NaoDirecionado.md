# 📌 Representação de Cidades e Estradas como um Grafo

Este exercício propõe a construção da **matriz de adjacência** de um grafo simples, onde os **vértices** são cidades (A, B, C e D) e as **arestas** indicam estradas que conectam essas cidades diretamente. O objetivo é compreender como a matriz de adjacência reflete as conexões, tanto no caso **não direcionado** (cada estrada serve nos dois sentidos) quanto no caso **direcionado** (a estrada tem apenas um sentido de percurso).

## 📍 Estrutura do Grafo

As cidades do grafo são:
- **A**
- **B**
- **C**
- **D**

As estradas (ou arestas) que ligam essas cidades são:
- A ↔ B
- A ↔ C
- B ↔ D
- C ↔ D

Neste modelo, interpretamos que A tem conexões diretas com B e C, enquanto B e C se conectam com D. Para um **grafo não direcionado**, a ligação A ↔ B é a mesma que B ↔ A, e assim por diante, resultando em uma matriz simétrica.

## 🔗 Construção da Matriz de Adjacência (Grafo Não Direcionado)

Na **matriz de adjacência** de um grafo não direcionado, cada linha e cada coluna correspondem a uma cidade, e a célula (i, j) assume valor 1 quando existe uma estrada direta ligando as cidades i e j, ou 0 caso contrário. Como as estradas são bidirecionais, a matriz final será simétrica em relação à diagonal principal.

Supondo a ordem dos vértices **A, B, C, D**, podemos montar a matriz abaixo:

|       | A | B | C | D |
|:-----:|:-:|:-:|:-:|:-:|
| **A** | 0 | 1 | 1 | 0 |
| **B** | 1 | 0 | 0 | 1 |
| **C** | 1 | 0 | 0 | 1 |
| **D** | 0 | 1 | 1 | 0 |

- A linha de A (primeira) tem 1 para B e C, pois há estradas A ↔ B e A ↔ C.
- B (segunda linha) tem 1 para A e D, refletindo as conexões B ↔ A e B ↔ D.
- C (terceira linha) tem 1 para A e D, pois C ↔ A e C ↔ D.
- D (quarta linha) tem 1 para B e C, indicando D ↔ B e D ↔ C.

Note que os valores acima da diagonal principal são espelhados abaixo dela, confirmando o caráter não direcionado das estradas.

## 🚦 Matriz de Adjacência (Grafo Direcionado)

Se considerarmos o **grafo direcionado**, cada estrada pode ter um único sentido. Por exemplo, se tivermos estradas A → B, A → C, B → D e C → D (sem o retorno), a **matriz de adjacência** deixa de ser simétrica. Utilizando novamente a ordem **A, B, C, D**, temos:

|       | A | B | C | D |
|:-----:|:-:|:-:|:-:|:-:|
| **A** | 0 | 1 | 1 | 0 |
| **B** | 0 | 0 | 0 | 1 |
| **C** | 0 | 0 | 0 | 1 |
| **D** | 0 | 0 | 0 | 0 |

Neste cenário, cada 1 indica uma estrada direcionada do vértice da linha para o vértice da coluna. Por exemplo, na posição (A, B) há 1, significando uma estrada A → B, mas (B, A) permanece 0, pois a mão contrária não está definida como existente.

## 📝 Conclusão

1. **Grafo não direcionado**: a matriz de adjacência é **simétrica**, pois cada conexão (A ↔ B) se traduz em **1** tanto em (A, B) quanto em (B, A).
2. **Grafo direcionado**: a matriz de adjacência se torna **assimétrica**, onde cada estrada (A → B) aparece apenas na posição (A, B), não havendo reciprocidade obrigatória em (B, A).

Esse exemplo mostra como a **matriz de adjacência** é útil para representar e manipular dados de conectividade em grafos, além de evidenciar as diferenças estruturais entre **arestas não direcionadas** e **arestas direcionadas**.