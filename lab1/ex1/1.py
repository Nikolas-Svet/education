import numpy as np

array1 = np.array([1, 7, 13, 105])
print(f"Размер памяти массива 1: {array1.nbytes} байт")

# Сохранение массива в текстовый и бинарный файлы
np.savetxt('array1.txt', array1)
np.save('array1.npy', array1)

loaded_array1 = np.load('array1.npy')
print("Загруженный массив 1:", loaded_array1)