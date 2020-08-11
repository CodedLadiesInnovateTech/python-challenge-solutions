# program to add an item in a tuple.
#create a tuple
tuplex = (4, 6, 2, 8, 3, 1) 
print(tuplex)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
#adding items in a specific index
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)
#converting the tuple to list
listx = list(tuplex) 
#use different ways to add items in list
listx.append(30)
tuplex = tuple(listx)
print(tuplex)
tuplex = tuplex[:0] + (0, 0 , 0,) + tuplex[:5]
print(tuplex)