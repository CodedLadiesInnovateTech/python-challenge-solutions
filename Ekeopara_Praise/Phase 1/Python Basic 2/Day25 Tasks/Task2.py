'''2. Write a Python program to calculate the median from a list of numbers.
Sample Output:
3
3.5
3.5
3.75
3.3
22.3'''
import statistics
def cal_median(nums):
    med = statistics.median(nums)
    return med
print(cal_median([1,2,3,4,5]))
print(cal_median([1,2,3,4,5,6]))
print(cal_median([6,1,2,4,5,3]))
print(cal_median([1.0,2.11,3.3,4.2,5.22,6.55]))
print(cal_median([1.0,2.11,3.3,4.2,5.22]))
print(cal_median([2.0,12.11,22.3,24.12,55.22]))
