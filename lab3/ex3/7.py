from data import df

# Получение преступлений, от которых страдают женщины и мужчины
female_crimes = df[df['Victim Sex'] == 'F']['Crime Code Description'].value_counts()
male_crimes = df[df['Victim Sex'] == 'M']['Crime Code Description'].value_counts()

# Вывод 5 самых распространенных преступлений для каждого пола
print("5 преступлений, от которых чаще страдают женщины:")
print(female_crimes.nlargest(5))

print("\n5 преступлений, от которых чаще страдают мужчины:")
print(male_crimes.nlargest(5))
