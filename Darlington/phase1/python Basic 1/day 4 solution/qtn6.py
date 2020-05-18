#program to create a histogram
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 4, 6, 5, 7, 10, 12, 15])