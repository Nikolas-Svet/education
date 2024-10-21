class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def search(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def add_front(self, item):
        new_node = Node(item)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def add_rear(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Удаление из пустого списка")
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return data

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Удаление из пустого списка")
        current = self.head
        while current.next:
            current = current.next
        data = current.data
        if current.prev:
            current.prev.next = None
        else:
            self.head = None
        return data

    def insert_before(self, target_item, new_item):
        if self.is_empty():
            raise ValueError("Список пуст")
        current = self.head
        while current and current.data != target_item:
            current = current.next
        if current is None:
            raise ValueError(f"Элемент {target_item} не найден")
        new_node = Node(new_item)
        new_node.next = current
        new_node.prev = current.prev
        if current.prev:
            current.prev.next = new_node
        else:
            self.head = new_node
        current.prev = new_node

    def insert_after(self, target_item, new_item):
        if self.is_empty():
            raise ValueError("Список пуст")
        current = self.head
        while current and current.data != target_item:
            current = current.next
        if current is None:
            raise ValueError(f"Элемент {target_item} не найден")
        new_node = Node(new_item)
        new_node.prev = current
        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def remove(self, item):
        if self.is_empty():
            raise ValueError("Список пуст")
        current = self.head
        while current and current.data != item:
            current = current.next
        if current is None:
            raise ValueError(f"Элемент {item} не найден")
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(elements) + ']'
