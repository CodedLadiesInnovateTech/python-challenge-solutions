"""
Write a Python program to check whether a sequence of numbers has an increasing trend or not.
Sample Output:
True
False
False
True
False
"""
def increase_trend_test(nums):
    if (sorted(nums)== nums):
        return True
    else:
        return False
print(increase_trend_test([1, 2, 3, 4, 5]))
print(increase_trend_test([4,5,3,2]))
print(increase_trend_test([9,5,3,25,5,4]))
print(increase_trend_test([10, 20, 30, 40]))
print(increase_trend_test([90, 50, 900, 54]))