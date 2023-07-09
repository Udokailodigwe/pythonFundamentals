recipe = ("boil water", "insert egg", "wait 5min", "eat")

print("length of recipe:", len(recipe)) # length of recipe tuple
print("The third step:", recipe[2:3]) # get the "wait 5min" step 3 from the recipe tuple
print("The last two steps:", recipe[2:]) # get the last two-step from the recipe tuple

print("The count of wait 5min:", recipe.count("wait 5min")) # count the occurrence of "wait 5min"

print("boil water index", recipe.index("boil water")) # the index of the first step
#print(recipe[0])

