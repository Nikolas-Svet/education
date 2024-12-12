class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, node, neighbor):
        if node not in self.adj_list:
            self.adj_list[node] = []
        self.adj_list[node].append(neighbor)

    def get_neighbors(self, node):
        return self.adj_list.get(node, [])

    def display(self):
        for node, neighbors in self.adj_list.items():
            print(f"{node}: {neighbors}")

def dfs_topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph.get_neighbors(node):
            #обрабатываются все узлы, от которых зависит текущий узел
            dfs(neighbor)
        stack.append(node)

    for node in graph.adj_list:
        if node not in visited:
            dfs(node)

    return stack[::-1]

recipe_graph = Graph()
recipe_graph.add_edge("1 Tbl Oil", "1 cup mix")
recipe_graph.add_edge("1 egg", "1 cup mix")
recipe_graph.add_edge("3/4 cup milk", "1 cup mix")
recipe_graph.add_edge("1 cup mix", "pour 1/4 cup")
recipe_graph.add_edge("heat griddle", "pour 1/4 cup")
recipe_graph.add_edge("pour 1/4 cup", "turn when bubbly")
recipe_graph.add_edge("turn when bubbly", "eat")
recipe_graph.add_edge("heat syrup", "eat")
recipe_graph.add_edge("1 cup mix", "heat syrup")

sorted_steps = dfs_topological_sort(recipe_graph)

print("Корректная последовательность шагов для рецепта блинов:")
for step in sorted_steps:
    print(step)
