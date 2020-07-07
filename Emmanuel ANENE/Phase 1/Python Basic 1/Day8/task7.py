'''
Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.
'''

# kPa to psi = 0.145
# kPa to mmHg = 7.50062
# kPa to atp = 0.00987

val = round(float(input("Enter a value: ")), 0)
kpaUnit = "kPa"
print(int(val), kpaUnit)

calPsi =  round(val * 0.145, 3)
calMmHg = round( val * 7.50062, 3)
calAtp =  round(val * 0.00987, 3)

print("{} conversions: {} psi, {} mmHg, and {} atp.".format(val, calPsi, calMmHg, calAtp))

