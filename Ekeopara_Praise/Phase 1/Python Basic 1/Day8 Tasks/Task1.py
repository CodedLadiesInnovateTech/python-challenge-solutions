'''1. Write a Python program to convert the distance (in feet) to inches, yards, and miles.'''

def conv_ft(ft):

    yrds = ft * 0.33333
    miles = ft/5280
    inch = ft/12
    return f"{ft} feet is equivalent to\n{inch}inches\n{yrds}yards\n {miles} miles"
print (conv_ft(400))

''''3. Write a Python program to get an absolute file path.

4. Write a Python program to get file creation and modification date/times.


5. Write a Python program to convert seconds to day, hour, minutes and seconds.


6. Write a Python program to calculate body mass index.


7. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.


8. Write a Python program to calculate the sum of the digits in an integer.


9. Write a Python program to sort three integers without using conditional statements and loops.

10. Write a Python program to sort files by date.'''
