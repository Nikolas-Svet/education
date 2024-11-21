# Светкин Никита ФИТ-221

import matplotlib.pyplot as plt

x1 = [0, 9, 18, 27, 36]
y1 = [22, 30, 33, 30, 26]

x2 = [3, 12, 21, 30, 39]
y2 = [25, 32, 30, 35, 29]
xlabels = ['G1', 'G2', 'G3', 'G4', 'G5']

plt.bar(x1, y1, width=3, color='green', label="Men")
plt.bar(x2, y2, width=3, color='red', label="Women")

plt.yticks([0, 5, 10, 15, 20, 25, 30, 35])
plt.xticks(x2, xlabels)

plt.tick_params(axis='both', length=3, direction='in', right=True, top=True)

plt.xlim(0, 43)
plt.ylim(0, 35)

plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')

plt.legend()

plt.show()