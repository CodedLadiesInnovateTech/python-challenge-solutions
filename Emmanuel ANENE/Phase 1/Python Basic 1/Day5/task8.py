from math import *

'''
Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
'''


varX = int(input("Enter first number: "))
varY = int(input("Enter second number: "))

def equa(varX, varY):
    summ = (varX + varY)
    tot =int(pow(summ, 2))
    return "The given equation ({0} + {1}) ^ 2) = {2}".format(varX, varY, tot)


print(equa(varX, varY))