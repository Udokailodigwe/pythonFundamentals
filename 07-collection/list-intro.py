#LIST MANIPULATION
list = []

# append item to list array
list.append("a")
list.append("x")
list.append("t")
list.append("c")

print(list)

list.extend(["i", "w", "q"]) # add list collection to existing list
print(list)
list.sort() # sort item
print(list)
list.insert(2, "h") # insert value at a particular index
print(list)
print(list[-1]) # last index of a list

print(list[len(list)-1]) # get the last item of the list

print(list)
print(list.pop()) # delete the last element of a list and returns the value

print(list.remove("t")) # removes an item from the list without returning a value
list.reverse() # reverse all list items
print(list)
list.clear() # clear all items from the list
print(list)
