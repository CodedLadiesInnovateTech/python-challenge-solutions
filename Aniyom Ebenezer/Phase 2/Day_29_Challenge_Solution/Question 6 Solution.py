"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3. Leave it unchanged.
sample string: 'abc'
Expected Result: 'abcing'
sample string: 'string'
expected result: 'stringly' 
"""
def add_to_string(str1):
    char1, char2 = 'ing', 'ly'
    if len(str1) >= 3:
        if char1 not in str1:
            return str1 + char1
        elif char1 in str1:
            return str1 + char2
    return str1
print(add_to_string('abc'))
print(add_to_string('string'))