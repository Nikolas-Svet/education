import numpy as np

sample_array = np.array([1, 2, 3, 4])
for i in range(1, 4):
    repeated_array = np.tile(sample_array, i)
    print(f"{i} повторение:")
    print(repeated_array)