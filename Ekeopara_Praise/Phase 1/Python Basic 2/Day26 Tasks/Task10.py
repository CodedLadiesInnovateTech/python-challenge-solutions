'''10. Write a Python program to compute the sum of all items of a given array of 
integers where each integer is multiplied by its index. Return 0 if there is no number.
Sample Output:
20
-20
0'''

lst = [1, 2, 3, 4, 5]
def arrayofIntegers(lst):
    lst1 = []
    for i in lst:
        n = lst.index(i)*i
        lst1.append(n)
    ans = sum(lst1)
    return ans
print(arrayofIntegers([1, 2, 3, 4, 6]))
print(arrayofIntegers([1, 3, 5, 4, -60]))
print(arrayofIntegers([23, 40, 35, 40, 60]))