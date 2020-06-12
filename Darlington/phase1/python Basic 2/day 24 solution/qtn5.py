#program to remove all instances of a given value from a given array of integers and find the length of the new array.
 def remove_element(array_nums, val):
    i = 0
    while i < len(array_nums):
        if array_nums[i] == val:
            array_nums.remove(array_nums[i])

        else:
            i += 1

    return len(array_nums)
print(remove_element([1, 2, 3, 4, 5, 6, 7, 5], 5))
print(remove_element([10,10,10,10,10], 10)) 
print(remove_element([10,10,10,10,10], 20)) 
print(remove_element([], 1))