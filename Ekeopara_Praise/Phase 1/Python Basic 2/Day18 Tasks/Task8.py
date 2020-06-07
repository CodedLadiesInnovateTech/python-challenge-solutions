'''8. Write a Python program to print the length of the series and the series from 
the given 3rd term, 3rd last term and the sum of a series.
Sample Data:
Input third term of the series: 3
Input 3rd last term: 3
Sum of the series: 15
Length of the series: 5
Series:
1 2 3 4 5'''

tn = int(input("Input third term of the series:"))
tltn = int(input("Input 3rd last term:"))
s_sum = int(input("Sum of the series:"))
n = int(2*s_sum/(tn+tltn))
print("Length of the series: ",n)


if n-5==0:
  d = (s_sum-3*tn)//6
else:
  d = (tltn-tn)/(n-5)

a = tn-2*d
j = 0
print("Series:")
for j in range(n-1):
  print(int(a),end=" ")
  a+=d
print(int(a),end=" ")