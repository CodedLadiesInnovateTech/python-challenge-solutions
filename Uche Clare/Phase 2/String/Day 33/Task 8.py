#Write a Python program to swap comma and dot in a string.
samp_strng = "32.054,23"
num =  samp_strng.maketrans
swapper = samp_strng.translate(num(".,", ",."))
print(swapper)