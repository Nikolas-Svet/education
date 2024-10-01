import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

# Даты и значения закрытия
dates = [
    datetime(2016, 10, 3),
    datetime(2016, 10, 4),
    datetime(2016, 10, 5),
    datetime(2016, 10, 6),
    datetime(2016, 10, 7)  # Новая точка
]
closing_values = [772.5, 776.4, 776.5, 776.9, 775.1]  # Значения с новой точкой

# Создание графика
plt.figure(figsize=(10, 6))
plt.plot(dates, closing_values, marker='o', color='red', label='Closing Value')

# Настройка осей
plt.title('Closing stock value of Alphabet Inc.')
plt.xlabel('Date')
plt.ylabel('Closing Value')
plt.xticks(dates)  # Устанавливаем отметки по оси X на даты
plt.yticks(np.arange(772.5, 777.1, 0.1))  # Устанавливаем отметки по оси Y с шагом 0.1

# Настройка сетки
plt.grid(color='red', linestyle='-', linewidth=0.7)  # Красная сетка линиями
plt.gca().yaxis.set_major_locator(plt.MultipleLocator(0.5))  # Промежуток по оси Y 0.5
plt.gca().xaxis.set_major_locator(mdates.DayLocator())  # Промежуток по оси X 1 день
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Форматирование дат

# Добавление серой сетки с шагом 0.1
plt.grid(which='minor', color='gray', linestyle=':', linewidth=1)  # Серая сетка штрихом
plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(0.1))  # Промежуток по оси Y 0.1

# Поворот меток по оси X
plt.gcf().autofmt_xdate()

# Добавление легенды
plt.legend()
plt.tight_layout()  # Уплотнение графика
plt.show()
