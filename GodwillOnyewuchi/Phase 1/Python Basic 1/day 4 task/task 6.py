import matplotlib.pyplot as plt
import numpy as np

lists = np.random.normal(size=50)

plt.hist(lists)
plt.show()

"""for a list of integers"""
list2 = [1, 2, 5, 7, 8, 5, 4]
plt.hist(list2)
plt.show()
