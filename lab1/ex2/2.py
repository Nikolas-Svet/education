import numpy as np

original_array1 = np.array([10, 10, 20, 20, 30, 30])
unique_elements1 = np.unique(original_array1)
print("Уникальные элементы:", unique_elements1)

original_array2 = np.array([[1, 1], [2, 3]])
unique_elements2 = np.unique(original_array2)
print("Уникальные элементы для двумерного массива:", unique_elements2)