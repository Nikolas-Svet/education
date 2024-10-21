from task1 import *

mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print("Список:", mylist)
print("Размер списка:", mylist.size())

mylist.append(100)
print("После append(100):", mylist)

print("Индекс элемента 93:", mylist.index(93))

mylist.insert(2, 55)
print("После insert(2, 55):", mylist)

print("Удаляем последний элемент:", mylist.pop())
print("Список после pop():", mylist)

print("Удаляем элемент на позиции 1:", mylist.pop(1))
print("Список после pop(1):", mylist)

sliced_list = mylist.slice(1, 4)
print("Срез списка от 1 до 4:", sliced_list)
