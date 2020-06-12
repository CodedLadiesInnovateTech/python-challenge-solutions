#6. Write a Python program to create a histogram from a given list of integers.

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

list = [1, 2, 2, 2, 3, 3]

num_bins = 5
n, bins, patches = plt.hist(list, num_bins)
plt.show()