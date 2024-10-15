import random
import time
import matplotlib.pyplot as plt
import sys

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = quick_sort([x for x in arr if x < pivot])
        middle = [x for x in arr if x == pivot]
        right = quick_sort([x for x in arr if x > pivot])
        return left + middle + right

sys.setrecursionlimit(1000000)

def measure_time(sort_func, arr):
    start_time = time.time()
    if sort_func == quick_sort:
        arr = sort_func(arr)
    else:
        sort_func(arr)
    end_time = time.time()
    return end_time - start_time

def run_experiment(input_type):
    sizes = [100, 500, 1000, 2000, 5000, 10000]
    selection_times = []
    quicksort_times = []

    for size in sizes:
        if input_type == 'random':
            arr = [random.randint(0, size) for _ in range(size)]
        elif input_type == 'sorted':
            arr = list(range(size))
        elif input_type == 'reversed':
            arr = list(range(size, 0, -1))

        arr_copy = arr.copy()
        t_selection = measure_time(selection_sort, arr_copy)
        selection_times.append(t_selection)

        arr_copy = arr.copy()
        t_quick = measure_time(quick_sort, arr_copy)
        quicksort_times.append(t_quick)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, selection_times, label='Сортировка выбором')
    plt.plot(sizes, quicksort_times, label='Быстрая сортировка')
    plt.xlabel('Размер массива')
    plt.ylabel('Время выполнения (секунды)')
    plt.title(f'Зависимость времени сортировки от размера массива ({input_type})')
    plt.legend()
    plt.grid(True)
    plt.show()

input_types = ['random', 'sorted', 'reversed']
for input_type in input_types:
    run_experiment(input_type)

