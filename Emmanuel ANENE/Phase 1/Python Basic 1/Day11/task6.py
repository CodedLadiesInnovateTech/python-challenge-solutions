'''
Write a Python program to print the current call stack.
'''
import traceback, inspect

def rule():
    nice()

def nice():
    for line in traceback.format_stack():
        print(line.strip())

rule()

print(inspect.stack())