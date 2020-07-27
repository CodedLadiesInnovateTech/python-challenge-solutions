# Write a Python program to calculate the time runs (difference between start and current time) of a program

import time
import datetime

start = time.time()

for i in range(1, 100000):
    print(i)
    if i == 50000:
        current = time.time()

TotalTime = float(current - start)

print(TotalTime)