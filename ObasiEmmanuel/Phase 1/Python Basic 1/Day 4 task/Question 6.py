def histogram(quantity):
    for i in quantity:
        frequency = ""
        times= i
        while times > 0:
            frequency= frequency + "*"
            times=times-1
            print(frequency)

histogram([1,4,6,3,8,9,2,4,5])



