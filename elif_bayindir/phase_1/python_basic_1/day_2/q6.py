# Question 6

# Comma-separated numbers to a list and a tuple

nums = input("Enter comma-seperated numbers: ")
list = nums.split(",")
tuple = tuple(list)
print("List : ", list, "\nTuple : ", tuple)

# split() method splits a string into a list. 
# string.split(separator, maxsplit) 
