import heapq

def dijkstra(graph, start, end):
    queue = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    shortest_path = {vertex: None for vertex in graph}

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_vertex == end:
            break

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                shortest_path[neighbor] = current_vertex

    path = []
    current_vertex = end
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = shortest_path[current_vertex]
    path = path[::-1]  # Reverso do caminho

    return distances, path

# Receber os nós de entrada do usuário
start_vertex = int(input("Digite o nó de origem: "))
end_vertex = int(input("Digite o nó de destino: "))
distances, path = dijkstra(graph, start_vertex, end_vertex)
print(f"Distâncias: {distances}")
print(f"Caminho mais curto de {start_vertex} para {end_vertex}: {path}")
