# Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number

num = int(input('Enter a postive integer: '))

sum = 0
for i in range(1, num):
    sum += i*i*i

print(sum)