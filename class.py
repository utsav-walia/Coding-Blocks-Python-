# Creating class First letter in Caps
class Person:
    pass # Pass means class is empty

# Declaring an object by class name
p = Person()
print(p)

# Printing integer value of ADDRESS
print(id(p))

# Printing hexadecimal value of ADDRESS
print(hex(id(p)),'\n')


class People:
    name = "Utsav"

    # Defination
    def hi(self):
        print("Hello my name is: " , self.name, '\n')
    

p = People()
p.hi()

# Using __init__ method

class New:
    
    name = "Utsav"

    def __init__(self, name):
        self.name = name

    def hi(self):
        print("I am ", self.name)

New.hi(p) # Shortcut

p = New("Freddy") # Change parameter call
p.hi()

# Only Sets, Dictionary, Lists are mutable 
# STRINGS CANNOT BE CHANGE i.e IMMUTABLE

class Dog:

    def __init__(self,name):
        self.name = name
        self.alltricks = [] 
        # After mutating the memory allocated address is the same
        # We should intantiate the tricks in each of the instance

    def addtrick(self,trick):
        self.alltricks.append(trick)

a = Dog("maxx")
b = Dog("Bruno")

a.addtrick("get")
a.addtrick("talk")
print('\n')
print(a.alltricks)
print(b.alltricks)

print(id(a.alltricks))
print(id(b.alltricks)) 










