import numpy as np

original_array3 = np.array([10, 10, 20, 10, 20, 20, 20, 30, 30, 50, 40, 40])
unique_elements3, counts = np.unique(original_array3, return_counts=True)
print("Уникальные элементы:", unique_elements3)
print("Частоты:", counts)