'''1. Write a Python program to convert JSON data to Python object. '''

# Python program showing 
# use of json package 

import json 

# {key:value mapping} 
a ={"name":"John", 
"age":31, 
	"Salary":25000} 

# conversion to JSON done by dumps() function 
b = json.dumps(a) 

# printing the output 
print(b) 
