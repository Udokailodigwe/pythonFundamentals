# Set intro

animal = {"dog", "cat", "elephant"}
animal.add("fish") # add to set
animal.update({"pig"}, {"lion"}) # add or update set

animal.remove("fish") # remove from the set..if item not found, error is thrown
animal.discard("dog") # remove item from set...if item not found, no error thrown

print(animal)

# union of set
set1 = {1,2,3,4}
set2 = [3,4,5,6]
print(set1.union(set2))

# intersection of set
print(set1.intersection(set2))