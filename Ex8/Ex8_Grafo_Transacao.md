# 📌 Detecção de Fraudes Financeiras com Grafos

## 📖 Descrição
Bancos e instituições financeiras utilizam algoritmos para **monitorar transações** e identificar possíveis **esquemas de lavagem de dinheiro**. Um dos comportamentos suspeitos mais comuns ocorre quando o dinheiro circula entre várias contas e **retorna à conta de origem**, dificultando a identificação da **origem ilícita dos fundos**.

Para detectar esse comportamento, podemos modelar as **transações financeiras como um grafo**, onde:
- **As contas bancárias** são representadas como **vértices**.
- **Cada transação** entre contas é uma **aresta direcionada**.
- **A existência de um ciclo** indica que o dinheiro está circulando entre contas e possivelmente retornando ao ponto de origem.

## 🏗 Estrutura do Código

O código é estruturado da seguinte maneira:

- **Classe `GrafoTransacoes`**: Representa o grafo das transações.
- **Método `adicionar_transacao(origem, destino)`**:
    - Adiciona uma **transação** ao grafo, criando uma conexão direcionada entre duas contas bancárias.
- **Método `detectar_ciclo_utilizando_dfs()`**:
    - Utiliza **DFS (Busca em Profundidade)** para verificar se há **ciclos no grafo**.
    - Se um ciclo for detectado, retorna `True` indicando possível **fraude financeira**.

## 📜 Código de Implementação

```python
from collections import defaultdict

class GrafoTransacoes:
    def __init__(self):
        self.grafo = defaultdict(list)

    def adicionar_transacao(self, origem: str, destino: str):
        """
        Adiciona uma transação (aresta direcionada) ao grafo.
        """
        self.grafo[origem].append(destino)

    def detectar_ciclo_utilizando_dfs(self):
        """
        Implementa DFS para detectar ciclos no grafo das transações.
        """
        visitados = set()
        pilha_recursao = set()

        def dfs(vertice):
            if vertice in pilha_recursao:
                return True  # Ciclo detectado

            if vertice in visitados:
                return False

            visitados.add(vertice)
            pilha_recursao.add(vertice)

            for vizinho in self.grafo[vertice]:
                if dfs(vizinho):
                    return True

            pilha_recursao.remove(vertice)
            return False

        # Criar uma **cópia das chaves** antes da iteração para evitar erro
        for vertice in list(self.grafo.keys()):  
            if dfs(vertice):
                return True

        return False

# Exemplo de uso - Caso com ciclo
grafo_transacoes = GrafoTransacoes()
grafo_transacoes.adicionar_transacao("A", "B")
grafo_transacoes.adicionar_transacao("B", "C")
grafo_transacoes.adicionar_transacao("C", "D")
grafo_transacoes.adicionar_transacao("D", "A")  # Cria um ciclo suspeito

# Verificando se há um ciclo
if grafo_transacoes.detectar_ciclo_utilizando_dfs():
    print("🚨 Alerta: Ciclo financeiro suspeito detectado!")
else:
    print("✅ Nenhuma atividade suspeita detectada.")

# Exemplo de uso - Caso sem ciclo
grafo = GrafoTransacoes()
grafo.adicionar_transacao("J", "K")
grafo.adicionar_transacao("L", "P")
grafo.adicionar_transacao("P", "O")
grafo.adicionar_transacao("O", "Y")

# Verificando se há um ciclo
if grafo.detectar_ciclo_utilizando_dfs():
    print("🚨 Alerta: Ciclo financeiro suspeito detectado!")
else:
    print("✅ Nenhuma atividade suspeita detectada.")
```

## 📊 Saída Esperada
```plaintext
🚨 Alerta: Ciclo financeiro suspeito detectado!
✅ Nenhuma atividade suspeita detectada.
```