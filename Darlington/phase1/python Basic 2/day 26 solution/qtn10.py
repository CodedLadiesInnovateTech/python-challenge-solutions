#program to compute the sum of all items of a given array of integers where
#  each integer is multiplied by its index.
def sum_index_multiplier(nums):
	return sum(j*i for i, j in enumerate(nums))

print(sum_index_multiplier([1,2,3,4]))
print(sum_index_multiplier([-1,-2,-3,-4]))
print(sum_index_multiplier([]))