'''
Write a Python to find local IP addresses using Python's stdlib
'''

import socket
print('The local IP address of the computer is:',socket.gethostbyname(socket.gethostname()))