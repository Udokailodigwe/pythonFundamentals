# PRINT 4 LETTERS FROM THE MIDDLE OF THE STRING IF ALL STRING ARE EVEN, OR 5 LETTERS WHEN ODD
string = "Python is a really nice language"

remainder = len(string) % 2 # to check if number is even
middle_index = len(string) // 2 # to get the middle index
amount_before_and_after_middle_index = 2 # to get 4/5 letters from middle character.

start_index = middle_index - amount_before_and_after_middle_index # to get beginning index in slice operator
end_index = middle_index + amount_before_and_after_middle_index + remainder # to get end index in slice operator

character_long = '' # variable to store arriving result

if remainder == 0:
     character_long = string[start_index:end_index]
if remainder == 1:
     character_long = string[start_index:end_index]

print(character_long)
