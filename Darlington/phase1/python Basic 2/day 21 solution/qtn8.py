#program that reads n digits (given) chosen from 0 to 9 and prints the number of combinations where the sum of the digits equals to another given number (s). Do not use the same digits in a combination.
import itertools
print("Input number of combinations and sum, input 0 0 to exit:")
while True:
  x, y = map(int, input(). split())
  if x == 0 and y == 0:
    break
  s = list(itertools.combinations(range(10), x))
  ctr = 0
  for i in s:
    if sum(i) == y:
            ctr += 1
 
print(ctr)