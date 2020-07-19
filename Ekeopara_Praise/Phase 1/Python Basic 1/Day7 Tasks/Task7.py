'''7. Write a program to get execution time for a Python method.'''

import time

start_time = time.time()
n1, n2 = 4, 3
num = (n1 + n2)* 4
end_time = time.time()
ans = end_time-start_time
print(f"The time to execute ({n1}+{n2})*4 is {ans} seconds")