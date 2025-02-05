import pandas as pd 

a = [1, 5, 6]

myvar = pd.Series(a)

print(myvar)


########################################################

b = [2, 4, 7]

myvar2 = pd.Series(b, index=["x", "y", "z"])
print(myvar2)

########################################################

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar3 = pd.Series(calories)
print(myvar3)