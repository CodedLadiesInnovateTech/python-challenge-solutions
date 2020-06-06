# Write a Python program to valid a IP address

import socket

address = '127.0.0.2561'
try:
    socket.inet_aton(address)
    print("Valid IP")
except socket.error:
    print("Invalid IP")
