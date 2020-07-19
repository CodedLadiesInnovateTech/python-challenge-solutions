#Write a Python program to count repeated characters in a string. 
Samp_string = 'thequickbrownfoxjumpsoverthelazydog'
for i in set(Samp_string):
    if Samp_string.count(i)>1:
      
        print(f"The repeated character '{i}' is: ", Samp_string.count(i))
        