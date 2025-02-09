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
    @classmethod
    def say_hello_teacher2(cls):
        print(f"Hello Madam, my name is {cls.name}")

result2 = Teacher()
result2.say_hello_teacher2()