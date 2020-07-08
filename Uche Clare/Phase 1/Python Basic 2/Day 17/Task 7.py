#Write a Python program to count the number of each character of a given text of a text file.
import collections
import pprint
Filename = input('File Name: ')
with open(Filename, 'r') as info:
  count = collections.Counter(info.read().upper())
  value = pprint.pformat(count)
print(value)