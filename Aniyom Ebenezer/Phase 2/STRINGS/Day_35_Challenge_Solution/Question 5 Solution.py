"""
Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no common letters print "No common characters".
"""
from collections import Counter
def common_chars(str1, str2):
    d1 = Counter(str1)
    d2 = Counter(str2)
    common_dict = d1 & d2
    if len(common_dict) == 0:
        return "No Common Characters."

    common_chars = list(common_dict.elements())
    common_chars = sorted(common_chars)

    return ''.join(common_chars)
str1 = 'Python'
str2 = 'PHP'
print("Two strings: "+str1+' : '+str2)
print(common_chars(str1, str2))