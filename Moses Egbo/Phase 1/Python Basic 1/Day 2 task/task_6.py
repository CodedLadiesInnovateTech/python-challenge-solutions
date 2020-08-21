''' Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. '''

num = (input("Input numbers separated by commas :"))
n = num.split(',')
print(n)
print(tuple((n)))

