from task_1 import G

# Додавання ваг до ребер
weighted_edges = [
    ('A', 'B', 2), ('B', 'C', 1), ('B', 'D', 4),
    ('C', 'D', 1), ('C', 'E', 3), ('D', 'E', 2), ('E', 'F', 5)
]

for u, v, w in weighted_edges:
    G[u][v]['weight'] = w

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes)
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes['weight']
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)

    return distances

distances = dijkstra(G, 'A')
print("Найкоротші відстані від вершини A до інших вершин:", distances)