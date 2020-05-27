#program to compute the product of a list of integers (without using for loop).from functools import reduce
from functools import reduce
nums = [10, 20, 30,]
nums_product = reduce( (lambda x, y: x * y), nums)
print("Product of the numbers : ",nums_product)