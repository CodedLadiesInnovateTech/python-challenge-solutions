"""
Write a Python program to find the position of the second occurrence of a given 
string in another given string. If there is no such string return -1.
Sample Output:
-1
31
"""
def find_string(txt, str1):
    return txt.find(str1, txt.find(str1)+1)
print(find_string("Python language is an easy doing language. ", "Python"))
print(find_string("the quick brown fox jumps over the lazy dog", "the"))