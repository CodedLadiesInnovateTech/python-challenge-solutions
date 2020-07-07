# program to get the name of the host on which the routine is running.
import socket
host_name = socket.gethostname()
print()
print("Host name:", host_name)
print()