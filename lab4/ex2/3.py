from data import df
import pandas as pd

df["published"] = pd.to_datetime(df.published, yearfirst=True)

print(df['published'].dtype)
