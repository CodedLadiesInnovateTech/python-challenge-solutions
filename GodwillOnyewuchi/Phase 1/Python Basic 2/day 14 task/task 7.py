# Write a Python program to check whether an integer fits in 64 bits

integer = 9090908293839303037339200383265
if integer.bit_length() <= 63:
    print(f'{integer} fits in 64 bits')
else:
    print(f'{integer} does not fit in 64 bits')
