# Write a Python program to test if a variable is a list or tuple or a set

List = (2, 3, 4)

try:
    List[2] = 3
    print(f'{List} is a List')
except TypeError:
    print(f'{List} is a tuple or a set')