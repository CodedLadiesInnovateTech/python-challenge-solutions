#program to get OS name, platform and release information.
import platform,os

def main():
    return (os.name+'\n'+platform.system()+'\n'+platform.release())

print(main())