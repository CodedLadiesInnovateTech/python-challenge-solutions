'''3. Write a Python program to reverse all the words which have even length.
Sample Output:
7
6
1
11'''
def reverse_even(txt):
         return ' '.join(i[::-1] if not len(i)%2 else i for i in txt.split())
print(reverse_even("The quick brown fox jumps over the lazy dog"))
print(reverse_even("Python Exercises"))

#Reference:w3resource