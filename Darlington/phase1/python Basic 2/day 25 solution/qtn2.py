#program to calculate the median from a list of numbers.
def cal_median(nums):
  nums.sort()
  n = len(nums)
  m = n // 2
  if n % 2 == 0:
    return (nums[m - 1] + nums[m]) / 2
  else:
    return nums[m]
print(cal_median([1,2,3,4,5]))
print(cal_median([1,2,3,4,5,6]))
print(cal_median([6,1,2,4,5,3]))
print(cal_median([1.0,2.11,3.3,4.2,5.22,6.55]))
print(cal_median([1.0,2.11,3.3,4.2,5.22]))
print(cal_median([2.0,12.11,22.3,24.12,55.22]))