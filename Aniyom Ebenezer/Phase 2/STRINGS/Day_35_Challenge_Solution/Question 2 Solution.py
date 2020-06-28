"""
Write a Python progran to compute sum of digits of a given string.
"""
def sum_digits_strings(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit
print(sum_digits_strings("abcd1234efgh"))