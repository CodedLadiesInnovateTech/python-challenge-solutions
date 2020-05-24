from __future__ import print_function

import os
import sys
import time
from stat import S_ISREG, ST_CTIME, ST_MODE

# Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'
print(dir_path)
print(sys.argv)
# all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))

print(data)
data = ((os.stat(path), path) for path in data)
print(data)
# regular files, insert creation date
data = ((stat[ST_CTIME], path)
        for stat, path in data if S_ISREG(stat[ST_MODE]))

print(data)

for creation_date, path in sorted(data):
    print(time.ctime(creation_date), os.path.basename(path))
