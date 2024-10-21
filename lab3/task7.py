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
