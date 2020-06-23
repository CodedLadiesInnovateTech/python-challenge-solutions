from functools import reduce
num= [-1, 5, 9, 7, 3, -4, 2, -8]
num_product= reduce(lambda x,y: x * y, num )
print(num_product)