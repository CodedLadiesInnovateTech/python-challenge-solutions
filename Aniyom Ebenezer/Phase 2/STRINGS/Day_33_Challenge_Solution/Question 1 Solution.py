"""
Write a Python program to strip a set of characters from a string.
"""
str = "The quick brown fox jumps over the lazy dog."
chars = "a,e,i,o,u"
print("Original String: ", str)
print()
print("String after characters strip: " + " ".join(c for c in str if c not in chars))