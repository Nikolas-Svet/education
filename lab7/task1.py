class BinaryTree:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None


def buildLogicParseTree(exp):
    tokens = exp.split()
    stack = []
    root = BinaryTree()
    current = root

    for token in tokens:
        if token == "(":
            if current.left is None:
                current.left = BinaryTree()
                stack.append(current)
                current = current.left
            else:
                current.right = BinaryTree()
                stack.append(current)
                current = current.right
        elif token in ["и", "или"]:
            current.key = token
            current.right = BinaryTree()
            stack.append(current)
            current = current.right
        elif token == "не":
            current.key = token
            current.left = BinaryTree()
            stack.append(current)
            current = current.left
        elif token in ["истина", "ложь"]:
            current.key = token
            if stack:
                current = stack.pop()
        elif token == ")":
            if stack:
                parent = stack.pop()
                if parent.left and parent.left.key is None:
                    parent.left = current
                elif parent.right and parent.right.key is None:
                    parent.right = current
                current = parent
    return root


def printTree(tree, level=0):
    """Вывод дерева для отладки"""
    if tree is not None and tree.key is not None:
        print(" " * (level * 4) + f"({tree.key})")
        printTree(tree.left, level + 1)
        printTree(tree.right, level + 1)


def evaluateLogic(tree):
    if tree is None or tree.key is None:
        return False


    operators = {
        "и": lambda x, y: x and y,
        "или": lambda x, y: x or y,
        "не": lambda x: not x,
    }

    if tree.key == "истина":
        return True
    if tree.key == "ложь":
        return False

    if tree.key == "не":
        left = evaluateLogic(tree.left)
        return operators["не"](left)

    left = evaluateLogic(tree.left)
    right = evaluateLogic(tree.right)
    result = operators[tree.key](left, right)
    return result


# Пример использования
exp = "( ( истина и ложь ) или ( истина или ложь) )"
tree = buildLogicParseTree(exp)
print("Дерево построено:")
printTree(tree)
print("Результат вычисления:", evaluateLogic(tree))
