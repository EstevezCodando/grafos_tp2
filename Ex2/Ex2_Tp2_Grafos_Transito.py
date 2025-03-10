import networkx as nx
import matplotlib.pyplot as plt

def cria_lista_adj():
    """Cria a lista de adjacência com bairros e distâncias (km) entre eles."""
    return {
        "Bairro D": {"Bairro A": 3, "Bairro B": 2},
        "Bairro A": {"Centro": 4, "Bairro C": 5},
        "Bairro B": {"Centro": 6, "Bairro D": 2, "Bairro E": 3},
        "Bairro C": {"Bairro A": 5, "Bairro F": 7},
        "Centro": {"Bairro A": 4, "Bairro B": 6, "Bairro F": 8, "Bairro C": 5},
        "Bairro E": {"Bairro B": 3, "Bairro F": 4},
        "Bairro F": {"Bairro C": 7, "Centro": 8, "Bairro E": 4}
    }

def construir_grafo_bairros(mapa_bairros):
    """Cria um grafo ponderado (com distâncias) a partir do dicionário de bairros."""
    grafo = nx.Graph()
    for bairro, vizinhos in mapa_bairros.items():
        for vizinho, distancia in vizinhos.items():
            grafo.add_edge(bairro, vizinho, weight=distancia)
    return grafo

def desenhar_mapa_grafo(grafo):
    """Desenha o grafo representando os bairros e as ruas com distâncias."""
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(grafo)
    
    # Desenhar nós e arestas
    nx.draw(grafo, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
    
    # Adicionar rótulos de distância (peso das arestas)
    labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels, font_size=10)
    
    plt.title("Mapa de Bairros - Grafo do Trânsito com Distâncias")
    plt.show()

def listar_bairros_e_ruas(grafo):
    """Retorna a lista de bairros (vértices) e ruas (arestas) do grafo."""
    return list(grafo.nodes), list(grafo.edges(data=True))

def encontrar_rota_mais_curta(grafo, origem, destino):
    """Encontra a menor rota entre dois bairros usando o algoritmo de Dijkstra."""
    try:
        caminho = nx.shortest_path(grafo, source=origem, target=destino, weight='weight')
        distancia = nx.shortest_path_length(grafo, source=origem, target=destino, weight='weight')
        return caminho, distancia
    except nx.NetworkXNoPath:
        return None, float('inf')

# Execução do código
mapa_bairros = cria_lista_adj()
grafo_bairros = construir_grafo_bairros(mapa_bairros)
desenhar_mapa_grafo(grafo_bairros)

# Listar bairros e ruas
bairros, ruas = listar_bairros_e_ruas(grafo_bairros)
print("Bairros:", bairros)
print("Ruas e distâncias:", ruas)

# Encontrar a rota mais curta entre dois bairros
origem = "Bairro A"
destino = "Bairro E"
caminho, distancia = encontrar_rota_mais_curta(grafo_bairros, origem, destino)
print(f"\nMenor rota entre {origem} e {destino}: {caminho} com {distancia} km.")

print("\nA melhor estrutura para encontrar a rota mais curta entre dois bairros é a **Lista de Adjacência**, pois ocupa menos memória e é mais eficiente para algoritmos como Dijkstra ou BFS.")
