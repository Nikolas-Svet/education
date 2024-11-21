from data import df

lognorm_columns = list(filter(lambda c: c.endswith("_lognorm"), df.columns))

print("Найденные столбцы для удаления:", lognorm_columns)

if lognorm_columns:
    df.drop(lognorm_columns, axis=1, inplace=True)
    print("Оставшиеся столбцы после удаления:", df.columns)
else:
    print("Нет столбцов, заканчивающихся на '_lognorm'")
