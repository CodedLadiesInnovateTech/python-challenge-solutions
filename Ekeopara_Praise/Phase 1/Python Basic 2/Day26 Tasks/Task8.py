'''8. Write a Python program to check whether a sequence of numbers has an increasing trend or not.
Sample Output:
True
False
False
True
False'''

def check_sequence(lst):
    response = all(i<j for i, j in zip(lst, lst[1:]))
    return response
print(check_sequence([1, 2, 3, 4]))
print(check_sequence([2, 3, 5, 7]))
print(check_sequence([2, 0, 1, 3]))
