'''9. Write a Python program to sort three integers without using conditional statements and loops.'''

def sort_num(n1, n2, n3):
    b1 = min(n1, n2, n3)
    b2 = max(n1, n2, n3)
    b3 = (n1+n2+n3) -b1-b2
    return "The sorted numbers are: ", b1, b3, b2
print(sort_num(84, 30, 22))

