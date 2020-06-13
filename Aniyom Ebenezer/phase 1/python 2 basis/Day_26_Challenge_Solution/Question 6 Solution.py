"""
Write a Python program to check whether a given number is a narcissistic number or not.
If you are a reader of Greek mythology, then you are probably familiar with Narcissus. He was a hunter of exceptional beauty that he died because he was unable to leave a pool after falling in love with his own reflection. That's why I keep myself away from pools these days (kidding).
In mathematics, he has kins by the name of narcissistic numbers - numbers that can't get enough of themselves. In particular, they are numbers that are the sum of their digits when raised to the power of the number of digits.
For example, 371 is a narcissistic number; it has three digits, and if we cube each digits 33 + 73 + 13 the sum is 371. Other 3-digit narcissistic numbers are
153 = 13 + 53 + 33
370 = 33 + 73 + 03
407 = 43 + 03 + 73.
There are also 4-digit narcissistic numbers, some of which are 1634, 8208, 9474 since
1634 = 14+64+34+44
8208 = 84+24+04+84
9474 = 94+44+74+44
It has been proven that there are only 88 narcissistic numbers (in the decimal system) and that the largest of which is
115,132,219,018,763,992,565,095,597,973,971,522,401
has 39 digits.
Ref.: //https://bit.ly/2qNYxo2
Sample Output:
True
True
True
False
True
True
True
False
"""
def is_narcissistic_num(num):
	return num == sum([int(x) ** len(str(num)) for x in str(num)])

print(is_narcissistic_num(153))
print(is_narcissistic_num(370))
print(is_narcissistic_num(407))
print(is_narcissistic_num(409))
print(is_narcissistic_num(1634))
print(is_narcissistic_num(8208))
print(is_narcissistic_num(9474))
print(is_narcissistic_num(9475))
