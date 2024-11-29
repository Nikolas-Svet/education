graph = {}
graph["start"] = {"a": 6, "b": 2}
graph["a"] = {"fin": 1}
graph["b"] = {"a": 3, "fin": 5}
graph["fin"] = {}

def reverse_graph(graph):
    reversed_graph = {}

    for node in graph:
        if node not in reversed_graph:
            reversed_graph[node] = {}
        for neighbor, weight in graph[node].items():
            if neighbor not in reversed_graph:
                reversed_graph[neighbor] = {}
            reversed_graph[neighbor][node] = weight

    return reversed_graph

reversed_graph = reverse_graph(graph)

print("Исходный граф:")
for node, neighbors in graph.items():
    print(f"{node}: {neighbors}")

print("\nОбратный граф:")
for node, neighbors in reversed_graph.items():
    print(f"{node}: {neighbors}")
