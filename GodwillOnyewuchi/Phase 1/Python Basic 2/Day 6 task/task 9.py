from os import listdir
from os.path import isfile, join
files = [f for f in listdir('/Users/Onyebuchi') if isfile(join('/Users/Onyebuchi', f))]
print(files);

#reference w3schools