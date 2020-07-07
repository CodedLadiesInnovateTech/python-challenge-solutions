#program to remove two duplicate numbers from a given number of list.
def two_unique_nums(nums):
  return [i for i in nums if nums.count(i)==1]
print(two_unique_nums([1,2,3,2,3,4,5]))
print(two_unique_nums([1,2,3,2,4,5]))
print(two_unique_nums([1,2,3,4,5]))