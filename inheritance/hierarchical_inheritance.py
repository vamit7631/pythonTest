class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetIntro(self):
        print(f"My name is {self.name} and my age is {self.age}")


class Child1(Parent):
    def __init__(self, name, age, school):
        Parent.__init__(self, name, age)
        self.school = school

    def schoolInfo(self):
        print(f"My daughter school name is {self.school}")


class Child2(Parent):
    def __init__(self, name, age, school):
        Parent.__init__(self, name, age)
        self.school = school

    def schoolInfo2(self):
        print(f"My son school name is {self.school}")


userObj1 = Child1("Krishvi", 2, "St Marry School")
userObj2 = Child2("Vinav", 1, "St Xavier School")

userObj1.schoolInfo()
userObj2.schoolInfo2()
