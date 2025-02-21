# swapping function
# input :
# a= 20, b= 30, c=40
# output:
# a= 30, b= 40, c= 20

a = 20 
b = 30 
c = 40

a = a + b + c
c = a - b - c 
b = a - c - b 
a = a - b - c

print(a)
print(b)
print(c)