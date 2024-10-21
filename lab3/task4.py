from task1 import *


class Stack:
    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def push(self, item):
        self.items.add(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Стек пуст")
        return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            raise IndexError("Стек пуст")
        return self.items.head.getData()

    def size(self):
        return self.items.size()


class Queue:
    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Очередь пуста")
        return self.items.pop(0)

    def size(self):
        return self.items.size()


class Deque:
    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def addFront(self, item):
        self.items.add(item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        if self.isEmpty():
            raise IndexError("Дек пуст")
        return self.items.pop(0)

    def removeRear(self):
        if self.isEmpty():
            raise IndexError("Дек пуст")
        return self.items.pop()

    def size(self):
        return self.items.size()


import time

def test_stack_performance():
    stack_list = []
    stack_linked = Stack()

    start_time = time.time()
    for i in range(15000):
        stack_list.append(i)
    while stack_list:
        stack_list.pop()
    list_time = time.time() - start_time

    start_time = time.time()
    for i in range(15000):
        stack_linked.push(i)
    while not stack_linked.isEmpty():
        stack_linked.pop()
    linked_time = time.time() - start_time

    print(f"Время работы стека на списках Python: {list_time:.5f} сек")
    print(f"Время работы стека на связном списке: {linked_time:.5f} сек")