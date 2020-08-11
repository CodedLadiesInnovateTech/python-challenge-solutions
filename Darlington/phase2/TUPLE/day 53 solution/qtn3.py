#Python program to slice a tuple.
#create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
#used tuple[start:stop] the start index is inclusive and the stop index
a_slice = tuplex[3:5]
#is exclusive
print(a_slice)
#if the start index isn't defined, is taken from the beginning of the tuple
a_slice = tuplex[:6]
print(a_slice)
#if the end index isn't defined, is taken until the end of the tuple
a_slice = tuplex[5:]
print(a_slice)
#if neither is defined, returns the full tuple
a_slice = tuplex[:]
print(a_slice)
#The indexes can be defined with negative values
a_slice = tuplex[-8:-4]
print(a_slice)
#create another tuple
tuplex = tuple("HELLO WORLD")
print(tuplex)
#step specify an increment between the elements to cut of the tuple
#tuple[start:stop:step]
a_slice = tuplex[2:9:2]
print(a_slice)
#returns a tuple with a jump every 3 items
a_slice = tuplex[::4]
print(a_slice)
#when step is negative the jump is made back
a_slice = tuplex[9:2:-4]
print(a_slice)