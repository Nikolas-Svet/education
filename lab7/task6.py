import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, priority, item):
        heapq.heappush(self.queue, (priority, item))

    def dequeue(self):
        return heapq.heappop(self.queue)[1]

pq = PriorityQueue()
pq.enqueue(2, "task2")
pq.enqueue(1, "task1")
pq.enqueue(3, "task3")
print(pq.dequeue())
