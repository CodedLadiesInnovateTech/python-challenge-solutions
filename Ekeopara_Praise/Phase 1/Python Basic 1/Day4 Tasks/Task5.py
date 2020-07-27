'''5. Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False'''

def check(lst, num):
    return num in lst

print(check([2, 3, 4, 5], 2))
print(check([1, 4, 2, 3], 7))