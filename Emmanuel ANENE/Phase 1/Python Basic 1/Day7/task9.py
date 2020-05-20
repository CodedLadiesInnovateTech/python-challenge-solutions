'''
Write a Python program to convert height (in feet and inches) to centimeters.
'''

varF = float(input("Enter your height in feet: "))
varI = float(input("Enter your height in inches: "))

totalF = varF * 30.48
totalI = varI * 2.54

print("Your height in feet is {}cm and in inches is {}cm. ".format(totalF, totalI))