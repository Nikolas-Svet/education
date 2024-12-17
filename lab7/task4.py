import heapq

class LimitedHeap:
    def __init__(self, size):
        self.size = size
        self.data = []

    def push(self, val):
        if len(self.data) < self.size:
            heapq.heappush(self.data, val)
        else:
            heapq.heappushpop(self.data, val)

    def get_elements(self):
        return sorted(self.data, reverse=True)

h = LimitedHeap(3)
for v in [5, 10, 3, 7, 8]:
    h.push(v)
print(h.get_elements())
