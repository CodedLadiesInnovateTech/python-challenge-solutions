#Write a Python program to find maximum length of consecutive 0's in a given binary string.
max_consecutive='10000011000000010'
max_consecutive_0=max(max_consecutive.split('1'))
print()
print("The maximum length of consecutive 0's is :" , len(max_consecutive_0))
