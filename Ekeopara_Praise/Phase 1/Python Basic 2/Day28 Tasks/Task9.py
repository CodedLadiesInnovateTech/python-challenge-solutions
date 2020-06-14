'''9. Write a Python program to check if two given numbers are coprime or not. Return True if two numbers are coprime otherwise return false.
Sample Output:
True
True
False
False'''

import math
def check_coprime(x, y):
    answer = math.gcd(x, y)
    if answer == 1:
        response = "True"
    else:
        response ="False"
    return response
print(check_coprime(2, 6))
print(check_coprime(2, 5))
print(check_coprime(3, 7))