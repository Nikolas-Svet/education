class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(repr(current.getData()))
            current = current.getNext()
        return '[' + ', '.join(elements) + ']'

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def append(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
            return
        current = self.head
        while current.getNext() is not None:
            current = current.getNext()
        current.setNext(temp)

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def index(self, item):
        current = self.head
        index = 0
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index += 1
        if found:
            return index
        else:
            raise ValueError(f"{item} не находится в списке")

    def insert(self, pos, item):
        if pos > self.size() or pos < 0:
            raise IndexError("Индекс вне диапазона")
        temp = Node(item)
        if pos == 0:
            temp.setNext(self.head)
            self.head = temp
            return
        current = self.head
        previous = None
        index = 0
        while index < pos:
            previous = current
            current = current.getNext()
            index += 1
        temp.setNext(current)
        previous.setNext(temp)

    def pop(self, pos=None):
        if self.isEmpty():
            raise IndexError("Попытка извлечь элемент из пустого списка")
        if pos is None:
            pos = self.size() - 1
        if pos < 0 or pos >= self.size():
            raise IndexError("Индекс вне диапазона")
        current = self.head
        previous = None
        index = 0
        while index < pos:
            previous = current
            current = current.getNext()
            index += 1
        data = current.getData()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return data

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if not found:
            raise ValueError(f"{item} не находится в списке")
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def slice(self, start, stop):
        if start < 0 or stop > self.size() or start > stop:
            raise IndexError("Некорректные значения start и stop")
        new_list = UnorderedList()
        current = self.head
        index = 0
        while current is not None and index < stop:
            if index >= start:
                new_list.append(current.getData())
            current = current.getNext()
            index += 1
        return new_list


ul = UnorderedList()

print("Начальный список:", ul)
print("Список пустой?", ul.isEmpty())

ul.append(10)
ul.append(20)
ul.append(30)
print("Список после добавления (append):", ul)

print("Индекс элемента 20:", ul.index(20))
try:
    print("Индекс элемента 40:", ul.index(40))
except ValueError as e:
    print(e)

ul.insert(1, 15)
ul.insert(0, 5)
ul.insert(5, 35)
print("Список после вставки (insert):", ul)

try:
    ul.insert(10, 50)
except IndexError as e:
    print(e)

print("Извлекаем последний элемент:", ul.pop())
print("Список после pop:", ul)
print("Извлекаем элемент на позиции 2:", ul.pop(2))
print("Список после pop(2):", ul)

try:
    ul.pop(10)
except IndexError as e:
    print(e)

print("Строковое представление списка:", str(ul))

sublist = ul.slice(1, 3)
print("Срез списка (1, 3):", sublist)

try:
    ul.slice(3, 1)
except IndexError as e:
    print(e)