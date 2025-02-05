import pandas as pd

df = pd.read_csv("./pandas/dataset/data.csv")

df.dropna(inplace = True)

print(df.info())

