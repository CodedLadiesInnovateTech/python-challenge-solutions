"""
Write a Python program to calculate the median from a list of numbers.
Sample Output:
3
3.5
3.5
3.75
3.3
22.3
"""
def median_calculation(nums):
    nums.sort()
    n = len(nums)
    m = n // 2
    if n % 2 == 0:
        return (nums[m-1] + nums[m]) / 2
    else:
        return nums[m]
print(median_calculation([1,2,3,4,5]))
print(median_calculation([1,2,3,4,5,6]))
print(median_calculation([9,8,4,2,3,1]))
print(median_calculation([5,4,4,3,2,3.5]))
print(median_calculation([1.0,2.11,3.3,4.2,5.22]))
print(median_calculation([2.0,12.11,22.3,24.12,55.22]))