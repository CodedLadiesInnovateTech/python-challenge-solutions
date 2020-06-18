"""
Two numbers are coprime if their highest common factor (or greatest common divisor if you must) is 1.
Write a Python program to check if two given numbers are coprime or not. Return True if two numbers are coprime otherwise return false.
"""
def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p
def is_coprime(x, y):
    return gcd(x, y) == 1
print(is_coprime(17, 13))
print(is_coprime(17, 21))
print(is_coprime(15, 21))
print(is_coprime(25, 45))