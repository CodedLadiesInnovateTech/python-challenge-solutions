'''7. Write a Python program to check whether a given number is Oddish or Evenish.
A number is called "Oddish" if the sum of all of its digits is odd, and a number is called "Evenish" if the sum of all of its digits is even.
Sample Output:
Oddish
Evenish
Oddish
Evenish
Oddish'''

'''def check_status(num):'''
num = 111
num = str(num)
for i in num:
    n = int(i)
    n += n
print(n)
print(n%2==0)
'''   if n%2==0:
        response = "Evenish"
    else:
        response = "Oddish"
    return response

print(check_status(123))
print(check_status(546))
print(check_status(545))
print(check_status(300))
print(check_status(100))'''
