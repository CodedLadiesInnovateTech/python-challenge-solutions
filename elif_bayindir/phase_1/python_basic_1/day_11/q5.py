# Question 5
# Check whether a string is numeric

string = input("Enter a string: ")
print("Is string numeric?:", string.isnumeric())

# Alternative,
"""
try:
	int(string) == int(string) + 1 - 1
	print("Is string numeric?:", True)
except:
	print("Is string numeric?:", False)
"""


