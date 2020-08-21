#program to remove leading zeros from an IP address.
def remove_zeros_from_ip(ip_add):
  new_ip_add = ".".join([str(int(i)) for i in ip_add.split(".")])  
  return new_ip_add ;

print(remove_zeros_from_ip("255.024.01.01"))
print(remove_zeros_from_ip("127.0.0.01 "))
