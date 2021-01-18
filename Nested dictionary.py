# Create a dictionary that contain three dictionaries:
mydict = {
    "child1": {
        "name": "orange",
        "color": "red"
    },
    "child2": {
        "name": "apple",
        "color": "pink"
    },
    "child3": {
        "name": "pineapple",
        "color": "green"
    }
}
print(mydict)

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
    "name": "orange",
    "color": "red",
}
child2 = {
    "name": "mango",
    "color": "green"
}
child3 = {
    "name": "guava",
    "color": "yellow"
}

mydict = {
    "child1": "child1",
    "child2": "child2",
    "child3": "child3"
}
print(mydict)
