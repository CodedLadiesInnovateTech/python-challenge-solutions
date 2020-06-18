"""
 Write a Python program to check whether a given number is Oddish or Evenish.
A number is called "Oddish" if the sum of all of its digits is odd, and a number is called "Evenish" if the sum of all of its digits is even.
Sample Output:
Oddish
Evenish
Oddish
Evenish
Oddish
"""
def oddish_evenish_num(n):
	return 'Oddish' if sum(map(int, str(n))) % 2 else 'Evenish'
print(oddish_evenish_num(120))
print(oddish_evenish_num(321))
print(oddish_evenish_num(43))
print(oddish_evenish_num(4433))
print(oddish_evenish_num(373))