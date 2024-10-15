from data import df
import matplotlib.pyplot as plt

# Подсчет преступлений по районам
area_crime_count = df['Area Name'].value_counts()

# Сортировка по убыванию
sorted_area_crime_count = area_crime_count.sort_values()

# Построение графика
sorted_area_crime_count.plot(kind='barh')
plt.title('Районы по количеству преступлений')
plt.xlabel('Количество преступлений')
plt.ylabel('Районы')
plt.show()
