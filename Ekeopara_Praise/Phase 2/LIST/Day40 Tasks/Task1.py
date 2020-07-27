'''1. Write a Python function that takes two lists and returns True if they have at least one common member. '''

def common_member(lst1, lst2):
    lst1 = set(lst1)
    lst2 = set(lst2)
    if lst1 & lst2:
        ans = "True"
    else:
        ans = "False"
    return ans
print(common_member([1, 2, 3, 4], [4, 5, 6, 7]))
print(common_member([1, 2, 3, 4], [0, 5, 6, 7]))
print(common_member([1, 2, 3, 4], [3, 5, 6, 7]))