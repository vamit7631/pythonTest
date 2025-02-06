import pandas as pd

df = pd.read_csv("./pandas/dataset/data.csv")

# df.fillna(130, inplace = True)
# df["Calories"].fillna(130, inplace = True)



# Mean = the average value (the sum of all values divided by number of values).
# Median = the value in the middle, after you have sorted all values ascending.
# Mode = the value that appears most frequently.
x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())