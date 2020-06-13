"""
Write a Python program to compute cumulative sum of numbers of a given list.
Note: Cumulative sum = sum of itself + all previous numbers in the said list.
Sample Output:
[10, 30, 60, 100, 150, 210, 217]
[1, 3, 6, 10, 15]
[0, 1, 3, 6, 10, 15]
"""
def cummulative_sum(num_lists):
    return (sum(num_lists[:i+1]) for i in range(len(num_lists)))
print(cummulative_sum([10, 20, 30, 40, 50, 60, 7]))
print(cummulative_sum([1, 2, 3, 4, 5]))
print(cummulative_sum([0, 1, 2, 3, 4, 5]))