"""
Write a Python program to generate and print a list except for the first 5 elements,
where the values are square of numbers between 1 and 30(both included)
"""
num_list = list()
for x in range(1,31):
    num_list.append(x**2)
print(num_list[5:])