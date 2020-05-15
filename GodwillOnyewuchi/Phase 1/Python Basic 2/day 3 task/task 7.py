
import math	

Number = int(input("Enter a number: "))	
if Number in range(0, 100):	
    print("Number is  in numbers 0-100")	
elif Number in range(100, 1000):	
    print("Number is  in numbers 100-1000")	

elif Number in range(1000, 2000):	
    print("Number is  in numbers 1000-2000")	
else:	
    print(" Number is not in numbers 0 - 2000")