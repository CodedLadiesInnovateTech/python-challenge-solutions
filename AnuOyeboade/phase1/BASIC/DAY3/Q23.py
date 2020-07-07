"""
Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. 
Return the n copies of the whole string if the length is less than 2.
"""
s = str(input("Enter a word"))
n = int(input("Enter no "))
def sub_str(s,n):
    length_of_word = 3
    if length_of_word > len(s):
        length_of_word = len(s)
    substr = s[:length_of_word]
    result = ""
    for i in range(n):
        result = result + substr
    return result
print(sub_str(s,n))
