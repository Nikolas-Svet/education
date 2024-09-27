import numpy as np
import matplotlib.pyplot as plt

# Пример функции
def f(x):
    return np.cos(x)**2 + np.cos(x + 1) + x

# Интервал и узлы
a, b = 0, 5
x_nodes = np.linspace(a, b, 10)
y_nodes = f(x_nodes)

#Промеж узлов добавить еще промежуточные точки

# Реализация многочлена Лагранжа
def lagrange_polynomial(x, x_nodes, y_nodes):
    n = len(x_nodes)
    result = 0.0
    for i in range(n):
        term = y_nodes[i]
        for j in range(n):  #базисные многочлены Лагранжа
            if i != j:
                term *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += term
    return result

# Погрешности
def theoretical_error(x):
    return np.abs(f(x) - lagrange_polynomial(x, x_nodes, y_nodes))

# Построение графиков
x_range = np.linspace(a, b, 100)
y_lagrange = [lagrange_polynomial(x, x_nodes, y_nodes) for x in x_range]

plt.plot(x_range, f(x_range), label="f(x)", color="blue")
plt.plot(x_range, y_lagrange, label="Lagrange Polynomial", color="red")
plt.scatter(x_nodes, y_nodes, color='black', zorder=5, label="Nodes")

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Polynomial Approximation')
plt.grid(True)
plt.show()

# Теоретическая погрешность
epsilon_theoretical = np.max(theoretical_error(x_range))
print(f"Теоретическая погрешность: {epsilon_theoretical}")


#2

