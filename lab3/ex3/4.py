# Светкин Никита ФИТ-221

from data import df

missing_values_count = df.isnull().sum()
print("Количество пропущенных значений в каждом столбце:")
print(missing_values_count)
