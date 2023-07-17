#LIST EXERCISE
name = input("Enter your name: ")
age = int(input("Enter your age in numbers: "))

subjects = input("Enter your favourite subject: ")
favourite_subjects_list = []
if subjects:
    favourite_subjects_list.append(subjects)
else:
    print("please enter one subject")


friend = input("Enter your friend name: ")
friends = []
if friend:
    friends.append(friend)
else:
    print("please enter one friend atleast")

list = [name, age, favourite_subjects_list, friends]

print("Name: ", name)
print("Age: ", age)
print("Favourite_subjects_list: ", favourite_subjects_list)
print("Friends: ", friends)
print(list)






#DICTIONARY EXERCISE
student_profile = {
    "Name": name,
    "Age": age,
    "Favourite Subject": favourite_subjects_list,
    "Friends": friends
}

print("Name:", student_profile["Name"])
print("Age:", student_profile["Age"])
print("Favourite Subject:", student_profile["Favourite Subject"])
print("Friends:", student_profile["Friends"])
print(student_profile)


