'''8. Write a python program to find the sum of the first n positive integers.'''

def num_sum(n):
    num_sum = 0
    lst = range(1, n+1)
    for i in lst:
        num_sum += i
    return num_sum
print(num_sum(4))
print(num_sum(3))