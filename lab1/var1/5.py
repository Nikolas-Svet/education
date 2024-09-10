import time
import matplotlib.pyplot as plt


def experiment_in_list_set(max_size):
    list_times = []
    set_times = []

    for size in range(1000, max_size, 1000):
        # Создаем список и множество
        lst = list(range(size))
        st = set(range(size))

        # Время поиска элемента в списке
        start_time = time.time()
        for i in range(size):
            i in lst
        list_times.append(time.time() - start_time)

        # Время поиска элемента в множестве
        start_time = time.time()
        for i in range(size):
            i in st
        set_times.append(time.time() - start_time)

    return list_times, set_times


# Проводим эксперимент
max_size = 20000
list_times, set_times = experiment_in_list_set(max_size)

# Построение графика
sizes = list(range(1000, max_size, 1000))

plt.plot(sizes, list_times, label="List in", marker='o')
plt.plot(sizes, set_times, label="Set in", marker='x')
plt.xlabel("Size of list/set")
plt.ylabel("Time (s)")
plt.title("Performance of 'in' operation on lists and sets")
plt.legend()
plt.grid(True)
plt.show()
