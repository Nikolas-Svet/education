import numpy as np

# 10. Нахождение корней полиномов

# a. Полином: x^2 - 4x + 7
coefficients_a = [1, -4, 7]
roots_a = np.roots(coefficients_a)
print("Корни полинома x^2 - 4x + 7:", roots_a)

# b. Полином: x^4 - 11x^3 + 9x^2 + 11x - 10
coefficients_b = [1, -11, 9, 11, -10]
roots_b = np.roots(coefficients_b)
print("Корни полинома x^4 - 11x^3 + 9x^2 + 11x - 10:", roots_b)