'''
Write a Python program to list the special variables used within the language.
'''

speVar = sorted((set(globals().keys()) | set(__builtins__.keys())) - set("_names i".split()))
spr = "\n".join(' '.join(speVar[i:i+8]) for i in range(0, len(speVar), 8))

stv = set(__builtins__.keys())
# print(speVar)
print(spr)
# print(stv)