from data import df

# 10. Добавление столбца col3
df['col3'] = df['col1'] * df['col2']
print("DataFrame после добавления столбца col3:\n", df)