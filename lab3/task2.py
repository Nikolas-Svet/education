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