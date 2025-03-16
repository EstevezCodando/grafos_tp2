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

        for vertice in list(self.grafo.keys()):  
            if dfs(vertice):
                return True

        return False

print('Caso 1:  Atividade Suspeita A-> B, B-> C, C -> D, D -> A ')
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

print('Caso 2:  Sem atividade Suspeita J -> K, L-> P, P -> O, O -> Y ')
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
