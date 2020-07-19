'''
Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
'''

amt = int(input("Enter the amount: "))
intr = float(input("Enter interest: "))
yrs = int(input("Enter the number of years: "))

I = amt * (intr/100) * yrs

print(I)