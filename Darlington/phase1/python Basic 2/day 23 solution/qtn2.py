#program to find the number of combinations that satisfy p + q + r + s = n where n is a 
# given number <= 4000 and p, q, r, s in the range of 0 to 1000.
from collections import Counter
print("Input a positive integer: (ctrl+d to exit)") 
pair_dict = Counter()
for i in range(2001):
  pair_dict[i] = min(i, 2000 - i) + 1 
 
while True:
  try:
    n = int(input())
    ans = 0
    for i in range(n + 1):
      ans += pair_dict[i] * pair_dict[n - i]
    print("Number of combinations of a,b,c,d:",ans) 
  except EOFError:
    break