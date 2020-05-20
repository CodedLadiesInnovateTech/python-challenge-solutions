#program to access environment variables
import os
# Access all environment variables 
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable 
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')