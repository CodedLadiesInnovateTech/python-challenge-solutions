'''
Write a Python program to sort three integers without using conditional statements and loops.
'''

num1 = int(input("Enter a number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the last number: "))

sortMax = max(num1, num2, num3 )
sortMin = min(num2, num1, num3)
sortTotal = (num1 + num2 + num3) - (sortMax + sortMin)
# files.append(lst)

print("The sorted given three integers are as follows: {}, {}, {}.".format(sortMin, sortTotal, sortMax))