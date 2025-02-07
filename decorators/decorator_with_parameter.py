def repeat(n):
    def repeat_decorator2(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        
        return wrapper
    return repeat_decorator2



@repeat(4)
def greet(name):
    print(f"Hello, {name}")

greet("Amit")