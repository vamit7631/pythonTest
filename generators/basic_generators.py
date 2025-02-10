def myGenerators():
    yield 1
    yield 2
    yield 3


gen = myGenerators()

print(next(gen))
print(next(gen))
print(next(gen))