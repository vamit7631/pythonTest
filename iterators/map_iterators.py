nums = [1, 2, 3, 4]
squared_iter = map(lambda x: x ** 2, nums)

print(next(squared_iter))  # Output: 1
print(next(squared_iter))  # Output: 4
print(next(squared_iter))  # Output: 9
print(next(squared_iter))  # Output: 16
