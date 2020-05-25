from __future__ import print_function

import sys

str1 = "one"
array1 = ['abs', 'fev', 'greet', 'hips']
tuple1 = ("three", "four", 8)

print("Memory size of '" + str1 + "' = " + str(sys.getsizeof(str1)) + " bytes")
print("Memory Size of", array1, "=", sys.getsizeof(array1), "bytes")
print("Memory Size of", tuple1, "=", sys.getsizeof(tuple1), "bytes")
