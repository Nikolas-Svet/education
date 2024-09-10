import time
import matplotlib.pyplot as plt


def experiment_del_list_dict(max_size):
    list_times = []
    dict_times = []

    for size in range(1000, max_size, 1000):
        # Создаем список и словарь
        lst = list(range(size))
        dct = {i: i for i in range(size)}

        # Время удаления элемента в списке
        start_time = time.time()
        for i in range(size):
            del lst[0]
        list_times.append(time.time() - start_time)

        # Время удаления элемента в словаре
        start_time = time.time()
        for i in range(size):
            del dct[i]
        dict_times.append(time.time() - start_time)

    return list_times, dict_times


# Проводим эксперимент
max_size = 20000
list_times, dict_times = experiment_del_list_dict(max_size)

# Построение графика
sizes = list(range(1000, max_size, 1000))

plt.plot(sizes, list_times, label="List del", marker='o')
plt.plot(sizes, dict_times, label="Dict del", marker='x')
plt.xlabel("Size of list/dict")
plt.ylabel("Time (s)")
plt.title("Performance of del operation on lists and dicts")
plt.legend()
plt.grid(True)
plt.show()
