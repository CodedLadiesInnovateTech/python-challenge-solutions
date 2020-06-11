#1. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
        #Sample function : abs()
        #Expected Result :
        #abs(number) -> number
        #Return the absolute value of the argument.

import builtins

input_Str = input("Enter a function to get it's Description:")
fun_Str = getattr(builtins, input_Str)
print(fun_Str.__doc__)