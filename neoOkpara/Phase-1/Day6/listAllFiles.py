from os import listdir
from os.path import isfile, join

path = "C:/Users/NEO/Desktop/python-challenges-solution/neoOkpara/Phase-1/Day6"

files_list = [f for f in listdir(path) if isfile(join(path, f))]

print(files_list)
print('\n')

included_extensions = ['.jpg', '.py', '.bmp', '.png', '.gif']
file_names = [fn for fn in listdir(path)
              if any(fn.endswith(ext) for ext in included_extensions)
              # if fn.endswith(included_extensions)
              ]

file_name = []
for fn in listdir(path):
    if any(fn.endswith(ext) for ext in included_extensions):
        file_name.append(fn)

print(file_names)
print(file_name)
