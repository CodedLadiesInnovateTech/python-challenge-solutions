# Question 6
# Add two objects if both objects are an integer type.
	
obj1 = {}
obj2 = {}

val1 = 2
val2 = 10

obj1['key1'] = val1
obj2['key2'] = val2

if type(obj1['key1']) == int and type(obj2['key2']) == int:
	print(obj1['key1'] + obj2['key2'])
	
# if val1 or val2 is not integer it prints nothing, just change the val1 and val2
