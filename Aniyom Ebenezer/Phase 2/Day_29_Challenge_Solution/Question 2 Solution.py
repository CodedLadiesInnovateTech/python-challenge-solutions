"""
Write a Python program to count the number of charaters (character frequency) in a string.
sample string: google.com
Expected Result: {'o': 3, 'g':2, '.': 1, 'l': 1, 'm' : 1, 'c': 1}
"""
def character_frequency(str1):
    dict = {}
    for n in  str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
        return dict
print(character_frequency("google.com"))