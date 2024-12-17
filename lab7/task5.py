import heapq

class MaxHeap:
    def __init__(self):
        self.data = []

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)

h = MaxHeap()
h.push(10)
h.push(5)
h.push(15)
print(h.pop())
