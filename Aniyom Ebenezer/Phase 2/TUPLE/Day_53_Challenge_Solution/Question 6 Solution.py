'''
Write a Python program to convert a tuple to a dictionary.
'''
tuplex = ((2, "w"),(3, "r"))
print(dict((y, x) for x, y in tuplex))