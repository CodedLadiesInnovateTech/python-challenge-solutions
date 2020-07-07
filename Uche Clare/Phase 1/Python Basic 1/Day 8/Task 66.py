#program to calculate body mass index.
weight = float(input('Weight= '))
height = float(input('Height= '))
unit1 = "lbs/in²"
unit2= 'kg/m²'
print('For Imperial BMI formula: ')
BMI = (weight*703)/height
print(BMI,unit1)
print('For Metric BMI: ')
BMI = weight/height
print(BMI,unit2)