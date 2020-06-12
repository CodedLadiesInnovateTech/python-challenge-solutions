#program to remove the duplicate elements of a given array of numbers such that each element appear only once and return the new length of the given array.
def remove_duplicates(nums):
    for i in range (len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            del nums[i-1]
    return len(nums)

print(remove_duplicates([0,0,1,1,2,2,3,3,4,4,4]))
print(remove_duplicates([1, 2, 2, 3, 4, 4]))