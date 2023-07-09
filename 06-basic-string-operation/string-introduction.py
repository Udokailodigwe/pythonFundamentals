#basic string operation
sentence = "My name is udoka"

print(len(sentence)) # count the length of the string
print(sentence.index("u")) # returns index number of individual characters in string
print(sentence.count("a")) # returns the amount of occurrence of a particular character
print(sentence[5]) # get a character from a group of character based on index position

#string slicing
print(sentence[11:14]) # get start index and stop index of characters
print(sentence[8:]) # get characters starting from a particular index
print(sentence[:8]) # get character stopping at a particular index
print(sentence[4:10:2]) # skip characters at every 2nd letter inbetween specified start and stop index
print(sentence.lower()) # turns character to lowercase
print(sentence.upper()) # turns character to uppercase



