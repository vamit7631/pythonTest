def myfunction(func):
    def wrapper():
        print("Hello before the function call")
        func()
        print("Hello after the function call")
    return wrapper


@myfunction
def say_hello():
    print("Hello Amit Verma")


say_hello()