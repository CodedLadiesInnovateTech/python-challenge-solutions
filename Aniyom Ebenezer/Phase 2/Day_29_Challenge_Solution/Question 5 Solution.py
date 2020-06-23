"""
Write a Python program to get a single string from two given strings, separated by a space and swap the fisrt two characters
of each string
sample string: 'abc', 'xyz'
expected result: 'xyc abz'
"""
def swap_char(str1, str2):
    char1 = str1[0:2]
    char2 = str2[0:2]
    str1 = str1.replace(char1, char2)
    str2 = str2.replace(char2, char1)
    return str1 + ' ' + str2
print(swap_char("abc", "xyz"))