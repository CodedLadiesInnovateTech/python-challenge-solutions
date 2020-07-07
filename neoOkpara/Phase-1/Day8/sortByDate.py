import glob
import os

files = glob.glob("*.py")
files.sort(key=os.path.getmtime, reverse=True)
print("\n".join(files))
