################### args ####################### 

def sumAll(*args):
    return sum(args)

print(sumAll(1, 2, 3, 4))
print(sumAll(5, 6))
print("===============================Result1")

################### kwargs ####################### 

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Amit", age=33, city="Bhopal")

print("===============================Result2")

################### args and kwargs ####################### 

def greet(greeting, name, age , city):
    return f"{greeting} ! I'm {name}. My age is {age}. I'm from {city}."

def printInfo(*args, **kwargs):
    return greet(*args, **kwargs)
    

print(printInfo("Hello", name = "Amit Verma", age = 34, city = "Bhopal"))