'''
Write a Python program to create a symmetric difference.
'''
setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setc = setx ^ sety
print(setc)