# Светкин Никита ФИТ-221

from data import df

descent_count = df['Victim Descent'].value_counts()
print("Частота происхождения жертв:")
print(descent_count.nlargest(5))
