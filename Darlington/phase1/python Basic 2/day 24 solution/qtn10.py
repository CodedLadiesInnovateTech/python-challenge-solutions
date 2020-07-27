#program to find the first missing positive integer that does not exist in a given list.
def first_missing_number(nums):
    if len(nums) == 0:
        return 1
        
    nums.sort()
    smallest_int_num = 0
    
    for i in range(len(nums) - 1):

        if nums[i] <= 0 or nums[i] == nums[i + 1]:
            continue
        else:
            if nums[i + 1] - nums[i] != 1:
                smallest_int_num = nums[i] + 1
                return smallest_int_num    
    if smallest_int_num == 0:
        smallest_int_num = nums[-1] + 1
    return smallest_int_num

print(first_missing_number([2, 3, 7, 6, 8, -1, -10, 15, 16])) 
print(first_missing_number([1, 2, 4, -7, 6, 8, 1, -10, 15]))
print(first_missing_number([1, 2, 3, 4, 5, 6, 7]))
print(first_missing_number([-2, -3, -1, 1, 2, 3]))