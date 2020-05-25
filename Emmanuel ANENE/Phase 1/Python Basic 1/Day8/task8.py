'''
Write a Python program to calculate the sum of the digits in an integer.
'''

varNum = input("Enter an integer: ")
sumOfNum = 0

for num in varNum:
    sumOfNum += int(num)
print(sumOfNum)