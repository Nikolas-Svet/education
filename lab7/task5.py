class MaxHeap:
    def __init__(self):
        self.data = []

    def push(self, val):
        """Добавление элемента в кучу и просеивание вверх"""
        self.data.append(val)
        self._sift_up(len(self.data) - 1)

    def pop(self):
        """Извлечение максимального элемента с восстановлением кучи"""
        if not self.data:
            raise IndexError("pop from empty heap")

        max_val = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self._sift_down(0)
        return max_val

    def _sift_up(self, idx):
        """Просеивание вверх: поддержка свойства максимальной кучи"""
        parent = (idx - 1) // 2
        while idx > 0 and self.data[parent] < self.data[idx]:
            self.data[parent], self.data[idx] = self.data[idx], self.data[parent]
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        """Просеивание вниз: поддержка свойства максимальной кучи"""
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < len(self.data) and self.data[left] > self.data[largest]:
            largest = left

        if right < len(self.data) and self.data[right] > self.data[largest]:
            largest = right

        if largest != idx:
            self.data[largest], self.data[idx] = self.data[idx], self.data[largest]
            self._sift_down(largest)

h = MaxHeap()
h.push(10)
h.push(5)
h.push(15)
print(h.pop())
