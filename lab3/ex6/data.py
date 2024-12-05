# Светкин Никита ФИТ-221

import pandas as pd

def load_data(filename):
    headers = ['index', 'year', 'month', 'day', 'min_t', 'average_t', 'max_t', 'rainfall']
    data = pd.read_table(filename, sep=';', names=headers)
    return data