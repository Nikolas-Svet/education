# Светкин Никита ФИТ-221

from data import df

victim_sex_count = df['Victim Sex'].value_counts()
print("Количество жертв по полу:")
print(victim_sex_count)

women_victims = victim_sex_count.get('F', 0)
men_victims = victim_sex_count.get('M', 0)
is_women_more_victims = women_victims > men_victims
print(f"Женщины чаще жертвы: {is_women_more_victims}")
