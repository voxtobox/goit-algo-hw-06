import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

nodes = ['A', 'B', 'C', 'D', 'E', 'F']
G.add_nodes_from(nodes)

edges = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E'), ('E', 'F')]
G.add_edges_from(edges)




if __name__ == "__main__":
    # Основні характеристики графа
    print(f"Кількість вершин: {G.number_of_nodes()}")
    print(f"Кількість ребер: {G.number_of_edges()}")
    print("Ступінь кожної вершини:")
    for node, deg in dict(G.degree()).items():
        print(f"{node}: {deg}")
        
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.title("Транспортна мережа міста")
    plt.show()

