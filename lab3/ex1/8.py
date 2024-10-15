from data import df

# 8. Изменение элемента 3 на 9
df.iloc[1, 0] = 9
print("DataFrame после изменения элемента 3 на 9:\n", df)