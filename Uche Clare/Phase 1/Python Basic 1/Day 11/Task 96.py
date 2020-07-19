import traceback

def t_b():
    return abc()
def abc():
    traceback.print_stack()
t_b()
print()