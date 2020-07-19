'''1. Write a Python program to compute and print sum of two given integers (more than or equal to zero).
 If given integers or the sum have more than 80 digits, print "overflow".
Input first integer:
25
Input second integer:
22
Sum of the two integers: 47'''

def sum_integers(x, y):
    if x >= 10 ** 80 or y >= 10 ** 80 or x + y >= 10 ** 80:
        response = "Overflow!"
    else:
        response = x + y
    return response
print(sum_integers(25, 22))
print(sum_integers(25**80, 22))