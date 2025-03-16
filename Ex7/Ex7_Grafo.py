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
