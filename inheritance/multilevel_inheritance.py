class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetIntro(self):
        print(f"My name is {self.name} and my age is {self.age}")
    

class Employee(Person):
    def __init__(self, name, age, empTitle, salary):
        Person.__init__(self, name, age)
        self.empTitle = empTitle
        self.salary = salary

    def companyJobIntro(self):
        print(f"Job Title: {self.empTitle}, Salary: {self.salary}")
    


class Child(Employee):
    def __init__(self, name, age, empTitle, salary, companyName):
        Employee.__init__(self, name, age, empTitle, salary)
        self.companyName = companyName

    def displayUserInfo(self):
        print(f"My company name is {self.companyName}")


userObj = Child("Amit", 34, "Software Engineer", 200000, "e-Zest Solutions Pvt LTd")
userObj.greetIntro()
userObj.companyJobIntro()
userObj.displayUserInfo()