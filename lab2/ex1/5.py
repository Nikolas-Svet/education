import matplotlib.pyplot as plt

x1 = [3, 4, 6, 7, 9]
y1 = [1, 6, 11, 20, 22]

x2 = [2, 3, 5, 6, 8]
y2 = [1, 5, 10, 17, 20]

plt.plot(x1, y1, color='white', marker='o', markerfacecolor='red', markersize=12)
plt.plot(x2, y2, color='white', marker='o', markerfacecolor='blue', markersize=6)
plt.title('Display marker')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.show()

