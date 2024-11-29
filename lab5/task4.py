import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, city_from, city_to, distance):
        if city_from not in self.adj_list:
            self.adj_list[city_from] = {}
        if city_to not in self.adj_list:
            self.adj_list[city_to] = {}
        self.adj_list[city_from][city_to] = distance

    def get_neighbors(self, city):
        return self.adj_list.get(city, {})

def dijkstra(graph, start, end):
    distances = {city: float('inf') for city in graph.adj_list}
    distances[start] = 0

    # Словарь для хранения предшествующих узлов на кратчайшем пути
    previous_nodes = {city: None for city in graph.adj_list}

    # Приоритетная очередь для обработки узлов (расстояние, узел)
    priority_queue = [(0, start)]

    # Основной цикл обработки узлов
    while priority_queue:
        # Извлечение узла с минимальным расстоянием из очереди
        current_distance, current_city = heapq.heappop(priority_queue)

        # Если текущий узел является конечным, прекращаем поиск
        if current_city == end:
            break

        # Обработка соседей текущего узла
        for neighbor, weight in graph.get_neighbors(current_city).items():
            # Вычисление нового расстояния до соседа
            distance = current_distance + weight

            # Если найден более короткий путь до соседа
            if distance < distances[neighbor]:
                # Обновляем минимальное расстояние до соседа
                distances[neighbor] = distance

                # Обновляем предшествующий узел для соседа
                previous_nodes[neighbor] = current_city

                # Добавляем соседа в очередь с новым расстоянием
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    city = end
    while city is not None:
        path.append(city)

        city = previous_nodes[city]

    path.reverse()

    return distances[end], path if distances[end] != float('inf') else (float('inf'), [])


graph = Graph()

graph.add_edge("Мариинск", "Яя", 40)
graph.add_edge("Мариинск", "Яшкино", 50)
graph.add_edge("Мариинск", "Юрга", 80)
graph.add_edge("Мариинск", "Анжеро-Судженск", 70)
graph.add_edge("Яя", "Кемерово", 100)
graph.add_edge("Яшкино", "Яя", 45)
graph.add_edge("Яшкино", "Томск", 90)
graph.add_edge("Юрга", "Яшкино", 30)
graph.add_edge("Юрга", "Томск", 120)
graph.add_edge("Юрга", "Анжеро-Судженск", 70)
graph.add_edge("Томск", "Кемерово", 110)

start_city = input("Введите начальный город: ")
end_city = input("Введите конечный город: ")

distance, path = dijkstra(graph, start_city, end_city)

if distance == float('inf'):
    print(f"Пути между городами {start_city} и {end_city} нет.")
else:
    print(f"Минимальный путь от {start_city} до {end_city}: {distance} км")
    print(f"Маршрут: {' -> '.join(path)}")

nx_graph = nx.DiGraph()

for city_from, neighbors in graph.adj_list.items():
    for city_to, distance in neighbors.items():
        nx_graph.add_edge(city_from, city_to, weight=distance)

pos = {
    "Мариинск": (0, 0),
    "Яя": (2, -1),
    "Яшкино": (2, 1),
    "Юрга": (1, 2),
    "Анжеро-Судженск": (-1, 2),
    "Томск": (3, 1.5),
    "Кемерово": (4, 0)
}

edge_labels = nx.get_edge_attributes(nx_graph, "weight")

plt.figure(figsize=(12, 8))
nx.draw(
    nx_graph, pos, with_labels=True,
    node_color="lightblue", node_size=2000,
    font_size=10, font_weight="bold", arrowsize=15
)
nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=edge_labels, font_size=9, label_pos=0.5)
plt.title("Маршруты между городами", fontsize=16)
plt.show()