#function to check whether a number is divisible by another number. Accept two integers values form the
import math
def multiple(m,n):
  return True if m % n == 0 else False

print(multiple(40,4))
print(multiple(35,3))
print(multiple(100,6))