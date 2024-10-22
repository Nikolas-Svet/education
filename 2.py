import numpy as np
import matplotlib.pyplot as plt

# Заданная функция
def f(x):
    return np.cos(x)**2 + np.cos(x + 1) + x

# Узлы интерполяции
x = np.array([0, 1, 2])  # три узла интерполяции
y = f(x)  # значения функции в узлах

# Шаг сетки
h = x[1] - x[0]

# Точка интерполяции
x_interp = 1.5

# Вычисляем t
t = (x_interp - x[1]) / h

# Конечные разности первого порядка
y1_j_half = y[2] - y[1]

# Конечные разности второго порядка
y2_j = y[2] - 2 * y[1] + y[0]

# Интерполяционная формула Гаусса
f_interp = y[1] + y1_j_half * t + y2_j * t * (t - 1) / 2

# Вывод приближенного значения интерполяции
print(f"Значение функции f(x) в точке x = {x_interp} по интерполяции Гаусса: {f_interp:.8f}")

# Точное значение функции для сравнения
exact_value = f(x_interp)
print(f"Точное значение функции f(x) в точке x = {x_interp}: {exact_value:.8f}")

# Остаточный член
def third_derivative(x):
    return -np.cos(x)  # Производная третьего порядка от исходной функции

R2_x = third_derivative(x_interp) * h**3 * t * (t**2 - 1) / 6
print(f"Остаточный член R2(x): {R2_x:.8f}")

# Заданная точность
epsilon = 1e-5

# Проверка точности
if abs(R2_x) <= epsilon:
    print(f"Интерполяция выполнена с точностью ε = {epsilon}")
else:
    print(f"Интерполяция не удовлетворяет точности ε = {epsilon}")

# Построение графика
x_range = np.linspace(0, 2, 100)
y_exact = f(x_range)

# Для интерполяции на всём интервале
y_interp_gauss = []
for xi in x_range:
    t = (xi - x[1]) / h
    f_interp_i = y[1] + y1_j_half * t + y2_j * t * (t - 1) / 2
    y_interp_gauss.append(f_interp_i)

# Построение графика
plt.figure(figsize=(10, 6))

# Точная функция
plt.plot(x_range, y_exact, label="Точная функция", color="blue")

# Интерполяция Гаусса
plt.plot(x_range, y_interp_gauss, label="Интерполяция Гаусса", color="red", linestyle='--')

# Узлы интерполяции
plt.scatter(x, y, color='black', zorder=5, label="Узлы интерполяции")

# Значение интерполяции Гаусса в точке
# plt.scatter(x_interp, f_interp, color='red', zorder=5, label=f"Интерполяция в x = {x_interp}", marker='x', s=100)

# Настройка осей и легенды
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяция Гаусса и точная функция')
plt.legend()
plt.grid(True)

# Отображение графика
plt.show()
