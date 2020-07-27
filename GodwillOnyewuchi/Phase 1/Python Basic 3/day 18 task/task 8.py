# Write a Python program to find the median among three given numbers
import math
List = [1, 3, 2]
List.sort()
median = math.ceil(len(List) / 2)

print(median)