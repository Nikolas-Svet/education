from collections import Counter
import time
import matplotlib.pyplot as plt
import numpy as np


# Первый алгоритм (через collections.Counter)

def most_common_letter_counter(s):
    # Используем Counter для подсчета всех символов
    counter = Counter(s)
    # Возвращаем символ с наибольшим количеством вхождений
    return counter.most_common(1)[0]  # Возвращает кортеж (символ, частота)


# Асимптотическая сложность:
# O(n), где n — длина строки, потому что мы проходим по строке один раз для подсчета символов.


# Второй алгоритм (без использования библиотек)

def most_common_letter_manual(s):
    freq = {}  # Словарь для подсчета частот символов
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Находим символ с максимальной частотой
    most_common = max(freq.items(), key=lambda item: item[1])
    return most_common  # Возвращает кортеж (символ, частота)


# Асимптотическая сложность:
# O(n), где n — длина строки. Мы проходим по строке один раз и
# выполняем операции вставки и поиска по словарю за амортизированное O(1).


# Генерация тестовых строк разной длины
sizes = np.arange(1000, 10001, 1000)  # Длины строк от 1000 до 10000 с шагом 1000
times_counter = []
times_manual = []

# Для каждой длины строки замеряем время выполнения обоих алгоритмов
for size in sizes:
    test_string = ''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), size))  # Генерируем случайную строку

    # Время для алгоритма с Counter
    start_time = time.time()
    most_common_letter_counter(test_string)
    end_time = time.time()
    times_counter.append(end_time - start_time)

    # Время для алгоритма с ручным подсчетом
    start_time = time.time()
    most_common_letter_manual(test_string)
    end_time = time.time()
    times_manual.append(end_time - start_time)

# Построение графика
plt.plot(sizes, times_counter, label='Counter')
plt.plot(sizes, times_manual, label='Manual Dictionary')
plt.xlabel('Size of input string')
plt.ylabel('Time (seconds)')
plt.title('Performance comparison: Counter vs Manual')
plt.grid(True)
plt.legend()
plt.show()
