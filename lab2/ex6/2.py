# Светкин Никита ФИТ-221

import matplotlib.pyplot as plt

plt.plot([0, 100], [0, 200])

plt.xlabel('x')
plt.ylabel('y')

ax = plt.axes([.6, .5, .2, .2])

ax.set_xticks([0, 100])
ax.set_yticks([0, 200])
ax.set(xlim=(-1, 100), ylim=(1, 200))

ax.set_xlabel('x')
ax.set_ylabel('y')

ax.plot([0, 100], [0, 200])

plt.show()