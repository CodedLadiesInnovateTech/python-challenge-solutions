'''7. Write a Python program to concatenate all elements in a list into a string and return it.'''

def lst_element(lst):
    ans = ""
    for ele in lst:
        ans += str(ele)
    return ans

print(lst_element([0, 9, 0, 6, 7, 8, 0, 0, 8, 1, 8]))
print(lst_element(['s', 't', 'r', 'i', 'n', 'g']))

