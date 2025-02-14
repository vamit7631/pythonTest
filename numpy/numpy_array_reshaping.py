import numpy as np 


########################## Reshape From 1-D to 2-D ##################################
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

print("===================================================")
########################## Reshape From 1-D to 3-D ##################################

newarr1 = arr.reshape(2, 3, 2)
print(newarr1)

print("===================================================")
########################## Flattening Array ##################################

arr2 = np.array([[1, 2, 3],[4, 5, 6]])
newarr2 = arr.reshape(-1)
print(newarr2)

