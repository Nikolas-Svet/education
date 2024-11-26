import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Функция
def new_f(x):
    return 1 / np.sqrt(1 - x**4)

a, b = -0.5, 0.5

# Метод трапеции
def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    y = f(x)
    print(h)
    integral = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])
    return integral

# Метод Симпсона
def simpsons_rule(f, a, b, n):
    if n % 2 == 1:
        n += 1
    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    print(h)
    y = f(x)
    integral = (h / 3) * (y[0] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2]) + y[-1])
    return integral

# Метод трёх-восьмых
def three_eighths_rule(f, a, b, n):
    if n % 3 != 0:
        n += 3 - (n % 3)
    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    y = f(x)

    coeff3_indices = [i for i in range(1, n) if i % 3 != 0]
    coeff3_sum = sum(y[i] for i in coeff3_indices)

    coeff2_indices = [i for i in range(3, n, 3)]
    coeff2_sum = sum(y[i] for i in coeff2_indices)

    integral = (3 * h / 8) * (y[0] + 3 * coeff3_sum + 2 * coeff2_sum + y[-1])

    return integral


n = 100

try:
    exact_integral_new, _ = quad(new_f, a, b)
except Exception as e:
    exact_integral_new = str(e)

trapezoidal_result_new = trapezoidal_rule(new_f, a, b, n)
simpsons_result_new = simpsons_rule(new_f, a, b, n)
three_eighths_result_new = three_eighths_rule(new_f, a, b, n)

# Вывод результатов
results_new = {
    "Точный интеграл": exact_integral_new,
    "Метод трапеции": trapezoidal_result_new,
    "Метод Симпсона": simpsons_result_new,
    "Метод трёх-восьмых": three_eighths_result_new,
}

for method, value in results_new.items():
    print(f"{method}: {value}")