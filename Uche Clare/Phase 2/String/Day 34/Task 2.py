#Write a Python program to print all permutations with given repetition number of characters of a given string.

import itertools
string = "123"
print()
print(tuple(itertools.permutations(string, 2)))

