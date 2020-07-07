from math import *

num1 = int(input("Enter first digit: "))
num2 = int(input("Enter second digit: "))

def lcm(num1, num2):
    val = int(num1 * num2 / gcd(num1, num2))
    return val

print(lcm(num1, num2))