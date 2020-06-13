"""
Write a Python program to find the middle character(s) of a given string. 
If the length of the string is odd return the middle character and 
return the middle two characters if the string length is even.
Sample Output:
th
H
av
"""
def middle_string_character(String_word):
    return String_word[(len(String_word)-1)//2 : (len(String_word)+2)//2]
print(middle_string_character("Python"))
print(middle_string_character("PHP"))
print(middle_string_character("Java"))