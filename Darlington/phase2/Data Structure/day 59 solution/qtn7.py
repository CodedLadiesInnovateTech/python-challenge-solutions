#program to convert an array to an array of machine values and return the bytes representation.
import array
import binascii
a = array.array('i', [1,2,3,4,5,6])
print("Original array:")
print('A1:', a)
bytes_array = a.tobytes()
print('Array of bytes:', binascii.hexlify(bytes_array))