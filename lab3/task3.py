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
