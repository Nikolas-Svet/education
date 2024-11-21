# Светкин Никита ФИТ-221

import matplotlib.pyplot as plt

lang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popul = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

plt.bar(lang, popul, color='blue', zorder=3)

plt.grid(True, which='both', linestyle='dashed', color='r', linewidth=0.5, zorder=0)

plt.title('Popularity of Programming Language\nWorldwide, Oct 2017 compared to a year ago')
plt.xlabel('Languages')
plt.ylabel('Popularity')

plt.ylim(0, 25)

plt.show()
