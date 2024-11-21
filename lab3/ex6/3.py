# Светкин Никита ФИТ-221

from data import load_data

data = load_data('wr294934.txt')
data.drop(columns=['index'], inplace=True)

data.info()

missing_summary = data.isna().sum()
print("\nКоличество пропусков в каждом столбце:")
print(missing_summary)

most_missing = missing_summary.idxmax()
print(f"\nСтолбец с наибольшим количеством пропусков: {most_missing}")
