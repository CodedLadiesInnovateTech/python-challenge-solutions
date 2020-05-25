import os

def show_files_by_date(dir):
 entrys = os.scandir(dir)

entrys = sorted(entrys, key=lambda e: e.stat().st_mtime)
for entry in entrys:
 print(entry.name)