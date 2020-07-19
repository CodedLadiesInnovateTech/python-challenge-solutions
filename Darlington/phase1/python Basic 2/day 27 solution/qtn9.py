#program find the indices of all occurrences of a given item in a given list.
def indices_in_list(nums_list, n):
	return [idx for idx, i in enumerate(nums_list) if i == n]

print(indices_in_list([1,2,3,4,5,2], 2))
print(indices_in_list([3,1,2,3,4,5,6,3,3], 3))
print(indices_in_list([1,2,3,-4,5,2,-4], -4))