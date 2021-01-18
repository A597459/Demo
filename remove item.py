# The pop() method removes the item with the specified key name:
from pip._vendor.requests import delete

thisdict = {
    "brand": "mahendra",
    "model": "i35",
    "year": "3ie"
}
thisdict.pop("year")
print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
    "brand": "mahendra",
    "model": "h64",
    "color": "orange"
}
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:\
thisdict = {
    "brand": "mahendra",
    "model": "o87",
    "year": "9484"
}
del thisdict["year"]
print(thisdict)

# The del keyword can also delete the dictionary completely:
# thisdict = {
#    "brand": "mahendra",
#   "model": "k87",
#   "color": "gray"
# }
# del thisdict
# print(thisdict)  # this will cause an error because "thisdict" no longer exists.

# Traceback (most recent call last):
# File "C:\Users\Aadi\NEW PYTHON PROJECT\pythonDictionary\remove item.py", line 37, in <module>
#  print(thisdict)
# NameError: name 'thisdict' is not defined


# The clear Method() empties the dictionary:
thisdict = {
    "brand": "mahendra",
    "model": "io2",
    "color": "brown"
}
thisdict.clear()
print(thisdict)
