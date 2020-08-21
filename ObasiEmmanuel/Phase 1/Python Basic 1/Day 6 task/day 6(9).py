from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/Users/Obasi Emmanuel C/Documents') if isfile(join('/Users/Obasi Emmanuel C/Documents',f))]