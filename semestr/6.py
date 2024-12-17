import random
import time
import matplotlib.pyplot as plt

def shell_sort(some_list, step_sequence, verbose=False):
    n = len(some_list)
    for step in step_sequence:
        for i in range(step, n):
            temp = some_list[i]
            j = i
            while j >= step and some_list[j - step] > temp:
                some_list[j] = some_list[j - step]
                j -= step
            some_list[j] = temp
    return

def generate_random_list(n):
    return [random.randint(0, n) for _ in range(n)]

def generate_reverse_sorted_list(n):
    return list(range(n, 0, -1))

def generate_almost_sorted_list(n):
    lst = list(range(1, n+1))
    if n >= n//2:
        lst[n//2], lst[n//2 -1] = lst[n//2 -1], lst[n//2]
    return lst

def generate_half_zero_list(n):
    half = n // 2
    return [0]*(half) + [1]*(n - half)

def generate_mixed_list(n):
    first_5 = int(n * 0.05)
    last_95 = n - first_5
    return [random.randint(0, n) for _ in range(first_5)] + list(range(1, last_95+1))

def generate_near_sorted_list(n):
    lst = list(range(1, n+1))
    for i in range(n):
        swap_idx = i + random.randint(-10, 10)
        if 0 <= swap_idx < n:
            lst[i], lst[swap_idx] = lst[swap_idx], lst[i]
    return lst

def measure_time(sort_function, lst, step_sequence):
    start_time = time.perf_counter()
    sort_function(lst, step_sequence)
    end_time = time.perf_counter()
    return end_time - start_time

if __name__ == "__main__":
    import sys
    import warnings
    warnings.filterwarnings("ignore")
    sizes = [100, 500, 1000, 2000, 4000, 6000, 8000, 10000]
    data_types = {
        'a. Случайные числа': generate_random_list,
        'b. Отсортированный в обратную сторону': generate_reverse_sorted_list,
        'c. Почти отсортированный список': generate_almost_sorted_list,
        'd. Половина 0, половина 1': generate_half_zero_list,
        'e. Первые 5% случайные, 95% упорядочены': generate_mixed_list,
        'f. Все элементы в пределах 10 позиций от места': generate_near_sorted_list
    }
    step_sequence = [5, 2, 1]

    results = {dtype: [] for dtype in data_types.keys()}

    for n in sizes:
        print(f"Размер списка: {n}")
        for dtype, gen_func in data_types.items():
            lst = gen_func(n)
            lst_copy = lst.copy()
            start = time.perf_counter()
            shell_sort(lst_copy, step_sequence)
            end = time.perf_counter()
            elapsed = end - start
            results[dtype].append(elapsed)
            print(f"  {dtype}: {elapsed:.6f} секунд")
        print("-"*40)

    plt.figure(figsize=(15, 10))
    for dtype, times in results.items():
        plt.plot(sizes, times, label=dtype)
    plt.xlabel('Размер списка (n)')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Зависимость времени выполнения сортировки Шелла от размера входных данных')
    plt.legend()
    plt.grid(True)
    plt.show()
