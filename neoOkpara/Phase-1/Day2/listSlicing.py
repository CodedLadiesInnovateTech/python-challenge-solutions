# Accept and Store First Name
firstName = raw_input("Please input your firstName: ")
# firstName = "Emmanuel"
print(firstName)
# Accept and Store Last Name
lastName = raw_input("Please input your lastName: ")
print(lastName)

var = len(firstName)
val = len(lastName)

reverseName = firstName[var::-1] + " " + lastName[val::-1]
print(reverseName)

