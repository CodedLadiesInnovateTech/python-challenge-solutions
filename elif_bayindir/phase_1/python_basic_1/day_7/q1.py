# Question 1
# Determine profiling of Python programs.
# A profile is a set of statistics that describes how often and for how long various parts of the program executed.

import cProfile
x = 5 
cProfile.run("x")

# Alternative,
""" import pstats

p = pstats.Stats().strip_dirs().sort_stats(-1).print_stats()
print(p) """



