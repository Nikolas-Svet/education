# Светкин Никита ФИТ-221
from data import load_data
import pandas as pd

# Загрузка данных
data = load_data('wr294934.txt')

data.drop(columns=['index'], inplace=True)

data['year'] = pd.to_numeric(data['year'], errors='coerce').astype('Int64')
data['average_t'] = pd.to_numeric(data['average_t'], errors='coerce')
data['rainfall'] = pd.to_numeric(data['rainfall'], errors='coerce')

data = data.dropna(subset=['year', 'average_t', 'rainfall'])

yearly_stats = data.groupby('year').agg(
    avg_temp=('average_t', 'mean'),
    total_rainfall=('rainfall', 'sum')
)

warmest_year = yearly_stats['avg_temp'].idxmax()
coldest_year = yearly_stats['avg_temp'].idxmin()
wettest_year = yearly_stats['total_rainfall'].idxmax()
driest_year = yearly_stats['total_rainfall'].idxmin()

print(f"Самый теплый год: {warmest_year}")
print(f"Самый холодный год: {coldest_year}")
print(f"Год с наибольшим количеством осадков: {wettest_year}")
print(f"Год с наименьшим количеством осадков: {driest_year}")
