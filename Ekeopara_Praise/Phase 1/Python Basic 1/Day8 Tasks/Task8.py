'''8. Write a Python program to calculate the sum of the digits in an integer.'''

number = 123
ans = 0
for n in str(number):
    ans += int(n)
print(ans)

