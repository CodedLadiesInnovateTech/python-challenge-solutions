#program that will return true if the two given integer values are equal or their sum or difference is 5.
import math
def values(a, b):
     # sum = a + b
      #diff = a - b 
    if a == b or abs(a - b) == 5 or (a + b) == 5:
        return True
    else:
        return False
print(values(3, 2)) 
print(values(5, 10))
print(values(9, 11))       
           

 
