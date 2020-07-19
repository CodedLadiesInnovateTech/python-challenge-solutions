'''8. In multiprocessing, processes are spawned by creating a Process object. Write a Python program to show the individual process IDs 
(parent process, process id etc.) involved.
Sample Output:
Main line
module name: __main__
parent process: 23967
process id: 27986
function f
module name: __main__
parent process: 27986
process id: 27987
hello bob'''

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

#Reference: w3resource 