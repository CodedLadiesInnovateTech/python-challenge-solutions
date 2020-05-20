'''
Write a python program to find the sum of the first n positive integers.
'''

num = int(input("Enter a positive number: "))

sumN = num * (num + 1) / 2

print("The sum of the first {} positive numbers {}.".format(num, sumN))