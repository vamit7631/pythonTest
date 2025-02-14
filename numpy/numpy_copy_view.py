import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

print("===================================================")
############################################################

y = arr.view()
arr[1] = 23

print(arr)
print(y)

print(x.base)
print(y.base)
