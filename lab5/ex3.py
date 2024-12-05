import pandas as pd
import numpy as np
from scipy import stats

# смертности
# жесткость

# 1. Импорт данных из файла
file_path = '14water.txt'
data = pd.read_csv(file_path, sep='\t', names=['location', 'town', 'mortality', 'hardness'])

# Преобразование числовых столбцов
data['mortality'] = pd.to_numeric(data['mortality'], errors='coerce')
data['hardness'] = pd.to_numeric(data['hardness'], errors='coerce')

# 2. Разделение данных на северные и южные города
north_data = data[data['location'] == 'Nort']
south_data = data[data['location'] == 'Sout']

# 3. Описательные статистики для северных и южных городов
north_stats = north_data[['mortality', 'hardness']].describe()
south_stats = south_data[['mortality', 'hardness']].describe()

# 4. Функция для вычисления доверительных интервалов
def confidence_interval(data, column):
    mean = data[column].mean()
    sem = stats.sem(data[column].dropna())  # Стандартная ошибка среднего
    ci = stats.t.interval(0.95, len(data[column].dropna())-1, loc=mean, scale=sem)
    return ci

# 5. Доверительные интервалы для смертности
north_mortality_ci = confidence_interval(north_data, 'mortality')
south_mortality_ci = confidence_interval(south_data, 'mortality')

# 6. Доверительные интервалы для жесткости воды
north_hardness_ci = confidence_interval(north_data, 'hardness')
south_hardness_ci = confidence_interval(south_data, 'hardness')

# Вывод результатов
print("Описательные статистики для северных городов:")
print(north_stats)

print("\nОписательные статистики для южных городов:")
print(south_stats)

print("\n95% доверительный интервал для средней смертности (север):", north_mortality_ci)
print("95% доверительный интервал для средней смертности (юг):", south_mortality_ci)

print("\n95% доверительный интервал для жесткости воды (север):", north_hardness_ci)
print("95% доверительный интервал для жесткости воды (юг):", south_hardness_ci)
