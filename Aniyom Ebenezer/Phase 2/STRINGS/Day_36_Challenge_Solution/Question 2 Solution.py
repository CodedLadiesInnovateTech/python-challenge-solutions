"""
Write a Python program to remove all consecutive duplicates from a given string.
"""
import itertools
def remove_consecutive_duplicates(s1):
     return (''.join(i for i, _ in itertools.groupby(s1)))

s1= "aabcdaee"
print("Original String: ",s1)
print("\nRemoving all consecutive duplicates:")
print(remove_consecutive_duplicates(s1))