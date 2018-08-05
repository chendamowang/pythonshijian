import os, shutil

for folderName, subfolders, filenames in os.walk('/home/chenmo/pythonshijian'):
    for filename in filenames:
        size = os.path.getsize(os.path.join(folderName, filename))
        if size > 0:
            print os.path.join(folderName, filename) 

