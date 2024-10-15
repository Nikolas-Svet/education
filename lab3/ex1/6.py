import pandas as pd

# 6. Создание объекта DataFrame
data = [[1, 2], [5, 3], [3.7, 4.8]]
df = pd.DataFrame(data, columns=['col1', 'col2'])
print("DataFrame:\n", df)