# Add 10 to argument a, and return the result:
x = lambda a: a + 10
print(x(8))

# Multiply argument a with argument b and return the result:
x = lambda a, b: a * b
print(x(3, 9))

# Summarize argument a, b, and c and return the result:
x = lambda a, b, c: a + b + c
print(x(8, 9, 3))


# Why Use Lambda Functions.
# Use that function definition to make a function that always doubles the number you send in:
def my_function(n):
    return lambda a: a * n


Name1 = my_function(2)
print(Name1(11))


# Or, use both function Name1 and Name2:
def my_function(n):
    return lambda a: a * n


Name1 = my_function(10)
Name2 = my_function(9)
print(Name1(2))
print(Name2(8))


