#Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string. 
word = input("Enter String: ")
if len(word)>=3:
    print(word[0:3])
else:
    print(word)