#program to test whether a given integer is pandigital number or not.
def is_pandigital_num(n):
    return len(set(str(n))) == 10

print(is_pandigital_num(1023456897))
print(is_pandigital_num(1023456798))
print(is_pandigital_num(1023457689))
print(is_pandigital_num(1023456789))
print(is_pandigital_num(102345679))