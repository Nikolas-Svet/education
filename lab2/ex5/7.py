# Светкин Никита ФИТ-221

import matplotlib.pyplot as plt

y = [31.3, 24.8, 12.4, 11.3, 10.8, 9.4]
labels = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
space = [0.1, 0, 0, 0, 0, 0]

plt.pie(y, labels=labels, explode=space, shadow=True, startangle=135, wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%')

plt.show()