# Join two list
list1 = ["Apple", "banana", "mango"]
list2 = [4, 7, 3]
list3 = list1 + list2
print(list3)

# append to list2 into list1
list1 = ["mango", "orange", "pineapple"]
list2 = [3, 4, 25, 6]
for x in list2:
    list1.append(x)
    print(list1)
# use the extend() method to add list2 at end of list1
list1 = ["Apple", "mango", "banana", "orange"]
list2 = [1, 2, 3, 4, 5, 6]
list1.extend(list2)
print(list1)
