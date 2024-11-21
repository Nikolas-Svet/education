# Светкин Никита ФИТ-221

from data import load_data

data = load_data('wr294934.txt')

data.drop(columns=['index'], inplace=True)

print(data.head())
