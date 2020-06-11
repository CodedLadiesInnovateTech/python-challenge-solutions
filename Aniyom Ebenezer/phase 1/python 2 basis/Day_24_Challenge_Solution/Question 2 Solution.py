"""
Write a Python program to check whether a given integer is a palindrome or not.
Note: An integer is a palindrome when it reads the same backward as forward. Negative numbers are not palindromic.
"""
def is_Palindrome(n):
    return str(n) == str(n)[::-1]
print(is_Palindrome(100))
print(is_Palindrome(252))
print(is_Palindrome(-838))