# Print each fruit in a fruit list:
fruits = ["apple", "orange", "mango", "guava"]
for x in fruits:
    print(x)
# Loop through the letters in the word "banana":
for x in "orange":
    print(x)

# Exit the loop when x is "mango":
fruits = ["orange", "guava", "grapes", "mango", "apple"]
for x in fruits:
    print(x)
    if x == "mango":
        break

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["orange", "mango", "pineapple", "guava"]
for x in fruits:
    if x == "guava":
        break
    print(x)

# With the continue statement we can stop the current iteration of the loop, and continue with the next:
# Do not print pineapple:
fruits = ["orange", "mango", "pineapple", "guava", "apple"]
for x in fruits:
    if x == "pineapple":
        continue
    print(x)

# Using the range() function:
for x in range(8):
    print(x)

# Using the start parameter:
for x in range(5, 10):
    print(x)
# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value
# by adding a third parameter: range(3, 33, 3)
for x in range(3, 33, 3):
    print(x)

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(7):
    print(x)
else:
    print("Finally Finished!")

# Break the loop when x is 20, and see what happens with the else block:
for x in range(19):
    if x == 20:
        break
    print(x)
else:
    print("Finally Finished")

# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
# Print each adjective for every fruit:
color = ["red", "green", "yellow"]
fruits = ["orange", "mango", "apple"]
for x in color:
    for y in fruits:
        print(x, y)


# Pass statement:


