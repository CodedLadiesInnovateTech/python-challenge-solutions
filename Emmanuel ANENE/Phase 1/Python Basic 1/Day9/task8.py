'''
Write a Python program to find the available built-in modules.
'''

import sys, textwrap

module_list = ", ".join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_list, width=100), end="\n\n")