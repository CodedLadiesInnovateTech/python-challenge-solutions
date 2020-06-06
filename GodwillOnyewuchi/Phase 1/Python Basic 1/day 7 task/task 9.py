feet = int(input("Enter the total feet: "))
inches = int(input("Enter the total inches: "))

calc_feet = feet * 30.48
calc_inches = inches * 2.54

centimeters = float(calc_feet + calc_inches)
print(f'Feet: {feet}ft')
print(f'Inch: {inches}in')
print(f'Centimeters: {centimeters}cm')