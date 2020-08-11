#program to unpack a tuple in several variables.
#create a tuple
tuplex = 4, 8, 3 
print(tuplex)
n1, n2, n3 = tuplex
#unpack a tuple in variables
print(n1 + n2 + n3) 
#the number of variables must be equal to the number of items of the tuple
n1, n2, n3, n4= tuplex 