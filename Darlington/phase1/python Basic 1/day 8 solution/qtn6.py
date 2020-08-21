#program to calculate body mass index.
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))
