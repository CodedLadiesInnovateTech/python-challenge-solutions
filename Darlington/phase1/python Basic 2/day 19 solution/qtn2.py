#program to create a sequence where the first four members of the sequence are equal to one, 
# and each successive term of the sequence is equal to the sum of the four previous ones. 
# Find the Nth member of the sequence.
def new_seq(n):
    if n==1 or n==2 or n==3 or n==4:
        return 1
    return new_seq(n-1) + new_seq(n-2) + new_seq(n-3) + new_seq(n-4)
print(new_seq(5))
print(new_seq(6))
print(new_seq(7))