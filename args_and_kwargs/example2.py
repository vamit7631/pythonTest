################### args ####################### 

def multiply(a, b, c):
    return a * b * c

def keyargs(*args):
    return multiply(*args)

print(keyargs(2, 4, 6))


################### kwargs ####################### 

def greet(name, age, city):
    return f"Hello, my name is {name}, I am {age} years old, and I live in {city}."

def pass_kwargs(**kwargs):
    return greet(**kwargs)  # Unpacking kwargs

result = pass_kwargs(name="Amit", age=33, city="Bhopal")
print(result)  


################### args and kwargs #######################

def full_info(greeting, name, age, city):
    return f"{greeting}! I am {name}, {age} years old from {city}."

def wrapper(*args, **kwargs):
    return full_info(*args, **kwargs)

result = wrapper("Hello", name="Amit", age=33, city="Bhopal")
print(result)
# Output: Hello! I am Amit, 33 years old from Bhopal.

