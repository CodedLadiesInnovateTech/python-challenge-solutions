#program to check whether a given integer is a palindrome or not.
def is_Palindrome(n):
    return str(n) == str(n)[::-1]
print(is_Palindrome(100))
print(is_Palindrome(252))
print(is_Palindrome(-838)) 
print(is_Palindrome('swims'))
print(is_Palindrome(1001)) 