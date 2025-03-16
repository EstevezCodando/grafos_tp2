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

#
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