"""
Write a Python program that accept a list of numbers and 
create a list to store the count of negative number in first element and 
store the sum of positive numbers in second element.
Sample Output:
[0, 15]
[5, 0]
[2, 6]
[3, 3]
"""
def count_num(nums):
    if not nums:
        return []
    return [len([i for i in nums if i < 0]), sum([i for i in nums if i > 0])]
print(count_num([1, 2, 3, 4, 5]))
print(count_num([-3, -5, -3, -2, -1]))
print(count_num([1, 2, 3, -4, -5]))
print(count_num([1, 2, -3, -4, -5]))