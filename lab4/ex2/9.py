from data import df
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df['published'] = pd.to_datetime(df['published'], errors='coerce', yearfirst=True)

if 'dayofweek' not in df.columns:
    df['dayofweek'] = df['published'].dt.dayofweek + 1

if 'hour' not in df.columns:
    df['hour'] = df['published'].dt.hour

df_saturday = df[df['dayofweek'] == 6]
df_monday = df[df['dayofweek'] == 1]

df_saturday['time_of_day'] = df_saturday['hour'].apply(lambda x: 'День' if 6 <= x < 18 else 'Вечер')
df_monday['time_of_day'] = df_monday['hour'].apply(lambda x: 'День' if 6 <= x < 18 else 'Вечер')

saturday_distribution = df_saturday['time_of_day'].value_counts(normalize=True)
monday_distribution = df_monday['time_of_day'].value_counts(normalize=True)

print("Распределение по времени суток в субботу:")
print(saturday_distribution)
print("\nРаспределение по времени суток в понедельник:")
print(monday_distribution)

plt.figure(figsize=(12, 6))
sns.histplot(df_saturday['hour'], bins=24, color='blue', kde=False, label='Суббота', alpha=0.5)
sns.histplot(df_monday['hour'], bins=24, color='red', kde=False, label='Понедельник', alpha=0.5)
plt.title('Распределение времени публикаций по часам в субботу и понедельник')
plt.xlabel('Час')
plt.ylabel('Количество публикаций')
plt.legend()
plt.show()