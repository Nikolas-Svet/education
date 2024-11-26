import numpy as np

# Функция f(x) = 1 / sqrt(1 - x^4)
def new_f(x):
    return 1 / np.sqrt(1 - x**4)

# Метод трапеции
def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    y = f(x)
    integral = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])
    return integral

# Метод Симпсона
def simpsons_rule(f, a, b, n):
    if n % 2 == 1:
        n += 1
    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    y = f(x)
    integral = (h / 3) * (y[0] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2]) + y[-1])
    return integral

# Метод трапеции с оценкой точности
def trapezoidal_rule_with_precision(f, a, b, epsilon):
    n = 1
    integral_prev = trapezoidal_rule(f, a, b, n)
    while True:
        n *= 2
        integral_next = trapezoidal_rule(f, a, b, n)
        error_estimate = abs(integral_next - integral_prev) / 3
        if error_estimate < epsilon:
            break
        integral_prev = integral_next
    return integral_next, n

# Метод Симпсона с последовательным удвоением числа шагов
def simpsons_rule_with_precision(f, a, b, epsilon):
    n = 2
    integral_prev = simpsons_rule(f, a, b, n)
    while True:
        n *= 2
        integral_next = simpsons_rule(f, a, b, n)
        error_estimate = abs(integral_next - integral_prev) / 15  # Оценка ошибки
        if error_estimate < epsilon:
            break
        integral_prev = integral_next
    return integral_next, n

# Границы интегрирования
a, b = -0.999, 0.999
epsilon = 1e-6

trapezoidal_result, trapezoidal_steps = trapezoidal_rule_with_precision(new_f, a, b, epsilon)
simpsons_result, simpsons_steps = simpsons_rule_with_precision(new_f, a, b, epsilon)

print("Метод трапеции:")
print(f"Значение интеграла: {trapezoidal_result}")
print(f"Число шагов: {trapezoidal_steps}")

print("\nМетод Симпсона:")
print(f"Значение интеграла: {simpsons_result}")
print(f"Число шагов: {simpsons_steps}")
