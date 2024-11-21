from data import df
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df['published'] = pd.to_datetime(df['published'], errors='coerce', yearfirst=True)

if 'dayofweek' not in df.columns:
    df['dayofweek'] = df['published'].dt.dayofweek + 1

print(df[['published', 'dayofweek']].head())

plt.figure(figsize=(10, 6))
sns.countplot(x='dayofweek', data=df, hue='domain')
plt.title('Количество публикаций по дням недели')
plt.xlabel('День недели (1 - Понедельник, 7 - Воскресенье)')
plt.ylabel('Количество публикаций')
plt.legend(title='Домен')
plt.show()
