import matplotlib.pyplot as plt
import numpy as np

# Данные
x = [1, 4, 5, 6, 7]
y = [2, 6, 3, 6, 3]

# Построение графика
plt.plot(x, y, 'r:', marker='o', markerfacecolor='blue', markersize=12) # Пунктир с маркерами
plt.title('Display marker')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.show()