import math
weight = float(input("Enter your weight in meters: "))

height = float(input("Enter your height in kilograms: "))

BodyMI = (weight / height)

print(f'Your Body Mass Index is {BodyMI}')

if BodyMI < 18.5:
    print(f'Ypu are Underweight')
elif 18.5 < BodyMI < 24.9:
    print(f'Ypu are Normal weight')
elif 25 < BodyMI < 29.9:
    print(f'Ypu are Over weight')
elif BodyMI > 30:
    print(f'You are Obessed')