# Python program to create a copy of its own source code

print((lambda str='print(lambda str=%r: (str %% str))()': (str % str))())
