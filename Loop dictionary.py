# Print all key name in the dictionary, one by one:
thisdict = {
    "brand": "mahendra",
    "model": "j67",
    "year": "8789"
}
for x in thisdict:
    print(x)
# print all value in the dictionary:
thisdict = {
    "brand": "ford",
    "model": "dj987",
    "color": "white"
}
for x in thisdict:
    print(thisdict[x])

# You can also use the values() method to return values of a dictionary:
thisdict = {
    "brand": "mahendra",
    "model": "jk74",
    "color": "green"
}
for x in thisdict.values():
    print(x)

# You can use the keys() method to return the keys of a dictionary:
thisdict = {
    "brand": "mahendra",
    "model": "hg98",
    "color": "pink"
}
for x in thisdict.keys():
    print(x)

# Loop through both keys and values, by using the items() method:
thisdict = {
    "brand": "mahendra",
    "model": "hi89",
    "year": "1919"
}
for x, y in thisdict.items():
    print(x, y)

