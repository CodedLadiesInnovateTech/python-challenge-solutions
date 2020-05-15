import math as ma

dig1 = int(input("Enter a first number: "))
dig2 = int(input("Enter a second number: "))
dig3 = int(input("Enter a third number: "))

def calcSum (num1, num2, num3):
    if num1 is num2 or num2 is num3 or num1 is num3:
        return ((num1 + num2 + num3) ** 3)
    else:
        return num1 + num2 + num3

print(calcSum(dig1,dig2,dig3))


