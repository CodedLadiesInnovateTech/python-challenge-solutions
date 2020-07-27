'''4. Write a Python program to create a list of the accumulating sum from a given list.
Sample Output:
[1, 3, 6, 10, 15]
[-1, -3, -6, -10, -15]
[2, 6, 12, 20, 30]'''

def accumulating_sum_list(nums):
	return [sum(nums[:i+1]) for i in range(len(nums))]

print(accumulating_sum_list([1,2,3,4,5]))
print(accumulating_sum_list([-1,-2,-3,-4,-5]))
print(accumulating_sum_list([2,4,6,8,10]))

#Reference: w3resource