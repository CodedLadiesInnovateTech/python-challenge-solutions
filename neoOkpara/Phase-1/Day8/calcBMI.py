from __future__ import print_function

height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilogram: "))

bmi = weight / (height * height)
print("Your body mass index is: ", round(bmi, 2))
