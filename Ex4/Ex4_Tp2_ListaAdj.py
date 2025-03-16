from collections import defaultdict

class Grafo:
    """
    Classe que representa um grafo utilizando lista de adjacência.
    Cada chave do dicionário 'lista_adjacencia' é um bairro (vértice)
    e o valor é uma lista de bairros conectados (vizinhos).
    """

    def __init__(self):
        self.lista_adjacencia = defaultdict(list)

    def adicionar_aresta(self, bairro_origem: str, bairro_destino: str) -> None:
        """Adiciona uma aresta bidirecional (bairro_origem ↔ bairro_destino) na lista de adjacência."""
        if bairro_destino not in self.lista_adjacencia[bairro_origem]:
            self.lista_adjacencia[bairro_origem].append(bairro_destino)
        if bairro_origem not in self.lista_adjacencia[bairro_destino]:
            self.lista_adjacencia[bairro_destino].append(bairro_origem)

    def obter_vizinhos(self, bairro: str) -> list:
        """Retorna a lista de bairros vizinhos de um determinado bairro."""
        return self.lista_adjacencia.get(bairro, [])

    def exibir_grafo(self) -> None:
        """Exibe todas as conexões do grafo."""
        for bairro, vizinhos in self.lista_adjacencia.items():
            print(f"{bairro} → {', '.join(vizinhos)}")

# Exemplo de uso:
if __name__ == "__main__":
    grafo_bairros = Grafo()

    # Adicionando conexões
    grafo_bairros.adicionar_aresta("Centro", "Bairro A")
    grafo_bairros.adicionar_aresta("Centro", "Bairro B")
    grafo_bairros.adicionar_aresta("Bairro A", "Bairro C")
    grafo_bairros.adicionar_aresta("Bairro B", "Bairro C")
    grafo_bairros.adicionar_aresta("Bairro C", "Bairro D")

    # Exibir o grafo completo
    print("Grafo de bairros:")
    grafo_bairros.exibir_grafo()

    # Consultar vizinhos
    bairro_consulta = "Bairro C"
    print(f"\nVizinhos de {bairro_consulta}: {grafo_bairros.obter_vizinhos(bairro_consulta)}")

    # Consultar bairro inexistente
    bairro_inexistente = "Bairro X"
    print(f"Vizinhos de {bairro_inexistente}: {grafo_bairros.obter_vizinhos(bairro_inexistente)}")
