from data import df
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df['published'] = pd.to_datetime(df['published'], errors='coerce', yearfirst=True)

if df['published'].isna().sum() > 0:
    print("Некорректные значения в столбце 'published':")
    print(df[df['published'].isna()])

df['year_month'] = df['published'].dt.to_period('M')

plt.figure(figsize=(15, 7))
sns.countplot(x='year_month', data=df, order=df['year_month'].sort_values().astype(str).unique())
plt.xticks(rotation=90)
plt.title('Количество публикаций по месяцам и годам')
plt.xlabel('Месяц и год')
plt.ylabel('Количество публикаций')
plt.tight_layout()
plt.show()
