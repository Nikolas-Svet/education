import matplotlib.pyplot as plt
import numpy as np

# Данные для графиков
x = np.linspace(0.1, 4, 10)
y1 = np.log(x) + np.random.randn(100) * 0.2  # Данные для синей линии
y2 = -np.log(x) + np.random.randn(100) * 0.2  # Данные для красной линии

# Создание изображения
fig, ax = plt.subplots()

# Построение синей и красной линий
ax.plot(x, y1, label='Синяя линия', color='blue')
ax.plot(x, y2, label='Красная линия', color='red')

# Добавление точек
ax.scatter(x, y1, color='black', marker='o', label='Точки')

# Сетка
ax.grid(True)

# Легенда
ax.legend()

# Подписи осей
ax.set_xlabel('Подпись оси OX (X axis label)')
ax.set_ylabel('Подпись оси OY (Y axis label)')

# Заголовок
ax.set_title('Элементы изображения')

# Основные и промежуточные деления (major/minor ticks)
ax.set_xticks([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
ax.set_yticks([0, 1, 2, 3, 4])
ax.set_xticks(np.arange(0, 4.1, 0.1), minor=True)
ax.set_yticks(np.arange(0, 4.1, 0.1), minor=True)

# Подписи основных делений (major tick labels)
ax.set_xticklabels(['0.50', '1.00', '1.50', '2.00', '2.50', '3.00', '3.50', '4.00'])
ax.set_yticklabels(['0', '1', '2', '3', '4'])

# Линии осей координат (Spines)
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

# Отображение графика
plt.show()
