import matplotlib.pyplot as plt
import numpy as np

# Названия языков и соответствующие значения
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
values = [22, 17.5, 8.8, 8, 7.8, 6.8]

# Ширины столбцов
widths = [0.5, 1, 2.5, 6, 1, 1.5]

# Создание графика
plt.figure(figsize=(10, 6))

# Создаем столбчатый график с синим цветом и разной шириной столбцов
plt.bar(languages, values, color='blue', width=widths, zorder=3, alpha=0.8)

# Настройка осей
plt.title('Programming Languages Popularity')
plt.xlabel('Programming Languages')
plt.ylabel('Values')
plt.yticks(np.arange(0, 26, 1))  # Устанавливаем отметки по оси Y от 0 до 25 с шагом 1

# Добавление сетки
plt.grid(axis='x', color='red', linestyle='-', linewidth=0.7, zorder=1)  # Красная сетка по оси X
plt.grid(axis='y', color='red', linestyle='-', linewidth=0.5, zorder=1)  # Красная сетка по оси Y
plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(1))  # Установка минорных делений по оси Y

# Показ графика
plt.tight_layout()  # Уплотнение графика
plt.show()
