# program to remove duplicate characters of a given string.
from collections import OrderedDict
def remove_duplicate(str1):
  return "".join(OrderedDict.fromkeys(str1))
     
print(remove_duplicate("python exercises practice solution"))
print(remove_duplicate("w3resource"))