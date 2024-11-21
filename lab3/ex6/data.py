# Светкин Никита ФИТ-221

import pandas as pd

def load_data(filename):
    headers = ['index', 'year', 'month', 'day', 'min_t', 'average_t', 'max_t', 'rainfall']
    data = pd.read_csv(filename, sep=r'\s+', header=None, names=headers)
    return data