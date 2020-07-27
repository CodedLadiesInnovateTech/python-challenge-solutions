#program to find out the number of CPUs using.
import os

def main():
    cpu=os.cpu_count()
    cores=cpu/2
    print("Cores: ",'{0:g}'.format(cores))
main()