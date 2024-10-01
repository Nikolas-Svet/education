import numpy as np

# 5. Удаление всех значений NaN из массива
array_with_nan1 = np.array([200., 300., np.nan, np.nan, np.nan, 700.])
cleaned_array1 = array_with_nan1[~np.isnan(array_with_nan1)]
print("После удаления NaN:", cleaned_array1)

array_with_nan2 = np.array([[1., 2., 3.], [np.nan, 0., np.nan], [6., 7., np.nan]])
cleaned_array2 = array_with_nan2[~np.isnan(array_with_nan2)]
print("После удаления NaN из двумерного массива:", cleaned_array2)