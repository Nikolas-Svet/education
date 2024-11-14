import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math


def f(x):
    return np.cos(x) ** 2 + np.cos(x + 1) + x


a, b = 0, 5
x_nodes = np.linspace(a, b, 10)
y_nodes = f(x_nodes)


def lagrange_polynomial(x, x_nodes, y_nodes):
    n = len(x_nodes)
    result = 0.0
    for i in range(n):
        term = y_nodes[i]
        for j in range(n):
            if i != j:
                term *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += term
    return result


def theoretical_error_per_point(x_range, x_nodes, n):
    x = sp.Symbol('x')
    f_sym = sp.cos(x) ** 2 + sp.cos(x + 1) + x

    # Вычисляем (n+1)-ю производную
    f_deriv = f_sym
    for i in range(n + 1):
        f_deriv = sp.diff(f_deriv, x)

    f_deriv_func = sp.lambdify(x, f_deriv, 'numpy')
    max_deriv_values = np.abs(f_deriv_func(x_range))  # Значения производной для каждого x в x_range

    # Вычисляем значения погрешности для каждого x в x_range
    error_terms = [np.prod([np.abs(xi - xk) for xk in x_nodes]) for xi in x_range]
    epsilon_theoretical_per_point = (max_deriv_values / math.factorial(n + 1)) * np.array(error_terms)

    return epsilon_theoretical_per_point


def practical_error(x_range):
    return np.max(np.abs(f(x_range) - np.array([lagrange_polynomial(x, x_nodes, y_nodes) for x in x_range])))


x_range = np.linspace(a, b, 100)
y_lagrange = [lagrange_polynomial(x, x_nodes, y_nodes) for x in x_range]

n = len(x_nodes) - 1
epsilon_theoretical_per_point = theoretical_error_per_point(x_range, x_nodes, n)
print(f"Теоретическая погрешность: {epsilon_theoretical_per_point}")

epsilon_practical = practical_error(x_range)
print(f"Практическая погрешность: {epsilon_practical}")

plt.figure(figsize=(10, 6))
plt.plot(x_range, f(x_range), label="f(x)", color="blue")
plt.plot(x_range, y_lagrange, label="Lagrange Polynomial", color="red")
plt.scatter(x_nodes, y_nodes, color='black', zorder=5, label="Nodes")

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Polynomial Approximation')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))

plt.plot(x_range, epsilon_theoretical_per_point, label="Теоретическая погрешность", color="orange")

practical_errors = np.abs(f(x_range) - y_lagrange)
plt.plot(x_range, practical_errors, label="Практическая погрешность", color="green")

plt.xlabel('x')
plt.ylabel('Error')
plt.title('График теоретической и практической погрешности')
plt.legend()
plt.grid(True)

plt.show()
