'''7. Write a Python program to convert pressure in kilopascals to 
pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.'''

def Kp(kps):
    ib_inch = kps * 0.14504
    mmHg = kps * 7.50062
    atm = kps * 0.00987
    return f"{kps} kilopascals:\n\n{ib_inch} pounds per square inch\n{mmHg} mmHg\n{atm} atm"
print(Kp(400))



'''8. Write a Python program to calculate the sum of the digits in an integer.


9. Write a Python program to sort three integers without using conditional statements and loops.

10. Write a Python program to sort files by date.'''