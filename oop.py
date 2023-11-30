#INTRO
#object is an instance of a class
#class - blueprint of an obj

#OOP - 

#INITIALIZATION
#__init__() magic method

class Engineers:
    def __init__(self,names):
        print(f'{names} is an Engineer')
        self.names = names
engineer1 = Engineers('Zac')
engineer2 = Engineers('Amina')
engineer3 = Engineers('Neemat')
engineer4 = Engineers('John')


#optional __init() args

class Animals:
    def __init__(self, name, age = 35):
        self.name = name
        self.age = age

duck = Animals('Bird')
cat = Animals('Kitty', 7)
print(cat.age)
print(cat.name)
print(duck.age)
