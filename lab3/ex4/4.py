# Светкин Никита ФИТ-221

from data import load_data

polit = load_data()
result = polit[((polit['afri'] == 1) | (polit['lati'] == 1)) & (polit['polity09'] >= 8)]
print(result)
