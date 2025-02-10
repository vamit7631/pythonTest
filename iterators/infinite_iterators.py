import itertools

def infinite_counter():
    num = 1
    while True:
        yield num
        num += 1

infinite_iter = infinite_counter()

print(next(infinite_iter))  # Output: 1
print(next(infinite_iter))  # Output: 2
print(next(infinite_iter))  # Output: 3
