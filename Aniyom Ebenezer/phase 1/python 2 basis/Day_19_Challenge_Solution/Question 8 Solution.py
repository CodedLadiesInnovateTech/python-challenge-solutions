"""
Write a Python program to print the length of the series and the series from the given 3rd term,
3rd last term and the sum of the series.
"""
third_term = int(input("Input the third term: "))
third_last = int(input("Input the third last term: "))
s_sum = int(input("Input the sum of the Series: "))
n = int(2* s_sum/ (third_term + third_last))
print("The Length of the series is: ", n)

if n-5 == 0:
    d = (s_sum-3*third_term)//6
else:
    d = (third_last - third_term)/(n-5)

a = third_term-2*d
j = 0
print("Series: ")
for j in range(n-1):
    print(int(a), end="")
    a+=d
print(int(a), end="")