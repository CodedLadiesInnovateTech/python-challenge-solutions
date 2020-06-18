"""
In multiprocessing, processes are spawned by creating a Process object.
Write a Python program to show the individual process IDs (parent process, process id etc.) involved
"""
from multiprocessing import Process
import os
def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
def f(name):
    info('function f')
    print('hello', name)
if __name__ == '__main__':
    info('Main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

