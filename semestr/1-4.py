def shell_sort(some_list, step_sequence, verbose=True):
    n = len(some_list)
    comparisons = 0

    for step in step_sequence:

        for i in range(step, n):
            temp = some_list[i]
            j = i
            while j >= step and some_list[j - step] > temp:
                comparisons += 1
                some_list[j] = some_list[j - step]
                j -= step
            if j >= step:
                comparisons += 1
            some_list[j] = temp
        if verbose:
            print(f"После шага {step}: {some_list}")
    return comparisons

if __name__ == "__main__":

    steps = [7, 5, 3, 1]
    lst = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Задание 1:")
    print("Исходный список:", lst)
    comparisons = shell_sort(lst, steps)
    print("Отсортированный список:", lst)
    print("Количество сравнений:", comparisons)

    steps = [8, 4, 2, 1]
    lst = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("\nЗадание 2:")
    print("Исходный список:", lst)
    comparisons = shell_sort(lst, steps)
    print("Отсортированный список:", lst)
    print("Количество сравнений:", comparisons)

    steps = [5, 2, 1]
    lst = [7, 3, 9, 4, 2, 5, 6, 1, 8]
    print("\nЗадание 3:")
    print("Исходный список:", lst)
    comparisons = shell_sort(lst, steps)
    print("Отсортированный список:", lst)
    print("Количество сравнений:", comparisons)

    steps = [5, 2, 1]
    lst = [3, 5, 2, 9, 8, 1, 6, 4, 7]
    print("\nЗадание 4:")
    print("Исходный список:", lst)
    comparisons = shell_sort(lst, steps)
    print("Отсортированный список:", lst)
    print("Количество сравнений:", comparisons)
