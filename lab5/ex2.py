# #Светкин Никита ФИТ-221
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
import seaborn as sns
from scipy.stats import norm
from scipy import stats
from pandas import DataFrame
#
# # Загрузка данных
pd.set_option('display.max_columns', 100)
df = pd.read_csv('house_train.csv')
df.drop('Id', axis=1, inplace=True)  # Удаление столбца Id
print("Первые 5 строк данных:")
print(df.head())
#
# # Информация о наборе данных
# print("\nИнформация о наборе данных:")
# df.info(memory_usage='deep')
#
# # Количество строк и столбцов
# print(f"\nРазмер данных: {df.shape}")
#
# # Список всех столбцов
# print("\nСписок параметров:")
# print(df.columns.tolist())
#
# # Есть ли категориальные признаки
# categorical_columns = df.select_dtypes(include=['object']).columns
# print("\nКатегориальные признаки:")
# print(categorical_columns.tolist())
#
# # Описательная статистика числовых данных
# print("\nОписательная статистика числовых данных:")
# print(df.describe().T)
#
# # Среднее и стандартное отклонение для SalePrice
# print("\nОписательная статистика для SalePrice:")
# saleprice_desc = df['SalePrice'].describe()
# mean_saleprice = saleprice_desc['mean']
# std_saleprice = saleprice_desc['std']
# print(f"Среднее значение: {mean_saleprice}")
# print(f"Стандартное отклонение: {std_saleprice}")
#
#
#
# # 3
#
# # Пропущенные значения
# na_count = df.isnull().sum().sort_values(ascending=False)
# na_rate = na_count / len(df)
# na_data = pd.concat([na_count, na_rate], axis=1, keys=['count', 'ratio'])
# print("\nПропущенные значения:")
# print(na_data)
#
# # Дубликаты
# duplicates = df.duplicated().sum()
# print(f"\nКоличество дублирующихся строк: {duplicates}")
#
#
# # 4
#
# Удаление столбцов с большим количеством пропущенных значений
columns_to_drop = ['PoolQC', 'MiscFeature', 'Alley']
df_cleaned = df.drop(columns_to_drop, axis=1)
#
# # Удаление дополнительных столбцов
# df_cleaned = df_cleaned.drop(['GarageQual', 'GarageCond', 'Fence'], axis=1)
# df_cleaned = df_cleaned.drop(['MasVnrArea', 'MasVnrType'], axis=1)
#
# # Проверка оставшихся столбцов
# print("\nОстаток данных после удаления столбцов:")
# print(df_cleaned.shape)
#
#
# # 5
#
# sns.histplot(df_cleaned['SalePrice'], kde=True)
# plt.title('Histogram of Sale Price')
# plt.xlabel('Price')
# plt.ylabel('Count')
# plt.show()
#
# # Асимметрия и эксцесс
# print(f"\nSkewness: {df_cleaned['SalePrice'].skew()}")
# print(f"Kurtosis: {df_cleaned['SalePrice'].kurt()}")
#
#
# sns.boxplot(df_cleaned['SalePrice'])
# plt.title('Box plot of Sale Price')
# plt.show()
#
#
# # 6
#
# sns.boxplot(x='CentralAir', y='SalePrice', data=df_cleaned)
# plt.title('Boxplot of Sale Price by air conditioning')
# plt.show()
#
# # Описательная статистика
# print("\nОписательная статистика для CentralAir и SalePrice:")
# print(df_cleaned.groupby('CentralAir')['SalePrice'].describe())
#
# sns.boxplot(x='GarageCars', y='SalePrice', data=df_cleaned)
# plt.title('Boxplot of Sale Price by garage size')
# plt.show()
#
#
# # 7
#
# # Частота размеров гаража
# garage_freq = df_cleaned['GarageCars'].value_counts(normalize=True)
# print("\nЧастота размеров гаража:")
# print(garage_freq)
#
# # Частота кондиционеров
# air_condition_freq = df_cleaned['CentralAir'].value_counts(normalize=True)
# print("\nЧастота наличия кондиционера:")
# print(air_condition_freq)
#
# # 8
#
# # Доля домов в пределах 25-го и 75-го процентиля
# q1, q3 = np.percentile(df_cleaned['SalePrice'], [25, 75])
# iqr = q3 - q1
# print(f"\nInterquartile Range (IQR): {iqr}")


# 9


df_numeric = df_cleaned.select_dtypes(include=['number'])
corrmat = df_numeric.corr()
# corrmat = df_cleaned.corr()
plt.figure(figsize=(12, 9))
sns.heatmap(corrmat, vmax=0.8, square=True)
plt.show()

# Топ-10 корреляций с SalePrice
top10_corr = corrmat.nlargest(10, 'SalePrice')['SalePrice']
print("\nТоп-10 корреляций с SalePrice:")
print(top10_corr)

# 10

var_set = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF']
sns.pairplot(df_cleaned[var_set])
plt.show()


# 11

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
sns.scatterplot(x='GrLivArea', y='SalePrice', data=df_cleaned, ax=axes[0])
sns.scatterplot(x='TotalBsmtSF', y='SalePrice', data=df_cleaned, ax=axes[1])
sns.scatterplot(x='OverallQual', y='SalePrice', data=df_cleaned, ax=axes[2])
plt.show()