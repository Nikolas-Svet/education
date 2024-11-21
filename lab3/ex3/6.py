# Светкин Никита ФИТ-221

from data import df
import matplotlib.pyplot as plt

top_crimes = df['Crime Code Description'].value_counts().nlargest(10)

top_crimes.plot(kind='bar')
plt.title('10 самых распространенных преступлений в Лос-Анджелесе')
plt.xlabel('Преступления')
plt.ylabel('Количество случаев')
plt.xticks(rotation=45)
plt.show()
