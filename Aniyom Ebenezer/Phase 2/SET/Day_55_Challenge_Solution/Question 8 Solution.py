'''
Write a Python program to create set difference.
'''
setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = setx & sety
print(setz)
setb = setx - setz
print(setb)