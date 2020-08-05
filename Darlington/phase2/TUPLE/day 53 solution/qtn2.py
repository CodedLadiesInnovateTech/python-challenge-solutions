# program to remove an item from a tuple.
tupledar = ('d','a','r','l')
print(tupledar)
#create a tuple
tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
print(tuplex)
#tuples are immutable, so you can not remove elements
#using merge of tuples with the + operator you can remove an item and it will create a new tuple
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)
#converting the tuple to list
listx = list(tuplex) 
#use different ways to remove an item of the list
listx.remove("c") 
#converting the tuple to list
tuplex = tuple(listx)
print(tuplex)