import numpy as np

array_border = np.ones((10, 10))
array_border[1:-1, 1:-1] = 0
print("Массив 10x10 с границами 1 и 0 внутри:\n", array_border)