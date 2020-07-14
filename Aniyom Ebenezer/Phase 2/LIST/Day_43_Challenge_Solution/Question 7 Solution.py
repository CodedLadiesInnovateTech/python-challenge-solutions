"""
Write a Python program to insert an element before each element of a list.
"""
color = ["Red", "Blue", "Black", "Yellow"]
color = [V for elt in color for V in ('c', elt)]
print(color)