import matplotlib.pyplot as plt
import numpy as np

def y(x):
    return x**2 - x - 6

x = np.linspace(-5, 5, 400)

plt.plot(x, y(x), label='y(x) = x^2 - x - 6')

plt.axhline(0, color='black',linewidth=1)

plt.xlabel('x')
plt.ylabel('y(x)')

plt.grid(True)

plt.title('График функции y(x) = x^2 - x - 6')

plt.show()
