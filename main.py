from Dijkstra import data
from Dijkstra import build_graph
from Dijkstra import dijkstra
from visualizaçãodografo import visualize_graph

graph = build_graph(data)
start = int(input("Digite o nó inicial: "))
end = int(input("Digite o nó final: "))

path, distance = dijkstra(graph, start, end)
print(f"O menor caminho do nó {start} ao nó {end} é: {path} com distância total de {distance}")

visualize_graph(graph, path)

#Por Ana Luisa e Saunay Coutinho