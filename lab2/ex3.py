import matplotlib.pyplot as plt
import numpy as np

# Определим функцию y(x)
def y(x):
    return x**2 - x - 6

# Определим диапазон значений x
x = np.linspace(-5, 5, 400)

# Построим график функции y(x)
plt.plot(x, y(x), label='y(x) = x^2 - x - 6')

# Добавим линию оси x для наглядности (y = 0)
plt.axhline(0, color='black',linewidth=1)

# Подписи осей
plt.xlabel('x')
plt.ylabel('y(x)')

# Добавим сетку для удобства
plt.grid(True)

# Добавим заголовок
plt.title('График функции y(x) = x^2 - x - 6')

# Отобразим график
plt.show()
