import time
import matplotlib.pyplot as plt
import numpy as np

# Функция возвращает строковое представление числа
# Асимптотическая сложность: O(log n)
def foo(i):
    digits = "0123456789"
    if i == 0:
        return "0"
    result = ""
    while i > 0:
        result = digits[i % 10] + result
        i = i // 10
    return result

# Генерация 20 массивов разного размера и измерение времени выполнения
sizes = np.random.randint(1, 1000000, 20)  # Генерируем 20 случайных чисел от 1 до 1,000,000
times = []

# Измерение времени выполнения для 20 массивов
for size in sizes:
    start_time = time.time()
    foo(size)  # Выполняем функцию foo
    end_time = time.time()
    times.append(end_time - start_time)  # Сохраняем время выполнения

# Рассчет среднего времени
average_time = sum(times) / len(times)

# Сортируем данные по возрастанию размера входных данных для корректного отображения графика
sizes, times = zip(*sorted(zip(sizes, times)))

# Вывод среднего времени в терминал
print(f"Среднее время выполнения: {average_time} секунд")

# Построение графика
plt.plot(sizes, times, 'o-', label='Execution time')
plt.xlabel('Size of input number')
plt.ylabel('Time (seconds)')
plt.title('Time complexity of foo (Convert number to string)')
plt.grid(True)
plt.legend()
plt.show()
