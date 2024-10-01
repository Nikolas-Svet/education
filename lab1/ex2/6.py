import numpy as np

# 6. Получение k наименьших значений массива
original_array = np.array([1., 7., 8., 2., 0.1, 3., 15., 2.5])
k = 4
k_smallest = np.partition(original_array, k)[:k]  # Быстрое нахождение k наименьших элементов
print(f"{k} наименьших значений:", np.sort(k_smallest))