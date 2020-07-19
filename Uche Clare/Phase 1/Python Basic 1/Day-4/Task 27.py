#program to concatenate all elements in a list into a string and return it.
f=('apple','banana','mango',"orange")
fruits=list(f)
print(fruits)
result =''
for x in fruits:
 result += " "+ x
print(result)