'''7. From Wikipedia,
A happy number is defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.
Write a Python program to find and print the first 10 happy numbers.
Sample Output:
[1, 7, 10, 13, 19, 23, 28, 31, 32, 44]'''

def happy_numbers(n):
    past = set()			
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    return True
print([x for x in range(500) if happy_numbers(x)][:10])

#Reference: w3resource