'''9. In abstract algebra, a group isomorphism is a function between two groups that sets up a one-to-one correspondence between the elements of the groups in a way that respects the given group operations. If there exists an isomorphism between two groups, then the groups are called isomorphic.
Two strings are isomorphic if the characters in string A can be replaced to get string B
Given "foo", "bar", return false.
Given "paper", "title", return true.
Write a Python program to check if two given strings are isomorphic to each other or not.
Sample Output:
False
False
True
True
False
False
False'''

def isIsomorphic(str1, str2):          
    dict_str1 = {}
    dict_str2 = {}
    
    for i, value in enumerate(str1):
        dict_str1[value] = dict_str1.get(value, []) + [i]
            
    for j, value in enumerate(str2):
        dict_str2[value] = dict_str2.get(value, []) + [j]
    
    if sorted(dict_str1.values()) == sorted(dict_str2.values()):
        return True
    else:
        return False

print(isIsomorphic("foo", "bar"));         
print(isIsomorphic("bar", "foo"));      
print(isIsomorphic("paper", "title"));   
print(isIsomorphic("title", "paper"));
print(isIsomorphic("apple", "orange"));
print(isIsomorphic("aa", "ab"));
print(isIsomorphic("ab", "aa"));

#Reference: w3resource