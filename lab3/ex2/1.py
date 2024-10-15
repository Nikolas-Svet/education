from data import data, df
import pandas as pd

df['cheer'] = df['cheer'].astype(float)

print(df.dtypes)