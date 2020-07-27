'''4. Write a Python program that accept a list of numbers and create a list to store the 
count of negative number in first element and store the sum of positive numbers in second element.
Sample Output:
[0, 15]
[5, 0]
[2, 6]
[3, 3]'''

def count_sum(nums):
    if not nums: return []
    return [len([n for n in nums if n < 0]), sum(n for n in nums if n > 0)]

print(count_sum([1, 2, 3, 4, 5]))
print(count_sum([-1, -2, -3, -4, -5]))
print(count_sum([1, 2, 3, -4, -5]))
print(count_sum([1, 2, -3, -4, -5])) 

#Reference: w3resource