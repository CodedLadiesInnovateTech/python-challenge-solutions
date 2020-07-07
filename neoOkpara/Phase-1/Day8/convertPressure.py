from __future__ import print_function

kPa = float(input("Input your pressure in kiloPascals: "))
psi = kPa / 6.89476
mmhg = kPa * 7.50062
atm = kPa / 101.325
atm2 = kPa * 0.00986923

print("The pressure in pounds per square inch: %.2f psi" % psi)
print("The pressure in millimeter of mercury: %.2f mmHg" % mmhg)
print("Atmosphere pressure: %.2f atm." % atm)
print("Atmosphere pressure: %.2f atm." % atm2)
