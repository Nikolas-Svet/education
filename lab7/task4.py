class LimitedHeap:
    def __init__(self, size):
        self.size = size
        self.data = []

    def push(self, val):
        if len(self.data) < self.size:
            self.data.append(val)
            self._sift_up(len(self.data) - 1)
        else:
            if val > self.data[0]:
                self.data[0] = val
                self._sift_down(0)

    def _sift_up(self, idx):
        """Просеивание вверх для поддержания кучи"""
        parent = (idx - 1) // 2
        while idx > 0 and self.data[parent] > self.data[idx]:
            self.data[parent], self.data[idx] = self.data[idx], self.data[parent]
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        """Просеивание вниз для поддержания кучи"""
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < len(self.data) and self.data[left] < self.data[smallest]:
            smallest = left
        if right < len(self.data) and self.data[right] < self.data[smallest]:
            smallest = right

        if smallest != idx:
            self.data[smallest], self.data[idx] = self.data[idx], self.data[smallest]
            self._sift_down(smallest)

    def get_elements(self):
        """Возвращает элементы в отсортированном порядке"""
        return sorted(self.data, reverse=True)


h = LimitedHeap(3)
for v in [5, 10, 3, 7, 8]:
    h.push(v)
print(h.get_elements())
