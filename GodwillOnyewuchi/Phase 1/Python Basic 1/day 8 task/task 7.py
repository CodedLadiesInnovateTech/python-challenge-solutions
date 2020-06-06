
import math
print("Conversion of kilo-pascals to pounds per square inch,a millimeter of mercury (mmHg) and atmosphere pressure ")

kilo_pascals = float(input("Enter the number of kilo-pascals: "))

pounds = math.ceil(kilo_pascals / 0.145)
print(f'{kilo_pascals} kilo-pascals is {pounds} pounds per square inch')

Mili_mercury = math.ceil(kilo_pascals *7.50062)
print(f'{kilo_pascals} kilo-pascals is {Mili_mercury} millimeter of mercury')

ATP = math.ceil(kilo_pascals / 0.00987)
print(f'{kilo_pascals} kilo-pascals is {ATP} atmosphere pressure')