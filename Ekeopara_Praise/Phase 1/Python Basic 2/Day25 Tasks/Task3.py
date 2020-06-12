'''3. Write a Python program to test whether a given number is symmetrical or not.
A number is symmetrical when it is equal of its reverse.
Sample Output:
True
True
False
True

def is_symmetrical_num(n):
  return str(n) == str(n)[::-1]
print(is_symmetrical_num(121))
print(is_symmetrical_num(0))
print(is_symmetrical_num(122))
print(is_symmetrical_num(990099))
'''
def reverse(num):
    num1 = str(num)
    n1 = num1[::-1]
    return n1==num1
    
print(reverse(121))
print(reverse(234))

