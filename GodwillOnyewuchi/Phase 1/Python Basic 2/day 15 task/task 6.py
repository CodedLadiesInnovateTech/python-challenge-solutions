# Write a Python program to find files and skip directories of a given directory

import os
print([f for f in os.listdir('C:Users/Onyebuchi') if os.path.isfile(os.path.join('C:Users/Onyebuchi/PycharmProjects', f))])
