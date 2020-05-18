'''2. Write a Python program to print to stderr.'''
import sys
stdout_file = sys.stdout
stderr_file = sys.stderr

sample_input = ['a + 1', 'hi', 'exit']

for val in sample_input:
    stdout_file.write(val + '\n')
    try:
        val = val + 100
    except:
          stderr_file.write('Exception occured!\n')