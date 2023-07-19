#Ask user for an input and print it out
user_input = ""
while user_input != "exit":
    user_input = input("Please enter any info: ")
    #if input is equal to "exit-no-print", terminate program without printing out anything
    if user_input == "exit-no-print":
        break
        #if input is equal "no-print" program moves to next loop iteration without printing anything
    if user_input == "no-print":
        continue
        #if input is not "no-print", "exit-no-print", "exit", program restarts
        print(user_input)
    else:
        print("Done")


