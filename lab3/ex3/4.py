from data import df

# Подсчет пропущенных значений
missing_values_count = df.isnull().sum()
print("Количество пропущенных значений в каждом столбце:")
print(missing_values_count)
