#program to determine profiling of Python programs.
import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')
