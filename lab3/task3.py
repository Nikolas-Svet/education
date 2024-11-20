def reverse_iterative(head):
    previous = None
    current = head
    while current is not None:
        next_node = current.getNext()
        current.setNext(previous)
        previous = current
        current = next_node
    return previous


def reverse_recursive(node, previous=None):
    if node is None:
        return previous
    next_node = node.getNext()
    node.setNext(previous)
    return reverse_recursive(next_node, node)


from task1 import *

linked_list = UnorderedList()
for i in range(1, 6):
    linked_list.append(i)

print("Исходный список:", linked_list)

head = linked_list.head

reversed_head_iterative = reverse_iterative(head)
print("Список после итеративного обращения:")
current = reversed_head_iterative
while current:
    print(current.getData(), end=" -> ")
    current = current.getNext()
print("None")

head = reverse_iterative(reversed_head_iterative)

reversed_head_recursive = reverse_recursive(head)
print("Список после рекурсивного обращения:")
current = reversed_head_recursive
while current:
    print(current.getData(), end=" -> ")
    current = current.getNext()
print("None")
