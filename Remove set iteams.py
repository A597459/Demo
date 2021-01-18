# Remove "Orange" by remove() method use:
thisset = {"apple", "orange", "mango"}
thisset.remove("orange")
print(thisset)

# Remove "apple" by using discard() Method:
thisset = {"apple", "orange", "mango", "banana"}
thisset.discard("apple")
print(thisset)

# Remove the last item using by pop() Method:
thisset = {"apple", "orange", "mango", "pineapple"}
x = thisset.pop()
print(x)
print(thisset)

# The clear() method empty the set
thisset = {"orange", "mango", "pineapple", "apple"}
thisset.clear()
print("Clear the set=", thisset)

# The del Keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)  # this will raise an error because the set no longer exists
