import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, interp1d


def f(x):
    return np.exp(np.sin(x) + x)


x = np.linspace(0, 10, 100)
y = f(x)


def linear_spline_manual(x, y, x_vals):
    n = len(x) - 1
    y_vals = []

    for x_val in x_vals:
        for i in range(n):
            if x[i] <= x_val <= x[i + 1]:
                a_i = y[i]
                b_i = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
                y_val = a_i + b_i * (x_val - x[i])
                y_vals.append(y_val)
                break

    return np.array(y_vals)


def cubic_spline_manual(x, y, x_vals):
    n = len(x) - 1
    h = np.diff(x)
    alpha = [0] * (n + 1)

    for i in range(1, n):
        alpha[i] = (3 / h[i]) * (y[i + 1] - y[i]) - (3 / h[i - 1]) * (y[i] - y[i - 1])

    l = [1] + [0] * n
    mu = [0] * (n + 1)
    z = [0] * (n + 1)

    for i in range(1, n):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    l[n] = 1
    z[n] = 0
    c = [0] * (n + 1)
    b = [0] * n
    d = [0] * n
    a = y[:-1]

    for j in range(n - 1, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (y[j + 1] - y[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    y_vals = []
    for x_val in x_vals:
        for i in range(n):
            if x[i] <= x_val <= x[i + 1]:
                delta_x = x_val - x[i]
                y_val = a[i] + b[i] * delta_x + c[i] * delta_x ** 2 + d[i] * delta_x ** 3
                y_vals.append(y_val)
                break

    return np.array(y_vals)


x_vals_dense = np.linspace(0, 10, 100)
y_dense = f(x_vals_dense)

linear_spline = interp1d(x, y, kind='linear')
cubic_spline = CubicSpline(x, y)
y_linear = linear_spline(x_vals_dense)
y_cubic = cubic_spline(x_vals_dense)

error_linear = np.abs(y_dense - y_linear)
error_cubic = np.abs(y_dense - y_cubic)


plt.figure(figsize=(12, 8))
plt.plot(x_vals_dense, y_dense, label='f(x) = exp(sin(x) + x)', color='blue')
plt.plot(x_vals_dense, y_linear, label='Линейный сплайн (SciPy)', linestyle='--', color='orange')
plt.plot(x_vals_dense, y_cubic, label='Кубический сплайн (SciPy)', linestyle='-.', color='green')
plt.scatter(x, y, color='red', zorder=5)
plt.title('Сравнение интерполяции функции exp(sin(x) + x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()


plt.subplot(2, 1, 2)
plt.plot(x_vals_dense, error_linear, label='Погрешность линейного сплайна', color='orange')
plt.plot(x_vals_dense, error_cubic, label='Погрешность кубического сплайна', color='green')
plt.title('График погрешностей интерполяции')
plt.xlabel('x')
plt.ylabel('Погрешность')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()