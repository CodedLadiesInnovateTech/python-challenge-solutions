"""
Write a Python program to change a given string to a new string where the first and last chars hav ebeen exchanged.
"""
def change_char(str1):
    return str1[-1:] + str1[1:-1] + str1[:1]
print(change_char("abcd"))
print(change_char("codedladies"))