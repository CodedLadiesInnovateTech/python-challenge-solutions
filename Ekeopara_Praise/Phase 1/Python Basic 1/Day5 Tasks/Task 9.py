'''9. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79'''


amt = 10000
intr = 3.5
yr = 7
F_A = amt *((1+(0.01*intr))**yr)
print(round(F_A, 2))



