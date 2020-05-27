'''3. Write a Python program to calculate the time runs 
(difference between start and current time) of a program.'''

from timeit import default_timer
def get_time():
    start_time = default_timer()
    lst = list(range(12, 30))
    for i in lst:
        print(i)

    return default_timer() - start_time

print(get_time())
