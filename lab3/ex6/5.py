# Светкин Никита ФИТ-221

import pandas as pd
from data import load_data

data = load_data('wr294934.txt')

data = data[data['month'].between(1, 12)]
data = data[data['day'].between(1, 31)]

data['date'] = pd.to_datetime(data[['year', 'month', 'day']])

print(data.head())