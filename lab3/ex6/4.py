# Светкин Никита ФИТ-221

from data import load_data

data = load_data('wr294934.txt')
data.drop(columns=['index'], inplace=True)

year_with_most_missing = data[data.isna().any(axis=1)]['year'].value_counts().idxmax()
print(f"\nГод с наибольшим количеством пропусков: {year_with_most_missing}")
