import matplotlib.pyplot as plt

x1 = [10, 20, 25, 30]
y1 = [20, 40, 20, 0]
x2 = [10, 20, 25, 35]
y2 = [40, 10, 20, 40]

plt.plot(x1, y1, 'r--', color='blue', linewidth=1, label='line2-dotted')
plt.plot(x2, y2, 'r--', linewidth=5, label='line2-dotted')
plt.title('Plot with two or more lines with different styles')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.legend()
plt.show()
