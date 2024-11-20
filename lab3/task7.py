class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Попытка извлечь элемент из пустого стека")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items[-1]

    def size(self):
        return len(self.items)


def evaluate_rpn(expression):
    stack = Stack()
    tokens = expression.split()
    operators = {'+', '-', '*', '/', '^'}

    try:
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                stack.push(int(token))
            elif token in operators:
                if token == '+':
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = operand1 + operand2
                    stack.push(result)
                elif token == '-':
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = operand1 - operand2
                    stack.push(result)
                elif token == '*':
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = operand1 * operand2
                    stack.push(result)
                elif token == '/':
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    if operand2 == 0:
                        return "Ошибка: Деление на ноль"
                    result = operand1 / operand2
                    stack.push(result)
                elif token == '^':
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = operand1 ** operand2
                    stack.push(result)
            else:
                return f"Ошибка: Неизвестный оператор или операнд '{token}'"
        if stack.size() == 1:
            return stack.pop()
        else:
            return "Ошибка: Некорректное выражение"
    except IndexError:
        return "Ошибка: Недостаточно операндов"


test_cases = [
    ("3 4 +", 7),
    ("10 2 *", 20),
    ("10 2 /", 5),
    ("10 0 /", "Ошибка: Деление на ноль"),
    ("2 3 ^", 8),
    ("5 1 2 + 4 * + 3 -", 14),
    ("1 2 + 4", "Ошибка: Некорректное выражение"),
    ("1 +", "Ошибка: Недостаточно операндов"),
    ("1 2 ?", "Ошибка: Неизвестный оператор или операнд '?'"),
    ("2 3 * 5 +", 11),
    ("4 2 5 * + 1 3 2 * + /", 2)
]

for expression, expected in test_cases:
    result = evaluate_rpn(expression)
    assert result == expected, f"Ошибка: для '{expression}' ожидалось {expected}, получено {result}"
    print(f"Выражение: {expression} -> Результат: {result}")
