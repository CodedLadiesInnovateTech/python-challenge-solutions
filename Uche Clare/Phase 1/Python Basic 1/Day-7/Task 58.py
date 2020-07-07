#program to find the sum of the first n positive integers.
x = int(input('enter a number: '))
count = 0
for i in range(x+1):
 count += i
print('The result is:', count)