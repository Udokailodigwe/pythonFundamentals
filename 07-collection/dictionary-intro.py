phonebook = {} # initialize dictionary

# add elements to dictionary
phonebook["Name"] = "Udoka"
phonebook["age"] = 20
phonebook["place"] = "joensuu"
phonebook["job"] = "developer"
print(phonebook["Name"]) # get an element from the dictionary

print(phonebook)

phonebook.pop("Name") # pop out an element from the dictionary
del phonebook["age"] # delete element from the dictionary
print(phonebook)

print(phonebook.get("place"))
print(phonebook.get("Name", "Udoka"))
print(phonebook.get("Age", 20))
# phonebook.clear()
print(len(phonebook)) # get the length of the dictionary
phonebook.update({"Name":"Udoka", "Age": 20}) # update or add elements to the dictionary
print(phonebook)


