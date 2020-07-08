#Write a Python program to display a number in left, right and center aligned of width 10.
num = "902"
print()
print(' Left number alignment:' , num.ljust(10, "0"))
print('\n Right number alignment:', num.rjust(10, "*"))
print('\n Center alignment:', num.center(10,"-"))