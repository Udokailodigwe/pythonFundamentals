#SET EXERCISE

name = input("Enter your name: ")
age = int(input("Enter your age in numbers: "))
favourite_subjects = set()

subjects = input("Enter your favourite subject: ")
if subjects:
    favourite_subjects.add(subjects)
else:
    print("please enter subject")

friends = set()
friend = input("Enter your favourite friend: ")

if friend:
    friends = friend
else:
    print("please enter a name")

student_set = {name, age,  str(favourite_subjects), str(friends)}
print(student_set)