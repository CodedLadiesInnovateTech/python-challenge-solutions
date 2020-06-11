'''3. Write a Python program to remove the duplicate elements of a given array of numbers such that each 
element appear only once and return the new length of the given array.
Sample Output:
5
4'''
def remove_duplicate(value):
    value = set(value)
    length = len(value)
    return length 
print(remove_duplicate((0, 6, 7, 1, 2, 2, 0)))
print(remove_duplicate((0, 0, 7, 1, 2, 2, 0)))