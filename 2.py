import numpy as np
import matplotlib.pyplot as plt


# Исходная функция f(x)
def f(x):
    return np.cos(x)  # Например, возьмем функцию cos(x)


# Функция для интерполяции полиномом Гаусса при n=2
def gauss_polynomial(x, x_nodes, y_nodes):
    # Для случая n = 2 используем два узла
    w1 = 1  # Вес для первого узла (на практике могут быть другими)
    w2 = 1  # Вес для второго узла

    # Интерполяционный полином Гаусса для двух узлов
    result = (w1 * y_nodes[0] * (x - x_nodes[1]) / (x_nodes[0] - x_nodes[1])
              + w2 * y_nodes[1] * (x - x_nodes[0]) / (x_nodes[1] - x_nodes[0]))

    return result


# Функция для вычисления практической погрешности
def practical_error_gauss(x, f, gauss_polynomial, x_nodes, y_nodes):
    return np.abs(f(x) - gauss_polynomial(x, x_nodes, y_nodes))


# Пример узлов и значений
x0 = 0.5
x_nodes = [0.25, 0.75]  # Узлы интерполяции
y_nodes = [f(x_nodes[0]), f(x_nodes[1])]  # Значения функции в узлах

# Вычисление значения в точке x0 с использованием полинома Гаусса
y_gauss = gauss_polynomial(x0, x_nodes, y_nodes)
print(f"Значение интерполяции полиномом Гаусса в точке x0: {y_gauss}")

# Вычисление практической погрешности
error = practical_error_gauss(x0, f, gauss_polynomial, x_nodes, y_nodes)
print(f"Практическая погрешность: {error}")

# Построение графиков для наглядности
x_range = np.linspace(0, 1, 100)
y_actual = f(x_range)  # Реальные значения функции
y_gauss_interp = [gauss_polynomial(x, x_nodes, y_nodes) for x in x_range]  # Интерполированные значения

plt.plot(x_range, y_actual, label='f(x)', color='blue')
plt.plot(x_range, y_gauss_interp, label='Gauss Polynomial', color='red', linestyle='--')
plt.scatter(x_nodes, y_nodes, color='green', zorder=5, label='Interpolation Nodes')  # Узлы
plt.legend()
plt.title('Интерполяция полиномом Гаусса при n=2')
plt.show()
