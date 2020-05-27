from __future__ import print_function

# print open(__file__).read()

# https://towardsdatascience.com/how-to-write-your-first-quine-program-947f2b7e4a6f

variable = 'print("variable = " + repr(variable) + "\\neval(variable)")'
eval(variable)
print("\t")
bob = 'print("bob is a god " + str(2 + 5) + "\\neval(bob)")'
eval(bob)
