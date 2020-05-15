"""
Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
"""
a = float(input("Principal = "))
r = float(input("Rate = "))
t = float(input("Time = "))
fv = a*((1+(0.01*r))**t)
print(round(fv,2))