"""
Write a Python program that takes two lists and returns True if they have at least one common member.
"""
list1 = [2,4,6,8,10,12]
list2 = [1, 2, 3, 5, 7, 11, 12]
result = False
for x in list1:
    for y in list2:
        if x in list2 or y in list1:
            result = True
print(result)