"""
Write a Python program to find maximum length of consecutive 0's in a given binary string.
"""
def max_consecutive_0(input_str):
    return max(map(len, input_str.split('1')))
str1 = "111000010000110"
print("Original String:", str1)
print("Maximum length of consecutive 0's:")
print(max_consecutive_0(str1))
