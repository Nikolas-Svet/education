from data import df
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df['published'] = pd.to_datetime(df['published'], errors='coerce', yearfirst=True)

if 'hour' not in df.columns:
    df['hour'] = df['published'].dt.hour

print(df[['published', 'hour']].head())

plt.figure(figsize=(12, 6))
sns.barplot(x='hour', y='views', data=df, estimator='mean', errorbar=None)
plt.title('Среднее количество просмотров по часу публикации')
plt.xlabel('Час публикации')
plt.ylabel('Среднее количество просмотров')
plt.show()
