import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd

# 2. Исходные данные
x = [10.0, 2, 2.5, 5, 26.0]
x_with_nan = [10.0, 2, 2.5, math.nan, 5, 26.0]
print(f"Вывод исходных данных, которые содержатся в x: {x}")
print(f"Вывод исходных данных, которые содержатся в x_with_nan: {x_with_nan}")

# 3. Создание массивов NumPy и объектов Pandas Series
y, y_with_nan = np.array(x), np.array(x_with_nan)
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)
print(f"Вывод данных, которые содержатся в y и y_with_nan: {y}, {y_with_nan}")
print(f"Вывод данных, которые содержатся в z и z_with_nan:\n{z}\n{z_with_nan}")

# 4. Центральная метрика: среднее значение
mean_1 = sum(x) / len(x)
mean_2 = statistics.mean(x)
mean_3 = statistics.fmean(x)
mean_4 = statistics.mean(x_with_nan) if not any(math.isnan(i) for i in x_with_nan) else math.nan
mean_5 = np.mean(y)
mean_6 = np.nanmean(y_with_nan)
mean_7 = z.mean()
print(f"Среднее значение (sum и len): {mean_1}")
print(f"Среднее значение (statistics.mean): {mean_2}")
print(f"Среднее значение (statistics.fmean): {mean_3}")
print(f"Среднее значение с nan (statistics.mean): {mean_4}")
print(f"Среднее значение (NumPy): {mean_5}")
print(f"Среднее значение с nan (NumPy): {mean_6}")
print(f"Среднее значение (Pandas): {mean_7}")

# 5. Средневзвешенное значение
w = [0.1, 0.2, 0.3, 0.25, 0.15]
wmean = sum(w[i] * x[i] for i in range(len(x))) / sum(w)
wmean2 = sum(x_ * w_ for (x_, w_) in zip(x, w)) / sum(w)
y, w = np.array(x), np.array(w)
wmean3 = np.average(y, weights=w)
wmean4 = (w * y).sum() / w.sum()
print(f"Средневзвешенное (range): {wmean}")
print(f"Средневзвешенное (zip): {wmean2}")
print(f"Средневзвешенное (NumPy average): {wmean3}")
print(f"Средневзвешенное (поэлементное умножение): {wmean4}")

# 6. Гармоническое среднее
hmean = len(x) / sum(1 / item for item in x)
hmean2 = statistics.harmonic_mean(x)
hmean3 = scipy.stats.hmean(y)
print(f"Гармоническое среднее (чистый Python): {hmean}")
print(f"Гармоническое среднее (statistics): {hmean2}")
print(f"Гармоническое среднее (scipy.stats.hmean): {hmean3}")

# 7. Геометрическое среднее
gmean = math.prod(x) ** (1 / len(x))
gmean2 = scipy.stats.gmean(y)
print(f"Геометрическое среднее (чистый Python): {gmean}")
print(f"Геометрическое среднее (scipy.stats.gmean): {gmean2}")

# 8. Медиана
n = len(x)
median_ = sorted(x)[n // 2] if n % 2 else (sorted(x)[n // 2 - 1] + sorted(x)[n // 2]) / 2
median_2 = statistics.median(x)
median_low = statistics.median_low(x)
median_high = statistics.median_high(x)
median_np = np.median(y)
print(f"Медиана (чистый Python): {median_}")
print(f"Медиана (statistics.median): {median_2}")
print(f"Медиана низшая (statistics.median_low): {median_low}")
print(f"Медиана высшая (statistics.median_high): {median_high}")
print(f"Медиана (NumPy): {median_np}")

# 9. Мода
u = [2, 3, 2, 8, 12]
mode_ = max((u.count(item), item) for item in set(u))[1]
mode_2 = statistics.mode(u)
mode_result = scipy.stats.mode(u, keepdims=True)
mode_3 = mode_result.mode[0]
print(f"Мода (чистый Python): {mode_}")
print(f"Мода (statistics.mode): {mode_2}")
print(f"Мода (scipy.stats.mode): {mode_3}")

# 10. Дисперсия
var_ = sum((item - mean_1) ** 2 for item in x) / (len(x) - 1)
var_2 = statistics.variance(x)
var_np = np.var(y, ddof=1)
print(f"Дисперсия (чистый Python): {var_}")
print(f"Дисперсия (statistics.variance): {var_2}")
print(f"Дисперсия (NumPy): {var_np}")

# 11. Стандартное отклонение
std_ = var_ ** 0.5
std_2 = statistics.stdev(x)
std_np = np.std(y, ddof=1)
print(f"Стандартное отклонение (чистый Python): {std_}")
print(f"Стандартное отклонение (statistics.stdev): {std_2}")
print(f"Стандартное отклонение (NumPy): {std_np}")

# 12. Смещение
skew_ = scipy.stats.skew(y)
print(f"Смещение: {skew_}")

# 13. Процентиль
percentile_5 = np.percentile(y, 5)
percentile_95 = np.percentile(y, 95)
print(f"5-й процентиль: {percentile_5}")
print(f"95-й процентиль: {percentile_95}")

# 14. Диапазон
range_ = np.ptp(y)
print(f"Диапазон: {range_}")

# 15. Сводка описательной статистики
scipy_summary = scipy.stats.describe(y, ddof=1, bias=False)
pandas_summary = z.describe()
print(f"Сводка описательной статистики (scipy.stats.describe): {scipy_summary}")
print(f"Сводка описательной статистики (Pandas):\n{pandas_summary}")
