import time
import matplotlib.pyplot as plt
import numpy as np

# Функция суммирует цифры в строке
# Асимптотическая сложность: O(n), где n — длина строки
def foo(s):
    val = 0
    for c in s:
        if c.isdigit():
            val += int(c)
    return val

# Генерация 20 строк разного размера и измерение времени выполнения
sizes = np.random.randint(100, 1000, 20)  # Генерируем 20 случайных размеров строк от 100 до 1000
times = []

# Измерение времени выполнения для 20 строк
for size in sizes:
    s = ''.join(np.random.choice(list('0123456789abcdefghijklmnopqrstuvwxyz'), size))  # Генерируем случайную строку
    start_time = time.time()
    foo(s)  # Выполняем функцию foo
    end_time = time.time()
    times.append(end_time - start_time)  # Сохраняем время выполнения

# Рассчет среднего времени
average_time = sum(times) / len(times)

# Сортируем данные по возрастанию размера строки для корректного отображения графика
sizes, times = zip(*sorted(zip(sizes, times)))

# Вывод среднего времени в терминал
print(f"Среднее время выполнения: {average_time} секунд")

# Построение графика
plt.plot(sizes, times, 'o-', label='Execution time')
plt.xlabel('Size of input string')
plt.ylabel('Time (seconds)')
plt.title('Time complexity of foo (Sum of digits in string)')
plt.grid(True)
plt.legend()
plt.show()
