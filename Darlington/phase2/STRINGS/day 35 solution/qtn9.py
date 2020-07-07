#program to find the longest common sub-string from two given strings.
from difflib import SequenceMatcher 
  
def longest_Substring(s1,s2): 
  
     seq_match = SequenceMatcher(None,s1,s2) 
  
     match = seq_match.find_longest_match(0, len(s1), 0, len(s2)) 
  
     # return the longest substring 
     if (match.size!=0): 
          return (s1[match.a: match.a + match.size])  
     else: 
          return ('Longest common sub-string not present')  

s1 = 'abcdefgh'
s2 = 'xswerabcdwd'
print("Original Substrings:\n",s1+"\n",s2)
print("\nCommon longest sub_string:")
print(longest_Substring(s1,s2))
