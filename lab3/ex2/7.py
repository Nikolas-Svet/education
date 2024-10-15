from data import *
import numpy as np

df['logcheer'] = np.log(df['cheer'])
print("Датафрейм с новым столбцом logcheer:")
print(df)
