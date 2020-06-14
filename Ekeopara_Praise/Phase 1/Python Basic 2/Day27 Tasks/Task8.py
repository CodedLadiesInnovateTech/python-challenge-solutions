'''8. Write a Python program that takes three integers and check whether the
 last digit of first number * the last digit of second number = the last digit of third number.
Sample Output:
True
True
True
False
False'''

def check(n1, n2, n3):
    n1 = str(n1)
    n2 = str(n2)
    n3 = str(n3)
    if int(n1[-1]) * int(n2[-1]) == int(n3[-1]):

        ans = 'True'
    else:
        ans = 'False'
    return ans 
print(check(123, 343, 456))
print(check(12, 22, 44))
print(check(145, 122, 1010))
print(check(0, 22, 40))
print(check(1, 22, 40))
print(check(145, 122, 101))