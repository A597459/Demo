# The union() method returns a new set with all items from both sets:

set1 = {"a" "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# The intersection_update() method will keep only the items that are present in both sets.
# Keep the items that exist in both set x, and set y:
# Keep ONLY the Duplicates:
set1 = {"apple", "orange", "mango"}
set3 = {"orange", "mango", "pineapple"}
set1.intersection_update(set3)
print(set1)

# Return a set that contains the items that exist in both set1, and set2:
set1 = {"apple", "orange", "mango"}
set2 = {"mango", "pineapple", "grapes"}
set3 = set1.intersection(set2)
print(set3)

# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
# Keep the items that are not present in both sets:

set1 = {"apple", "orange", "mango"}
set2 = {"pineapple", "guava", "apple"}
set1.symmetric_difference_update(set2)
print(set1)


# Return a set that contains all items from both sets, except items that are present in both:
set1 = {"apple", "orange", "mango"}
set2 = {"grapes", "guava", "orange"}
set3 = set1.symmetric_difference(set2)
print(set3)

