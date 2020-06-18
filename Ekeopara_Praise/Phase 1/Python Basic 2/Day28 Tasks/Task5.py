'''5. Write a Python program to generate and prints a list of numbers from 1 to 10.
Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
['1', '2', '3', '4', '5', '6', '7', '8', '9']'''

lst = []
numbers = list(range(1, 10))
for num in numbers:
    lst.append(str(num))

print(numbers)
print(lst)
