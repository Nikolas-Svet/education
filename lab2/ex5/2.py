import matplotlib.pyplot as plt
import numpy as np

# Названия языков и соответствующие значения
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
values = [22, 17.5, 8.8, 8, 7.8, 6.8]

# Создание графика
plt.figure(figsize=(10, 6))

# Создаем горизонтальный столбчатый график
plt.barh(languages, values, color='green', zorder=3, alpha=0.8)

# Настройка осей
plt.title('Programming Languages Popularity')
plt.xlabel('Values')
plt.ylabel('Programming Languages')
plt.xticks(np.arange(0, 26, 1))  # Устанавливаем отметки по оси X от 0 до 25 с шагом 1

# Добавление сетки
plt.grid(axis='x', color='red', linestyle='-', linewidth=0.7, zorder=1)  # Красная сетка по оси X
plt.grid(axis='y', color='red', linestyle='-', linewidth=0.7, zorder=1)  # Серая сетка по оси Y

# Установка минорных делений по оси X
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(0.5))  # Установка минорных делений по оси X для 0.5

# Показ графика
plt.tight_layout()  # Уплотнение графика
plt.show()
