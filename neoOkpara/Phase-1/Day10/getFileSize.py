from __future__ import print_function

import os

filename = 'isFileorDir.py'
file_size = os.path.getsize(filename)

print("\nThe size of", filename, "is:", file_size, 'Bytes')
