# palindrome example
x = "test"
y = "".join(reversed(x))
if y == x:
    print(True)
else:
    print(False)    

###########################################################

a = "malayalam"
b = a[::-1]
if b == a:
    print(True)
else:
    print(False) 

###########################################################

x = "malayalam"
w = ""
for i in x:
    w = i + w
if w == x:
    print(True)
else:
    print(False)
