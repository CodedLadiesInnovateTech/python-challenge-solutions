'''1. Write a Python program to create a list of empty dictionaries. '''

def empty_dict(num):
    lst = [{} for _ in range(num)]
    return lst
print(empty_dict(10))