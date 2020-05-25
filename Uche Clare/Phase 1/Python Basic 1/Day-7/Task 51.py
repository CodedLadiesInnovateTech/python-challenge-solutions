import cProfile

def add(n):
    print(n*(n+1)/2)
cProfile.run('add(39)')