import pandas as pd

df = pd.read_csv("./pandas/dataset/data.csv")

print(df.head())
print(df.tail())
print(df.info())