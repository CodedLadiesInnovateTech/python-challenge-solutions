#program to sum of two given integers
import math
def sum(p, q):
    sum = p + q
    if sum in range(15, 20):
       return 20
    else:
      return sum

print(sum(4, 4))   
print(sum(10, 2))   
print(sum(16, 2))