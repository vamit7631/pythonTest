class Base:
    def func1(self):
        print("This is the Base class.")

class Parent1(Base):
    def func2(self):
        print("This is Parent1 class.")

class Parent2(Base):
    def func3(self):
        print("This is Parent2 class.")

class Child(Parent1, Parent2):
    def func4(self):
        print("This is the Child class.")

obj = Child()
obj.func1()
obj.func2()
obj.func3()
obj.func4()
