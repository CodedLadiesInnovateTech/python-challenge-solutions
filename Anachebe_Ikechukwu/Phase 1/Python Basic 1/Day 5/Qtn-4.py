#4. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

a = int(input("Enter an integer:"))
b = int(input("Enter another integer:"))

sum = a + b

if (15 <= sum <= 20):
    sum = 20

print(sum)