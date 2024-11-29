from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, node, neighbors):
        self.adj_list[node] = neighbors

    def get_neighbors(self, node):
        return self.adj_list.get(node, [])

def person_is_seller(name):
    return name[0] == 'a'

graph = Graph()
graph.add_edge("you", ["alice", "bob", "claire"])
graph.add_edge("bob", ["anuj", "peggy"])
graph.add_edge("alice", ["peggy"])
graph.add_edge("claire", ["thom", "jonny"])
graph.add_edge("anuj", [])
graph.add_edge("peggy", [])
graph.add_edge("thom", [])
graph.add_edge("jonny", [])

def search(name):
    search_queue = deque()
    search_queue += graph.get_neighbors(name)
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph.get_neighbors(person)
                searched.add(person)
    return False

search("you")