import numpy as np

# 7. Нахождение ближайшего по значению элемента массива
array_for_comparison = np.array([0.5, 1.8, 2.1, 3.5, 4.87, 5.13, 6.49])
value = 3.09066280756759
closest_value = array_for_comparison[np.abs(array_for_comparison - value).argmin()]
print("Ближайшее значение:", closest_value)