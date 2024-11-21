# Светкин Никита ФИТ-221

from data import load_data
import pandas as pd

data = load_data('wr294934.txt')

data.drop(columns=['index'], inplace=True)

data['date'] = pd.to_datetime(data[['year', 'month', 'day']], errors='coerce')

data['temp_range'] = data['max_t'] - data['min_t']
data['days_no_rain'] = 0

no_rain_days = 0
for i, row in data.iterrows():
    if row['rainfall'] == 0:
        no_rain_days += 1
    else:
        no_rain_days = 0
    data.at[i, 'days_no_rain'] = no_rain_days

print(data.columns)

max_dry_period = data['days_no_rain'].max()
print(f"Max dry period: {max_dry_period}")

print(data[['date', 'temp_range', 'days_no_rain']].head())