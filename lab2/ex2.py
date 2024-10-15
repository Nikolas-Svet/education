import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 4, 10)

y1 = np.log(x) + np.random.randn(10) * 0.2
y2 = -np.log(x) + np.random.randn(10) * 0.2

fig, ax = plt.subplots()

ax.plot(x, y1, label='Синяя линия', color='blue')
ax.plot(x, y2, label='Красная линия', color='red')

ax.scatter(x, y1, color='black', marker='o', label='Точки')

ax.grid(True)

ax.legend()

ax.set_xlabel('Подпись оси OX (X axis label)')
ax.set_ylabel('Подпись оси OY (Y axis label)')

ax.set_title('Элементы изображения')

ax.set_xticks([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
ax.set_yticks([0, 1, 2, 3, 4])
ax.set_xticks(np.arange(0, 4.1, 0.1), minor=True)
ax.set_yticks(np.arange(0, 4.1, 0.1), minor=True)

ax.set_xticklabels(['0.50', '1.00', '1.50', '2.00', '2.50', '3.00', '3.50', '4.00'])
ax.set_yticklabels(['0', '1', '2', '3', '4'])

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

plt.show()
