# Basic example 

input = [1, 4, 7, 12, 5, 10]
result = [num for num in input if num % 2 == 0]
print(result)


result2 = ["even" if num % 2 == 0 else "odd" for num in input]
print(result2)