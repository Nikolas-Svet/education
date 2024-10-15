import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

dates = [
    datetime(2016, 10, 3),
    datetime(2016, 10, 4),
    datetime(2016, 10, 5),
    datetime(2016, 10, 6),
    datetime(2016, 10, 7)
]
closing_values = [772.5, 776.4, 776.5, 776.9, 775.1]

plt.figure(figsize=(10, 6))
plt.plot(dates, closing_values, marker='o', color='red', label='Closing Value')

plt.title('Closing stock value of Alphabet Inc.')
plt.xlabel('Date')
plt.ylabel('Closing Value')
plt.xticks(dates)
plt.yticks(np.arange(772.5, 777.1, 0.1))


plt.grid(color='red', linestyle='-', linewidth=0.7)
plt.gca().yaxis.set_major_locator(plt.MultipleLocator(0.5))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))


plt.grid(which='minor', color='gray', linestyle=':', linewidth=1)
plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(0.1))


plt.gcf().autofmt_xdate()


plt.legend()
plt.tight_layout()
plt.show()
