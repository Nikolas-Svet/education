# Светкин Никита ФИТ-221

from data import df

female_crimes = df[df['Victim Sex'] == 'X']['Crime Code Description'].value_counts()
male_crimes = df[df['Victim Sex'] == 'H']['Crime Code Description'].value_counts()

print("5 преступлений, от которых чаще страдают женщины:")
print(female_crimes.nlargest(5))

print("\n5 преступлений, от которых чаще страдают мужчины:")
print(male_crimes.nlargest(5))
