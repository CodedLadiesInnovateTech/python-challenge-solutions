"""
Write a Python program to count repeated characters in a string. 
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2
"""
import collections
sample_string = "thequickbrownfoxjumpsoverthelazydog"
d = collections.defaultdict(int)
for c in sample_string:
    d[c] += 1
for c in sorted(d, key=d.get, reverse=True):
    if d[c] > 1:
        print("{} {}".format(c, d[c]))


#Reference: w3resource.com