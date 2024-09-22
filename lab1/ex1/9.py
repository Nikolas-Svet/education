import numpy as np

array_chess = np.zeros((4, 4), dtype=int)
array_chess[1::2, ::2] = 1
array_chess[::2, 1::2] = 1
np.fill_diagonal(array_chess, 0)
print("Шахматный массив 4x4:\n", array_chess)