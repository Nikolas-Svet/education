import numpy as np

# Генерация списка случайных чисел
random_list = np.random.randint(0, 100, size=20)  # Список из 20 случайных чисел от 0 до 99
print("Список случайных чисел:", random_list)

# Способ 1: Использование встроенной функции sorted
def top_three_sorted(lst):
    return sorted(lst, reverse=True)[:3]

# Способ 2: Использование метода max
def top_three_max(lst):
    max1 = max(lst)
    lst.remove(max1)
    max2 = max(lst)
    lst.remove(max2)
    max3 = max(lst)
    return max1, max2, max3

# Получение трех самых больших значений
top_three_sorted_values = top_three_sorted(random_list)
top_three_max_values = top_three_max(random_list.copy())

print("Три самых больших значения (sorted):", top_three_sorted_values)
print("Три самых больших значения (max):", top_three_max_values)
