import numpy as np

# 8. Поэлементное объединение строковых массивов
array1 = np.array(['Python', 'PHP'])
array2 = np.array(['Java', 'C ++'])
combined = np.core.defchararray.add(array1, ' ' + array2)
print("Поэлементное объединение строковых массивов:", combined)