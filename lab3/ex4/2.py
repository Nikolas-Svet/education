# Светкин Никита ФИТ-221

from data import load_data

polit = load_data()
result = polit[polit['fh09'] > 5]
print(result)