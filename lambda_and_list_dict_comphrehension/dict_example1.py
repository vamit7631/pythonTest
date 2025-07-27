# Basic example 
keys = ['a','b','c','d','e']
values = [1,2,3,4,5] 

mydict = {k:v for (k, v) in zip(keys, values)}
mydict2 = dict(zip(keys, values))


print(mydict,"========================1")
print(mydict2,"========================2")


##################################################


mydict3 = {x: x*x for x in [1, 2, 3, 3, 4, 5]}
print(mydict3,"========================3")

##################################################


mydict4 = {x: x*x for x in [1, 2, 3, 3, 4, 5] if x % 2 == 0}
print(mydict4,"========================3")
##################################################


mydict5 = {x: x*x if x % 2 == 0 else "odd" for x in [1, 2, 3, 3, 4, 5]}
print(mydict5,"========================4")