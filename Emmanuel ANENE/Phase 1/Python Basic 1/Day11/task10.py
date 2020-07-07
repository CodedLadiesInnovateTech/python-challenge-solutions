'''
Write a Python program to get the name of the host on which the routine is running
'''

import socket

hostt = socket.gethostbyname()
print("Name of host:", hostt)

# print(help(sok.gethostbyname))