#Vowel counter and string reverser.
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for character in input_string:
        if character in vowels:
            vowel_count += 1
    return vowel_count


def reverse_str(input_string):
    return input_string[::-1]


input_string = input("Enter a string: ")
print(input_string)
print(f"The number of vowels is {count_vowels(input_string)}")
print(f"The reversed string is {reverse_str(input_string)}")





