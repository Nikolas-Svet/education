import pandas as pd

data = [[1, 2], [5, 3], [3.7, 4.8]]
df = pd.DataFrame(data, columns=['col1', 'col2'])

series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
