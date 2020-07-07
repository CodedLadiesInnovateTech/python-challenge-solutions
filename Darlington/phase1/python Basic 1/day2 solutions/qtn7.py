#printing the extension name
filename = input("Input the Filename with extension: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))