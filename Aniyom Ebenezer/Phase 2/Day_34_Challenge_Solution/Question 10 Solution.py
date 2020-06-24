"""
Write a Python program to capitalize first and last letters of each word of a given string.
"""
str1 = "CodedLadies Innovate is a python oriented group."
str1 = result = str1.title()
result = ""
for word in str1.split():
    result += word[:-1] + word[-1].upper() + " "
print(result[:-1])