import numpy as np 

arr = np.array([1, 2, 3])

for x in arr:
    print(x)

print("===================================================")
########################## Iterating 2-D Array ##################################

arr1 = np.array([[4, 5, 6],[7, 8, 9]])

for x in arr1:
    for y in x:
        print(y)

print("===================================================")
########################## Iterating Arrays Using nditer ##################################

arr2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr2):
    print(x)