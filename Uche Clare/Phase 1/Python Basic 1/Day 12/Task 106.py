#Write a Python program to divide a path on the extension separator.
import os.path
for path in [ 'python.py', 'filename', '/user/system/test.txt', '/', '' ]:
    print(path, os.path.splitext(path))
