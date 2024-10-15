import matplotlib.pyplot as plt
import numpy as np

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
values = [22, 17.5, 8.8, 8, 7.8, 6.8]

plt.figure(figsize=(10, 6))

plt.barh(languages, values, color='green', zorder=3, alpha=0.8)

plt.title('Programming Languages Popularity')
plt.xlabel('Values')
plt.ylabel('Programming Languages')
plt.xticks(np.arange(0, 26, 1))

plt.grid(axis='x', color='red', linestyle='-', linewidth=0.7, zorder=1)
plt.grid(axis='y', color='red', linestyle='-', linewidth=0.7, zorder=1)

plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(0.5))

plt.tight_layout()
plt.show()
