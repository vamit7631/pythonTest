################### Basic example without decorator ####################### 

class Person:
    def __init__(self, name):
        self._name = name

    # getter function
    def get_name(self):
        print("Getting name...")
        return self._name
    
    # setter function
    def set_name(self, value):
        print("Setting name : ", value)
        self._name = value

    # deleter function
    def del_name(self):
        print('Deleting name...')
        del self._name

    
    name = property(get_name, set_name, del_name)

p = Person("Mugdha")
print(p.name)
p.name = "Amit"
del p.name
print("==============================================================================")

################### with property decorator ####################### 


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Getting name...')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to:', value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name...')
        del self._name

p = Person('David')
print(p.name)
p.name = 'Rocky'
del p.name