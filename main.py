# if statement:
a = 10
b = 84
if b > a:
    print("b is greater than a")
# If statement, without indentation (will raise an error)
# a = 33
# b = 200

# if b > a:
# print("b is greater than a")


# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 80
b = 80
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")

    # The else keyword catches anything which isn't caught by the preceding conditions.
    a = 200
    b = 34
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

    # You can also have an else without the elif:
    a = 200
    b = 49
if b <= a:
    print("b is not greater than a")
else:
    print("b is greater than a")

    # One line if statement:
a = 399
b = 98
if a > b:
    print("a is greater than b")

# One line if else statement:
a = 9
b = 983
print("A") if a > b else print("B")

# One line if else statement, with 3 conditions:
a = 434
b = 434
print("A") if a > b else print("=") if a == b else print("B")

# The and keyword is a logical operator, and is used to combine conditional statements:
# Test if a is greater than b, AND if c is greater than a:
a = 800
b = 80
c = 900
if a > b and c > a:
    print("both condition are true")
# Test if a is greater than b, OR if a is greater than c:
a = 209
b = 39
c = 399
if a > b or a > c:
    print("At least on of the condition is true")

# You can have if statements inside if statements, this is called nested if statements
x = 80
if x > 78:
    print("x is greater than 78")
if x > 67:
    print("x is greater than 67")
else:
    print("but not above 67")


# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass
# statement to avoid getting an error.
a = 33
b = 200

if b > a:
    pass
# having an empty if statement like this, would raise an error without the pass statement
