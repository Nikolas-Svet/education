from data import df
import pandas as pd

df["published"] = pd.to_datetime(df["published"], errors="coerce", yearfirst=True)

if df["published"].isna().sum() > 0:
    print("Внимание: Некоторые значения в 'published' не удалось преобразовать.")
    print(df[df["published"].isna()])

df["year"] = df["published"].dt.year
df["month"] = df["published"].dt.month
df["dayofweek"] = df["published"].dt.dayofweek
df["hour"] = df["published"].dt.hour

print(df[["published", "year", "month", "dayofweek", "hour"]].head())
