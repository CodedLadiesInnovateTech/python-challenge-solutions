"""
Write a Python program to duplicate characters of a given string.
"""
from collections import OrderedDict
def remove_duplicate(str1):
    return "".join(OrderedDict.fromkeys(str1))
print(remove_duplicate("CodedLadies Python Challenge."))