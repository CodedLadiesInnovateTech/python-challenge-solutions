def simple_interest(amount, interest, years):
    i = interest/100
    future=amount*(1+i)**years
    return future

print(simple_interest(10000,3.5,7))


