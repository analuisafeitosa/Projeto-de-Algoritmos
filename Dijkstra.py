import heapq
from acessoaobanco import acessoaobd

def dijkstra(graph, start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    path, current_node = [], end
    while previous_nodes[current_node] is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    if path:
        path.insert(0, current_node)
    return path, distances[end]

def build_graph(data):
    graph = {}
    for edge in data:
        u, v, w = edge
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = w
        graph[v][u] = w  # If the graph is undirected
    return graph

data = acessoaobd()

graph = build_graph(data)
start = int(input("Digite o nó inicial: "))
end = int(input("Digite o nó final: "))

path, distance = dijkstra(graph, start, end)
print(f"O menor caminho do nó {start} ao nó {end} é: {path} com distância total de {distance}")
