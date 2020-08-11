#program to create the colon of a tuple.
from copy import deepcopy
#create a tuple
tuplex = ("HELLO", 5, [], True) 
print(tuplex)
#make a copy of a tuple using deepcopy() function
tuplex_colon = deepcopy(tuplex)
tuplex_colon[2].append(50)
print(tuplex_colon)
print(tuplex)