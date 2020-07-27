#program to create a dictionary of keys x, y, and z where each key has as
#  value a list from 11-20, 21-30, and 31-40 respectively.
#  Access the fifth value of each key from the dictionary.
from pprint import pprint
dict_nums = dict(x=list(range(11, 20)), y=list(range(21, 30)), z=list(range(31, 40)))
pprint(dict_nums)
print(dict_nums["x"][4])
print(dict_nums["y"][4])
print(dict_nums["z"][4])
for k,v in dict_nums.items():
   print(k, "has value", v)