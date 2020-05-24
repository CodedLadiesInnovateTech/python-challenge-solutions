import socket

# https://intellipaat.com/community/4305/finding-local-ip-addresses-using-pythons-stdlib

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

print(s.getsockname()[0])
s.close()
