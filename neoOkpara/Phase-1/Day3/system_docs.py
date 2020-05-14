def printout(functype):
    docs = functype.__doc__
    assert isinstance(docs, object)
    print ("Expected Result: \n" + docs)


printout(callable)