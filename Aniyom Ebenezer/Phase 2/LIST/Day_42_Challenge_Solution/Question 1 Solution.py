"""
Write a Python program to count the number of elements in a list within a specified range.
"""
def count_elemnts(list1):
    count = 0
    for x in list1:
        if list1[1] <= x <= list1[4]:
            count += 1
    return count
print(count_elemnts([1, 2, 3, 4, 5, 6, 7, 6, 3]))