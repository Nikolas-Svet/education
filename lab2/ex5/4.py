import matplotlib.pyplot as plt
import numpy as np

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
values = [22, 17.5, 8.8, 8, 7.8, 6.8]

plt.figure(figsize=(10, 6))

plt.bar(languages, values, color='blue', zorder=3, alpha=0.8)

for i, value in enumerate(values):
    plt.text(i, value + 0.5, str(value), ha='center', va='bottom', fontsize=10, color='black')

plt.title('Programming Languages Popularity')
plt.xlabel('Programming Languages')
plt.ylabel('Values')
plt.yticks(np.arange(0, 26, 1))

plt.grid(axis='x', color='red', linestyle='-', linewidth=0.7, zorder=1)
plt.grid(axis='y', color='red', linestyle='-', linewidth=0.5, zorder=1)
plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(1))


plt.tight_layout()
plt.show()
