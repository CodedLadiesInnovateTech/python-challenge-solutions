#9. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
#Test Data : amt = 10000, int = 3.5, years = 7
#Expected Output : 12722.79

amt = 10000
int_rate = 3.5
years = 7

fv = (amt * (1 + (0.01 * int_rate)) ** years)

print(fv)