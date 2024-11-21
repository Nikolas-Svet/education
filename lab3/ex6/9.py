# Светкин Никита ФИТ-221

from data import load_data
import pandas as pd

data = load_data('wr294934.txt')
data.drop(columns=['index'], inplace=True)

data['date'] = pd.to_datetime(data[['year', 'month', 'day']], errors='coerce')

data['days_no_rain'] = 0
no_rain_days = 0
for i, row in data.iterrows():
    if row['rainfall'] == 0:
        no_rain_days += 1
    else:
        no_rain_days = 0
    data.at[i, 'days_no_rain'] = no_rain_days

condition_1 = data['average_t'] < -30
condition_2 = (data['average_t'] > 27) & (data['days_no_rain'] > 3)

below_minus_30 = data[condition_1]
above_27_no_rain = data[condition_2]

print("Наблюдения со средней температурой ниже -30:")
print(below_minus_30)

print("\nНаблюдения со средней температурой выше 27 и более 3 дней без осадков:")
print(above_27_no_rain)