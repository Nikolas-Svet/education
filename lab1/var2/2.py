from collections import Counter
import time
import matplotlib.pyplot as plt
import numpy as np


# Первый алгоритм (через collections.Counter)

def all_unique_counter(lst):
    # Используем Counter для подсчета всех элементов
    counter = Counter(lst)
    # Проверяем, что все элементы встречаются только один раз
    return all(count == 1 for count in counter.values())


# Асимптотическая сложность:
# O(n), где n — длина списка, так как мы проходим по списку один раз для подсчета элементов.


# Второй алгоритм (без использования библиотек)

def all_unique_manual(lst):
    seen = set()  # Множество для хранения уникальных элементов
    for item in lst:
        if item in seen:
            return False  # Если элемент уже встречался, возвращаем False
        seen.add(item)
    return True  # Если все элементы уникальны, возвращаем True


# Асимптотическая сложность:
# O(n), где n — длина списка. Мы проходим по списку один раз, и операции добавления и проверки в множестве имеют амортизированное O(1).


# Генерация тестовых списков разной длины
sizes = np.arange(1000, 10001, 1000)  # Длины списков от 1000 до 10000 с шагом 1000
times_counter = []
times_manual = []

# Для каждой длины списка замеряем время выполнения обоих алгоритмов
for size in sizes:
    test_list = np.random.choice(range(size), size, replace=False)  # Генерируем уникальные случайные числа

    # Время для алгоритма с Counter
    start_time = time.time()
    all_unique_counter(test_list)
    end_time = time.time()
    times_counter.append(end_time - start_time)

    # Время для алгоритма с ручным подсчетом
    start_time = time.time()
    all_unique_manual(test_list)
    end_time = time.time()
    times_manual.append(end_time - start_time)

# Построение графика
plt.plot(sizes, times_counter, label='Counter')
plt.plot(sizes, times_manual, label='Manual Set')
plt.xlabel('Size of input list')
plt.ylabel('Time (seconds)')
plt.title('Performance comparison: Counter vs Manual')
plt.grid(True)
plt.legend()
plt.show()
