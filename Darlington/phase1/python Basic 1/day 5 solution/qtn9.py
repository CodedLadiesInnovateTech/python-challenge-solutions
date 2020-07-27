#program to compute future principal amount
#I = PTR/100
import math
amt, inte = 10000, 3.5
years = 7
future_value  = amt*((1+(0.01*inte)) ** years)
print(round(future_value,2))
