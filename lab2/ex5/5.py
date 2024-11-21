# Светкин Никита ФИТ-221

import matplotlib.pyplot as plt
import numpy as np

x = [0, 5, 7.5, 15, 20, 25]
lang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']

popul = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]
w = [0.5, 1, 3, 5.5, 1, 1.5]

plt.bar(x, popul, width=w, color='blue', zorder=3)

plt.xlim(-1, 30)
plt.ylim(0, 25)

plt.xticks(np.arange(0, 36, 1), minor=True)
plt.yticks(np.arange(0, 26, 1), minor=True)

plt.xticks(x, lang)
plt.yticks(x)

plt.grid(color='red', zorder=0)
plt.grid(which='minor', color='gray', linestyle='dashed', zorder=0)

plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title('PopularitY of Programming Language\nWorldwide, Oct 2017 compared to \
a year ago')

plt.show()