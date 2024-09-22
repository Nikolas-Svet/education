import time
import matplotlib.pyplot as plt
import numpy as np

# Функция находит все простые числа до n
# Асимптотическая сложность: O(n^2)
def foo(n):
    res = []
    for i in range(1, n + 1):
        divisors = 0
        j = 2
        while j < i and divisors == 0:
            if i % j == 0:
                divisors += 1
            j += 1
        if divisors == 0 and i > 1:  # 1 не является простым числом
            res.append(i)
    return res

# Генерация 20 чисел разного размера и измерение времени выполнения
sizes = np.random.randint(10, 1000, 20)  # Генерируем 20 случайных чисел от 10 до 1000
times = []

# Измерение времени выполнения для 20 чисел
for size in sizes:
    start_time = time.time()
    foo(size)  # Выполняем функцию foo
    end_time = time.time()
    times.append(end_time - start_time)  # Сохраняем время выполнения

# Рассчет среднего времени
average_time = sum(times) / len(times)

# Сортируем данные по возрастанию размера для корректного отображения графика
sizes, times = zip(*sorted(zip(sizes, times)))

# Вывод среднего времени в терминал
print(f"Среднее время выполнения: {average_time} секунд")

# Построение графика
plt.plot(sizes, times, 'o-', label='Execution time')
plt.xlabel('Size of input number (n)')
plt.ylabel('Time (seconds)')
plt.title('Time complexity of foo (Find prime numbers)')
plt.grid(True)
plt.legend()
plt.show()
