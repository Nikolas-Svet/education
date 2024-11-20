from task1 import *


def move_to_front():
    n = int(input("Введите количество строк: "))
    linked_list = UnorderedList()
    items_set = set()

    for _ in range(n):
        item = input("Введите строку: ")
        if linked_list.search(item):
            linked_list.remove(item)
        linked_list.add(item)
        items_set.add(item)
        print("Текущий список:", linked_list)

    return linked_list


test_data = ["apple", "banana", "apple", "cherry", "banana", "date", "apple"]
linked_list = UnorderedList()

print("Тестовые данные:", test_data)

for item in test_data:
    if linked_list.search(item):
        linked_list.remove(item)
    linked_list.add(item)
    print("Текущий список после ввода", repr(item) + ":", linked_list)

print("Итоговый список:", linked_list)
