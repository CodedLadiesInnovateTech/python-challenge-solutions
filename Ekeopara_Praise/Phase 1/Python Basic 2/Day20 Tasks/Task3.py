'''3. Write a Python program to compute the digit number of sum of two given integers.
Input:
Each test case consists of two non-negative integers x and y which are separated by a space in a line.
0 = x, y = 1,000,000
Input two integers(a b):
5 7
Sum of two integers a and b.:
2'''

lst = []
a_b = str(input("Enter the two integers with space in between them: "))
a_b = a_b.split()
for i in a_b:
    ans = int(i)
    lst.append(ans)

print("Sum of two integers a and b.:\n", len(str(sum(lst))))