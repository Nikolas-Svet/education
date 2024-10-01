import matplotlib.pyplot as plt
import numpy as np

# Данные
x1 = [10, 20, 25, 30]
y1 = [20, 40, 20, 0]
x2 = [10, 20, 25, 35]
y2 = [40, 10, 20, 40]

# Построение графика
plt.plot(x1, y1, color='blue', linewidth=5, label='line2-width-5')  # Пунктирная линия
plt.plot(x2, y2, 'r--', linewidth=5, label='line2-dotted')  # Штриховая линия
plt.title('Plot with two or more lines with different styles')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.legend()
plt.show()
