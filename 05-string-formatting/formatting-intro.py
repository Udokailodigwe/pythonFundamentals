# Formatting and printing (old style python 2.7)
name_1 = "Udoka"
name_2 = "Uche"
print("Hello there, %s, %s" % (name_1, name_2))
print("Hello there, %(name_1)s, %(name_2)s" % {"name_1":name_1, "name_2":name_2})

# Formatting and printing (new style in python 3)
name_1 = "udoka"
name_2 = "uche"

print("Hello there, {} {}".format(name_1, name_1))
print("Hello there, {name_1} {name_2}".format(name_1 = name_1, name_2 = name_2))

# String interpolation or literals or f-strings but allows for variable substitution
name_1 = "udoka"
name_2 = "uche"
print(f"Hello everyone,  {name_2} {name_1}")

# Changing how variables are displayed
header_1 = "name"
header_2 = "age"
name = "John"
age= 19

print(f"| {header_1:10} | {header_2:10} |")
print("-" * 27)
print(f"| {name:10} | {age:10} |")