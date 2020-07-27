#program to find the index of a given string at which a given substring starts. 
# If the substring is not found in the given string return 'Not found'.
import itertools
def remove_consecutive_duplicates(s1):
     return (''.join(i for i, _ in itertools.groupby(s1)))

s1= "aabcdaee"
print("Original String: ",s1)
print("\nRemoving all consecutive duplicates:")
print(remove_consecutive_duplicates(s1))