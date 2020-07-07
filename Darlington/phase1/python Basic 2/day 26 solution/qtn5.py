#program to check whether every even index contains an even number
#  and every odd index contains odd number of a given list.
def odd_even_position(nums):
	return all(nums[i]%2==i%2 for i in range(len(nums)))
print(odd_even_position([2, 1, 4, 3, 6, 7, 6, 3]))
print(odd_even_position([2, 1, 4, 3, 6, 7, 6, 4]))
print(odd_even_position([4, 1, 2]))