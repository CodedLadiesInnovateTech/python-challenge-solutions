#program to create two strings from a given string. Create the first 
# string using those character which occurs only once 
# and create the second string which consists of multi-time occurring characters in the said string.
from collections import Counter  
def generateStrings(input): 
     str_char_ctr = Counter(input) 
     part1 = [ key for (key,count) in str_char_ctr.items() if count==1] 
     part2 = [ key for (key,count) in str_char_ctr.items() if count>1] 
     part1.sort() 
     part2.sort()
     return part1,part2
input = "aabbcceffgh"
s1, s2 = generateStrings(input)
print(''.join(s1))   
print(''.join(s2))