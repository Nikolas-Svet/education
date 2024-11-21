# Светкин Никита ФИТ-221

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

xdata = [1.5, 2.7, 4, 5.4, 6.3]
ydata = [0.28, 0.03, 0.2, 0.27, 0.08]

xl=[-0.9, -0.3,1.4, 2.9, 4.8, 7.8, 8.8]
yl=[ 0, 0.04, 0.18, 0.07, 0.25, 0.05, 0]

spline = make_interp_spline(xl, yl)

x = np.linspace(np.min(xl), np.max(xl), 500)
y = spline(x)

plt.bar(xdata, ydata, width=1.4, color='pink')
plt.plot(x,y, color='r')

plt.xlim(-1,9)
plt.ylim(0, 0.30)

plt.xlabel('petal_length')

plt.show()