'''
Write a Python program to test whether all numbers of a list is greater than a certain number.
'''

numList = [100, 40, 30, 80, 75, 54]
nums = int(input("Enter a number: "))

print(all(num > nums for num in numList))


