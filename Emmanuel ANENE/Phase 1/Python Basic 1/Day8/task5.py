'''
Write a Python program to convert seconds to day, hour, minutes and seconds.
'''

varSec = int(input("Enter the your time in seconds: "))
varD =  varSec // 86400
varSec =  varSec % 86400
varH = varSec // 3600
varSec = varSec % 3600
varM = varSec // 60
varSec = varSec % 60
varS = varSec


print("The seconds entered is equivalent to {} day(s), {} hour(s), {} minute(s) and {} seconds.".format(varD, varH, varM, varS))