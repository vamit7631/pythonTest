################### Basic example without decorator ####################### 

class Student:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello my name is {self.name}")

result = Student("Amit")
result.say_hello()



################### with staticmethod decorator ####################### 

class Teacher:
    # def __init__(self, name):
    #     self.name = name

    @staticmethod
    def say_hello_teacher(name):
        print(f"Hello Teacher. my name is {name}")

result2 = Teacher()
result2.say_hello_teacher("Ankit")