'''6. From Wikipedia, the free encyclopaedia:
A happy number is defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.
Write a Python program to check whether a number is "happy" or not.
Sample Output:
True
True'''

def is_Happy_num(num):       
    while num != 1:
        
        num = str(num)
        sum_square = 0
        
        for i in num:
            sum_square += int(i) ** 2
        
        num = sum_square
    
    return True

print(is_Happy_num(7))
print(is_Happy_num(932))

#Reference: w3resource