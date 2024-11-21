# Светкин Никита ФИТ-221

import matplotlib.pyplot as plt

x1 = [0, 100]
y1 = [0, 200]

x2 = [0, 45, 70, 85, 100]
y2 = [0, 2500, 5000, 7500, 10000]

plt.figure(figsize=(6, 3))

plt.subplot(2, 2, 1)
plt.plot(x1, y1, color='blue')

plt.subplot(2, 2, 2)
plt.plot(x2, y2, color='red', linestyle="dashed")

plt.tight_layout()
plt.show()