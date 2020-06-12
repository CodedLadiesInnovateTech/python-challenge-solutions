"""
 Write a Python program to count the number of equal numbers from three given integers.
Sample Output:
3
2
0
3
"""
def count_num(num1, num2, num3):
    result = set([num1, num2, num3]) 
    if len(result)==3:
        return 0
    else:
        return (4 - len(result))
print(count_num(2, 2, 2))
print(count_num(1, 8, 8))
print(count_num(2, 3, 4))
print(count_num(7, 7, 7))