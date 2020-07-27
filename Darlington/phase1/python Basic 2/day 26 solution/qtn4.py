#program to find the largest product of the pair of adjacent elements from a given list of integers.
def adjacent_num_product(list_nums):
    return max(a*b for a, b in zip(list_nums, list_nums[1:]))
print(adjacent_num_product([1,2,3,4,5,6]))
print(adjacent_num_product([1,2,3,4,5]))
print(adjacent_num_product([2,3]))