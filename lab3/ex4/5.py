# Светкин Никита ФИТ-221

from data import load_data

polit = load_data()
polit['corr_round'] = polit['corr0509'].round(2)
print(polit)
