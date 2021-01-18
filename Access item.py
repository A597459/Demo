# Get the value of "model" key:
from pyexpat import model

thisdict = {
    "Brand": "Mahendra",
    "Model": "S10",
    "Year": 2020
}
x = thisdict["Model"]
print(x)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)

# There is also a method called get() that will give you the same result:
# Get the value of the "model" key:
thisdict = {
    "model": "s3",
    "brand": "mahendra",
    "color": "red"
}
x = thisdict.get("color")
print(x)

# The keys() method will return a list of all the keys in the dictionary.
# Get a list of the keys:
thisdict = {
    "brand": "mahendra",
    "model": "s85",
    "year": "2020",
    "color": "yellow"
}
x = thisdict.keys()
print(x)

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
thisdict = {
    "brand": "mahendra",
    "model": "s85",
    "year": "2020"
}
x = thisdict.keys()
print(x)  # before add item
thisdict["color"] = "pink"
print(x)  # after the change

# Get a list of the value:
thisdict = {
    "brand": "mahendra",
    "model": "s49",
    "color": "black"
}
x = thisdict.values()
print(x)

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
thisdict = {
    "brand": "mahendra",
    "model": "w87"
}
x = thisdict.items()
print(x)  # before update
thisdict["Year"] = 1997
print(x)  # after update

# Check if "model" is present in the dictionary:
thisdict = {
    "brand": "mahendra",
    "color": "blue",
    "year": "2021",
    "model": "f11"
}
if model in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


