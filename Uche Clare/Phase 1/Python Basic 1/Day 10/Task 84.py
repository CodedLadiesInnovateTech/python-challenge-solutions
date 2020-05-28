#program to count the number occurrence of a specific character in a string.
a_string='My name is Clare, what\'s yours?'
count = 0
for i in a_string:

 if i == "a":
    
    count += 1
    

print('Occurrences= ', count)
