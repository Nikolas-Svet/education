import numpy as np

# 9. Подсчет количества букв 'P' в строках массива
string_array = np.array(['Python', 'PHP', 'JS', ' examples', 'html'])
count_P = np.char.count(string_array, 'P')
print("Количество 'P':", count_P)