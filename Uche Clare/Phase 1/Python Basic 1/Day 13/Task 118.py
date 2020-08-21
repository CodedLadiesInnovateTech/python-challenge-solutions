# Write a Python program to create a bytearray from a list.
num = list(map(int,input('Enter numbers:').split()))

byte_array = bytearray(num)
for i in byte_array:
    print(i)
