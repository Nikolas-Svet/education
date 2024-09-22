import numpy as np

array_diag = np.zeros((5, 5))
np.fill_diagonal(array_diag, [1, 2, 3, 4, 5])
print("Массив 5x5 с диагональю:\n", array_diag)