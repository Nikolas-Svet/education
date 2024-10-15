import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 50, 1)
y = x * 3

plt.plot(x, y, color='blue')
plt.title('Draw a line.')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.show()