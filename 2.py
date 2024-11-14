import numpy as np

def f(x):
    return np.cos(x) ** 2 + np.cos(x + 1) + x

x_interp = 1.5
epsilon = 1e-5

def third_derivative(x):
    return 4 * np.sin(x) * np.cos(x) + np.sin(x + 1)

def compute_residual(h, x_interp, x):

    nearest_index = np.argmin(np.abs(x - x_interp))
    x_i = x[nearest_index]


    t = (x_interp - x_i) / h


    y = f(x)
    y1_j_half = y[nearest_index + 1] - y[nearest_index] if nearest_index + 1 < len(y) else 0
    y2_j = y[nearest_index + 1] - 2 * y[nearest_index] + y[nearest_index - 1] if nearest_index > 0 else 0


    approx_value = y[nearest_index] + y1_j_half * t + y2_j * t * (t - 1) / 2


    exact_value = f(x_interp)


    print(f"Точное значение f(x_interp) = {exact_value:.8f}")
    print(f"Аппроксимированное значение в x_interp = {approx_value:.8f}")


    R2_x = third_derivative(x_interp) * h ** 3 * t * (t ** 2 - 1) / 6

    return abs(R2_x), R2_x, y1_j_half, y2_j, t

def find_optimal_h(a, b, epsilon):
    h = b - a
    iteration = 1

    while h >= 0.00001:
        x = np.array([a + i * h for i in range(int((b - a) / h) + 1)])
        residual_abs, residual, y1_j_half, y2_j, t = compute_residual(h, x_interp, x)

        print(f"\nИтерация {iteration}:")
        print(f"  Шаг h = {h:.8f}")
        print(f"  Остаточный член R2(x) = {residual:.8f}")
        print(f"  Абсолютное значение R2(x) = {residual_abs:.8f}")
        print(f"  Разница с ε = {abs(residual_abs - epsilon):.8f}")
        print(f"  Промежуточные значения:")
        print(f"    y1_j_half = {y1_j_half:.8f}")
        print(f"    y2_j = {y2_j:.8f}")
        print(f"    t = {t:.8f}\n")


        if residual_abs <= epsilon:
            print(f"Подходящее значение h найдено: {h:.8f}")
            print(f"Остаточный член R2(x) при этом h: {residual:.8f}")
            return h

        h /= 2
        iteration += 1

    print("Не удалось найти значение h, которое бы удовлетворяло требуемой точности ε.")
    return None

a, b = 0, 5

optimal_h = find_optimal_h(a, b, epsilon)

if optimal_h is not None:
    print(f"\nОптимальное значение h: {optimal_h:.8f}")
else:
    print("\nПодходящее значение h не найдено в указанном диапазоне.")
