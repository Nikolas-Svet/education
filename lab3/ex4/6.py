# Светкин Никита ФИТ-221

from data import load_data

def get_fh_status(fh09):
    if fh09 <= 2.5:
        return 'free'
    elif 2.5 < fh09 <= 5.5:
        return 'partly free'
    else:
        return 'not free'

polit = load_data()
polit['fh_status'] = polit['fh09'].apply(get_fh_status)
print(polit)
