#program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.
x= float(input('Pressure= '))
print('Convert kPa to psi:')
x1 = x*0.15
print(x1,"psi")
print('Convert kPa to mmHg:')
x2 = x* 7.501
print(x2, "mmHg")
print('Convert kPa to atm:')
x3 = x/101
print(x3, "atm")