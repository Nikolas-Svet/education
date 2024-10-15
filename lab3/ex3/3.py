from data import df

# Получение количества уникальных значений в каждом столбце
unique_values_count = df.nunique()
print("Количество уникальных значений в каждом столбце:")
print(unique_values_count)
