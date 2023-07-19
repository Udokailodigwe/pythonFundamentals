def max_of_three(a,b,c):
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result

max_result = max_of_three(100, 200, 300)
print(max_result)

#supplying a default parameter
def greet_by_name(name="world"):
    print(f"hello {name}")

greet_by_name("udoka")
greet_by_name()