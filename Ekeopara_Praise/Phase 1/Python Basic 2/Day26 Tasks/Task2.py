'''2. Write a Python program to compute cumulative sum of numbers of a given list.
Note: Cumulative sum = sum of itself + all previous numbers in the said list.
Sample Output:
[10, 30, 60, 100, 150, 210, 217]
[1, 3, 6, 10, 15]
[0, 1, 3, 6, 10, 15]'''

def nums_cumulative_sum(nums_list):
  return [sum(nums_list[:i+1]) for i in range(len(nums_list))]

print(nums_cumulative_sum([10, 20, 30, 40, 50, 60, 7]))
print(nums_cumulative_sum([1, 2, 3, 4, 5]))
print(nums_cumulative_sum([0, 1, 2, 3, 4, 5]))

#Reference: w3resource