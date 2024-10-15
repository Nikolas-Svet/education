from data import df

# Подсчет происхождения жертв
descent_count = df['Victim Descent'].value_counts()
print("Частота происхождения жертв:")
print(descent_count.nlargest(5))  # Вывод 5 самых частых
