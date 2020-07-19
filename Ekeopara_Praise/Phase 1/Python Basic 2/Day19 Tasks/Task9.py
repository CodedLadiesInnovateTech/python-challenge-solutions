'''9. Write a Python program to find common divisors between two numbers in a given pair.'''
import math
def comon_divisors(x, y):
    ans = math.gcd(x, y)
    return ans
print(comon_divisors(20, 40))
print(comon_divisors(12, 24))
print(comon_divisors(15, 4))

