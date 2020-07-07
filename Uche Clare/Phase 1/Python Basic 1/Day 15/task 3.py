#write a Python program to calculate the time runs (difference between start and current time) of a program.
import timeit
start_time= timeit.timeit()
sum(range(10))
end_time= timeit.timeit()
print( start_time - end_time)