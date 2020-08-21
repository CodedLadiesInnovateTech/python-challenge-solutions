'''7. Write a Python program to check whether a given employee code is exactly 8 digits or 12 digits. 
Return True if the employee code is valid and False if it's not.
Sample Output:
True
False
False
True
False'''
def check_digit(num):
    num1 = str(num)
    if len(num1) == 8 or len(num1) == 12:
        ans = 'True'
    else:
        ans = 'False'
    return ans
print(check_digit((12345678)))
print(check_digit((123456789017)))
print(check_digit((12345678901745)))