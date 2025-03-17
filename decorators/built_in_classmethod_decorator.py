################### Basic example without decorator ####################### 

class Student:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello my name is {self.name}")

result = Student("Amit")
result.say_hello()


################### with classmethod decorator ####################### 

class Teacher:
    name = "Ankit"
    age = 34
    @classmethod
    def say_hello_teacher2(cls):
        print(f"Hello Madam, my name is {cls.name} and my age is {cls.age}")

result2 = Teacher()
result2.say_hello_teacher2()