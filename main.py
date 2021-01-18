# In Python a function is defined using the def and calling  keyword:
def my_function():
    print("Hello World")
    print("Apple")


my_function()


# Arguments:
def my_function():
    Name = "Aditya"
    print("welcome", Name)


my_function()


# Addition:
def add():
    a = 48
    b = 83
    c = a + b
    print(c)


add()


# subtraction:
def sub():
    a = 77
    b = 33
    c = a - b
    print(c)


sub()


# multiplication:
def mul():
    a = 9
    b = 4
    c = a * b
    print(c)


mul()


# function without argument and parameter:
# Defining a function without parameter:
def add():
    x = 10
    y = 89
    c = x + y
    print(c)


add()


# calling a function without parameter:
def add(y):
    x = 10
    c = x + y
    print(c)


add(10)


# string value:
def add(a):
    print(a)


add("red")


# shot method:
def add(x):
    y = 44.9873
    print(x + y)
    print(f"formatted output{x + y:5.2f}")


add(44)


# When we call a function without a value for an argument, its default value (as mentioned) is used.
def my_function(name='user'):
    print(f"hello,{name}")


my_function('Aditya Kumar')


# Python Keyword Arguments:
def my_function(a, b):
    return a / b


my_function(38, 2)


# This function expects 2 arguments, but gets only 1: If you try to call the function with 1 or 3 arguments,
# you will get an error:
# def my_function(name, fruits):
#    print(name + "" + fruits)


# my_function('Aditya')


# *args for variable number of arguments:

def my_function(*argv):
    for arg in argv:
        print(type(argv))
        print(arg)


my_function('Welcome', 'Hello', 'Aditya', 'Ankit', 'Atul')


# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):  # that is called packing: as a list:
    print("The youngest child is " + kids[3])


my_function("Emil", "Tobias", "Linus", "Facebook")


# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*args):
    for item in args:
        print(type(args))
        print(item)


fruits = ["orange", "mango", "guava", "apple"]
my_function(*fruits)


# next as a tuple:
def my_function(*args):
    print(args)


name = ['Aditya', 'mohan', 'shivam', 'rahul']

my_function(*name)


#  *kwargs for variable number of keyword arguments:
def my_function(**Kwargs):
    for key, value in Kwargs.items():
        print("%s == %s" % (key, value))


my_function(first='fruits', second='vegetable', third='flowers')


# how to use *args and **kwargs in same line to call a function:
def my_function(*args, **kwargs):
    print("args", args)
    print("kwargs", kwargs)


my_function('Aditya', 'rohan', 'mohit', orange="fruits", rose="flower", carrot="vegetable")


# Example:
# def my_function(*args, **kwargs):
# for arg in args:
#  print(arg)
#  for key, value in kwargs.items():
# print("my name is", + kwargs["name1"])
#  print("my name is", + kwargs["name2"])


# my_function('hello', 'World')


# def kwargs(name1, name2):
# pass
# kwargs(name1="Raja", name2="Himanshu")
# my_function(**kwargs)

# Default parameter value:
def my_function(fruits="banana"):
    print('This is', fruits)


my_function("apple")
my_function("orange")
my_function()
my_function("guava")


# Passing a List as an Argument:
def my_function(flowers):
    for x in flowers:
        print('fruits', x)
        fruits = ["orange", "guava", "mango", "apple"]


my_function(fruits)


# Return Value:
def my_function(x):
    return 10 * x


print(my_function(10))
print(my_function(20))


# The pass statement:
def my_function():
    pass
