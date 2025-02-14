import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) # output = 2,3,4,5
print(arr[4:]) # output = 5,6,7
print(arr[:4]) # output = 1,2,3,4

print("===================================================")
#################### Negative slicing ########################

arr1 = np.array([8, 9, 10, 11, 12, 13, 14])
print(arr1[-3:-1]) # output = 12,13

print("===================================================")
#################### Steps in slicing ########################

arr1 = np.array([8, 9, 10, 11, 12, 13, 14])
print(arr1[1:5:2]) # output = 9,11
print(arr1[::2]) # output = [ 8 10 12 14]

print("===================================================")
#################### 2D Array slicing ########################

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr2[1, 1:4]) # output = [7 8 9]
print(arr[0:2, 2]) # output = [3 8]
print(arr[0:2, 1:4]) # output = [[2 3 4] [7 8 9]]