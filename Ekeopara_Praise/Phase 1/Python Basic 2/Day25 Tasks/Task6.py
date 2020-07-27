'''6. Write a Python program to count the number of equal numbers from three given integers.
Sample Output:
3
2
0
3'''
def count(num):
    if num[0]==num[1] and num[0]==num[2]:
        ans = 3
    elif num[0]==num[1] or num[1]==num[2] or num[0]==num[2]:
        ans = 2
    else:
        ans = 0
    return ans
print(count((1, 1, 1)))
print(count((1, 2, 2)))
print(count((-1, -2, -3)))
print(count((-1, -1, -1)))