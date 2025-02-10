nums = [1, 2, 3, 4, 5, 6]
even_iter = filter(lambda x: x % 2 == 0, nums)

for num in even_iter:
    print(num)
