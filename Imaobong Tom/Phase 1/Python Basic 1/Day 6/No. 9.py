import glob, os
os.chdir("C:/Windows")
for file in glob.glob("*.*"):
    print(file)