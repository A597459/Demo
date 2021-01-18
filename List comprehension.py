fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "e" in x]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi"]
newlist = [x for x in fruits if x != "mango"]
print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango", "guava"]
newlist = [x for x in fruits]
print(newlist)
# you can use to range function
newlist = [x for x in range(11)]
print(newlist)

# Accept only lower than 10
newlist = [x for x in range(20) if x < 15]
print(newlist)

newlist = [x for x in range(20) if x % 2 ==0]
print(newlist)

newlist = [x for x in range(20) if x > 15]
print(newlist)


# set the value in the new list to {upper} case :
fruits = ["apple", "banana", "mango", "guava"]
newlist = [x.upper() for x in fruits]
print(newlist)


# set all value in the new list to 'hello'
fruits = ["mango", "banana", "guava", "orange"]
newlist = ['helo' for x in fruits]
print(newlist)

# return type in list comprehension
name = ["Aadi", "raju", "jon", "tom"]
newlist = [x if x != "tom" else "Krishna" for x in name]
print(newlist)





