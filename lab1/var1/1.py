import time
import matplotlib.pyplot as plt
import numpy as np

#Функция возвращает первое по порядку четное число

# Асимптотическая сложность: O(n)

# Функция foo
def foo(nums):
    for x in nums:
        if x % 2 == 0:
            return True
    else:
        return False

sizes = np.random.randint(100, 1000, 20)
times = []

for size in sizes:
    nums = np.random.randint(0, 1000, size).tolist()
    start_time = time.time()
    foo(nums)
    end_time = time.time()
    times.append(end_time - start_time)

average_time = sum(times) / len(times)

sizes, times = zip(*sorted(zip(sizes, times)))

print(f"Среднее время выполнения: {average_time} секунд")

plt.plot(sizes, times, 'o-', label='Execution time')
plt.xlabel('Size of input array')
plt.ylabel('Time (seconds)')
plt.title('Time complexity of foo (Check for even number)')
plt.grid(True)
plt.legend()
plt.show()
