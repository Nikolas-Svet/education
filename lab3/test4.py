from task4 import *

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Размер стека:", stack.size())
print("Верхний элемент:", stack.peek())
print("Извлекаем элемент:", stack.pop())
print("Новый верхний элемент:", stack.peek())

queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
print("Размер очереди:", queue.size())
print("Извлекаем элемент:", queue.dequeue())
print("Новый первый элемент:", queue.items.head.getData())

deque = Deque()
deque.addFront(10)
deque.addRear(20)
deque.addFront(5)
print("Размер дека:", deque.size())
print("Удаляем с конца:", deque.removeRear())
print("Удаляем с начала:", deque.removeFront())

test_stack_performance()
