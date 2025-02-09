def logDecorator(func):
    def wrapper(*args, **kwargs):
        print(f"Logging data with arguments : {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"result of log Data returned : {result}")
        return result
    return wrapper

@logDecorator
def addData(a, b):
    c = a + b
    return c 


@logDecorator
def greet(name, age):
    return f"Hello {name}, you are {age} years old!"    

print(addData(6, 7))
print(greet(name="Amit", age=33))