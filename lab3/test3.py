from task3 import *
from task1 import *

mylist = UnorderedList()
for i in [1, 2, 3, 4, 5]:
    mylist.add(i)
print("Исходный список:", mylist)

new_head = reverse_iterative(mylist.head)
reversed_list = UnorderedList()
reversed_list.head = new_head
print("Обращенный список (итеративно):", reversed_list)

new_head = reverse_recursive(reversed_list.head)
restored_list = UnorderedList()
restored_list.head = new_head
print("Восстановленный список (рекурсивно):", restored_list)
