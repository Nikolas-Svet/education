from data import df
import matplotlib.pyplot as plt

# Получение 10 самых распространенных преступлений
top_crimes = df['Crime Code Description'].value_counts().nlargest(10)

# Построение графика
top_crimes.plot(kind='bar')
plt.title('10 самых распространенных преступлений в Лос-Анджелесе')
plt.xlabel('Преступления')
plt.ylabel('Количество случаев')
plt.xticks(rotation=45)
plt.show()
