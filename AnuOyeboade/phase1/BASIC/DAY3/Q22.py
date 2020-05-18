"""
Write a Python program to count the number 4 in a given list.
"""
nums = str(input("Enter a list of comma seperated numbers"))
numbs = nums.split(",")
def list_4(numbs):
    count = 0
    for num in numbs:
        if num==4:
            count = count + 1
    return count
print(list_4(numbs))