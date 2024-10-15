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

import time

n = 10

start_time = time.time()
fib_standard = fibonacci(n)
time_standard = time.time() - start_time

start_time = time.time()
fib_optimized = fib_with_lucas(n)
time_optimized = time.time() - start_time

print(f"Fibonacci({n}) стандартный: {fib_standard}, время: {time_standard:.6f} с")
print(f"Fibonacci({n}) оптимизированный: {fib_optimized}, время: {time_optimized:.6f} с")

assert fib_standard == fib_optimized, "Результаты функций не совпадают!"
