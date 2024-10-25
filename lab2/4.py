import matplotlib.pyplot as plt
import time
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def fib_with_lucas(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        i = n // 2
        j = n - i
        fi = fib_with_lucas(i)
        fj = fib_with_lucas(j)
        li = lucas_with_fib(i)
        lj = lucas_with_fib(j)
        return (fi * lj + fj * li) // 2


def lucas_with_fib(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n + 1)

n_values = list(range(1, 31))
fib_standard_times = []
fib_optimized_times = []

for n in n_values:
    start_time = time.time()
    fib_standard = fibonacci(n)
    time_standard = time.time() - start_time
    fib_standard_times.append(time_standard)

    start_time = time.time()
    fib_optimized = fib_with_lucas(n)
    time_optimized = time.time() - start_time
    fib_optimized_times.append(time_optimized)

    assert fib_standard == fib_optimized, f"Результаты для n={n} не совпадают!"

plt.figure(figsize=(10, 6))

plt.plot(n_values, fib_standard_times, label="Стандартный метод", color="blue", marker='o')
plt.plot(n_values, fib_optimized_times, label="Оптимизированный метод", color="green", marker='x')

plt.xlabel('n')
plt.ylabel('Время (секунды)')
plt.title('Сравнение времени выполнения: стандартный vs оптимизированный метод Фибоначчи')
plt.legend()
plt.grid(True)

plt.show()