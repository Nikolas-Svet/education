# Светкин Никита ФИТ-221

from data import df
import matplotlib.pyplot as plt

area_crime_count = df['Area Name'].value_counts()

sorted_area_crime_count = area_crime_count.sort_values()

sorted_area_crime_count.plot(kind='barh')
plt.title('Районы по количеству преступлений')
plt.xlabel('Количество преступлений')
plt.ylabel('Районы')
plt.show()
