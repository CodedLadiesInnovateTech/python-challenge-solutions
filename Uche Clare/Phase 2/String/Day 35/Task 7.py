#Write a Python program to remove all consecutive duplicates of a given string.

string='10000011000000010'
lst=[]
for i in string:
    lst.append(i)
    m=set(lst)
    lst=list(m)
duplicate_rmvr=''.join(lst)
print(duplicate_rmvr)