'''6. Write a Python program to create a histogram from a given list of integers.'''
def hist(lst):
    for i in lst:
        print("*" * i)
print(hist([1, 2, 3, 4,5]))