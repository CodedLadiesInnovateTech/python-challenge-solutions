'''7. Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java'''

fle_name = str(input("Enter the filename: "))
fle_extn = fle_name.split(".")
print("The file extention is: " + repr(fle_extn[-1]))

