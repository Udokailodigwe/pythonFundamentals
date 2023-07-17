name = input("Enter student name: ")
age = input("Enter student age: ")
topic = input("Enter favorite topic (or press Enter to finish): ")

favorite_topics = ()
if topic:
    favorite_topics += (topic,)

friends = ()
while True:
    friend = input("Enter student friend (or press Enter to finish): ")
    if friend == "":
        break
    friends += (friend,)

student_info = (name, age, favorite_topics, friends)

print("Name:", student_info[0])
print("Age:", student_info[1])
print("Favorite Subjects:", student_info[2])
print("Friends:", student_info[3])
print(student_info)