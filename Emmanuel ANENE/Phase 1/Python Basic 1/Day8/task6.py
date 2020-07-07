'''
Write a Python program to calculate body mass index.
'''

import math as m

# BMI formula = kg/m^2

varHgt = int(input("Enter your height in cm: "))
calCM = varHgt / 100
varWgt =  int(input("Enter your weight in kg: "))
BMI = round(varWgt / m.pow(calCM, 2), 2)

print("Your Body Mass Index (BMI) is: {}.".format(BMI))