"""
Write a Python program to get a string from a given string where all occcerences of its first char
have been changed to '$', except the first character itself.
smaple string: 'restart'
expected result: 'resta$t'
"""
def change_string_char(str1):
    char = str1[0]
    str1 = str1.replace(char, "$")
    str1 = char + str1[1:]
    return str1
print(change_string_char('restart'))