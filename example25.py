# Write a program to identify the missing numbers in the sequence without using any loop.
# seq = [1,2,3,4,6,7,8,9,14,15]

input = [1,2,3,4,6,7,8,9,14,15]

Output = set(range(min(input), max(input) + 1))
missing = sorted(Output - set(input))
print(missing) # [5, 10, 11, 12, 13]