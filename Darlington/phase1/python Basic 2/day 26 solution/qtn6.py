#program to check whether a given number is a narcissistic number or not.
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