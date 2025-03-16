from collections import deque

class GrafoLogistica:
    def __init__(self):
        self.lista_adjacencia = {}
    
    def adicionar_rota(self, origem: str, destino: str, tempo_transporte: int) -> None:
        """
        Adiciona uma conexão bidirecional (origem ↔ destino) com peso representando o tempo médio de transporte.
        """
        if origem not in self.lista_adjacencia:
            self.lista_adjacencia[origem] = []
        if destino not in self.lista_adjacencia:
            self.lista_adjacencia[destino] = []
        
        self.lista_adjacencia[origem].append((destino, tempo_transporte))
        self.lista_adjacencia[destino].append((origem, tempo_transporte))
    
    def obter_vizinhos(self, centro: str) -> list:
        """
        Retorna os centros de distribuição conectados a um determinado centro.
        """
        return self.lista_adjacencia.get(centro, [])
    
    def bfs_rota_mais_curta(self, inicio: str, destino: str) -> list:
        """
        Implementa a busca em largura (BFS) para encontrar a rota mais curta entre dois centros de distribuição.
        """
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

# Adicionando rotas com tempo médio de transporte
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
