'''
Write a python program to access environment variables.
'''

import os

for item, value in os.environ.items():
    print('{}: {}'.format(item, value))    