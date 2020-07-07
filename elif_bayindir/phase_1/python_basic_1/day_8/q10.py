# Question 10
# Sort files by date

import os
import time
from pprint import pprint

pprint([(x[0], time.ctime(x[1].st_ctime)) for x in sorted([(fn, os.stat(fn)) for fn in os.listdir(".")], key = lambda x: x[1].st_ctime)])
