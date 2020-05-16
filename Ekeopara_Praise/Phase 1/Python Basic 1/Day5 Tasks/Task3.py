'''3. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.'''

def three_num(n1, n2, n3):

    if n1 != n2 and n2 !=n3:
        return f"The sum of the three numbers is {n1 + n2 + n3}"
    elif (n1 == n2 and n1 !=n3) or (n2 ==n3 and n1 !=n2):
        return f"The sum of the three numbers is {0}"


print(three_num(1, 2, 3))
print(three_num(1, 2, 2))

