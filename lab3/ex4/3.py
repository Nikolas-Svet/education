# Светкин Никита ФИТ-221

from data import load_data

polit = load_data()
result = polit[(polit['afri'] == 1) & (polit['fparl08'] > 30)]
print(result)
