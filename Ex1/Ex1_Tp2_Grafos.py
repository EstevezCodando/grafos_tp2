import networkx as nx
import matplotlib.pyplot as plt

def obter_conexoes():
    """dicionario das conexões"""
    return {
        "Alice": ["Bob", "Carlos"],
        "Bob": ["Diana"],
        "Carlos": ["Diana", "Eduardo"],
    }

def construir_grafo(conexoes):
    """Cria um grafo não direcionado a partir de um dicionário de conexões."""
    grafo = nx.Graph()
    for pessoa, amigos in conexoes.items():
        for amigo in amigos:
            grafo.add_edge(pessoa, amigo)
    return grafo

def desenhar_grafo(grafo):
    """Desenha o grafo representando a rede social."""
    plt.figure(figsize=(6, 4))
    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
    plt.title("Rede Social - Grafo de Amizades")
    plt.show()

def obter_vertices_arestas(grafo):
    """Retorna a lista de vértices e arestas do grafo."""
    return list(grafo.nodes), list(grafo.edges)

# Execução principal
conexoes = obter_conexoes()
print(conexoes.items())
grafo = construir_grafo(conexoes)
desenhar_grafo(grafo)

# Listar vértices e arestas
vertices, arestas = obter_vertices_arestas(grafo)
print("Vértices:", vertices)
print("Arestas:", arestas)

# Resposta sobre a direção do grafo
print("\nO grafo é não direcionado, pois a relação de amizade é bidirecional.")
