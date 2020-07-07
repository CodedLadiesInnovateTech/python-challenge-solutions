# program to check if two given strings are isomorphic to each other or not.
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