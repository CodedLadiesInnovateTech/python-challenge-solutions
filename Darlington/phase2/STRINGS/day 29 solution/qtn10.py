# program to change a given string to a new string where the first and last
#  chars have been exchanged.
def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
	  
print(change_sring('abcd'))
print(change_sring('12345'))