'''4. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.'''

def Num_sum(n1, n2):
    add = n1 + n2
    if add >= 15 and add <=20: 
        return 20
    else:
        return add
print(Num_sum(1, 2))
print(Num_sum(10, 9))

