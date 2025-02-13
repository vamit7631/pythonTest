class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetIntro(self):
        print(f"My name is {self.name} and my age is {self.age}")


class Employee:
    def __init__(self, empTitle, salary):
        self.empTitle = empTitle
        self.salary = salary

    def companyJobIntro(self):
        print(f"Job Title: {self.empTitle}, Salary: {self.salary}")


class Child(Person, Employee):
    def __init__(self, name, age, empTitle, salary, companyName):
        Person.__init__(self, name, age)
        Employee.__init__(self, empTitle, salary)
        self.companyName = companyName

    def displayUserInfo(self):
        self.greetIntro()
        self.companyJobIntro()
        print(f"My company name is {self.companyName}")


userObj = Child("Amit", 34, "Software Engineer", 200000, "e-Zest Solutions Pvt LTd")
userObj.displayUserInfo()