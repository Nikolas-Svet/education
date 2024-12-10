import numpy as np
from sympy import symbols, diff, sqrt, lambdify


# Функция f(x) = 1 / sqrt(1 - x^4)
def new_f(x):
    return 1 / np.sqrt(1 - x ** 4)


x_sym = symbols('x')
f_sym = 1 / sqrt(1 - x_sym ** 4)
f_fourth_derivative = diff(f_sym, x_sym, 4)
fourth_derivative_func = lambdify(x_sym, f_fourth_derivative, "numpy")

def fourth_derivative_f(x):
    # return fourth_derivative_func(x)
    return (105 * (2 * x**4 + 1)) / ((1 - x**4)**(9 / 2))


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
        error_estimate = abs(integral_next - integral_prev) / 15
        if error_estimate < epsilon:
            break
        integral_prev = integral_next
    return integral_next, n


# Метод Симпсона с оценкой остаточного члена
def simpsons_rule_with_exact_residual(f, a, b, epsilon):
    n = 2
    while True:
        integral = simpsons_rule(f, a, b, n)
        h = (b - a) / n

        x_segments = np.linspace(a, b, n + 1)
        residuals = []
        for i in range(len(x_segments) - 1):
            x0, x2 = x_segments[i], x_segments[i + 1]
            xi = (x0 + x2) / 2
            residual = (-(h ** 5) / 90) * abs(fourth_derivative_f(xi))
            residuals.append(residual)

        max_residual = max(residuals)
        if abs(max_residual) < epsilon / 2:
            break
        n *= 2
    return integral, n


# Границы интегрирования
a, b = -0.5, 0.5
epsilon = 1e-6

trapezoidal_result, trapezoidal_steps = trapezoidal_rule_with_precision(new_f, a, b, epsilon)
simpsons_result, simpsons_steps = simpsons_rule_with_exact_residual(new_f, a, b, epsilon)
simpsons_residual_result, simpsons_residual_steps = simpsons_rule_with_precision(new_f, a, b, epsilon)

print("Метод трапеции:")
print(f"Значение интеграла: {trapezoidal_result}")
print(f"Число шагов: {trapezoidal_steps}")

print("Метод Симпсона с остаточной формулой:")
print(f"Значение интеграла: {simpsons_result}")
print(f"Число шагов: {simpsons_steps}")
print(f"Последовательное удвоение шагов: {simpsons_residual_steps} шагов, значение: {simpsons_residual_result}")
