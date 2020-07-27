#Write a Python program to valid a IP address.
import socket
hostname = socket.gethostname()
print(hostname)
ip_address = socket.gethostbyname(hostname)
print(ip_address)
try:
    socket.inet_aton(ip_address)
    print('Vaild IP')
except socket.error:
    print('Invalid IP')