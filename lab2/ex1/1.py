import matplotlib.pyplot as plt
import numpy as np

# Данные
x = np.arange(0, 50, 1)
y = x * 3

# Построение графика
plt.plot(x, y, color='blue')
plt.title('Draw a line.')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.show()