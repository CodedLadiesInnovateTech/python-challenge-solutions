name=input("Enter name of string").lower()
f=name[0:2]
if f=="is":
    print(name)
else:
    new_name="is"+name
    print(new_name)