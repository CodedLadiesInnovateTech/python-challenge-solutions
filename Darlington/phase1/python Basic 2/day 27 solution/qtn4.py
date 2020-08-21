#program to create a list of the accumulating sum from a given list.
def accumulating_sum_list(nums):
	return [sum(nums[:i+1]) for i in range(len(nums))]

print(accumulating_sum_list([1,2,3,4,5]))
print(accumulating_sum_list([-1,-2,-3,-4,-5]))
print(accumulating_sum_list([2,4,6,8,10]))