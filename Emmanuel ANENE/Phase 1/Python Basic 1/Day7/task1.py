'''
Write a Python program to determine profiling of Python programs.
Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.
'''

import pstats
from pstats import SortKey

p = pstats.Stats()
p.strip_dirs().sort_stats(-1).print_stats()

print(p)
