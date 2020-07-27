# Question 8
# Sum of the digits in an integer

num = int(input("Enter an maximum 3 digit integer: "))
sum1 = 0
sum1 += (num // 100) # //: floor division
num %= 100 
sum1 += (num // 10)
num %= 10 
sum1 += (num)
num %= 1
print(sum1)

# Alternative,

""" num = int(input("Enter an maximum 3 digit integer: "))
sum1 = 0
for i in str(num):
    sum1 += int(i)
print(sum1) """

# Another alternative,

""" num = int(input("Enter n digit integer: "))
sum1 = 0
while (num != 0): 
	sum1 += int(num % 10) 
	num //= 10
print(sum1) """ 
