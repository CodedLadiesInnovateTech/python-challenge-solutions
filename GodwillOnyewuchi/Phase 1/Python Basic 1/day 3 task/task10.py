text = input("Enter a String of numbers: ")	
texts = list(text)	 
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']	
integer = ""	
for i in texts:	
    if i in numbers:	
        integer += i	
print(integer)