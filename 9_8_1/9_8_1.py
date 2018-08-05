import os, shutil

for folderName, subfolders, filenames in os.walk('/home/chenmo/pythonshijian/9_8_1'):
    for filename in filenames:
        if filename.endswith('.txt'):
            shutil.copy(folderName + '/' + filename, '/home/chenmo/pythonshijian/9_8_1_new'+'/'+filename)
