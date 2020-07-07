import cProfile
def sum():
    print(3+2)
cProfile.run('sum()')