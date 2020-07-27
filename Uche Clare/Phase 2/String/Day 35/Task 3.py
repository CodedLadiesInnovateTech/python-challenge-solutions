#Write a Python program to remove leading zeros from an IP address.
ip_address = '192.168.01.01'
le = ""
ip_address1 = ip_address.split(".")
for i in ip_address1:
    if i[0] == "0" and len(i)> 1:
       i = i.replace("0", "")
    le = le +"."+ i
print(le[1:len(le)])