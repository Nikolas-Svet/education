import math


def find_equal_time():
    N = 2
    while True:
        # Первый алгоритм: O(N * log(N))
        time_algo1 = N ** 2 - N - 10
        # Второй алгоритм: O(N^2)
        time_algo2 = 4 * N + 40

        if abs(time_algo1 - time_algo2) < 1e-5:  # Условие равенства с малой точностью
            return N

        N += 1


result = find_equal_time()
print(f"Размер массива N, для которого время выполнения обоих алгоритмов одинаково: {result}")
