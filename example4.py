
def factorial(n):
    x = 1
    for i in range(n,0, -1):
        x = x * i 
    return x


print(factorial(5))


##################### using recursion ######################################

def secondfactorial(n):
    if n == 0 | n == 1:
        return 1
    return n * secondfactorial(n - 1)

print(secondfactorial(5))


##################### list comprehension ######################################

def factorialfn(n):
    x = 1
    factoriallist = [x := x * i for i in range(n, 0, -1)][-1]
    return factoriallist

print(factorialfn(6))