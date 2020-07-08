"""
Write a Python program to generate and print a list of first and last 5 elements
where the values are square of numbers between 1 and 30(both included).
"""
numbers = list()
for x in range(1, 31):
    numbers.append(x**2)
print("The Square of numbers from 1 - 30 is: \n", numbers)
print()
print("First 5 Elements: \n", numbers[:5])
print()
print("Last 5 Elements: \n", numbers[-5:])