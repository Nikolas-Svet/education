import time
import matplotlib.pyplot as plt
import numpy as np

#Функция возвращает первое по порядку четное число

# Асимптотическая сложность: O(n)

# Функция foo
def foo(nums):
    for x in nums:
        if x % 2 == 0:
            return True
    else:
        return False

# Генерация 20 массивов разного размера и измерение времени выполнения
sizes = np.random.randint(100, 1000, 20)  # Генерируем 20 случайных размеров массивов от 100 до 1000
times = []

# Измерение времени выполнения для 20 массивов
for size in sizes:
    nums = np.random.randint(0, 1000, size).tolist()  # Генерируем случайный массив
    start_time = time.time()
    foo(nums)  # Выполняем функцию foo
    end_time = time.time()
    times.append(end_time - start_time)  # Сохраняем время выполнения

# Рассчет среднего времени
average_time = sum(times) / len(times)

# Сортируем данные по возрастанию размера массива для корректного отображения графика
sizes, times = zip(*sorted(zip(sizes, times)))

# Вывод среднего времени в терминал
print(f"Среднее время выполнения: {average_time} секунд")

# Построение графика
plt.plot(sizes, times, 'o-', label='Execution time')
plt.xlabel('Size of input array')
plt.ylabel('Time (seconds)')
plt.title('Time complexity of foo (Check for even number)')
plt.grid(True)
plt.legend()
plt.show()
