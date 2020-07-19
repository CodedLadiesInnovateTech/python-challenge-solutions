'''
Write a Python program to calculate midpoints of a line.
'''
x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))

def findMin(x1, x2, y1, y2):
    return (x1 + x2) // 2,  (y1 + y2) // 2

print(findMin(x1, x2, y1, y2))



