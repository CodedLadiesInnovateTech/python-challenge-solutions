from math import *

num1 = int(input("Enter first digit: "))
num2 = int(input("Enter second digit: "))

def comDiv(num1, num2):
    return gcd(num1, num2)

print(comDiv(num1, num2))