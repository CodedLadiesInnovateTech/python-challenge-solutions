'''1. Write a Python program to access and print a URL's content to the console.'''
'''import os
os.system('cls||clear')
from urllib.request import urlopen
link = 'http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html'
f = urlopen(link)
myfile = f.readline()
print(myfile)'''

from http.client import HTTPConnection
conn = HTTPConnection('example.com')
conn.request("GET", "/")
result = conn.getresponse()
contents = result.read()
print(contents)
