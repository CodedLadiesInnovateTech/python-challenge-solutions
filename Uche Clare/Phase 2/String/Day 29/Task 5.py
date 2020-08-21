#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
samp_string = 'abc', 'xyz'
samp1 = samp_string[0][0:2] +  samp_string[1][-1]
samp2 = samp_string[1][0:2] + samp_string[0][-1]
print(samp2+" "+samp1)

