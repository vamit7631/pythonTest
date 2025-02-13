class Parent:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def display(self):
        print(f"My name is {self.name}. My age is {self.age}")


class Child(Parent):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def show(self):
        print(f"I'm {self.name}. My age is {self.age}. And I'm working with {self.company}")


obj = Child("Amit Verma", 34, "e-Zest Solutions")
obj.show()

