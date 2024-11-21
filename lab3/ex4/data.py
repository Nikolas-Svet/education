# Светкин Никита ФИТ-221

import pandas as pd

def load_data():
    polit = pd.read_csv('data.csv')
    polit.dropna(inplace=True)
    return polit
