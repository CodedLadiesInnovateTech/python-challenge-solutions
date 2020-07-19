#program to locate Python site-packages.
import site

def main():
    return (site.getsitepackages())
print(main())