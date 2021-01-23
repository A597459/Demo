# Basic of  Object oriented programing :
from os import name


class fruits:
    color = 'red'  # That is variable:


Apple = fruits()  # That is Object:
print(Apple.color)

Orange = fruits()
Orange.color = "orange"

print(Orange.color)
print(Apple.color)


# Object oriented programing:
class car:
    def __init__(self):
        self.breaks_speed = 88
        self.increase_speed = 55

    speed = 20
    color = 'Blue'


tata = car()
print(tata.speed)
print(tata.increase_speed)
print(tata.speed)
print(tata.breaks_speed)


# Create a class named Person, use the __init__() function to assign values for name and age::
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = person("john", 48)
print(p1.name)
print(p1.age)


# Insert a function that prints a greeting, and execute it on the p1 object:
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_function(self):
        print("Hello This is ", self.name)


p1 = person("Aditya", 36)
p1.my_function()


#  Use the words mysillyobject and abc instead of self:
class person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def my_function(asdf):
        print("Hello i am ", asdf.name)


p1 = person("Aditya", 100)
p1.my_function()


# You can modify properties on objects like this:
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_function(self):
        print("Hello Who is ", self.name)


p1 = person("Aditya", 84)
p1.my_function()

p1.age = 49
print(p1.age)


# Delete Object Properties.
# You can delete properties on objects by using the del keyword:
# Delete the age property from the p1 object:
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_function(self):
        print("My name is ", self.name)
        print("I am", self.age)


var = p1.age
print(p1.age)

p1 = person('Ravi', 22)
p1.my_function()
