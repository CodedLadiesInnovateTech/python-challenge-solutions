#code to show file extension
file_name = input("ENTER THE FILENAME.EXTENSION: ")
f_extns = file_name.split(".")
print("The file extension is: "+repr(f_extns[-1]))