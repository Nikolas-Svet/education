import numpy as np
import matplotlib.pyplot as plt

def f(x):
    base = 1 + np.tan(1 / (1 + np.sin(x)**2))

    return np.log((x**2 + 1) * np.exp(-np.abs(x) / 10)) / np.log(base)

x = np.linspace(-20, 20, 400)

y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$f(x) = \log_{1 + \tan(\frac{1}{1 + \sin^2(x)})}((x^2 + 1) e^{-\frac{|x|}{10}})$', color='blue')
plt.title('График функции')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.ylim(-10, 10)
plt.show()
