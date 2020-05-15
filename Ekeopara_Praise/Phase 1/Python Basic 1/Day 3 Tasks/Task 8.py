'''8. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
    Tools: math, input function'''

def check(n1, n2, n3):
    if n1 == n2 == n3:
        return 3 * (n1+n2+n3)  
    else:
        return n1+n2+n3

print(check(2, 2, 2))

