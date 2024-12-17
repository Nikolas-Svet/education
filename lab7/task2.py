class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def has_no_duplicates(node, seen=set()):
    if node is None:
        return True
    if node.key in seen:
        return False
    seen.add(node.key)
    return has_no_duplicates(node.left, seen) and has_no_duplicates(node.right, seen)

def insertOrReplace(root, key):
    if root is None:
        return BSTNode(key)
    if key < root.key:
        root.left = insertOrReplace(root.left, key)
    elif key > root.key:
        root.right = insertOrReplace(root.right, key)
    else:
        root.key = key
    return root


print("\nПроверка на отсутствие дубликатов")
root = BSTNode(10)
root.left = BSTNode(5)
root.right = BSTNode(15)
root.left.left = BSTNode(2)
root.left.right = BSTNode(7)
print("Ожидается True:", has_no_duplicates(root))

print("\nПроверка с дубликатами")
root_with_duplicates = BSTNode(10)
root_with_duplicates.left = BSTNode(5)
root_with_duplicates.right = BSTNode(15)
root_with_duplicates.left.left = BSTNode(5)
print("Ожидается False:", has_no_duplicates(root_with_duplicates))

print("\nПроверка insertOrReplace")
root = None
root = insertOrReplace(root, 10)
root = insertOrReplace(root, 5)
root = insertOrReplace(root, 15)
print("Вставлено дерево:")
print("Корень:", root.key)
print("Левый узел:", root.left.key)
print("Правый узел:", root.right.key)

print("\nЗамена существующего значения")
root = insertOrReplace(root, 15)
print("Заменённый правый узел:", root.right.key)