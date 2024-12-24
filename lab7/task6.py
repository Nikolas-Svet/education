class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, priority, item):
        """Добавление элемента с приоритетом"""
        self.queue.append((priority, item))
        self._sift_up(len(self.queue) - 1)

    def dequeue(self):
        """Извлечение элемента с минимальным приоритетом"""
        if not self.queue:
            raise IndexError("dequeue from empty priority queue")

        min_item = self.queue[0][1]
        self.queue[0] = self.queue[-1]
        self.queue.pop()
        self._sift_down(0)
        return min_item

    def _sift_up(self, idx):
        """Просеивание вверх для восстановления свойств минимальной кучи"""
        parent = (idx - 1) // 2
        while idx > 0 and self.queue[parent][0] > self.queue[idx][0]:
            self.queue[parent], self.queue[idx] = self.queue[idx], self.queue[parent]
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        """Просеивание вниз для восстановления свойств минимальной кучи"""
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < len(self.queue) and self.queue[left][0] < self.queue[smallest][0]:
            smallest = left
        if right < len(self.queue) and self.queue[right][0] < self.queue[smallest][0]:
            smallest = right

        if smallest != idx:
            self.queue[smallest], self.queue[idx] = self.queue[idx], self.queue[smallest]
            self._sift_down(smallest)

pq = PriorityQueue()
pq.enqueue(2, "task2")
pq.enqueue(1, "task1")
pq.enqueue(3, "task3")
print(pq.dequeue())
print(pq.dequeue())
