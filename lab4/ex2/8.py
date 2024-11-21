from data import df
import seaborn as sns
import matplotlib.pyplot as plt

# Находим топ-20 авторов по количеству публикаций
top_authors = df['author'].value_counts().head(20).index

df_top_authors = df[df['author'].isin(top_authors)]

author_downvotes = df_top_authors.groupby('author')['votes_minus'].sum().reset_index()

author_downvotes = author_downvotes.sort_values(by='votes_minus', ascending=False)

print(author_downvotes)

plt.figure(figsize=(12, 6))
sns.barplot(x='author', y='votes_minus', data=author_downvotes)
plt.xticks(rotation=90)
plt.title('Общее количество минусов, полученных топ-20 авторами')
plt.xlabel('Автор')
plt.ylabel('Количество минусов')
plt.show()
