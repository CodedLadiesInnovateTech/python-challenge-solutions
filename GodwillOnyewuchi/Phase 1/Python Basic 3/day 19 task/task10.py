# Write a Python program to reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure

Number = '123454321'
reverse = Number[ : : -1]
Sum = Number + reverse
SumReverse = Sum[ : : -1]
if Sum == SumReverse:
    print("panlidrome")
else:
    Sum = Sum + SumReverse
    print("Nothing")

