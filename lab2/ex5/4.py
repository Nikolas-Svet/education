# Светкин Никита ФИТ-221

import matplotlib.pyplot as plt
import numpy as np

x = [0, 5, 10, 15, 20, 25]
lang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']

popul = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

plt.bar(x, popul, width=4, color='blue', zorder=3)

plt.xlim(0, 30)
plt.ylim(0, 25)

plt.xticks(np.arange(0, 31, 1), minor=True)
plt.yticks(np.arange(0, 26, 1), minor=True)

plt.xticks(x, lang)
plt.yticks(x)

for i, v in enumerate(popul):
    plt.text(x[i], v + 1, str(v)+"00000")

plt.grid(color='red', zorder=0)
plt.grid(which='minor', color='gray', linestyle='dashed', zorder=0)

plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title('PopularitY of Programming Language\nWorldwide, Oct 2017 compared to \
a year ago')

plt.show()