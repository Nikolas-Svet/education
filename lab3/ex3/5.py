from data import df

# Подсчет количества жертв по полу
victim_sex_count = df['Victim Sex'].value_counts()
print("Количество жертв по полу:")
print(victim_sex_count)

# Проверка, являются ли женщины чаще жертвами
women_victims = victim_sex_count.get('F', 0)  # 'F' для женщин
men_victims = victim_sex_count.get('M', 0)    # 'M' для мужчин
is_women_more_victims = women_victims > men_victims
print(f"Женщины чаще жертвы: {is_women_more_victims}")
