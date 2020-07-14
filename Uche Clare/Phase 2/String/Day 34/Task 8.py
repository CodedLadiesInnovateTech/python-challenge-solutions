#Write a Python program to move spaces to the front of a given string.
space_rmvr = " My name is Clare "
space_rmvr1 = space_rmvr.replace(" ", "")
space_mover = len(space_rmvr) - len(space_rmvr1)
result = " "*space_mover
space_mover =  '"'+ result+ space_rmvr1 +'" '
print(space_mover)