# Светкин Никита ФИТ-221

from data import load_data

polit = load_data()
polit['fh_status'] = polit['fh09'].apply(lambda x: 'free' if x <= 2.5 else 'partly free' if x <= 5.5 else 'not free')
result = polit.groupby('fh_status')['gini'].agg(['min', 'mean', 'max'])
print(result)
