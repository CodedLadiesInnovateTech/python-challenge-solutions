'''4. Write a Python program to get file creation and modification date/times.'''
import  os 
import datetime

file = "MYSIWES.docx"

print("Created")
print(os.path.getctime(file))
print(datetime.datetime.fromtimestamp(os.path.getctime(file)))
print("")
print("Modifed")
print(os.path.getmtime(file))
print(datetime.datetime.fromtimestamp(os.path.getmtime(file)))
