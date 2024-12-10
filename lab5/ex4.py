import pandas as pd

# Загрузка данных
file_path = 'travel.csv'  # Укажите путь к файлу
data = pd.read_csv(file_path)

# 1. Вывод первых 10 записей
print("Первые 10 записей:")
print(data.head(10))

# 2. Описание данных
print("\nИнформация о данных:")
print(data.info())

print("\nОписание количественных данных:")
print(data.describe())

# 3. Определение типов признаков
def classify_features(df):
    quantitative = []
    ordinal = []
    nominal = []

    for column in df.columns:
        unique_values = df[column].nunique()
        dtype = df[column].dtype

        if dtype in ['int64', 'float64']:
            if unique_values < 20:
                ordinal.append(column)
            else:
                quantitative.append(column)
        elif dtype == 'object':
            nominal.append(column)

    return quantitative, ordinal, nominal


quantitative, ordinal, nominal = classify_features(data)

print("\nКоличественные признаки:", quantitative)
print("\nКачественные порядковые признаки:", ordinal)
print("\nКачественные номинальные признаки:", nominal)


# 4. Параметры описательной статистики
quantitative_stats = data[quantitative].describe()
nominal_stats = data[nominal].describe()

print("\nОписание количественных признаков:")
print(quantitative_stats)

print("\nОписание номинальных признаков:")
print(nominal_stats)

# Проверка на выбросы в количественном признаке
q1 = data['orig_destination_distance'].quantile(0.25)
q3 = data['orig_destination_distance'].quantile(0.75)
iqr = q3 - q1
outliers = data[
    (data['orig_destination_distance'] < (q1 - 1.5 * iqr)) |
    (data['orig_destination_distance'] > (q3 + 1.5 * iqr))
]

print("\nКоличество выбросов в 'orig_destination_distance':", len(outliers))

# Группировка данных по категориальному признаку
grouped_by_hotel_cluster = data.groupby('hotel_cluster')['cnt'].sum()
print("\nСуммарное количество бронирований по hotel_cluster (первые 10):")
print(grouped_by_hotel_cluster.head(10))

# 5. Визуализация
import matplotlib.pyplot as plt

# Количественные признаки
for feature in quantitative:
    data[feature].dropna().plot(kind='hist', bins=30, title=f"Распределение {feature}")
    plt.xlabel(feature)
    plt.show()

# Категориальные признаки
for feature in nominal:
    data[feature].value_counts().head(10).plot(kind='bar', title=f"Распределение {feature}")
    plt.xlabel(feature)
    plt.ylabel("Частота")
    plt.show()

# 6. Корреляционный анализ
import matplotlib.pyplot as plt
import seaborn as sns

# Удаление нечисловых признаков
numeric_data = data.select_dtypes(include=['int64', 'float64'])

# Вычисление корреляционной матрицы
correlation_matrix = numeric_data.corr()

# Вывод корреляционной матрицы
print("\nКорреляционная матрица:")
print(correlation_matrix)

# Визуализация корреляционной матрицы
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Корреляционная матрица")
plt.show()
