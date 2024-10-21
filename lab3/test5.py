from task5 import  *
dlist = DoubleList()

print("Список пуст:", dlist.is_empty())

dlist.add_front(10)
dlist.add_front(20)
dlist.add_rear(30)
dlist.add_rear(40)
print("Список после добавлений:", dlist)

print("Размер списка:", dlist.size())

print("Поиск элемента 20:", dlist.search(20))
print("Поиск элемента 50:", dlist.search(50))

removed_front = dlist.remove_front()
print(f"Удален из начала: {removed_front}")
removed_rear = dlist.remove_rear()
print(f"Удален из конца: {removed_rear}")
print("Список после удалений:", dlist)

dlist.insert_before(30, 25)
print("Список после вставки 25 перед 30:", dlist)
dlist.insert_after(10, 15)
print("Список после вставки 15 после 10:", dlist)

dlist.remove(25)
print("Список после удаления 25:", dlist)

try:
    dlist.remove(100)
except ValueError as e:
    print(e)
