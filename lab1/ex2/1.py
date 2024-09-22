import numpy as np

array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([10, 30, 40])
common_elements = np.intersect1d(array1, array2)
print("Общие элементы:", common_elements)