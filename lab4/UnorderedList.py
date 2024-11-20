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


