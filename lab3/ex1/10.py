# Светкин Никита ФИТ-221

from data import df

df['col3'] = df['col1'] * df['col2']
print("DataFrame после добавления столбца col3:\n", df)