# Question 9
# Compute the future value

amt = 10000 # amt: amount
inter = 3.5 # int: rate of interest
years = 7 
ftr_val = amt * ((1 + (inter / 100)) ** years)
print("Future value:", round(ftr_val, 2))
