#print out days of the week based on the user input

week_days = int(input("Enter numbers 1 - 7 to get days of the week: "))

if week_days < 1:
    print("No negative number is allowed to display weekdays")
elif week_days == 1:
    print("Monday")
elif week_days == 2:
    print("Tuesday")
elif week_days == 3:
    print("Wednesday")
elif week_days == 4:
    print("Thursday")
elif week_days == 5:
    print("Friday")
elif week_days == 6:
    print("Saturday")
elif week_days == 7:
    print("Sunday")
else:
    print("Numbers above 7 are not allowed to display weekdays")