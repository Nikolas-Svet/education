from data import *
import matplotlib.pyplot as plt

x = df['class'].value_counts().index
y = df['class'].value_counts().values

plt.bar(x, y)
plt.title('Частота значений в столбце class')
plt.xlabel('Класс')
plt.ylabel('Частота')
plt.xticks(rotation=45)
plt.show()
