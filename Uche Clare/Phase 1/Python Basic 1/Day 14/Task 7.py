#Write a Python program to check whether an integer fits in 64 bits.
integer = 890
if integer.bit_length() <= 63:
    print(f'{integer} fits in 64 bits')
else:
    print(f'{integer} does not fit in 64 bits')
