from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('\Users\Motunrayo Koyejo') if isfile(join('/\Users\Destop'))]
print(files_list)