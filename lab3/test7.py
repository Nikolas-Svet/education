from task7 import *

expressions = [
    "3 4 +",
    "10 2 5 * +",
    "6 2 /",
    "5 1 2 + 4 * + 3 -",
    "2 3 ^",
    "4 0 /",
    "3 +",
    "5 5 5 +"
]

for expr in expressions:
    result = evaluate_rpn(expr)
    print(f"Выражение: {expr} \nРезультат: {result}\n")
