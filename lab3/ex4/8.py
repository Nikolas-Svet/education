# Светкин Никита ФИТ-221

from data import load_data

polit = load_data()
polit.drop(polit.columns[0], axis=1 , inplace=True)
polit['fh_status'] = polit['fh09'].apply(lambda x: 'free' if x <= 2.5 else 'partly free' if x <= 5.5 else 'not free')

for status, group in polit.groupby('fh_status'):
    filename = f'polit_{status}.csv'
    group.to_csv(filename, index=False)
    print(f'Сохранен файл: {filename}')
