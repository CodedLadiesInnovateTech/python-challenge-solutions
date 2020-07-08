char = 'google.com'
print(len(char))  #To check for the number of characters in the string
char1 = list(char[0:11])
print(char1) 
freq = [char1.count(n) for n in char1]
print('The Characters and frequencies is:', str(set(zip(char1, freq))))